import pandas as pd

## Dictionary mapping of the hedgefund name to the CIK ID
df1 = pd.read_excel('/Users/curranshah/PycharmProjects/TriCellCapital2/CIK_IDs.xlsx')
CIK_IDs_dict = dict(df1.values)