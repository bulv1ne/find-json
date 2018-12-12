import argparse
import json
from collections import deque
from contextlib import contextmanager


def main():
    parser = argparse.ArgumentParser(description="Find a field in a json file")
    parser.add_argument("file", type=argparse.FileType("r"), help="The file to analyze")
    parser.add_argument("search_value")
    args = parser.parse_args()
    data = json.load(args.file)
    stack = Stack()
    for match in deep_find(data, stack, args.search_value):
        print(match)


def deep_find(data, stack, search_value):
    if isinstance(data, dict):
        for key, value in data.items():
            with stack(key):
                if search_value in key:
                    yield str(stack)
                yield from deep_find(value, stack, search_value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            with stack(i):
                yield from deep_find(item, stack, search_value)
    elif isinstance(data, str):
        if search_value in data:
            yield f"{stack} = {data}"


class Stack:
    def __init__(self):
        self.stack = deque()

    @contextmanager
    def __call__(self, value):
        self.stack.append(value)
        try:
            yield
        finally:
            self.stack.pop()

    def __iter__(self):
        return iter(self.stack)

    def __str__(self):
        return "".join(map(jq_part, self))


def jq_part(value):
    if isinstance(value, int):
        return f"[{value}]"
    return f".{value}"


if __name__ == "__main__":
    main()
