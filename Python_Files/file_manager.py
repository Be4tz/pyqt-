import os
import shutil

def organize():
    dir = os.getcwd()
    if not os.path.isdir(dir):
        print(f"'{dir}' is not a directory")
        return
    os.chdir(dir)
    files = [f for f in os.listdir(dir) if os.path.isfile(f)]
    file_type = {
         'Python_Files': ['py'],
        'Audio_Files': ['mp3'],
        'Video_Files': ['mp4'],
        'Json_Files': ['json'],
        'Picture_File': ['jpg'],
        'Others': []
    }
    for category in file_type:
        category_path = os.path.join(dir, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    for file in files:
        file_ext = file.split(".")[-1] if "." in file else 'no extension'
        for key, exstension in file_type.items():
            if file_ext in exstension:
                category = key
                break
        category_dir = os.path.join(dir, category)
        shutil.move(file, os.path.join(category_dir, file))

organize()

