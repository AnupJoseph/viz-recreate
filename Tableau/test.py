from rich import print
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,200,size=(10, 4)), columns=list('ABCD'))
df.to_csv("test_data.csv")