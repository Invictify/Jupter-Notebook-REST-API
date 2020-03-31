import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def trigger(notebook_filename='chp-traffic.ipynb'):
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    r = ep.preprocess(nb)
    return r
