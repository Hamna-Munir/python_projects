import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "20", orientation = "v",
    measure = ["relative", "relative", "total", "relative", "relative", "total"],
    x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
    textposition = "outside",
    text = ["+60", "+80", "", "-40", "-20", "Total"],
    connector = {"line":{"color":"rgb(63, 63, 63)"}}
))

fig.update_layout(
    title = "Profit and loss statement 2024",
    showlegend = True
)

fig.show()
