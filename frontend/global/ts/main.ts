import {LoadAlgoliaSearch} from 'global/ts/algolia-search';
import {initMainMenu} from 'global/ts/main-menu';
import {main} from 'global/ts/on-page-edit-reload'


document.addEventListener('DOMContentLoaded', () => {
    main();
    LoadAlgoliaSearch();
    initMainMenu();
})
