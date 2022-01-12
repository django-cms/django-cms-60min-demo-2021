Currently this project has 3 live instances:
- 1fortheworld.org chapter's resource - http://chapters.1fortheworld.org/
- it's the official demo for [DjangoCMS project](https://github.com/divio/django-cms/) - https://control.divio.com/demo/get-new/
- Effective Altruism Netherlands - https://effectiefaltruisme.nl/en/


Development Setup
-------------------------------------------------------------------------------

See the general [setup instructions](https://github.com/django-cms/djangocms-template/blob/master/docs/local-setup-instructions.md)

[Project intro & guidelines](https://github.com/django-cms/djangocms-template/blob/master/docs/README.md)

You can download and import the demo data [here](https://drive.google.com/drive/folders/1Q3ZyK4uvCAWR-qWa3Nk1zL3a7RyQgEJM?usp=sharing). In order to import the data:
- extract data.zip into the root directory of the project
- docker-compose up
- import demo-2021-07-09 into the `db` database



Codebase Source
-------------------------------------------------------------------------------

This project is built upon https://gitlab.com/effective-altruism/ea-cms-template/ (with friendly permission from EA).


## Tech Stack

- Debian 10
- Python 3.9
- Django 3.1
- DjangoCMS 3.8
- Node 14
- Webpack 5
- TypeScript 4
- Bootstrap 4
