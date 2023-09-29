from src.modules.CommandGenerator import CommandGenerator
from src.modules.DataGenerator import DataGenerator
from src.modules.ExcelReport import ExcelReport

OPTIONAL_PRESS_ENTER = "(opcional, presiona enter para continuar):\n"


def run_project():
    print("¡Bienvenido a Fill_DocAgil_APP!\n")
    branch_action = CommandGenerator()
    branch_action.get_branch_names()

    data_generator = DataGenerator()
    output_filename = data_generator.get_output_filename(
        input(f"Indica el nombre del archivo de salida {OPTIONAL_PRESS_ENTER}"))
    out_path = input(f"Ingresa la ruta donde guardarás el archivo de manera local {OPTIONAL_PRESS_ENTER}")
    final_output_path = data_generator.get_output_path(out_path, output_filename)
    branch_name = input(f"ingresa path de la rama en Bitbucket {OPTIONAL_PRESS_ENTER}")
    data_generator.get_branch_name(branch_name)
    print("\n")
    print("Ingresa el git diff copiado, presiona Enter y escribe 'Exit' para finalizar.\n")
    data_generator.generate_data()
    excel_report = ExcelReport()
    excel_report.generate_excel_report(final_output_path)


if __name__ == '__main__':
    run_project()
