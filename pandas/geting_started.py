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


#for specific row and column
print(df.loc[
    (df.age == 48)&                       #cond's for rows
    (df.auto_year>=2005)&
    (df.fraud_reported=='Y'),
    ['age','policy_bind_date','auto_year']  #comd's for column
    ])

