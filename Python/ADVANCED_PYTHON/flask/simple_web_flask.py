from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    name = 'uniminin'
    return render_template('index.html', name=name )

# /peppy
@app.route('/peppy')
def peppy():
    return "peppy doesn't suck :("

# check /name/any_name
@app.route('/name/<name>')
def greet(name):
    return f'Hello {name}'

# Run the server
app.run(host="0.0.0.0", port=5000)
