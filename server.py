from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', template_folder='templates',static_folder='static')

@app.route('/learn-with-us')
def learning():
    return render_template('learning.html', template_folder='templates',static_folder='static')

@app.route('/practice-skills')
def practicing():
    return render_template('practice.html', template_folder='templates',static_folder='static')

@app.route('/compete-with-others')
def compete():
    return render_template('compete.html', template_folder='templates',static_folder='static')

@app.route('/jobs-offers')
def jobs():
    return render_template('jobs.html', template_folder='templates',static_folder='static')

@app.route('/sign-in')
def sign_in():
    return render_template('sign_in.html', template_folder='templates',static_folder='static')

app.run(debug=True)