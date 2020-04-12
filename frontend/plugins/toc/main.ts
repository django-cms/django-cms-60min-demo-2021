import * as tocbot from 'tocbot';


document.addEventListener('DOMContentLoaded', () => {
    const tocSelector = '.djangocms-toc';
    const contentSelector = 'article';
    
    tocbot.init({
        tocSelector: tocSelector,
        headingSelector: 'h2, h3',
        contentSelector: contentSelector,
        collapseDepth: 4,
        positionFixedSelector: tocSelector,
        fixedSidebarOffset: calculateFixedPosOffset(contentSelector),
        orderedList: false,
        positionFixedClass: getFixedPosCssCls(),
    });
    tocbot.refresh();
})


function calculateFixedPosOffset(contentSelector: string): number {
    let fixedPosTopOffset = $(contentSelector).offset().top;
    const cmsToolbar = document.querySelector('.cms-toolbar');
    if (cmsToolbar) {
        fixedPosTopOffset -= cmsToolbar.clientHeight;
    } else {
        const fixedPosTopCssOffset = 10;
        fixedPosTopOffset -= fixedPosTopCssOffset; 
    }
    return fixedPosTopOffset
}


function getFixedPosCssCls(): string {
    let fixedCssCls = 'is-position-fixed';
    const cmsToolbar = document.querySelector('.cms-toolbar');
    if (cmsToolbar) {
        fixedCssCls = 'is-position-fixed-with-toolbar';
    }
    return fixedCssCls;
}
