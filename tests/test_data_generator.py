import os


def test_get_output_filename(data_generator):
    # Test con nombre de archivo vacío
    assert data_generator.get_output_filename("") == "nuevo_doc_agil"

    # Test con nombre de archivo proporcionado
    assert data_generator.get_output_filename("archivo_prueba") == "archivo_prueba"


def test_get_output_path(data_generator):
    # Test con ruta
    project_path = os.getcwd()
    out_path = "doc_agil"
    output_filename = "archivo_prueba2"
    route = f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx"
    assert route in data_generator.get_output_path("", output_filename)

    # Test con ruta proporcionada
    out_path = "carpeta_prueba"
    route = f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx"
    assert route in data_generator.get_output_path(route, output_filename)


def test_get_branch_name(data_generator):
    # Test con nombre de rama vacío
    assert data_generator.get_branch_name("") is None
