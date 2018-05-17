from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_world():
    if len(request.form) > 0:
        name = request.form["firstname"]
        lastname = request.form["lastname"]
        if name == "Andrey":
            return render_template('Autorize.html', name=name, lastname=lastname)
        else:
            render_template('index.html', tryagain=True)

    return render_template('index.html')


if __name__ == "__main__":
    app.run("localhost", 8000)













# import uuid
#
#
# import sqlite3
#
# conn = sqlite3.connect('invites.db')
#
#
# c = conn.cursor()
#
# #
# # c.execute('''CREATE TABLE users
# #              (id integer primary key autoincrement not null, email text, password text, invite text, status integer not null)''')
#
# c.execute("INSERT INTO users(email, password, invite, status) VALUES ('pak-andrei@gmail.com', 'dwadwa', '%s', 0)" % uuid.uuid4())
#
#
# c.execute("select * from users")
#
# conn.commit()
# print(c.fetchall())
#
#
# conn.close()