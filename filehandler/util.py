"""
Utils for file handling.
"""

import shutil


def copy_file(src: str, dst: str):
    """
    Copy a file from source to destination.

    Args:
        src (str): The path of the source file.
        dst (str): The path of the destination file.
    """
    shutil.copy2(src, dst)


def move_file(src: str, dst: str):
    """
    Move a file from source to destination.

    Args:
        src (str): The path of the source file.
        dst (str): The path of the destination file.
    """
    shutil.move(src, dst)
