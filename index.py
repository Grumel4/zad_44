import pandas as pd
import random

# Данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# One-hot encoding вручную
whoAmI_mapping = {'robot': [1, 0], 'human': [0, 1]}
data_encoded = pd.DataFrame()
for key, value in whoAmI_mapping.items():
  data_encoded[key] = data['whoAmI'].apply(lambda x: value[0] if x == key else value[1])

print(data_encoded)
