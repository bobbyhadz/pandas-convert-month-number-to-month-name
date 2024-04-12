# Pandas: Convert Month Number to Month Name

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'start_month': [1, 2, 4, 7, 9],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

df['start_month'] = pd.to_datetime(
    df['start_month'], format='%m').dt.month_name()

#     name start_month  salary
# 0  Alice     January   175.1
# 1  Bobby    February   180.2
# 2   Carl       April   190.3
# 3    Dan        July   205.4
# 4  Ethan   September   210.5
print(df)