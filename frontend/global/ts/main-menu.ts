const MetisMenu = require('metismenujs');
require('metismenujs/dist/metismenujs.min.css');



export function initMainMenu() {
    new MetisMenu('#menu', {
        toggle: false,
    });
}
