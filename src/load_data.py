import json

def load_watch_history(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    data = load_watch_history("data/watch-history.json")
    print(type(data))
    print(len(data))
    print(data[0])
