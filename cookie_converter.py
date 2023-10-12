import json
import os
import random
import tkinter
from tkinter import filedialog
import shutil

# while True:
#     print("\n<<< Select Netscape cookies folder >>>\n\n")
#     tkinter.Tk().withdraw()
#     folder_path = filedialog.askdirectory()
#     if folder_path != "":
#         break
folder_path='/content/Netflix-cookie-checker/Cookies'
rand_number = random.randint(1, 99999)


def convert_netscape_cookie_to_json(cookie_file_content):
    cookies = []
    for line in cookie_file_content.splitlines():
        fields = line.strip().split("\t")
        if len(fields) >= 7:
            cookie = {
                "domain": fields[0],
                "flag": fields[1],
                "path": fields[2],
                "secure": fields[3] == "TRUE",
                "expiration": fields[4],
                "name": fields[5],
                "value": fields[6],
            }
            cookies.append(cookie)

    JSON_DATA = json.dumps(cookies, indent=4)
    return JSON_DATA


path = "json_cookies"
try:
    os.mkdir(path)
    print(f"Folder {path} created!")
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                content = file.read()

            json_data = convert_netscape_cookie_to_json(content)

            with open(f"json_cookies/{filename}", "w") as f:
                f.write(json_data)
                print(f"{filename} - DONE!")

except FileExistsError:
    if (
        input(
            "Do you want to remove old cookies folder? (y/n)\n [y] Recommended \n > : "
        )
        == "y"
    ):
        shutil.rmtree(path)
        os.mkdir(path)
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if os.path.isfile(filepath):
                with open(filepath, "r") as file:
                    content = file.read()

                json_data = convert_netscape_cookie_to_json(content)

                with open(f"json_cookies/{filename}", "w") as f:
                    f.write(json_data)
                    print(f"{filename} - DONE!")

    else:
        os.mkdir(str(f"temp {rand_number}"))
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if os.path.isfile(filepath):
                with open(filepath, "r") as file:
                    content = file.read()

                json_data = convert_netscape_cookie_to_json(content)

                with open(f"temp {rand_number}/{filename}", "w") as f:
                    f.write(json_data)
                    print(f"{filename} - DONE!")

        print(f"\n\nsaved cookies to the temp folder - temp {rand_number}")
