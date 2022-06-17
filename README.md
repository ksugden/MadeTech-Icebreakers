# MadeTech-Icebreakers
Simple icebreaker app from Made Tech icebreaker cards.

---

## Prerequisites
- Python 3, with packages pip and venv
- Git
## Installation
1. Clone the repo: Open a terminal or command prompt in the folder you want the code, then run `git clone https://github.com/JazJax/MadeTech-Icebreakers.git`
2. Navigate into the folder: usually by running `cd MadeTech-Icebreakers`
3. Create a python virtual environment using the venv utility: `python3 -m venv .venv`
4. Activate the virtual environment: `source .venv/bin/activate`
5. Restore packages: `pip install -r requirements.txt`

## Running Locally
- Ensure your virtual environment is activated (see above)
- In the terminal run `export FLASK_APP=webserver` to tell your terminal where your server is
- To run in development mode (*only* in development mode!) run `export FLASK_ENV=development`
- Run using flask run