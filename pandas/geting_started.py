''' pandas is a python library which deals with csv file in python or exel but more powerful

we can use pandas in python by importing it in python as'''

import pandas as pd


#the first step is to read the csv file
#dhayan rakhana ki csv file code ki file mai hona chaiye

#reading CSV file
df=pd.read_csv(r"C:\Users\dell\OneDrive\Documents\GitHub\python\pandas\insurance_claims.csv")
print(df.head(10))#the first 10 rows of our data!
#alag alga requirment ke hisab se table se content nikal sakte hai
#sare columns ayenge
print(df[(df.age == 48)&(df.auto_year>=2005)&(df.fraud_reported=='Y')])

'''define  a new table by 
.Dataframe({'COLUMN KA NAAM':[CONTENT AS A LIST]})'''

df1=pd.DataFrame({'name':['acca' , 'bacca' , 'cacca' , 'dacca'] ,
                 'age' :[10, 20,30,40]
                 })
          #.to_sring(index=False) se extra column nahi aata hai
print(df1.to_string(index=False))