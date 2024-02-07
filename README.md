# Best Job Portal in Armenia

Welcome to the Best Job Portal in Armenia! This repository contains the source code for a simple and intuitive job portal web application built with FastAPI, SQLite, HTML, CSS, and JavaScript.

## Installation

To run this application locally on your machine, follow these steps:

### 1. Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/best-job-portal.git
cd best-job-portal
# Create a virtual environment (optional but recommended)
python3 -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
uvicorn main:app --reload
