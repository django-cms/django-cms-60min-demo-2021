import {initAsideRightPositionFixed} from 'global/ts/aisde-right-pos-fixed';
import {initMainMenu} from 'global/ts/main-menu';
import {initReloadScriptsOnContentRefresh} from 'global/ts/reload-scripts-on-content-refresh';


document.addEventListener('DOMContentLoaded', () => {
    initReloadScriptsOnContentRefresh();
    initMainMenu();
    initAsideRightPositionFixed();
}, {once: true});
