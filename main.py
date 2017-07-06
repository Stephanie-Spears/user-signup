from flask import Flask, request, redirect, render_template, url_for
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/user-signup", methods=['POST'])
def get_signup():
    # error = None
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    # use an if for email field not empty?
    email = request.form['email']


    if email:
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) or (2 >= len(email) or len(email) >= 20):
        # re.match("/^[a-zA-Z]{3,20}$/", email):
            error = "True"
            return redirect("/?error=" + error)

    if (not username) or (not password) or (password != verify) or (username.strip() == "") or (password.strip() == "") or (verify.strip() == "") or (" " in username or " " in password) or (2 >= len(username) or len(username) >= 20) or (2 >= len(password) or len(password) >= 20):
         error = "True"
         return redirect("/?error=" + error)

    username_escaped = cgi.escape(username, quote=True)
    password_escaped = cgi.escape(password, quote=True)
    verify_escaped = cgi.escape(verify, quote=True)
    email_escaped = cgi.escape(email, quote=True)

    return render_template('welcome.html', username=username)


@app.route("/")
def index():

    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
