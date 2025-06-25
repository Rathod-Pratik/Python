import plotly.express as px
data={"Name":['Mohit','Krish'],"Mark":[99,99]}
# f=px.bar(data,x="Name",y="Age")
# f=px.line(data,x="Name",y="Age")
# f=px.scatter(data,x="Name",y="Age")
f = px.pie(data, names="Name", values="Mark")

f.show()