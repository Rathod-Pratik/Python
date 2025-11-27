import plotly.express as px
data={"Name":['Mohit','Krish'],"Mark":[99,99]}
f = px.pie(data, names="Name", values="Mark")

f.show()