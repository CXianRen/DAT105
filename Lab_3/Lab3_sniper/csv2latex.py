import pandas as pd

csv_file = 'hpps.csv'

df = pd.read_csv(csv_file)
# dft = df.transpose() 
df = df.sort_values(by=['EDP'],ascending=True)

latex_table = df.to_latex(index=False,escape=False)
print(latex_table)