import pandas as pd
df = pd.read_csv("people.csv")
print(df)
#df.head()       # Show first 5 rows
#df.tail()       # Show last 5 rows
#df.info()       # Show info (column names, types, null values)
#df.describe()   # Show basic stats (mean, std, min, max)
print(df.columns)
print(df['Name']) # show name column
print(df[["Name","City"]]) #show name and city column
print(df.iloc[0]) #show first row
print(df[df["Age"]>27]) #show rows where age>27
print(df[df["Salary"]>500000]) #show rows where salary>50000
print(df["Age"].describe()) #show  statitcs of age column
print(df.sort_values(by="Age")) #sort by age ascending
print(df.sort_values("Age",ascending=False)) #sort by age descending
print(df.groupby("Graduation_batch")["Salary"].mean()) #average salary by graduation batch
print(df.groupby("City")["Salary"].mean()) #average salary by city
print(df.groupby("Occupation")["Salary"].mean()) #average salary by occupation
print(df.groupby("Graduation_batch")["Age"].max()) #max age by graduation batch
print(df.groupby("City")["Age"].max()) #max age by city
print(df.groupby("Occupation")["Age"].max()) #max age by occupation
print(df.groupby("Graduation_batch")["Age"].min()) #min age by graduation batch
print(df.groupby("City")["Age"].min()) #min age by city
print(df.groupby("Occupation")["Age"].min()) #min age by occupation
print(df.groupby("Graduation_batch")["Salary"].min()) #min salary by graduation batch