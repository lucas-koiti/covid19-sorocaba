import pandas as pd
import plotly.express as px

dataf = pd.read_csv('../dados/planilha_csv/dados.csv')

fig = px.line(dataf, x = 'Dia', y = 'Confirmados', title='Covid-19 Casos Confirmados')
fig.show()

fig = px.line(dataf, x = 'Dia', y = 'Obitos', title='Covid-19 Óbitos em Sorocaba')
fig.show()