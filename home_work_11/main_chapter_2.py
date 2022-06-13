from flask import Flask, render_template
from utils import load_all_candidates, get_candidate_by_id, get_candidate_by_name

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = load_all_candidates()
    return render_template("all_candidates.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate_by_id(candidate_id):
    candidate = get_candidate_by_id(candidate_id)
    return render_template("candidate_id.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_candidate_by_name(candidate_name):
    candidates = get_candidate_by_name(candidate_name)
    return render_template("search_candidate_name.html", candidates=candidates)


app.run()
