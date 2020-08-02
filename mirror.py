from flask import Flask, render_template

import features


app = Flask(__name__)

@app.route('/')
def mirror():
    return render_template('app.html',
                           gregorian_date=features.gregorian_date(),
                           hebrew_date=features.hebrew_date(),
                           currency_list=features.currency(),
                           news_list=features.news(),
                           time=features.time())


if __name__ == '__main__':
    app.run()
