Install Postgres in docker
```
docker run -d --name my_postgres -v my_dbdata:/var/lib/postgresql/data -p 54320:5432 -e POSTGRES_PASSWORD=my_password postgres:13
```

[Schema migrations with Alembic, Python and PostgreSQL](https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/)

На основе скриптов создать таблицы
```
alembic revision --autogenerate -m "add root_cause table"
```

Обновить БД
```
alembic upgrade head
```