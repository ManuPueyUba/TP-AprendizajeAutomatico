import json


def append_jsonl(path, item):

    with open(path, "a", encoding="utf-8") as f:

        f.write(
            json.dumps(item, ensure_ascii=False)
        )

        f.write("\n")