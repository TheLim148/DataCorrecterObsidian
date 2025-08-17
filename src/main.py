with open("temp/2025-01-11.md", "r") as f:
    for line in f:
        if line.find("Title") > 0 or line.find(" date:") > 1:
            print(line.strip())