from fastapi import FastAPI, Request
from pprint import pprint
app = FastAPI()
import inspect
import os

from .trigger import trigger

filename     = inspect.getframeinfo(inspect.currentframe()).filename
BASE_DIR     = os.path.dirname(os.path.abspath(filename))
NOTEBOOKS_DIR = BASE_DIR + '/notebooks'

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/trigger/{filepath:path}")
async def read_item(filepath, request: Request):
    filepath = os.path.join(NOTEBOOKS_DIR, filepath)
    ep = trigger(notebook_filename=filepath, params=request.query_params)
    
    cells = ep[0]['cells']
    all_outputs = []
    for i, cell in enumerate(cells):
        output = cell.get("outputs", [])
        if len(output) > 0:
            output_data = {
                "cell": i,
                "output": output
            }
            all_outputs.append(output_data)
    return {"filepath": filepath, "all_outputs": all_outputs}
