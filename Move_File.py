import os
import shutil

from_dir = "C:/Users/sywon/OneDrive/Desktop/Coding/Python/Byjus python/Project C102/Document_Files"
to_dir = "C:/Users/sywon/OneDrive/Desktop/Coding/Python/Byjus python/Project C102/Moved_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    file_root,file_ext = os.path.splitext(file_name)
    if file_ext == " ":
        continue
    if file_ext in ['.txt', '.doc', '.docx','.pdf', '.rtf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "text_documents"
        path3 = to_dir + '/' + "text_documents" + '/' + file_name

        if os.path.exists(path2):
            print("moving " + file_name + "....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving " + file_name + "....")
            shutil.move(path1,path3)
