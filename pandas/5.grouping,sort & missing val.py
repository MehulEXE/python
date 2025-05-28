import pandas as pd
df = pd.read_csv(r'C:\Users\dell\OneDrive\Documents\GitHub\python\pandas\insurance_claims.csv')

grp1 = df.groupby('collision_type').collision_type.count()
print(grp1)

'''df.groupby([list]).agg(['max'])'''
grp2 = df.groupby(['insured_sex', 'incident_severity', 'insured_education_level']).total_claim_amount.agg(['min', 'max'])
grp2 = grp2.rename(columns={'min': 'min amount', 'max': 'max amount'})
print(grp2)
mi=grp2.index
print(type(mi))# <class 'pandas.core.indexes.multi.MultiIndex'>
