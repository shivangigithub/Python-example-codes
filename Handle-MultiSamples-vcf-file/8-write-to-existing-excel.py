import pandas as pd
import numpy as np
from openpyxl import load_workbook

path = r"/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/PrCa-venn/P2/SP19-4668.xlsx"


book = load_workbook(path)
writer = pd.ExcelWriter(path, engine = 'openpyxl')
writer.book = book

x3 = pd.read_csv("count-INDEX.txt",sep="\t")
# x3 = np.random.randn(100, 2)
df3 = pd.DataFrame(x3)

# x4 = np.random.randn(100, 2)
# df4 = pd.DataFrame(x4)

df3.to_excel(writer, sheet_name = 'INDEX',index=False,header=True)
# df4.to_excel(writer, sheet_name = 'x4')
writer.save()
writer.close()

# x1 = np.random.randn(100, 2)
# df1 = pd.DataFrame(x1)

# x2 = np.random.randn(100, 2)
# df2 = pd.DataFrame(x2)

# writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
# df1.to_excel(writer, sheet_name = 'x1')
# df2.to_excel(writer, sheet_name = 'x2')
# writer.save()
# writer.close()