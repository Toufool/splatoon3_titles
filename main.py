import requests
import json

def get_data(url):
    resp = requests.get(url)
    data = json.loads(resp.text)
    return data

def get_adjectives(data):
    adjectives = []
    for num, adjective in data["CommonMsg/Byname/BynameAdjective"].items():
        adjectives.append(adjective)
    return adjectives

def get_subjects(data):
    subjects = []
    for num, subject in data["CommonMsg/Byname/BynameSubject"].items():
        if "[group=" not in subject and "params=]" not in subject:
            subjects.append(subject)
    return subjects

def get_all_titles(adjectives, subjects):
    titles = []
    for adjective in adjectives:
        for subject in subjects:
            titles.append(adjective + " " + subject)
    return titles

def dump_titles(titles, sort=True):
    if sort:
        titles.sort()
    with open('titles.txt', 'w', encoding="utf-8") as f:
        for title in titles:
            f.write(f"{title}\n")

def main():
    url = "https://raw.githubusercontent.com/Leanny/leanny.github.io/master/splat3/data/language/USen.json"
    data = get_data(url)
    adjectives = get_adjectives(data)
    subjects = get_subjects(data)
    titles = get_all_titles(adjectives, subjects)
    dump_titles(titles)

if __name__ == "__main__":
    main()
