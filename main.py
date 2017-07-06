from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/user-signup", methods=['POST'])
def get_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    if not username or not re.match("^[a-zA-Z0-9_]{3,20}$", username):
        error = "Username error"
        return redirect("/?error=" + error)
    if not password or not re.match("^[a-zA-Z0-9_]{3,20}$", password):
        error = "Password error"
        return redirect("/?error=" + error)
    if not verify or (password != verify):
        error = "Verify error"
        return redirect("/?error=" + error)
    if email:
        if not re.match("^[a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$", email) or re.match("^[a-zA-Z0-9_]{3,20}$", email):
            error = "Email error"
            return redirect("/?error=" + error)

    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
