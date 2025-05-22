''' pandas is a python library which deals with csv file in python or exel but more powerful

we can use pandas in python by importing it in python as'''

import pandas as pd


#the first step is to read the csv file
#dhayan rakhana ki csv file code ki file mai hona chaiye

#reading CSV file
df=pd.read_csv(r"C:\Users\dell\OneDrive\Documents\GitHub\python\pandas\insurance_claims.csv")
print(df.head(10))#the first 10 rows of our data!
df.tail(12)#last ki 12 values
#alag alga requirment ke hisab se table se content nikal sakte hai
#sare columns ayenge
print(df[(df.age == 48)&(df.auto_year>=2005)&(df.fraud_reported=='Y')])

'''define  a new table by 
.Dataframe({'COLUMN KA NAAM':[CONTENT AS A LIST]})
just like dictionary'''

df1=pd.DataFrame({'name':['acca' , 'bacca' , 'cacca' , 'dacca'] ,
                 'age' :[10, 20,30,40]
                 })
          #.to_sring(index=False) se extra column nahi aata hai
print(df1.to_string(index=False))
#for specific row and column
print(df.loc[
    (df.age == 48)&                       #cond's for rows
    (df.auto_year>=2005)&
    (df.fraud_reported=='Y'),
    ['age','policy_bind_date','auto_year']  #comd's for column
    ])
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
