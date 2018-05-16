from flask import Flask, render_template
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

site_links = {
    "about": {
        "title": "more about who I am",
        "display": "about"
    },
    "source": {
        "title": "code history, sprockets and repos",
        "display": "projects / code"
    },
    "websites": {
        "title": "websites and web apps",
        "display": "websites"
    },
    "written-by-soon-van": {
        "title": "writing portfolio",
        "display": "writes"
    },
    "contact-soon": {
        "title": "send me an email",
        "display": "contact me"
    }
}

@app.route("/")
def index():
    return render_template("index.html", site_links = site_links, slug = "home")

@app.route("/about/")
def about():
    return render_template("about.html", site_links = site_links, slug = "about")

@app.route("/written-by-soon-van/")
def author():
    return render_template("author.html", site_links = site_links, slug = "written-by-soon-van")

@app.route("/contact-soon/")
def contact():
    return render_template("contact.html", site_links = site_links, slug = "contact-soon")

@app.route("/source/")
def repos():
    return render_template("repos.html", site_links = site_links, slug = "source")

@app.route("/websites/")
def websites():
    return render_template("websites.html", site_links = site_links, slug = "websites")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
