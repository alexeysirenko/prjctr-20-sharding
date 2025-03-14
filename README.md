# prjctr-20-sharding

## Without sharding

```
docker compose -f docker-compose.noshards.yml up -d
PGPASSWORD=postgres docker exec -i postgresql-b psql -U postgres -d books_db < scripts/no-shards/init.sql
docker exec -it app python write_data.py 100000 --batch-size 10000
```

### Result without sharding

```
Total books inserted: 100000
Batch size: 10000
Total time: 22.76 seconds
Average rate: 4394.32 books per second
```

### Stop the noshards cluster

```
docker compose -f docker-compose.noshards.yml down
```

## FDW (Foreign Data Wrapper) approach

```
docker compose -f docker-compose.fdw.yml up -d
PGPASSWORD=postgres docker exec -i postgresql-b1 psql -U postgres -d books_db < scripts/fdw/shard-1.sql
PGPASSWORD=postgres docker exec -i postgresql-b2 psql -U postgres -d books_db < scripts/fdw/shard-2.sql
PGPASSWORD=postgres docker exec -i postgresql-b psql -U postgres -d books_db < scripts/fdw/main.sql
docker exec -it app python write_data.py 100000 --batch-size 10000
```

### Result with FDW sharding

```
Total books inserted: 100000
Batch size: 10000
Total time: 34.50 seconds
Average rate: 2898.71 books per second
```

### Stop the fdw cluster

```
docker compose -f docker-compose.fdw.yml down
```

## Citus approach

```
docker compose -f docker-compose.citus.yml up -d
PGPASSWORD=postgres docker exec -i postgresql-b psql -U postgres -d books_db < scripts/citus/main.sql
docker exec -it app python write_data.py 100000 --batch-size 10000
```

### Result with Citus sharding

```
Total books inserted: 100000
Batch size: 10000
Total time: 26.91 seconds
Average rate: 3716.71 books per second
```

### Stop the citus cluster

```
docker compose -f docker-compose.citus.yml down
```
