import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


def romanToInt(s):
    myTable = {
        "I" : 1, 
        "V" : 5,
        "X" : 10, 
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    
    result = 0 
    myLength = len(s)
    current = 0 
    prev = 0 
    for i in range(myLength):
        current = myTable[s[myLength-i-1]]
        if current < prev:
            result -= current
        else:
            result += current 
        prev = current
    
    return result

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    roman = request.form.get("roman")
    result = romanToInt(roman)
    return render_template("result.html", roman = result)

