import pandas as pd
import csv
import plotly_express as exp

df=pd.read_csv('data.csv')

lev_1=[]
lev_2=[]
lev_3=[]
lev_4=[]

data_csv=list(csv.reader(open('data.csv')))
data_csv.pop(0)

def group_data(p):
    level='Level '+p
    for i in data_csv:
        raw=i[1]
        if raw==level:
            if p=='1':
                lev_1.append(i[2])
            elif p=='2':
                lev_2.append(i[2])
            elif p=='3':
                lev_3.append(i[2])
            elif p=='4':
                lev_4.append(i[2])

def average_attempt(arr):
    sum=0
    num=len(arr)
    for i in arr:
        sum+=int(i)
    mean=sum/num

    return mean

for i in range(1,5):
    group_data(str(i))

a=average_attempt(lev_1)    
b=average_attempt(lev_2)
c=average_attempt(lev_3)
d=average_attempt(lev_4)

print("")
print("")

print("Average attempts of level 1 is, ",a,". Average attempts of level 2 is, ",b,". Average attempts of level 3 is, ",c,". Average attempts of level 4 is, ",d)

print(df.groupby("level")["attempt"].mean())

fig=exp.bar(df,x='attempt',y='level')
fig.show()