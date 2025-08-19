import os
import re

def foo() -> list:
    global date;       date = ""
    global clean_time; clean_time = ""
    
    pattern = re.compile(
        r"^Creation date: \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$",
        re.MULTILINE
    )

    files: list = os.listdir("bak")

    new: list = []

    for file in files:
        with open(f"bak/{file}", "r", encoding="utf-8") as text:
            list_of_lines = text.readlines()
            text.seek(0)
            whole_text = text.read().strip()
        
        match = pattern.search(whole_text)

        if match:
            print(f"\n{file}: соответствует формату")
            pass
        else:
            print(f"\n{file}")
            for line in list_of_lines:
                elem = line.strip()
    
                if elem.startswith("\"Title"):
                    elem = elem.replace("\"", "").replace(":", "", 1)
                    date = elem.split(":")[1].replace("\n", "").strip()

                if elem.startswith("\"Modification date"):
                    elem = elem.replace("\"", "").replace(":", "", 1)
                    raw_time = elem.split("2025")[-1].strip().split(":")[0:2]
                    clean_time = ":".join(raw_time) + ":00"

                if elem.startswith("\"Creation date"):
                    elem = elem.replace("\"", "").replace(":", "", 1)

            format_string = date + "T" + clean_time
            print(format_string)
            # new.append(elem)
        
    return new
        

def main() -> None:
    foo()

if __name__ == "__main__":
    main()