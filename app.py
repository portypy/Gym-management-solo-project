from flask import Flask, render_template

from controllers.members_controller import members_blueprint
from controllers.sessions_controller import sessions_blueprint
from controllers.bookings_controller import bookings_blueprint

app = Flask(__name__)
app.secret_key = 'this is secret key'

app.register_blueprint(members_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)