import {LoadAlgoliaSearch} from 'global/ts/algolia-search';
import {initMainMenu} from 'global/ts/main-menu';
import {initOnPageEditReloadScript} from 'global/ts/on-page-edit-reload';


document.addEventListener('DOMContentLoaded', () => {
    main();
    LoadAlgoliaSearch();
    initMainMenu();
}, {once: true})
