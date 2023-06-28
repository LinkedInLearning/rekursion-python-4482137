import os

def iterate_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            # Datei gefunden
            print("Datei:", item_path)
        elif os.path.isdir(item_path):
            # Unterverzeichnis gefunden
            print("Verzeichnis:", item_path)
            iterate_directory(item_path)

# Verzeichnisstruktur durchlaufen
root_directory = "/"
iterate_directory(root_directory)
