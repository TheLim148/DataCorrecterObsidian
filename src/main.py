import os
import re

def print_files_information() -> None:
    files: list = os.listdir("bak")

    for file in files:
        print(f"\n{file}")
        with open(f"bak/{file}", "r+", encoding="utf-8") as text:
            for line in text:
                if line.find("Title") > 0:
                    line = line.replace("\"", "").replace(":", "", 1)
                    date = line.split(":")[1].replace("\n", "").strip()
                    print(date)
                    print(line.strip())
                if line.find(" date") > 0:
                    print(line.strip())

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
        print(f"\n{file}")

        with open(f"bak/{file}", "r", encoding="utf-8") as text:
            list_of_lines = text.readlines()
            text.seek(0)
            whole_text = text.read().strip()
        
        for line in list_of_lines:
            elem = line.strip()
            
            match = pattern.match(elem)
            if match:
                pass
            else:
                if elem.startswith("\"Title"):
                    elem = elem.replace("\"", "").replace(":", "", 1)

                    date = elem.split(":")[1].replace("\n", "").strip()

                if elem.startswith("\"Modification date"):
                    elem = elem.replace("\"", "").replace(":", "", 1)

                    raw_time = elem.split("2025")[-1].strip().split(":")[0:2]
                    clean_time = ":".join(raw_time) + ":00"

                if elem.startswith("\"Creation date"):
                    elem = elem.replace("\"", "").replace(":", "", 1)

            
            # new.append(elem)
        match1 = pattern.search(whole_text)
        # print(match1)
        if match1:
            pass
        else:
            format_string = date + "T" + clean_time
            print(format_string)
    return new
        

def main() -> None:
    foo()

    # print(foo1)
    # print_files_information()
    

if __name__ == "__main__":
    main()