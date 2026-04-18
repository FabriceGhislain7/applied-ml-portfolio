# Applied ML Portfolio

Monorepo Streamlit portfolio for applied machine learning and data analytics projects.

The repository keeps each project shaped like a standalone application while exposing all projects through one Render deployment.

## Projects

- `projects/air_quality`: air-quality sensor calibration and regression dashboard.
- `projects/titanic`: Titanic survival analysis dashboard.

## Architecture

```text
app.py
projects/
  air_quality/
    app.py
    pages/
    src/
    data/
    tests/
    docs/
  titanic/
    app.py
    pages/
    src/
    data/
    tests/
    docs/
shared/
```

Each project keeps its own application structure. The root `app.py` only exposes a single portfolio navigation for local use and Render deployment.

## Local Run

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe -m streamlit run app.py
```

## Render

Render starts the portfolio with:

```text
streamlit run app.py --server.headless true --server.port $PORT --server.address 0.0.0.0
```
