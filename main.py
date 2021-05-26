import json
from collections import Counter

weight = [3, 1, 5, 5, 4, 3]
tend = [False, False, True, True, True, True, ]


def get_data_table():
    with open("Electra/table.json") as f:
        data = json.load(f)

    return data


def translate(data: dict):
    mod_data = {
        "A2": [],
        "A3": [],
        "Mi10": [],
        "Mi10lite": [],
        "Mi10Tlite": [],
        "Mi10T": [],
        "Mi10Tpro": [],
        "Mi8": [],
        "Mi play": [],
        "Mi9": []
    }

    for job in data:
        for element in data[job]:
            if element == "salary":
                if data[job][element] == 10:
                    mod_data[job].append(10)
                elif data[job][element] == 9:
                    mod_data[job].append(9)
                else:
                    data[job][element] = 8
                    mod_data[job].append(8)

            if element == "Weight":
                if data[job][element] <= 200:
                    mod_data[job].append(1)
                elif data[job][element] > 200 and data[job][element] <= 230:
                    mod_data[job].append(2)
                elif data[job][element] > 230:
                    mod_data[job].append(3)
        if element == "Opmemory":
            mod_data[job].append(data[job][element])

        if element == "Memory":
            if data[job][element] <= 64:
                mod_data[job].append(4)
            elif data[job][element] > 64:
                mod_data[job].append(8)

        if element == "Battery":
            if data[job][element] <= 3400:
                mod_data[job].append(3)
            elif data[job][element] > 3400 and data[job][element] <= 4500:
                mod_data[job].append(4)
            elif data[job][element] > 4500:
                mod_data[job].append(5)

        if element == "Cameras":
            mod_data[job].append(data[job][element])


return mod_data


def compare(job: list, to_job: list):
    pros = 0
    cons = 0

    for i in range(len(job)):
        if tend[i] and job[i] != to_job[i]:
            if job[i] > to_job[i]:
                pros += weight[i]
            else:
                cons += weight[i]
        else:
            if job[i] != to_job[i]:
                if job[i] < to_job[i]:
                    pros += weight[i]
                else:
                    cons += weight[i]

    if cons != 0:
        return pros / cons

    if pros != 0:
        return 100
    return 0


def electra2(limit: int):
    tr_data = translate(get_data_table())
    to_ret = []

    for job in tr_data:
        for to_job in tr_data:

            if job != to_job and compare(tr_data[job], tr_data[to_job]) > limit:
                if compare(tr_data[job], tr_data[to_job]) == 100:
                    to_ret.append(to_job)
                else:
                    to_ret.append(job)

    count = Counter(map(str, to_ret))

    for i in range(len(list(tr_data))):
        if list(tr_data)[i] not in list(count):
            count[list(tr_data)[i]] = 0

    return count.most_common()


if __name__ == "__main__":
    print(translate(get_data_table()))
    print(electra2(2.5))
