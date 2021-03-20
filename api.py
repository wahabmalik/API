from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/about')
def about():
    return 'this is company about page'

@app.route('/about/<string:name>/<int:years>')
def teamname(name ,years):
    return f'Hello {name}, you have {str(years)} experience in NexAI'

if __name__ == '__main__':
    app.run(debug=True)