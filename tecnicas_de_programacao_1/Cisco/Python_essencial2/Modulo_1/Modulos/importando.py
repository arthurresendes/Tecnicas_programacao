import math

print(math.factorial(5))

import time, pandas as pd
time.sleep(5)

dataframe = {"Numeros": [1,2,3,4,5,6,7,8,9,0], "Letras": ["A", "B", "C", "D", "E", "F", "G", "H", "J", "I"]}

df = pd.DataFrame(dataframe, index=False)
print(df)