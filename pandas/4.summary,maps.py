import pandas as pd
df = pd.read_csv(r'C:\Users\dell\OneDrive\Documents\GitHub\python\pandas\insurance_claims.csv')
'''summary have main four function
1.describe()
2.mean()
3.unique()
4.value_counts'''
#info about age
print(df.age.describe())
#info about dates
print(df.policy_bind_date.describe())
print(df.insured_sex.unique())
print(df.property_claim.mean())
print(df.insured_relationship.value_counts())

'''      maps      '''
