from flask import Flask, render_template

import features


app = Flask(__name__)


@app.route('/')
def mirror():
    return render_template('mirror.html',
                           gregorian_date=features.gregorian_date(),
                           currency_list=features.currency_string(),
                           news_list=features.news(),
                           time=features.time(),
                           weather=features.weather()
                           )


if __name__ == '__main__':
    app.run(debug=True)
