import json


def main():
    data = dict()

    for index, category in enumerate(["korean", "western", "chinese", "japanese", "other"]):
        data_txt = open(f"data/{category}.txt", "r", encoding="utf-8")
        line = data_txt.readline().strip()

        while line != "Coupon Image":
            line = data_txt.readline().strip()

        line = data_txt.readline().strip()
        data[category] = list()

        while line != "사업장주소 :인천광역시 연수구 송도과학로 16번길 33-4 트리플 스트리트 D동 3층":
            data[category].append({
                "category": index,
                "name": line,
                "location": data_txt.readline().strip(),
                "hours": data_txt.readline().strip()
            })

            data_txt.readline()
            line = data_txt.readline().strip()

        data_txt.close()

    data_js = open("../scripts/data.js", "w", encoding="utf-8")
    data_js.write("const data = " + json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    data_js.close()


if __name__ == "__main__":
    main()
