# SWK_Single_Sign_On

## Projekt einrichten

```
git clone --recurse-submodules git@github.com:JonasBechler/SWK.git
cd SWK
docker-compose create
docker start sso-db-1
cat SWK_FusionAuth/backup/example_swk.sql | docker exec -i sso-db-1 psql -U postgres
docker-compose start
```


## Projekt starten
```
docker-compose up
```


## Projekt stoppen
```
docker-compose down
```


### Datenbank speichern
```
docker exec -t swk_fusionauth-db-1 pg_dumpall -c -U postgres > backup/backup_`date +%d-%m-%Y"_"%H_%M_%S`
```
