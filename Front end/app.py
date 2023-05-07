import requests
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import Depends
from fastapi import Header, HTTPException
from fastapi import BackgroundTasks
from fastapi import Response
from fastapi import FastAPI, Form, Body
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
import uvicorn
from fastapi.responses import FileResponse
from fastapi import FastAPI, Form, Body, Request, Query
from fastapi.templating import Jinja2Templates
from datetime import datetime
import json
import pymysql
app = FastAPI()

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='users'
)
cursor = conn.cursor()


@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/home", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("home.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/login", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("login.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/signup", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("registration.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/login.js", response_class=HTMLResponse)
def get_js() -> HTMLResponse:
    with open("./public/login.js") as js:
        return HTMLResponse(content=js.read(), media_type="application/javascript")


@app.get("/home.js", response_class=HTMLResponse)
def get_js() -> HTMLResponse:
    with open("./public/home.js") as js:
        return HTMLResponse(content=js.read(), media_type="application/javascript")


@app.get("/index.js", response_class=HTMLResponse)
def get_js() -> HTMLResponse:
    with open("./public/index.js") as js:
        return HTMLResponse(content=js.read(), media_type="application/javascript")


@app.get("/signup.js", response_class=HTMLResponse)
def get_js() -> HTMLResponse:
    with open("./public/registration.js") as js:
        return HTMLResponse(content=js.read(), media_type="application/javascript")


@app.post("/register")
def register(
    username: str = Form(...),
    password: str = Form(...),
    info: str = Form(...)
):

    user_id = randint(100000, 999999)

    cursor.execute(
        "INSERT INTO users (id, username) VALUES (%s, %s, %s)",
        (user_id, username)
    )
    conn.commit()

    cursor.execute(
        "INSERT INTO user_info (user_id, user_password, info) VALUES (%s, %s, %s)",
        (user_id, password, info)
    )
    conn.commit()

    return RedirectResponse(url="/login", status_code=302)


@app.post("/login_user")
def login_user(username: str = Body(...), password: str = Body(...)):
    # Check if the username or email and password are correct
    cursor.execute(
        "SELECT * FROM users WHERE (username=%s) AND password=%s",
        (username, password)
    )
    result = cursor.fetchone()

    if result is None:
        return "Incorrect username or password"
    else:
        login_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            "INSERT INTO session (id, created_at) VALUES (%s, %s)",
            (result[0], login_time)
        )
        conn.commit()
        print(result[0], login_time)
        return result
