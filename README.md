# SWK_Single_Sign_On

This is the code entry point for my bachelor thesis. It is an example how different Applicatins can work together in a native environment. The following lines of code help to reproduce the final example. 

It is important mention that a specific local ip adresses must be used for the host system to get it up and running which is 192.168.178.0 . This can be changen in the FusionAuth's Application settings at http://localhost:9011/ with the admin user admin@admin.de and its password adminadmin. An example user given as maxmuster@web.de and it's simple password 12345678 . 

A more specific overview is given in the Report under document.pdf which will be released when the project is finished.

## Setup

```
git clone --recurse-submodules https://github.com/JonasBechler/SWK.git
cd SWK
git checkout dev
docker-compose create
docker start sso-db-1
cat SWK_FusionAuth/backup/example_swk.sql | docker exec -i sso-db-1 psql -U postgres
docker-compose start
```


## Start up
```
docker-compose up -d
```


## Shut down
```
docker-compose down
```


### Save Settings
```
docker exec -t sso-db-1 pg_dumpall -c -U postgres > SWK_FusionAuth/backup/backup_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```
