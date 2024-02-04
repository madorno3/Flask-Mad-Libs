from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"




@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    # prompts = story.prompts

    return render_template('questions.html')

@app.route("/story")
def story():
    place = request.args["place"]
    adj = request.args["adj"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    plural_noun = request.args["plural_noun"]
    return render_template('story.html', place = place, adj = adj, noun=noun,verb=verb,plural_noun=plural_noun)

# @app.route("/story")
# def ask_questions():
#     """Generate and show form to ask words."""

#     # prompts = story.prompts

#     return "story"


# @app.route("/story")
# def show_story():
#     """Show story result."""

#     text = story.generate(request.args)

#     return render_template("story.html", text=text)
