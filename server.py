from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'movintarg'

@app.route('/')
def index():
    if 'ranNum' not in session:
        session['ranNum'] = random.randrange(0, 101)
    if 'msg' not in session:
        session['msg'] = ''
    return render_template('index.html', msg=session['msg'])

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['number'])
    if guess == session['ranNum']:
        session['msg'] = "That was the number!"
    if guess > session['ranNum']:
        session['msg'] = "Too high!"
    elif guess < session['ranNum']:
        session['msg'] = "Too low!"
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('ranNum')
    session.pop('msg')
    return redirect('/')

app.run(debug=True)