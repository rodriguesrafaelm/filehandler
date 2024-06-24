"""
Test utils for filehandle module.
"""

import os
from filehandler.util import (
    copy_file,
    move_file
)


def test_copy_file(tmp_path):
    """
    Test copying a file using filehandler.util.copy_file.

    Args:
    - tmp_path (pathlib.Path): Temporary directory path provided by pytest.

    Writes "Hello, world!" to a source file in the temporary directory,
    copies it to a destination file, and verifies that the copied file
    contains the same content.

    Raises:
    - AssertionError: If the copied file does not match the expected content.
    """
    src = tmp_path / "source.txt"
    dst = tmp_path / "destination.txt"
    with open(src, "w", encoding='utf-8') as f:
        f.write("Hello, world!")

    copy_file(src, dst)
    assert os.path.exists(dst)
    with open(dst, "r", encoding='utf-8') as f:
        assert f.read() == "Hello, world!"


def test_move_file(tmp_path):
    """
    Test moving a file using filehandler.util.move_file.

    Args:
    - tmp_path (pathlib.Path): Temporary directory path provided by pytest.

    Writes "Heello, world!" to a source file in the temporary directory,
    moves it to a destination file, and verifies that the moved file
    exists in the destination and no longer exists in the source.

    Raises:
    - AssertionError: If the destination file does not exist after move,
      if the source file still exists after move, or if the content of
      the destination file does not match the expected content.
    """
    src = tmp_path / "source.txt"
    dst = tmp_path / "destination.txt"
    with open(src, "w", encoding='utf-8') as f:
        f.write("Heello, world!")

    move_file(src, dst)
    assert os.path.exists(dst)
    assert not os.path.exists(src)
    with open(dst, "r", encoding='utf-8') as f:
        assert f.read() == "Heello, world!"
