print("an ASPL file uses a .aspl file extension")
filename = input("Input filename without the .aspl: ")

with open(f"{filename}.aspl", "r") as r:
    with open("file.py", "w") as w:
        w.write(r.read())

import asplinterpreter
import file
