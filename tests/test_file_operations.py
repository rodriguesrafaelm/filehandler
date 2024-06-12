import xml.etree.ElementTree as ET
from filehandler.file_operations import *


def test_text_file_operations(tmp_path):
    file_path = tmp_path / "test.txt"
    write_text_file(file_path, "Hello, world!")
    assert read_text_file(file_path) == "Hello, world!"


def test_csv_file_operations(tmp_path):
    file_path = tmp_path / "test.csv"
    print(file_path)
    print("hmm")
    data = [["Name", "Age"], ["Alice", "30"]]
    write_csv_file(file_path, data)
    assert read_csv_file(file_path) == data


def test_json_file_operations(tmp_path):
    file_path = tmp_path / "test.json"
    data = {"name": "Alice", "age": 30}
    write_json_file(file_path, data)
    assert read_json_file(file_path) == data


def test_xml_file_operations(tmp_path):
    file_path = tmp_path / "test.xml"
    root = ET.Element("root")
    child = ET.SubElement(root, "child")
    child.text = "Hello, world!"
    write_xml_file(file_path, root)
    assert ET.tostring(read_xml_file(file_path)) == ET.tostring(root)
