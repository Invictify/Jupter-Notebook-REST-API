import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbparameterise import (
    extract_parameters, replace_definitions, parameter_values
)

def trigger(notebook_filename='chp-traffic.ipynb', params={}):
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)

    orig_parameters = extract_parameters(nb)
    new_nb = replace_definitions(nb, parameter_values(orig_parameters, **params))

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    r = ep.preprocess(new_nb)
    return r
