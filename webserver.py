from flask import Flask, render_template
from icebreaker import *
#from markupsafe import escape #use this to make your inputs safer and escape HTML

app = Flask(__name__)

baseMessage = 'Your card is:'

mycard = random_card()

def resultPageTemplate(resultMessage, resultCard):
    return f'<p>{resultMessage}</p><br/><p>{resultCard}</p>'

@app.route("/")
def random_card():
    return render_template('icebreaker.html', message=baseMessage, card=mycard)