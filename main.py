from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from pprint import pprint
from pymongo import MongoClient

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/menu', methods=['POST'])
def menu():
    print(request.form['inputColName'])
    return render_template('menu.html', data=request.form)


@app.route('/geodata')
def geodata():
    client = MongoClient()
    db = client["Tweets"]
    delhi_collection = db["Delhi"]
    delhi_tweets = delhi_collection.find()
    data = []
    for tweet in delhi_tweets:
        data.append(tweet['geo'])
    return render_template('geodata.html', data=data)


# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
