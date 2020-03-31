from fastapi import FastAPI
from pprint import pprint
app = FastAPI()
import inspect
import os

from .trigger import trigger

filename     = inspect.getframeinfo(inspect.currentframe()).filename
BASE_DIR     = os.path.dirname(os.path.abspath(filename))

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# @app.get("/trigger/{filepath:path}")
@app.post("/trigger/{filepath:path}")
async def read_item(filepath):
    filepath = os.path.join(BASE_DIR, filepath)
    ep = trigger(notebook_filename=filepath)
    # data = vars(ep)
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
