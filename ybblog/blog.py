from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    numbers = [
        {"id":1, "title":"DenemeTitle1","content":"DenemeContent1"},
        {"id":2, "title":"DenemeTitle2","content":"DenemeContent2"},
        {"id":3, "title":"DenemeTitle3","content":"DenemeContent3"}
    ]
    return render_template("index.html", numbers = numbers)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/article/<string:id>")
def detail(id):
    return "Article Id: " + id
if __name__ == "__main__":
    app.run(debug=True)