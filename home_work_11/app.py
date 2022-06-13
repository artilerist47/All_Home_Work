from flask import Flask
from utils import load_all_candidates, formate_candidates, \
    get_candidate_by_id, get_candidate_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_main():
    all_candidates = load_all_candidates()
    result = formate_candidates(all_candidates)
    return result


@app.route("/candidate/<int:candidate_id>")
def page_candidate_by_id(candidate_id):
    candidate = get_candidate_by_id(candidate_id)
    result = f"<img src='{candidate['picture']}'>" + formate_candidates([candidate])
    return result


@app.route("/candidate/<candidate_name>")
def page_candidate_by_name(candidate_name):
    candidate = get_candidate_by_name(candidate_name)
    result = f"<img src='{candidate['picture']}'>" + formate_candidates([candidate])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates = get_candidates_by_skill(skill.lower())
    result = formate_candidates(candidates)
    return result


app.run()