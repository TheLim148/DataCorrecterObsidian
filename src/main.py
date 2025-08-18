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

def foo() -> None:
    files: list = os.listdir("bak")

    new: list = []

    for file in files:
        print(f"\n{file}")
        with open(f"bak/{file}", "r", encoding="utf-8") as text:
            list_of_lines = text.readlines()
        
        for element in list_of_lines:
            strip_element = element.rstrip("\n")
            if strip_element.startswith("\"Title"):
                print(strip_element)

            if strip_element.startswith("\"Mod"):
                print(strip_element)

            if strip_element.startswith("\"Creation") or strip_element.startswith("Creation"):
                print(strip_element)
        # print(lines)

def main() -> None:
    foo()
    # print_files_information()
    

if __name__ == "__main__":
    main()