import marimo

app = marimo.App()

@app.cell
def _():
    import marimo as mo
    return mo

@app.cell
def _(mo):
    slider = mo.ui.slider(0, 10, value=5, label="Select a number")
    return slider, mo

@app.cell
def _(slider, mo):
    mo.md(f"You selected **{slider.value}**")

if __name__ == "__main__":
    app.run()
