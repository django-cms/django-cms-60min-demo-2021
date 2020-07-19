const MetisMenu = require('metismenujs');
require('metismenujs/dist/metismenujs.min.css');


export function initMainMenu() {
    const isMenuPresent = document.getElementById('menu') !== null;
    if (isMenuPresent) {
        new MetisMenu('#menu', {toggle: false});
        activeCurrentMenuNodes();
    }
}


function activeCurrentMenuNodes() {
    activateCurrentMenuNode('.selected');
    activateCurrentMenuNode('.ancestor');
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
