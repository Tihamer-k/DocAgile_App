"""
This module contains unit tests for the DataGenerator class.

Tests:
    - test_get_output_filename: Verifies the generation of the output filename.
    - test_get_output_path: Verifies the generation of the output path.
    - test_get_branch_name: Verifies the retrieval of the branch name.
"""

import os
def test_get_output_filename(data_generator):
    """
    Verifies the generation of the output filename.
    """
    assert data_generator.get_output_filename("") == "nuevo_doc_agil"

    # Test with provided filename
    assert data_generator.get_output_filename("archivo_prueba") == "archivo_prueba"


def test_get_output_path(data_generator):
    """
    Verifies the generation of the output path.
    """
    # Test with path
    project_path = os.getcwd()
    out_path = "doc_agil"
    output_filename = "archivo_prueba2"
    route = f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx"
    assert route in data_generator.get_output_path("", output_filename)

    # Test with provided path
    out_path = "carpeta_prueba"
    route = f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx"
    assert route in data_generator.get_output_path(route, output_filename)


def test_get_branch_name(data_generator):
    """
    Verifies the retrieval of the branch name.
    """
    # Test with empty branch name
    assert data_generator.get_branch_name("") is None
