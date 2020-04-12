import * as tocbot from 'tocbot';


document.addEventListener('DOMContentLoaded', () => {
    const tocSelector = '.djangocms-toc';
    const contentSelector = 'article'
    
    tocbot.init({
        tocSelector: tocSelector,
        headingSelector: 'h2, h3',
        contentSelector: contentSelector,
        collapseDepth: 4,
        positionFixedSelector: tocSelector,
        fixedSidebarOffset: $(contentSelector).offset().top as any,
        orderedList: false,
        
    });
    tocbot.refresh();
})
