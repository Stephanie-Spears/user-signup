from flask import Flask, request, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/", methods=['POST', 'GET'])
def index():
    error=None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        if (not username) and (not password) and (not verify):
            error="Username and Password and Verify error"
            return render_template("index.html", error=error)
        if (not username) and (not password):
            error="Username and Password error"
            return render_template("index.html", error=error)
        if not username or not re.match("^[a-zA-Z0-9_]{3,20}$", username):
            error = "Username error"
            return render_template("index.html", error=error)
        if not password or not re.match("^[a-zA-Z0-9_]{3,20}$", password):
            error = "Password error"
            return render_template("index.html", error=error)
        if not verify or (password != verify):
            error = "Verify error"
            return render_template("index.html", error=error)
        if email:
            if not re.match("^[a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$", email) or re.match("^[a-zA-Z0-9_]{3,20}$", email):
                error = "Email error"
                return render_template("index.html", error=error)


        # return render_template("index.html", error=error)

        if error == None:
            return render_template('welcome.html', username=username)

    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))


if __name__ == '__main__':
    app.run()
