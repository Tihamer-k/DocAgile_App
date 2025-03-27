import pytest
from src.modules.DataGenerator import DataGenerator
from src.modules.ExcelReport import ExcelReport
from src.modules.CommandGenerator import CommandGenerator


@pytest.fixture
def data_generator():
    return DataGenerator()


@pytest.fixture
def excel_report():
    return ExcelReport()


@pytest.fixture
def mocker():
    from unittest.mock import Mock
    return Mock()
