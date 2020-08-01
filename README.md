# targets_list

# Install
* clone repo
* go to target_list directory
* create ```.env``` file with this configs:
```python
DATABASE_SECRET_KEY=etsttesets    
    
DATABASE_DEBUG=False    
WEB_DEBUG=False    
    
DATABASE_PORT=8111    
WEB_PORT=8112    
    
DEFAULT_LONGITUDE=38    
DEFAULT_LATITIUDE=37    
```
* docker-compose up -d
* go to address http://127.0.0.1:8050 - web_app
* go to address http://127.0.0.1:8000/admin - database

