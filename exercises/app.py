from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    likes_same_sport = True
    fav_players = ["Ori Sasson","Sagi Muki","Tedy Rinner"]
    return render_template("index.html",
        fav_players=fav_players,
         likes_same_sport = likes_same_sport)

if __name__ == '__main__':
   app.run(debug = True)
