import json


def load_all_candidates():
    with open("candidates.json", encoding="utf-8") as file:
        all_candidates = json.load(file)
        return all_candidates


def get_candidate_by_id(candidate_id):
    candidates = load_all_candidates()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidate_by_name(candidate_name):
    candidates = load_all_candidates()
    result = []
    for candidate in candidates:
        if candidate_name in candidate["name"]:
            result.append(candidate)
    return result


def get_candidates_by_skill(candidate_skill):
    candidates = load_all_candidates()
    result = []
    for candidate in candidates:
        if candidate_skill in candidate["skills"].lower().split(', '):
            result.append(candidate)
    return result
