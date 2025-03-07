import os
import shutil


def cleanup() -> None:
    logs_path = "../../logs/"
    for filename in os.listdir(logs_path):
        file_path = os.path.join(logs_path, filename)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)  # Delete subfolder and its contents
        else:
            os.remove(file_path)  # Delete file
