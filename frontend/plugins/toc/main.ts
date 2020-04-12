import * as tocbot from 'tocbot';


document.addEventListener('DOMContentLoaded', () => {
    const tocSelector = '.djangocms-toc';
    const contentSelector = 'article';
    
    const posFixedTopPadding = 25;
    let topOffset = $(contentSelector).offset().top - posFixedTopPadding;
    const cmsToolbar = document.querySelector('.cms-toolbar');
    let fixedCssCls = 'is-position-fixed';
    if (cmsToolbar) {
        topOffset -= cmsToolbar.clientHeight;
        fixedCssCls = 'is-position-fixed-with-toolbar';
    }

    tocbot.init({
        tocSelector: tocSelector,
        headingSelector: 'h2, h3',
        contentSelector: contentSelector,
        collapseDepth: 4,
        positionFixedSelector: tocSelector,
        fixedSidebarOffset: topOffset,
        orderedList: false,
        positionFixedClass: fixedCssCls,
        
    });
    tocbot.refresh();
})
