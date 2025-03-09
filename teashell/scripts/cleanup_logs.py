import os
import shutil


def cleanup(path: str) -> None:
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)  # Delete subfolder and its contents
        else:
            os.remove(file_path)  # Delete file
