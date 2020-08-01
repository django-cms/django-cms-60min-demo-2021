FROM divio/base:4.18-py3.6-slim-stretch


RUN apt-get update --quiet && apt-get install --yes git gnupg2 apt-transport-https fish gcc nano


# yarn
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update --quiet && apt-get install --yes yarn nodejs


RUN yarn install --pure-lockfile
RUN yarn run build
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
RUN DJANGO_MODE=build python manage.py compilemessages
