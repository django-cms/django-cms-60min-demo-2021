import {initAsideRightPositionFixed} from 'global/ts/aisde-right-pos-fixed';
import {initMainMenu} from 'global/ts/main-menu';
import {initReloadScriptsOnContentRefresh} from 'global/ts/reload-scripts-on-content-refresh';
import * as Sentry from '@sentry/browser';


try {
    document.removeEventListener('DOMContentLoaded', initScripts);
} catch (error) {
    // todo try catch might be redundant
}
document.addEventListener('DOMContentLoaded', initScripts, {once: true});


function initScripts() {
    tryScriptExecution(initReloadScriptsOnContentRefresh);
    tryScriptExecution(initMainMenu);
    tryScriptExecution(initAsideRightPositionFixed);
}


function tryScriptExecution(callable: CallableFunction) {
    try {
        callable()
    } catch (error) {
        Sentry.captureException(error);
    }
}
