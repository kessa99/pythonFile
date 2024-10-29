import os

def display_cwd():
    cwd = os.getcwd()
    print("repertoire actuel de travail: ", cwd)
    print("--------------------------------")

def up_one_directory_level():
    os.chdir("../")

def display_entries_in_directory(directory):
    abs_dirctory = os.path.abspath(directory)
    with os.scandir(directory) as entries:
        for entry in entries:
            print("nom: ",entry.name)
    print("--------------------------------")

if __name__ == "__main__":
    display_cwd()
    up_one_directory_level()
    display_cwd()
    display_entries_in_directory("file")
