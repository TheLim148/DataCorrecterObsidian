import os

files = os.listdir("temp")

for file in files:
    print(f"\n{file}")
    with open(f"temp/{file}", "r") as f:
        for line in f:
            if line.find("Title") > 0:
                print(line.strip())
                # print(line.split("\""))
                # print(line.split(":"))
            if line.find(" date") > 0:
                print(line.strip())
