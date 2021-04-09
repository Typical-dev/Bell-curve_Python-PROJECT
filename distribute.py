import csv
import plotly.figure_factory as ff
import pandas as pd
import scipy
df = pd.read_csv("SOCR-HeightWeight.csv")
fig = ff.create_distplot([df["Weight"].tolist()], ["Weight"])
fig.show()