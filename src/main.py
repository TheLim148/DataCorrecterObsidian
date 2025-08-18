import os

def print_files_information() -> list:
    # info = []
    files: list = os.listdir("temp")

    for file in files:
        # info.append(file)
        print(f"\n{file}")
        with open(f"temp/{file}", "r") as text:
            for line in text:
                if line.find("Title") > 0:
                    # info.append(line.strip())
                    print(line.strip())
                    # print(line.split("\""))
                    # print(line.split(":"))
                if line.find(" date") > 0:
                    # info.append(line.strip())
                    print(line.strip())
    # return info

def main() -> None:
    print_files_information()
    # info = print_file_information()
    # print(info)

if __name__ == "__main__":
    main()