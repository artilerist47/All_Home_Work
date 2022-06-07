from flask import Flask
from utils import get_all_candidates, get_candidate_by_id, formate_candidates, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_main():
    all_candidates = get_all_candidates()
    result = formate_candidates(all_candidates)
    return result


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = get_candidate_by_id(uid)
    result = f"<img src='{candidate['picture']}'>" + formate_candidates([candidate])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates = get_candidates_by_skill(skill.lower())
    result = formate_candidates(candidates)
    return result


app.run()
