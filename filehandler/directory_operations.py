"""
Directory operations module.
"""

import os
import shutil
from typing import List


def create_directory(directory_path: str):
    """
    Create a directory at the specified path.

    Args:
        directory_path (str): The path of the directory to create.
    """
    os.makedirs(directory_path, exist_ok=True)


def list_directory(directory_path: str) -> List[str]:
    """
    List the contents of a directory.

    Args:
        directory_path (str): The path of the directory.

    Returns:
        List[str]: A list of filenames in the directory.
    """
    return os.listdir(directory_path)


def remove_directory(directory_path: str):
    """
    Remove a directory and its contents.

    Args:
        directory_path (str): The path of the directory to remove.
    """
    shutil.rmtree(directory_path)
