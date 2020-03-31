# Jupter Notebook REST API
Run your jupyter notebooks as a REST API endpoint. This isn't a jupyter server but rather just a way to run your notebooks as a REST API Endpoint.


## Running locally

#### Clone project
```
mkdir rest-project
cd rest-project
git clone https://github.com/Invictify/Jupter-Notebook-REST-API .
```

#### Install via Pipenv
```
pipenv install
pipenv shell
```
> You can also use `pip install -r requirements.txt`


### Add your notebook(s) to "src/notebooks"
There's an example notebook already in there called `scrape.ipynb`. 


### Run locally

```
pipenv run uvicorn src.server:app --reload
```
You can also do: 

```
chmod +x run.sh
./run.sh
```

## Trigger a notebook.
With the server running, trigger notebook (relative path) like `notebooks/scrape.ipynb`

```python
import requests
r = requests.post("http://localhost:8000/trigger/notebooks/scrape.ipynb")
print(r.json())
```


## Deployment

#### Create Heroku app
You'll only have to do this 1 time.
```
heroku apps:create
```


### Using Git
```
git init
git add --all
git commit -m "Project commit"
git push heroku master
```

### Using Docker

#### Login to Heroku Container Registry
```
heroku container:login
```

#### Build & Push to Heroku
```
docker build -t -f Dockerfile.web .
heroku container:push web --recursive
heroku container:release web 
```