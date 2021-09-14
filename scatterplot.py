import pandas as pd
import plotly.express as px

sf =pd.read_csv(r"C:\Users\lokita\Desktop\Dherya\P 103\cases.csv")
fig=px.scatter(sf,x = "date",y = "cases",color = "country")
fig.show()