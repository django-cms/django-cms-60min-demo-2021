const MetisMenu = require('metismenujs');
require('metismenujs/dist/metismenujs.min.css');


export function initMainMenu() {
    const isMenuPresent = document.querySelectorAll('.metismenu-root').length;
    if (isMenuPresent) {
        const navMenuSelector = '.navbar-nav .metismenu-root';
        if (document.querySelector(navMenuSelector)) {
            new MetisMenu(navMenuSelector, {toggle: false});
        }
        const leftMenuSelector = '.one-column-with-menu-and-sidebar .metismenu-root';
        if (document.querySelector(leftMenuSelector)) {
            new MetisMenu(leftMenuSelector, {toggle: false});
        }
        activeCurrentMenuNodes();
    }
}


function activeCurrentMenuNodes() {
    activateCurrentMenuNode('.selected');
    activateCurrentMenuNode('.ancestor');
}


function activateCurrentMenuNode(selector: string) {
    const activeElems = document.querySelectorAll(selector) as any as Array<HTMLElement>;
    for (const activeElem of activeElems) {
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
