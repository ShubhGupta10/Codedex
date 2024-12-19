import pandas as pd
import plotly.express as px


df = pd.read_csv("C:/Users/dell/Downloads/most_subscribed_youtube_channels.csv")
df = df.replace(',', '')
print(df)
fig = px.histogram(df, x='subscribers', title='Subscriber Count')
fig.show()

fig = px.pie(df, names='category', title='YouTube Categories')
fig.show()

fig = px.box(df, y='started', title='Years Started')
fig.show()
