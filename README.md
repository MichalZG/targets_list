# Target list

Target list is composision of website and objects database, 
which provides a quick look at which astronomical objects are visible and where they are on the sky for specific location and time.
Moreover, you can find there basic informations about sunset, sunrise, Moon phase/alt/az and LST.
Objects table allows advanced filtering and sorting, informations about syntax you can find [here](https://dash.plotly.com/datatable/filtering).

Live demo: http://104.248.129.33:8888/

## INSTALL
* Clone repo
* Go to target_list directory
* Create ```.env``` file with following configs (change values if you want):
```python
DATABASE_SECRET_KEY=fasdfksdajlu34w423423
DATABASE_ADMIN_NAME=adminname
DATABASE_ADMIN_PASS=adminpass

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

DATABASE_DEBUG=False
WEB_DEBUG=False

DATABASE_PORT=8889
WEB_PORT=8888

DEFAULT_LONGITUDE=37
DEFAULT_LATITUDE=38
```
*  Build application and database images
    * ```bash install.sh```

## RUN
* ```docker-compose up -d```
* Open in browser:
    * http://127.0.0.1:WEB_PORT - web_app
    * http://127.0.0.1:DATABASE_PORT/admin - database admin interface 

## ADD OBJECTS
Each objects in the database have to be assigned to the objects group.
The first step to add a new object in empty database is creation of objects group.
For this, open a admin interface and choose *Target groups* -> *Add*.
Then you can add new objects with *Target* -> *Add* and assign them to the choosed group. 
Refresh web_app website and check the objects visibility.

## STOP
* ```docker-compose stop```
