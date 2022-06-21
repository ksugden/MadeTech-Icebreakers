from flask import Flask, render_template
from randomcard import *

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def random_card():
    baseMessage = 'Your card is:'
    mycard = RandomCard()
    return render_template('icebreaker.html', message=baseMessage, card=mycard.text)
