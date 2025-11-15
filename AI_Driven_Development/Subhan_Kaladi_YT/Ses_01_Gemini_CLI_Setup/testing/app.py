
import feedparser
from flask import Flask, render_template

app = Flask(__name__)

RSS_FEED = "https://static.cricinfo.com/rss/livescores.xml"

@app.route("/")
def index():
    feed = feedparser.parse(RSS_FEED)
    scores = [entry.title for entry in feed.entries]
    return render_template("index.html", scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
