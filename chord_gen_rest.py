import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/format_chordpro/', methods=['GET'])
def home():
    return "<h1>Good Morning, weirdo!</h1><p>You were fooled by yourself! =D =,C                  inferno</p>"

app.run()

def main():
   print('Hello cruel World!')
   

if __name__ == "__main__":
   main()