"""
This module contains unit tests for the ExcelReport class.

Tests:
    - test_modify_excel_report: Verifies the modification of an Excel report.
"""

import os

def test_modify_excel_report(mocker):
    """
    Verifies the modification of an Excel report using a mocker.
    """
    mocker.patch('openpyxl.reader.excel.load_workbook')
    mocker.patch('os.startfile')
    project_path = os.getcwd()
    out_path = "doc_agil"
    output_filename = "prueba3"
    route = f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx"

    from src.modules.excel_report import modify_excel_report
    modify_excel_report(route)

    assert True
