import json


def load_candidates():
    with open("candidates.json", encoding="utf-8") as file:
        all_candidates = json.load(file)
        return all_candidates


def formate_candidates(all_candidates):
    result = "<pre>"

    for candidate in all_candidates:
        result += f"""
            {candidate['name']}\n
            {candidate['position']}\n
            {candidate['skills']}\n
            """

    result += "</pre>"

    return result


def get_all_candidates():
    return load_candidates()


def get_candidate_by_id(uid):
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate
    return None


def get_candidates_by_skill(skill):
    candidates = get_all_candidates()
    for candidate in candidates:
        if skill in candidate["skills"].lower():
            return candidate
    return None
