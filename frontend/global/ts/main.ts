import {initAsideRightPositionFixed} from 'global/ts/aisde-right-pos-fixed';
import {initMainMenu} from 'global/ts/main-menu';
import {initOnPageEditReloadScript} from 'global/ts/on-page-edit-reload';


document.addEventListener('DOMContentLoaded', () => {
    initOnPageEditReloadScript();
    initMainMenu();
    initAsideRightPositionFixed();
}, {once: true});
