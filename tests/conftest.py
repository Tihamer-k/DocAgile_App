"""
This module defines fixtures for unit tests using pytest.

Fixtures:
    data_generator: Returns an instance of DataGenerator.
    excel_report: Returns an instance of ExcelReport.
    mocker: Returns an instance of Mock from unittest.mock.
"""

import pytest
from unittest.mock import Mock
from src.modules.DataGenerator import DataGenerator
from src.modules.ExcelReport import ExcelReport


@pytest.fixture
def data_generator():
    return DataGenerator()


@pytest.fixture
def excel_report():
    return ExcelReport()


@pytest.fixture
def mocker():
    return Mock()
