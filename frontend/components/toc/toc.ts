import * as tocbot from 'tocbot';
const slugify = require('slugify');


document.addEventListener('DOMContentLoaded', () => {
    const tocSelector = '.djangocms-toc';
    const contentSelector = 'article';
    addAnchorsToAllHeadings();
    tocbot.init({
        tocSelector: tocSelector,
        headingSelector: 'h1, h2, h3, h4, h5',
        contentSelector: contentSelector,
        collapseDepth: 6,
        positionFixedSelector: tocSelector,
        orderedList: false,
        hasInnerContainers: true,
        scrollSmooth: true,
    });
})


function addAnchorsToAllHeadings(){
    const headers = document.querySelectorAll('h1, h2, h3, h4, h5') as any as HTMLElement[];
    for (const header of headers) {
        const isIdNotSet = !header.id;
        if (isIdNotSet) {
            header.id = slugify(header.textContent, {lower: true, strict: true});
        }
    }
}
