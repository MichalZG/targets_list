# Target list

Target list is composision of website and objects database, 
provides a quick look at which astronomical objects are visible and where they are on the sky.
Moreover, you can find informations about sunset, sunrise, Moon phase/alt/az or LST for specific location and time.

After installation you have to add some "target group" and assign new objects to it. 
You can do it with django admin interface.
Then, open website and check your objects visibility. 

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
    * http://127.0.0.1:DATABASE_PORT/admin - database

## STOP
* ```docker-compose stop```
