# SWK_Single_Sign_On

Hier befindet sich die Umsetztung meiner Bachelorarbeit bei den Stadtwerken Konstanz. 
Es wird ein Testplatz aufgebaut um SSO von FusionAuth mit verschiedenen Anwendungen zu testen.  

## Projekt einrichten

```
git clone --recurse-submodules https://github.com/JonasBechler/SWK.git
cd SWK
git checkout dev
docker-compose create
docker start sso-db-1
cat SWK_FusionAuth/backup/example_swk.sql | docker exec -i sso-db-1 psql -U postgres
docker-compose start
```


## Projekt starten
```
docker-compose up -d
```


## Projekt stoppen
```
docker-compose down
```


### Datenbank speichern
```
docker exec -t sso-db-1 pg_dumpall -c -U postgres > SWK_FusionAuth/backup/backup_`date +%d-%m-%Y"_"%H_%M_%S`
```
