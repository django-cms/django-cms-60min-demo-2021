import * as Sentry from '@sentry/browser';


window.$ = window.jQuery = require('jquery');


require('bootstrap');
require('./main.scss');


require('lightgallery.js/dist/css/lightgallery.min.css');


// djangocms-bootstrap4 icons
require('@fortawesome/fontawesome-free/scss/fontawesome.scss');
require('@fortawesome/fontawesome-free/scss/brands.scss');
require('@fortawesome/fontawesome-free/scss/solid.scss');
require('@fortawesome/fontawesome-free/scss/regular.scss');


Sentry.init({
    dsn: '',
    environment: DJANGO.env,
});
