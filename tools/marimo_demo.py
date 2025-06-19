import marimo
import plotly.express as px

mo = marimo.App()

@mo.cell
def _():
    slider = mo.ui.slider(1, 10, 5, label="Number of points")
    return slider

@mo.cell
def _(slider):
    import pandas as pd
    df = pd.DataFrame({'x': range(slider.value), 'y': [i**2 for i in range(slider.value)]})
    fig = px.line(df, x='x', y='y', markers=True)
    fig.update_layout(width=500, height=300)
    fig.show()
    return df

if __name__ == "__main__":
    mo.main()
