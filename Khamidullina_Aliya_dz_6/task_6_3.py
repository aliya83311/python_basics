import json


def write_to_file(f1, f2, f3):
  with open(f1, "r", encoding="utf-8") as n, open(f2, "r", encoding="utf-8") as h:
    last_names = n.read().splitlines()
    hobbies = h.read().splitlines()
    if len(hobbies) < len(last_names):
      while hobbies < last_names:
        hobbies.append(None)
      user_hobbies = {name: hobby for name, hobby in zip(last_names, hobbies)}
      with open(f3, "w", encoding="utf-8") as d:
        d.write(json.dumps(user_hobbies, ensure_ascii=False))
      return "Data written to file"
    elif len(hobbies) > len(last_names):
      return 1
    else:
      user_hobbies = {name: hobby for name, hobby in zip(last_names, hobbies)}
      with open(f3, "w", encoding="utf-8") as d:
        d.write(json.dumps(user_hobbies, ensure_ascii=False))
      return "Data added to file"
  

print(write_to_file("last_names.csv", "hobbies.csv", "dict.txt"))