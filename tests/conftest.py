"""
This module defines fixtures for unit tests using pytest.

Fixtures:
    data_generator: Returns an instance of DataGenerator.
    excel_report: Returns an instance of ExcelReport.
    mocker: Returns an instance of Mock from unittest.mock.
"""

from unittest.mock import Mock
import pytest
from src.modules.data_generator import DataGenerator
from src.modules.excel_report import ExcelReport


@pytest.fixture
def data_generator():
    """
    Fixture that returns an instance of DataGenerator.

    :return: An instance of DataGenerator.
    """
    return DataGenerator()


@pytest.fixture
def excel_report():
    """
    Fixture that returns an instance of ExcelReport.

    :return: An instance of ExcelReport.
    """
    return ExcelReport()


@pytest.fixture
def mocker():
    """
    Fixture that returns an instance of Mock from unittest.mock.

    :return: An instance of Mock.
    """
    return Mock()
