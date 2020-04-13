import * as tocbot from 'tocbot';


document.addEventListener('DOMContentLoaded', () => {
    const tocSelector = '.djangocms-toc';
    const contentSelector = 'article';

    const posFixedCssCls = getFixedPosCssCls();
    tocbot.init({
        tocSelector: tocSelector,
        headingSelector: 'h2, h3, h4, h5',
        contentSelector: contentSelector,
        collapseDepth: 4,
        positionFixedSelector: tocSelector,
        fixedSidebarOffset: calculateFixedPosOffset(contentSelector),
        orderedList: false,
        positionFixedClass: posFixedCssCls,
    });
    tocbot.refresh();

    window.addEventListener('scroll', () => {
        fixWidthOnFixedPos(tocSelector, posFixedCssCls);
    })
    window.addEventListener('resize', () => {
        fixWidthOnFixedPos(tocSelector, posFixedCssCls);
    })
})


function fixWidthOnFixedPos(tocSelector: string, posFixedCssCls: string) {
    const tocElem = $(tocSelector);
    const isPosFixedActive = tocElem.hasClass(posFixedCssCls);
    if (isPosFixedActive) {
        const parentWidth = tocElem.parent('aside').width();
        tocElem.css('max-width', parentWidth + 'px');
    } else {
        tocElem.css('max-width', '100%');
    }
}


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
