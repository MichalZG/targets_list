# targets_list

# INSTALL
* Clone repo
* Go to target_list directory
* Create ```.env``` file with following configs (change values if you want):
```python
DATABASE_SECRET_KEY=your_secret_key    
    
DATABASE_DEBUG=False    
WEB_DEBUG=False    
   
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
   
DATABASE_PORT=8000
WEB_PORT=8050
   
DEFAULT_LONGITUDE=38    
DEFAULT_LATITUDE=37    
```
*  Build application and database images
    * ```docker-compose build``` 
    * ```bash install.sh```

# RUN
* ```docker-compose up -d```
* Open in browser:
    * http://127.0.0.1:WEB_PORT - web_app
    * http://127.0.0.1:DATABASE_PORT/admin - database

# STOP
* ```docker-compose stop```
