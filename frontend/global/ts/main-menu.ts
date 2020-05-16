const MetisMenu = require('metismenujs');
require('metismenujs/dist/metismenujs.min.css');


export function initMainMenu() {
    const isMenuPresent = document.getElementById('menu') !== null;
    if (isMenuPresent) {
        new MetisMenu('#menu', {
            toggle: false,
        });
    }
}
