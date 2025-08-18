import os

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
                    # print(line.split("\""))
                    # print(line.split(":"))
                if line.find(" date") > 0:
                    print(line.strip())

def foo() -> list:
    files: list = os.listdir("bak")

    new: list = []
    global date
    global clean_time

    for file in files:
        print(f"\n{file}")

        with open(f"bak/{file}", "r", encoding="utf-8") as text:
            list_of_lines = text.readlines()
        
        for elem in list_of_lines:
            strip_elem = elem.rstrip("\n")

            if not strip_elem.startswith("\"Title"):
                pass

            if strip_elem.startswith("\"Title"):
                strip_elem = strip_elem.replace("\"", "").replace(":", "", 1)

                date = strip_elem.split(":")[1].replace("\n", "").strip()
                # print(strip_elem)

            if strip_elem.startswith("\"Modification date"):
                strip_elem = strip_elem.replace("\"", "").replace(":", "", 1)

                raw_time = strip_elem.split("2025")[-1].strip().split(":")[0:2]
                clean_time = ":".join(raw_time)

                # print(clean_time)
                # print(strip_elem)

            if strip_elem.startswith("Creation date"):
                pass
                # print(strip_elem)

            if strip_elem.startswith("\"Creation date"):
                strip_elem = strip_elem.replace("\"", "").replace(":", "", 1)
                # print(strip_elem)

            # new.append(strip_elem)
    # return new
        

def main() -> None:
    # foo1: list = foo()
    foo()
    # print(date)
    
    ideal_string = date + "T" + clean_time
    print(ideal_string)

    # print(foo1)
    # print_files_information()
    

if __name__ == "__main__":
    main()