Install Postgres in docker
```
docker run -d --name my_postgres -v my_dbdata:/var/lib/postgresql/data -p 54320:5432 -e POSTGRES_PASSWORD=my_password postgres:13
```