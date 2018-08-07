from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	fav_players = ["Messi","Neymar","someone"],
    return render_template("index.html"),
    fav_players=fav_players

if __name__ == '__main__':
   app.run(debug = True)
