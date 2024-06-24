"""
Fixtures and configuration for filehandler module tests.
"""

import shutil
import pytest

from filehandler.directory_operations import (
    create_directory
)

@pytest.fixture(scope="function")
def setup_test_dir():
    """
    Fixture to create a test directory for integration tests.
    """
    test_dir = "test_dir"
    create_directory(test_dir)
    yield test_dir
    shutil.rmtree(test_dir)
