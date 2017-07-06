from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/user-signup", methods=['POST', 'GET'])
def get_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    # use an if for email field not empty?
    email = request.form['email']

    if (not username) or (not password) or (password != verify) or (username.strip() == "") or (password.strip() == "") or (verify.strip() == ""):
         error = "Whoops"
        #  return redirect("/?error=" + error)
         return redirect("/?error=" + error)

    # username_escaped = cgi.escape(username, quote=True)
    # password_escaped = cgi.escape(password, quote=True)
    # verify_escaped = cgi.escape(verify, quote=True)
    # email_escaped = cgi.escape(email, quote=True)

    return render_template('welcome.html', username=username)

# @app.route("/index")

@app.route("/")
def index():

# error in user=get_signup()
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
