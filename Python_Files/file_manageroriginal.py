import os
import shutil

class FileManager:
    def organize(self, dir):
        if not os.path.isdir(dir):
            print(f"'{dir}' is not a directory")
            return
        os.chdir(dir)
        files = [f for f in os.listdir(dir) if os.path.isfile(f)]
        file_types = {
        'Python_Files': ['py'],
        'Audio_Files': ['mp3'],
        'Video_Files': ['mp4'],
        'Json_Files': ['json'],
        'Picture_File': ['jpg'],
        'Others': []
    }
        for cat in file_types:
            cat_path = os.path.join(dir, cat)
            if not os.path.exists(cat_path):
                os.makedirs(cat_path)

        for file in files:
            file_extension = file.split(".")[-1] if "." in file else "no extension"
            cat = 'Others'
            for key, extension in file_types.items():
                if file_extension in extension:
                    cat = key
                    break
            cat_dir = os.path.join(dir, cat)
            shutil.move(file, os.path.join(cat_dir, file))
direc = r"c:\Users\USER\Documents\python_class"
fil = FileManager()
fil.organize(direc)