# prjctr-20-sharding

```
docker compose up -d
docker exec -it app python seed.py
docker exec -it app python write_data.py 100 --batch-size 20
```

## Testing insertion speed

```
docker exec -it app python write_data.py 100000 --batch-size 10000
```

### Without sharding

```
Total books inserted: 100000
Batch size: 10000
Total time: 22.17 seconds
Average rate: 4510.36 books per second
```
