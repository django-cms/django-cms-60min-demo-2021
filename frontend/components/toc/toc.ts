import * as tocbot from 'tocbot';


document.addEventListener('DOMContentLoaded', () => {
    const tocSelector = '.djangocms-toc';
    const contentSelector = 'article';

    const posFixedCssCls = getFixedPosCssCls();
    tocbot.init({
        tocSelector: tocSelector,
        headingSelector: 'h1, h2, h3, h4, h5',
        contentSelector: contentSelector,
        collapseDepth: 6,
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
    let fixedPosTopOffset = ($(contentSelector).offset() as any).top;
    const cmsToolbar = document.querySelector('.cms-toolbar');
    const navbarFixed = document.querySelector('.navbar.fixed-top');
    
    if (cmsToolbar) {
        fixedPosTopOffset -= cmsToolbar.clientHeight;
        if (navbarFixed) {
            fixedPosTopOffset -= navbarFixed.clientHeight; 
        }
    } else {
        let fixedPosTopCssOffset = 10;
        if (navbarFixed) {
            fixedPosTopOffset -= navbarFixed.clientHeight; 
        }
        fixedPosTopOffset -= fixedPosTopCssOffset; 
    }
    return fixedPosTopOffset;
}


function getFixedPosCssCls(): string {
    let fixedCssCls = 'is-position-fixed';
    const cmsToolbar = document.querySelector('.cms-toolbar');
    if (cmsToolbar) {
        fixedCssCls = 'is-position-fixed-with-toolbar';
    }
    return fixedCssCls;
}


function addAnchorsToAllHeadings(){
    //loop through all your headers
    $.each($('h1, h2, h3, h4, h5'),function(index,value){
        //append the text of your header to a list item in a div, linking to an anchor we will create on the next line
        $('#box-anchors').append('<li><a href="#anchor-'+index+'">'+$(this).html()+'</a></li>');
        //add an a tag to the header with a sequential name
        $(this).html('<a name="anchor-'+index+'">'+$(this).html()+'</a>');
    });
}
