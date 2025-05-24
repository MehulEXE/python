import pandas as pd

"""METHOD-1 define  a new table by 
.Dataframe({'COLUMN KA NAAM':[CONTENT AS A LIST]})
just like dictionary"""

df1 = pd.DataFrame(
    {"name": ["acca", "bacca", "cacca", "dacca"], "age": [10, 20, 30, 40]}
)
#column wise entery
# .to_sring(index=False) se extra column nahi aata hai
print(df1.to_string(index=False))
"""METHOD-2 FOR CREATING TABLES
data entery by list method
       pd.dataframes([lists],columns=[])"""
#rows wise entery
df2 = pd.DataFrame(
    [
        [1, "mehul", "pass", 98],
        [2, "subansh", "pass", 78],
        [2, "pavitra", "pass", 90],
        [4, "sakashi", "pass", 80],
        [5, "rudrax", "fail", 32],
    ],
    columns=["S.no.", "name", "status", "total percentile"],
)
print(df2.to_string(index=False))
print(df2.name)
"""METHOD-3 FOR CREATING TABLES
.series se column wise data feed hota hai"""

animal = ["cat", "dog", "parrot", "fish", "lepord"]
quantity = [10, 25, 12, 45, 1]
df3 = pd.Series(quantity, index=animal, name="pet shop")
print(df3)
