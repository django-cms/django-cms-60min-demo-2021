const algoliasearch = require('algoliasearch');


function renderAlgoliaData(render_block: HTMLElement, value: string, index, hits_per_page = 1000) {
    let search_results_block = document.querySelector('.search-results') as any;
    search_results_block.dataset.isVisible = String(true);
    if (value != '') {
        index.search(value, {hitsPerPage: hits_per_page, highlightPreTag: "<b>", highlightPostTag: "</b>"})
            .then((obj) => {
                if (obj.hits.length > 0) {
                    render_block.innerHTML = '';
                    render_results_count(obj.hits.length);

                    for (const hit of obj.hits) {
                        let description = ''
                        if (hit._snippetResult) {
                            description = hit._snippetResult['page_content'].value;
                        }
                        render_block.innerHTML += `
                            <a href="${hit.url}">
                                <div class="item">
                                    <span class="search-res-title">
                                        ${hit._highlightResult.title.value}
                                    </span>
                                    <p class="search-res-description">
                                        ${description || ''}
                                    </p>
                                </div>
                            </a>
                         `;
                    }
                } else {
                    render_block.innerHTML = '<div class="item">Nothing found</div>';
                    render_results_count(0);
                }
            })
            .catch(err => {
                render_block.innerHTML = '';
                render_results_count(0);
            });
    } else {
        render_block.innerHTML = '';
    }
}

function render_results_count(count = 0) {
    let results_count_block = document.getElementById('search-results-count-block') as any;
    if (count==0){
        results_count_block.innerText = '';
    } else {
        results_count_block.innerText = 'Results count: ' + String(count);
    }
}

export function LoadAlgoliaSearch() {
    const isSearchFormNotPresent = document.getElementById('search-form') === null;
    if (isSearchFormNotPresent) {
        return
    }
    
    const client = algoliasearch(window.DJANGO.algoliaApplicationId, window.DJANGO.algoliaApiKey);
    const index = client.initIndex('pages');
    index.setSettings({
        attributesToSnippet: [
            'page_content:50',
            'description'
        ]
    });

    // Update suggestions on click or input
    let input = document.getElementById('search-input') as HTMLInputElement;
    let suggestions_block = document.getElementById('search-suggestions') as any;
    ["click", "input"].forEach(evt =>
        input.addEventListener(evt, (event) => {
            let element = event.currentTarget as HTMLInputElement;
            let value = element.value;
            renderAlgoliaData(suggestions_block, value, index, 8);
        })
    );
    
    let search_results_block = document.querySelector('.search-results') as any;

    // Hide suggestions block on click out of suggestions area
    let search_element = document.getElementById('search-form') as any;
    document.addEventListener('click', event => {
        if (!search_element.contains(event.target as Node)) {
            suggestions_block.innerHTML = '';
            search_results_block.dataset.isVisible = String(false);
        }
    });

    // Show search results on form submit
    let form = document.getElementById('search-form') as any;
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        render_results_count(0);
        let input = document.getElementById('search-input') as HTMLInputElement;
        let value = input.value;
        renderAlgoliaData(search_results_block, value, index, 1000);
        suggestions_block.innerHTML = '';
        search_results_block.dataset.isVisible = String(false);
    });
}
