import sys, os, time, json
import datetime as dt
from flask import Flask, render_template, session, request, redirect, url_for, send_from_directory
from flask import make_response
from functools import wraps, update_wrapper

app = Flask(__name__)


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = dt.datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)

@app.route("/", methods=['GET', 'POST'])
def main():
    # if "verified" in session.keys():
        resp = make_response(render_template('index.html'))
        # info = str(json.load(open('www/static/json/quote.json')))
        return resp
    # else:
    #     if request.method == 'POST':
    #         password = request.form.get('inputPassword')
    #         print(password)
    #         if password == "password":
    #             session["verified"] = True
    #             return main()
    #         return render_template('login.html')
    #     return render_template('login.html')

# @app.route("/logout", methods=['GET'])
# def logout():
#     session.clear()
#     return redirect(url_for('main'))

# @app.route("/save")
# def save():
#     if 'schedule' in request.cookies:
#         json.dump(json.loads(request.cookies["schedule"].replace("'", '"')), open('www/static/schedule.json', 'w'), indent=4)
#     return redirect(url_for('main'))

# @app.route("/update")
# def siteUpdate():
#     update.updateSchedule()
#     return redirect(url_for('main'))

# @app.route("/ring")
# def siteRing():
#     ring.ring()
#     return redirect(url_for('main'))

@app.route('/static/<path:filepath>')
@nocache # stops data caching
def data(filepath):
    return send_from_directory('static', filepath)

app.secret_key = os.urandom(12) #generate secret key
if __name__ == "__main__":
    app.run(debug=True) #run Flask application
