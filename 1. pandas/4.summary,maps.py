import pandas as pd

df = pd.read_csv(r"C:\Users\dell\OneDrive\Documents\GitHub\python\pandas\insurance_claims.csv")
"""summary have main four function
1.describe()
2.mean()
3.unique()
4.value_counts"""
# info about age
print(df.age.describe())
# info about dates
print(df.policy_bind_date.describe())
print(df.insured_sex.unique())
print(df.property_claim.mean())
print(df.insured_relationship.value_counts())

# maps
'''2 type of function
1.map(lambda kis ki jhagha: kya)

2.apply(kya,axis='column /index')
isko use karne ke liye phale def fun bao
def som(row):row.change=row. '''
print(df)
ext=df.auto_year.map(lambda auto: auto-2000)
print(ext)
def year(row):
    row.auto_year=row.auto_year -2000
    return row
ext2=df.apply(year, axis='columns')
print(ext2)