"""
Test directory integrations module.
"""

import os

import xml.etree.ElementTree as ET

from filehandler.directory_operations import (
    create_directory,
    list_directory,
    remove_directory,
)
from filehandler.file_operations import (
    read_text_file,
    write_text_file,
    read_csv_file,
    write_csv_file,
    read_json_file,
    write_json_file,
    read_xml_file,
    write_xml_file,
)
from filehandler.util import (
    copy_file,
    move_file,
)

def test_text_file_operations(setup_test_dir):
    """
    Test writing and reading a text file.
    """
    file_path = os.path.join(setup_test_dir, "test.txt")
    content = "Hello, World!"

    # Write and read text file
    write_text_file(file_path, content)
    read_content = read_text_file(file_path)
    assert content == read_content


def test_csv_file_operations(setup_test_dir):
    """
    Test writing and reading a CSV file.
    """
    file_path = os.path.join(setup_test_dir, "test.csv")
    rows = [
        ["Name", "Age", "City"],
        ["Alice", "30", "New York"],
        ["Bob", "25", "Los Angeles"],
    ]

    # Write and read CSV file
    write_csv_file(file_path, rows)
    read_rows = read_csv_file(file_path)
    assert rows == read_rows


def test_json_file_operations(setup_test_dir):
    """
    Test writing and reading a JSON file.
    """
    file_path = os.path.join(setup_test_dir, "test.json")
    data = {"name": "Alice", "age": 30, "city": "New York"}

    # Write and read JSON file
    write_json_file(file_path, data)
    read_data = read_json_file(file_path)
    assert data == read_data


def test_xml_file_operations(setup_test_dir):
    """
    Test writing and reading an XML file.
    """
    file_path = os.path.join(setup_test_dir, "test.xml")
    root = ET.Element("root")
    child = ET.SubElement(root, "child")
    child.text = "Hello, XML!"

    # Write and read XML file
    write_xml_file(file_path, root)
    read_root = read_xml_file(file_path)
    assert ET.tostring(root, encoding="unicode") == ET.tostring(
        read_root, encoding="unicode"
    )


def test_copy_move_file_operations(setup_test_dir):
    """
    Test copying and moving files.
    """
    src_file = os.path.join(setup_test_dir, "src.txt")
    dst_file = os.path.join(setup_test_dir, "dst.txt")
    moved_file = os.path.join(setup_test_dir, "moved.txt")
    content = "Test file content"

    # Write source file
    write_text_file(src_file, content)

    # Copy file
    copy_file(src_file, dst_file)
    assert os.path.exists(dst_file)
    assert read_text_file(dst_file) == content

    # Move file
    move_file(dst_file, moved_file)
    assert os.path.exists(moved_file)
    assert not os.path.exists(dst_file)
    assert read_text_file(moved_file) == content


def test_directory_operations(setup_test_dir):
    """
    Test creating, listing, and removing directories.
    """
    sub_dir = os.path.join(setup_test_dir, "sub_dir")
    file_path = os.path.join(sub_dir, "test.txt")
    content = "Hello, World!"

    # Create directory and file
    create_directory(sub_dir)
    write_text_file(file_path, content)

    # List directory contents
    contents = list_directory(sub_dir)
    assert "test.txt" in contents

    # Remove directory
    remove_directory(sub_dir)
    assert not os.path.exists(sub_dir)
