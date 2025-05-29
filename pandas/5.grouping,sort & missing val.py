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

#   sorting 
str=grp2.reset_index()
# print(str)
sot1=str.sort_values(by='min amount')
print(sot1)
sot2=df.sort_values(by=['auto_make','vehicle_claim'])
print(sot2)
''' data type and replace
isnull() and fillna() ye do operater hai'''
show=df.auto_make.dtypes
print(show)
plo=df._c39.fillna('unknown').value_counts().sort_values(ascending=False)
# df.name.replace('kis ki ghjha','kya')
#value_counts wala fun sirf single column hi outout deta hai
print(plo)
'''rename and combining'''

'''df.rename(columns={dict})'''
'''df.rename_axis('name',axis='column/index')'''

#combining have 2 command
'''
1> pd.concat([name1, name2])
2> name1.set_index('same thinge').join(name2.set_index('same thingee'))
'''
