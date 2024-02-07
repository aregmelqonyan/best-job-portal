from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import sqlite3
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")

templates = Jinja2Templates(directory="templates")


class Job(BaseModel):
    title: str
    description: str
    requirements: str


conn = sqlite3.connect('jobs.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS jobs
             (id INTEGER PRIMARY KEY, title TEXT, description TEXT, requirements TEXT)''')
conn.commit()
conn.close()


@app.get("/view_jobs/", response_class=HTMLResponse)
async def view_jobs(request: Request):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM jobs')
    jobs = c.fetchall()
    conn.close()
    return templates.TemplateResponse("read_jobs.html", {"request": request, "jobs": jobs})


@app.get("/create_job/", response_class=HTMLResponse)
async def create_job_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/create_job/")
async def create_job(request: Request, title: str = Form(...), description: str = Form(...), requirements: str = Form(...)):
    job = Job(title=title, description=description, requirements=requirements)
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('INSERT INTO jobs (title, description, requirements) VALUES (?, ?, ?)', (job.title, job.description, job.requirements))
    conn.commit()
    conn.close()
    return templates.TemplateResponse("create_job_success.html", {"request": request, "title": title, "description": description, "requirements": requirements})


@app.get("/create_job_success/", response_class=HTMLResponse)
async def create_job_success(request: Request):
    return templates.TemplateResponse("create_job_success.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    return templates.TemplateResponse("introduction.html", {"request": request})


@app.post("/apply_job/{job_id}")
async def apply_job(request: Request):
    return templates.TemplateResponse("apply_success.html", {"request": request})
