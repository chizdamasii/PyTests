import os

def print_directory_contents(path):
    if os.path.exists(path):
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            if os.path.isdir(child_path):
                print_directory_contents(child_path)
            else:
                print(child_path)

print_directory_contents('D:\PyTests')
