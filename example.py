import os
if (not os.path.exists("data")):
    try:
        os.rmdir("data")
        print("Folder deleted successfully.")
    except OSError as e:
        print(f"Error: {e}")