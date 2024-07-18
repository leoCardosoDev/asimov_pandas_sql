import pandas as pd
import numpy as np
from numpy.random import randn

# DataFrame
df = pd.DataFrame(randn(5,4), index=['A', 'B', 'C', 'D', 'E'], columns='W X Y Z'.split())
df['new'] = df['W'] + df['Y']

print(df)

