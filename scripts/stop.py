#!/usr/bin/env python
# importing modules
import json, os

#setuping path
script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, "data.json")

# Load data from JSON file
with open(file_path) as file:
    data = json.load(file)

data["status"] = "0"

with open(file_path, "w") as file:
    json.dump(data, file, indent=6)
