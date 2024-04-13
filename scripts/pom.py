#!/usr/bin/env python
# importing modules
import json, os, dbus

# setting up alerts

obj = dbus.SessionBus().get_object("org.freedesktop.Notifications", "/org/freedesktop/Notifications")
obj = dbus.Interface(obj, "org.freedesktop.Notifications")

# setting up path
script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, "data.json")

# load data from JSON file
with open(file_path) as file:
    data = json.load(file)


# round change and time change
if data["time"] == "0" and data["status"] == "1":
    data["round"] = str(int(data["round"])+1)
    if data["round"] in ["0", "2", "4", "6"]:
        data["time"] = "1200"
        obj.Notify("", 0, "", "WORK", "This is time for a WORK!", [], {"urgency": 2}, 10000)
    elif data["round"] in ["1", "3", "5"]:
        data["time"] = "300"
        obj.Notify("", 0, "", "SHORT BREAK", "This is time for a SHORT BREAK!", [], {"urgency": 3}, 10000)
    elif data["round"] == "7":
        data["time"] = "900"
        obj.Notify("", 0, "", "LONG BREAK", "This is time for a LONG BREAK!", [], {"urgency": 3}, 10000)
    else:
        data["time"] = "1200"
        data["round"] = "0"
elif data["status"] == "1":
    data["time"] = str(int(data["time"]) - 1)


# showing time in minutes and seconds
def add_zero(num):
    if(num >= 0 and num <= 9):
        return f"0{num}"
    else:
        return str(num)

all = data["time"]
m = int(data["time"]) // 60
s = int(data["time"]) % 60


# visualising data

if data["round"] in ["0", "2", "4", "6"]:
    data["text"] = f"W{int(int(data['round'])/2+1)} {add_zero(m)}:{add_zero(s)}"
else:
    data["text"] = f"B{int(int(data['round'])/2+1)} {add_zero(m)}:{add_zero(s)}"


print(json.dumps(data))

data["time"] = all

with open(file_path, "w") as file:
    json.dump(data, file, indent=6)
