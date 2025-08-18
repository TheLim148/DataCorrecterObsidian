import os

def print_files_information() -> list:
    files: list = os.listdir("bak")

    for file in files:
        print(f"\n{file}")
        with open(f"bak/{file}", "r+") as text:
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
    # return info

def main() -> None:
    print_files_information()

if __name__ == "__main__":
    main()