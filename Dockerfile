FROM registry.gitlab.com/what-digital/djangocms-template:2.0.0.0


COPY . /app/


RUN pip install --no-deps --no-cache-dir -r /app/backend/requirements.txt


WORKDIR /app/


WORKDIR /app/frontend/
RUN yarn install --pure-lockfile
RUN yarn run build


WORKDIR /app/
RUN python manage.py collectstatic --noinput --ignore=node_modules
