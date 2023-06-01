import paramiko
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
import random
import json
import pymysql
app = FastAPI()

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='HealthHive'
)
cursor = conn.cursor()


@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/home_jv", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("home_jv.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/login", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("login.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/signup", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("signup.html") as html:
        return HTMLResponse(content=html.read())
    

@app.get("/style.css")
def get_css() -> FileResponse:
    return FileResponse("style.css", media_type="text/css")
    

@app.get("/index.js", response_class=HTMLResponse)
def get_js() -> HTMLResponse:
    with open("./public/index.js") as js:
        return HTMLResponse(content=js.read(), media_type="application/javascript")
    

@app.get("/home_jv.js", response_class=HTMLResponse)
def get_js() -> HTMLResponse:
    with open("./public/home_jv.js") as js:
        return HTMLResponse(content=js.read(), media_type="application/javascript")


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
    with open("./public/signup.js") as js:
        return HTMLResponse(content=js.read(), media_type="application/javascript")


@app.post("/register")
def register(
    username: str = Form(...),
    password: str = Form(...),
    info: str = Form(...)
):

    user_id = random.randint(100000, 999999)

    cursor.execute(
        "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)",
        (user_id, username, password)
    )
    conn.commit()

    cursor.execute(
        "INSERT INTO user_info (user_id, info) VALUES (%s, %s)",
        (user_id, info)
    )
    conn.commit()
    
    # cursor.execute(
    #     "INSERT INTO user_items (user_id) VALUES (%s)",
    #     (user_id)
    # )
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


@app.post("/ssh_open")
async def ssh_open(password: str = Body(...)):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("raspberrypi.local", username="pi", password=password)
    ssh.close()
    return {"success": True}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6789)
