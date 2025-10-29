from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Codespaces Demo</title>
    </head>
    <body>
        <h1>Hello from GitHub Codespaces!</h1>
        <p>Email: 23f2005282@ds.study.iitm.ac.in</p>
        <p>Status: Running</p>
        <!-- 23f2005282@ds.study.iitm.ac.in -->
    </body>
    </html>
    """
