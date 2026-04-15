import numpy as np
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# -----------------------------
# 1. Create Data (NumPy + Pandas)
# -----------------------------
np.random.seed(1)

df = pd.DataFrame({
    "Day": np.arange(1, 31),
    "Sales": np.random.randint(100, 1000, 30),
    "Profit": np.random.randint(50, 500, 30),
    "Category": np.random.choice(["Electronics", "Clothing", "Food"], 30)
})

# -----------------------------
# 2. Create Dash App
# -----------------------------
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Smart Business Dashboard", style={'textAlign': 'center'}),

    # Dropdown Filter
    dcc.Dropdown(
        id='category_filter',
        options=[{"label": i, "value": i} for i in df["Category"].unique()],
        value="Electronics",
        clearable=False
    ),

    # Graphs
    dcc.Graph(id='sales_graph'),
    dcc.Graph(id='profit_graph')
])

# -----------------------------
# 3. Callback (Interactive)
# -----------------------------
@app.callback(
    [Output('sales_graph', 'figure'),
     Output('profit_graph', 'figure')],
    [Input('category_filter', 'value')]
)
def update_graph(selected_category):
    filtered_df = df[df["Category"] == selected_category]

    fig1 = px.line(filtered_df, x="Day", y="Sales",
                   title=f"{selected_category} Sales Trend")

    fig2 = px.bar(filtered_df, x="Day", y="Profit",
                  title=f"{selected_category} Profit Analysis")

    return fig1, fig2

# -----------------------------
# 4. Run App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
