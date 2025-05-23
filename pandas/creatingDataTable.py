import pandas as pd
df=pd.read_csv(r"C:\Users\dell\OneDrive\Documents\GitHub\python\pandas\insurance_claims.csv")
'''define  a new table by 
.Dataframe({'COLUMN KA NAAM':[CONTENT AS A LIST]})
just like dictionary'''

df1=pd.DataFrame({'name':['acca' , 'bacca' , 'cacca' , 'dacca'] ,
                 'age' :[10, 20,30,40]
                 })
          #.to_sring(index=False) se extra column nahi aata hai
print(df1.to_string(index=False))
'''data entery by list method
       pd.dataframes([lists],columns=[])'''
df2=pd.DataFrame([
    [1,'mehul','pass',98],
    [2,'subansh','pass',78],
    [2,'pavitra','pass',90],
    [4,'sakashi','pass',80],
    [5,'rudrax','fail',32]],
    columns=['S.no.','name','status','total percentile']
)
print(df2.to_string(index=False))