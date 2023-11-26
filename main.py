from colorama import Fore, Style

from src.modules.CommandGenerator import CommandGenerator
from src.modules.DataGenerator import DataGenerator
from src.modules.ExcelReport import ExcelReport

OPTIONAL_PRESS_ENTER = "(opcional, presiona enter para continuar):\n"


def run_project():
    print("¡Bienvenido a DocAgile_APP!\n")
    branch_action = CommandGenerator()
    data_generator = DataGenerator()
    excel_report = ExcelReport()

    branch_action.get_branch_names()

    output_filename = data_generator.get_output_filename(
        input(f"Indica el nombre del archivo de salida {Fore.RED + OPTIONAL_PRESS_ENTER + Style.RESET_ALL}"))

    path = input(f"Ingresa la ruta donde guardarás el archivo de manera local "
                 f"{Fore.RED + OPTIONAL_PRESS_ENTER + Style.RESET_ALL}")

    final_out_path = data_generator.get_output_path(path, output_filename)

    branch_name = input(f"ingresa path de la rama en Bitbucket {Fore.RED + OPTIONAL_PRESS_ENTER + Style.RESET_ALL}")

    data_generator.get_branch_name(branch_name)
    print("\n")
    print("Ingresa el git diff copiado, presiona Enter y escribe "
          + Fore.RED + "'Exit'" + Style.RESET_ALL + " para finalizar.\n")

    data_generator.generate_data()

    excel_report.generate_excel_report(final_out_path)


if __name__ == '__main__':
    run_project()
