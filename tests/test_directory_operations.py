"""
Test directory operations module.
"""

import os
from filehandler.directory_operations import (
    create_directory,
    list_directory,
    remove_directory,
)


def test_directory_operations(tmp_path: str) -> None:
    """
    Test the directory operations.
    """
    dir_path: str = str(tmp_path) + "/test_dir"
    create_directory(dir_path)
    assert os.path.isdir(dir_path)

    file_path: str = str(dir_path) + "/test.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Hello, world!")

    assert list_directory(dir_path) == ["test.txt"]
    remove_directory(dir_path)
    assert not os.path.exists(dir_path)
