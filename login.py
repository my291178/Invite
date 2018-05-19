from flask import Flask, Response, render_template
from flask_login import LoginManager, UserMixin, login_required

login_manager = LoginManager()
app = Flask(__name__)
# фласк написан в ООП и мы работаем соотв в ООП
login_manager.init_app(app)
# добавочный модуль к существующему объекту

class User(UserMixin):
    user_database = {"JohnDoe": "John",
                     "JaneDoe": "12345"}

    def __init__(self, login, password):
        self.login = login
        self.password = password


    def is_valid(self):
        valid = True

        if self.login not in self.user_database:
            valid = False
        else:
            if self.user_database[self.login] != self.password:
                valid = False

        return valid



@login_manager.request_loader
def load_user(request):

    if len(request.form) > 0:

        login = request.form["login"]
        password = request.form["password"]

        user = User(login, password)

        if user.is_valid():
            return user

    return None


@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/protected/", methods=["GET", "POST"])
@login_required
def protected():
    return Response(response="Hello Protected World!", status=200)


if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(port=8000,debug=True)


