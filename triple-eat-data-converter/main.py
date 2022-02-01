import json


def main():
    data = dict()
    data_txt = open("data.txt", "r", encoding="utf-8")

    for index, category in enumerate(["korean", "western", "chinese", "japanese", "other"]):
        data[category] = list()
        line = data_txt.readline().strip()

        while line != ";":
            data[category].append({
                "category": index,
                "name": line,
                "location": data_txt.readline().strip(),
                "hours": data_txt.readline().strip()
            })

            data_txt.readline()
            line = data_txt.readline().strip()

        data_txt.readline()

    data_txt.close()

    data_js = open("../scripts/data.js", "w", encoding="utf-8")
    data_js.write("const data = " + json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    data_js.close()


if __name__ == "__main__":
    main()
