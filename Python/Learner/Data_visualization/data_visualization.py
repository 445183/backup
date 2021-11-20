import pandas as pd
import plotly.express as px

data_frame=pd.read_csv("data.csv")
fig=px.bar(data_frame,x='Country',y='InternetUsers')

fig2=px.scatter(data_frame,x='Country',y='Per capita')

fig.show()
fig2.show()

data_frame=pd.read_csv('line_chart.csv')
fig=px.line_3d(data_frame,z='Country',x='Year',y='Per capita income',color='Country')
fig.show()