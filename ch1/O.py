import os

def print_dir_contents(path="."):
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        print(f"Error: {e}")

# List current working directory
print_dir_contents(".")
