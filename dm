#!/usr/bin/env python3
import json
import sys

with open('data.json', "r") as data_fp:
    data = json.load(data_fp)
    data_fp.close()


def add():
    i = 0
    while sys.argv[2][i] != ":":
        i += 1

    label = sys.argv[2][:i]
    response = sys.argv[2][i + 1:]
    data[label] = response
    print(f"added \"{label}:{response}\" to {data_fp.name}")


if len(sys.argv) > 1:
    if sys.argv[1] == "add":
        add()

with open('data.json', 'w') as data_fp:
    json.dump(data, data_fp)
    data_fp.close()
