import os
import shutil

# print(os.getcwd())
# # os.mkdir("test_folder")
# # os.makedirs("folder1/folder2/folder3")
# # os.rmdir("test_folder")
# # shutil.rmtree("folder1")
# # print(os.listdir("test"))

# # print(os.path.isdir("test"))
# # print(os.path.isfile("acc.py"))

# # path = "folder1/folder2/folder3"
# # path = os.path.join("folder1/folder2/folder3")

# size = os.path.getsize("acc.py")
# print(size)

# os.rename("11..py", "111.py")

# project = "my_project"

# folders = [
#     project,
#     f"{project}/templates",
#     f"{project}/styles",
#     f"{project}/images"
# ]

# for folder in folders:
#     os.makedirs(folder, exist_ok=True)

# print("проект создан")

# os.makedirs("folder_a", exist_ok=True)
# path = os.path.join("folder_a","info.txt")
# with open(path, "w", encoding="UTF-8") as file:
#     file.write("abcdefg")

# if os.path.exists(path):
#     print("файл существует")
# else:
#     print("файла не существует")

# folder = os.listdir("folder_a")
# for file in folder:
#     print (file)

def directory_info(path):
    file_count = 0
    folder_count = 0
    size_count = 0
    folder = os.listdir(path)
    for ff in folder:
        full_path = os.path.join(path, ff)
        if os.path.isfile(full_path):
            file_count += 1
            size_count += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            folder_count += 1
    return {"file_count": file_count, "folder_count": folder_count, "size_count": size_count}

print(directory_info(os.getcwd()))
