import pandas as pd

csv_file = 'task_1.csv'

df = pd.read_csv(csv_file)
# dft = df.transpose() 
# df = df.sort_values(by=[' data_size(MB)','thread_num'])

latex_table = df.to_latex(index=False,escape=False)
print(latex_table)