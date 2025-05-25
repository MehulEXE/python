import pandas as pd
df = pd.read_csv(r'C:\Users\dell\OneDrive\Documents\GitHub\python\pandas\insurance_claims.csv')
#pd.set_option('display.max_rows', 5)
print(df)

print(df.iloc[2])

a=int(input('enter the policy number '))
row=df.loc[df.policy_number==a]#creates a new database with only one entery
#print(row)
print(row.iloc[0])#aur fir usi ko call kar diya
#print(df.loc[df.policy_number==a].iloc[0])

'''iloc = interger location'''
'''.iloc[start:end , 0(for 2nd only)(baki ke index no likne hai, in [])]'''
print(df.iloc[:10, [3, 5, 9]].to_string(index=False))#remove extra index

#for .loc
print(df.loc[:5 ,['policy_number' , 'policy_state' , 'umbrella_limit']].to_string(index=False))