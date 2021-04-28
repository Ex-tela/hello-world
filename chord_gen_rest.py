import flask
from flask import request
import chord_formatter

app = flask.Flask(__name__, static_url_path='/web/')
app.config["DEBUG"] = True


@app.route('/format_chordpro/', methods=['GET'])
def home():
   chord = request.data.decode()
   return chord_formatter.format(chord), print('<p>oi</p>')



@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('hello_world.html')


if __name__ == "__main__":
    app.run()
