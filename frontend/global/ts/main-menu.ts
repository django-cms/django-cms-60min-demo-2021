const MetisMenu = require('metismenujs');
require('metismenujs/dist/metismenujs.min.css');


export function initMainMenu() {
    const isMenuPresent = document.querySelectorAll('.metismenu-root');
    if (isMenuPresent) {
        const navMenuSelector = '.navbar-nav .metismenu-root';
        if (document.querySelector(navMenuSelector)) {
            new MetisMenu(navMenuSelector, {toggle: false});
        }
        const leftMenuSelector = '.one-column-with-menu-and-sidebar .metismenu-root';
        if ($(leftMenuSelector)) {
            new MetisMenu(leftMenuSelector, {toggle: false});
        }
        activeCurrentMenuNodes();
        fixLeftMenuOnScroll();
    }
}


function activeCurrentMenuNodes() {
    activateCurrentMenuNode('.selected');
    activateCurrentMenuNode('.ancestor');
}


function fixLeftMenuOnScroll() {
    const toolbarHeight = $('.cms-toolbar').height() || 0 as number;
    const navbarHeight = $('header nav').outerHeight() as number;
    const floatingTopOffset = toolbarHeight + navbarHeight;
    const menuLeft = $('.one-column-with-menu-and-sidebar .menu-container');
    const elementPosition = menuLeft.offset();
    $(window).scroll(function () {
        if ($(window).scrollTop() > elementPosition.top - floatingTopOffset) {
            menuLeft.css('position', 'fixed').css('top', floatingTopOffset);
        } else {
            menuLeft.css('position', 'relative');
            menuLeft.css('top', 0);
        }
    });
    const menuContainerWidth = menuLeft.outerWidth() as number;
    menuLeft.css('width', `${menuContainerWidth}px`);
    $(window).resize(function() {
        const menuContainerWidth = $('.one-column-with-menu-and-sidebar .menu-container').outerWidth() as number;
        menuLeft.css('width', `${menuContainerWidth}px`);
    })
}


function activateCurrentMenuNode(selector: string) {
    const activeElems = document.querySelectorAll(selector) as any as Array<HTMLElement>;
    for (let activeElem of activeElems) {
        const selectElemParent = activeElem.parentElement as HTMLElement;
        if (selectElemParent.tagName === 'UL') {
            // show list
            selectElemParent.classList.add('mm-show');
            
            // activate expand mode
            const selectedParentParent = selectElemParent.parentElement as HTMLElement;
            const selectedContainerAElem = selectedParentParent.querySelector('a') as HTMLElement;
            // selectedContainerAElem.setAttribute('aria-expanded', String(true));
            selectedContainerAElem.classList.remove('mm-collapsed');
        }
    }
}
