#!/usr/bin/python3
import dis
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    filtered_names = sorted(name for name in names if not name.startswith("__"))
    for name in filtered_names:
        print(name)
