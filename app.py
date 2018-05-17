import uuid
from flask import Flask, render_template, request
app = Flask(__name__)


global_uuids = []

@app.route('/', methods=["GET","POST"])
def index():



    if len(request.form) > 0:


        if "email" in request.form:

            random_uuid = uuid.uuid4()
            print(random_uuid)
            global_uuids.append(str(random_uuid))

            return "Invite link sended"


        name = request.form["firstname"]
        lastname = request.form["lastname"]
        if name == "Andrey":
            return render_template('autorize.html', name=name, lastname=lastname)
        else:
            return render_template('index.html', tryagain=True)

    return render_template('index.html')


@app.route('/<uuid>')
def register(uuid):

    if uuid in global_uuids:
        return "Invite link is valid"
    else:
        return "Invite link isn't valid"

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