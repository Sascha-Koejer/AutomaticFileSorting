import os
import shutil

# Ordner der sortiert wird. Sortierte Ordner müssen in diesem Ordner liegen
source = "C:/Users/koeje/Downloads/"

# Angabe der Ordner und welche Dateiendung verschoben werden soll
categories = {"Bilder":[".jpg", ".png"],
              "Exe":[".exe"],
              "Zip":[".zip", ".rar"],
              "Dokumente":[".pdf", ".doc", ".pptx", ".xlsx"]
              }

try:
    for file in os.listdir(source):
        # Pfad zur Datei
        file_path = os.path.join(source,file)
        # Nur Dateien werden verschoben. Keine Ordner
        if os.path.isfile(file_path):
            for category, extensions in categories.items():
                for extention in extensions:
                    if extention in file:
                        shutil.move(file_path, os.path.join(source,category,file))
        
except PermissionError:
    pass

