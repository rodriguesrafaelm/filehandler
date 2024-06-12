"""
File operations module.
"""

import csv
import json
import xml.etree.ElementTree as ET
from typing import Any, Dict, List


def read_text_file(file_path: str) -> str:
    """
    Read the content of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the text file.

    Example:
        content = read_text_file("example.txt")
        print(content)
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_text_file(file_path: str, content: str) -> None:
    """
    Write content to a text file.

    Args:
        file_path (str): The path to the text file.
        content (str): The content to be written.

    Returns:
        None

    Example:
        write_text_file("example.txt", "Hello, World!")
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def read_csv_file(file_path: str) -> List[List[str]]:
    """
    Read the content of a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        List[List[str]]: The content of the CSV file as a list of rows.

    Example:
        rows = read_csv_file("example.csv")
        for row in rows:
            print(row)
    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)


def write_csv_file(file_path: str, rows: List[List[str]]) -> None:
    """
    Write content to a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        rows (List[List[str]]): The rows to be written.

    Returns:
        None

    Example:
        rows = [
            ["Name", "Age", "City"],
            ["Alice", "30", "New York"],
            ["Bob", "25", "Los Angeles"]
        ]
        write_csv_file("example.csv", rows)
    """
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Read the content of a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Dict[str, Any]: The content of the JSON file.

    Example:
        data = read_json_file("example.json")
        print(data)
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """
    Write content to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (Dict[str, Any]): The data to be written.

    Returns:
        None

    Example:
        data = {
            "name": "Alice",
            "age": 30,
            "city": "New York"
        }
        write_json_file("example.json", data)
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def read_xml_file(file_path: str) -> ET.Element:
    """
    Read the content of an XML file.

    Args:
        file_path (str): The path to the XML file.

    Returns:
        ET.Element: The root element of the XML file.

    Example:
        root = read_xml_file("example.xml")
        print(ET.tostring(root, encoding="unicode"))
    """
    tree = ET.parse(file_path)
    return tree.getroot()


def write_xml_file(file_path: str, element: ET.Element) -> None:
    """
    Write content to an XML file.

    Args:
        file_path (str): The path to the XML file.
        element (ET.Element): The element to be written.

    Returns:
        None

    Example:
        element = ET.Element("root")
        write_xml_file("example.xml", element)
    """
    tree = ET.ElementTree(element)
    tree.write(file_path)
