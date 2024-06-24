"""
Test file operations module.
"""

import xml.etree.ElementTree as ET
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


def test_text_file_operations(tmp_path):
    """
    Test writing and reading a text file.

    Args:
    - tmp_path: Temporary directory path provided by pytest.

    Writes the string "Hello, world!" to a text file and then reads it back.
    Asserts that the read content matches the written content.
    """
    file_path = tmp_path / "test.txt"
    write_text_file(file_path, "Hello, world!")
    assert read_text_file(file_path) == "Hello, world!"


def test_csv_file_operations(tmp_path):
    """
    Test writing and reading a CSV file.

    Args:
    - tmp_path: Temporary directory path provided by pytest.

    Writes a CSV data structure to a file and then reads it back.
    Asserts that the read data matches the written data.
    """
    file_path = tmp_path / "test.csv"
    print(file_path)
    print("hmm")
    data = [["Name", "Age"], ["Alice", "30"]]
    write_csv_file(file_path, data)
    assert read_csv_file(file_path) == data


def test_json_file_operations(tmp_path):
    """
    Test writing and reading a JSON file.

    Args:
    - tmp_path (pathlib.Path): Temporary directory path provided by pytest.

    Writes a JSON object to a file and then reads it back.
    Asserts that the read data matches the written data.
    """
    file_path = tmp_path / "test.json"
    data = {"name": "Alice", "age": 30}
    write_json_file(file_path, data)
    assert read_json_file(file_path) == data


def test_xml_file_operations(tmp_path):
    """
    Test writing and reading an XML file.

    Args:
    - tmp_path (pathlib.Path): Temporary directory path provided by pytest.

    Writes an XML structure to a file and then reads it back.
    Asserts that the read XML structure matches the written structure.
    """
    file_path = tmp_path / "test.xml"
    root = ET.Element("root")
    child = ET.SubElement(root, "child")
    child.text = "Hello, world!"
    write_xml_file(file_path, root)
    assert ET.tostring(read_xml_file(file_path)) == ET.tostring(root)
