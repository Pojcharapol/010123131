def f(I0,I1,I2):
    return (((I0 and I1) or not (I1 and I2)))
import pandas as pd
from itertools import product

def truth_table(f):
    values = [list(x) + [f(*x)] for x in product([False,True], repeat=f.__code__.co_argcount)]
    return pd.DataFrame(values,columns=(list(f.__code__.co_varnames) + [f.__name__]))

print(truth_table(f))
