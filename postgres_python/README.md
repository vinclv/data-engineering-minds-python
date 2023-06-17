## Steps to execute the code

```
cd python_postgres
docker-compose -f docker-compose.yaml up -d
```

### To run the python app locally

* Replace *postgres* with *localhost* for the host in SQLAlchemy [*create_engine*](https://github.com/vinclv/data-engineering-minds-python/blob/main/postgres_python/postgres.py#L6).
* Install virtual environment, requirements and then run the python script.
```
pip3 install virtualenv virtualenvwrapper
python3 -m venv venv
source venv/bin/activate
cd python_postgres
pip3 install -r requirements.txt
python3 postgres.py
```
### Note
* I would recommend to use either Python 3.6 or Python 3.9.
* The detailed step-by-step implementation can be found on my YouTube video.
  `