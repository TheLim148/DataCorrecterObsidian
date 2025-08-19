import os
import re

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]

def edit_files() -> list:
    global date;       date = ""
    global clean_time; clean_time = ""
    
    pattern: str = re.compile(
        r"^Creation date: \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$",
        re.MULTILINE
    )

    local_dir = input("Введите путь к файлам: ")
    files: list = os.listdir(local_dir)

    for file in files:
        with open(os.path.join(local_dir, file), "r", encoding="utf-8") as text:
            list_of_lines = text.readlines()
            text.seek(0)
            whole_text = text.read().strip()

        new: list = []

        date = os.path.basename(file)

        match = pattern.search(whole_text)
        if match:
            print(f"\n{file}: соответствует формату")
        else:
            print(f"\n{file}")
            swap(list_of_lines, 4, 5) #Now string "Creation date" above string "Modification date" in array
            for line in list_of_lines:
                elem = line.rstrip("\n")
                if elem.startswith("\"Title"): # index = 3
                    # date = elem.split(":")[2].replace("\n", "").strip()
                    continue

                if elem.startswith("\"Modification date"): #index = 4
                    raw_time = elem.split("2025")[-1].strip().split(":")[0:2]
                    clean_time = ":".join(raw_time) + ":00"
                    continue

                if elem.startswith("\"Creation date"): # index = 5
                    elem = elem.replace("\"", "").replace(":", "", 1)
                    elem = elem.split(":")[0] + ": "
                    format_string = date + "T" + clean_time
                    elem += format_string
                new.append(elem + "\n")

            with open(os.path.join(local_dir, file), "w", encoding="utf-8") as f:
                f.writelines(new)

def main() -> None:
    edit_files()

if __name__ == "__main__":
    main()