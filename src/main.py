"""
Copyright 2024 Tihamer Aldana.
"""
from colorama import Fore, Style

import pyfiglet as pf
from src.modules.command_generator import CommandGenerator
from src.modules.data_generator import DataGenerator
from src.modules.excel_report import ExcelReport

OPTIONAL_PRESS_ENTER = "(opcional, presiona enter para continuar):\n"


def run_project():
    """
    Runs the DocAgile APP project.

    Steps:

    1. Prints the project name using figlet_format.
    2. Creates instances of CommandGenerator, DataGenerator, and ExcelReport.
    3. Retrieves branch names using get_branch_names method of CommandGenerator.
    4. Prompts the user for the output filename and generates the output_filename
     using get_output_filename method of DataGenerator.
    5. Prompts the user for the path where the output file will be saved and generates
     the final_out_path using get_output_path method of DataGenerator.
    6. Prompts the user for the branch name in Bitbucket or GitHub and retrieves the
     branch name using get_branch_name method of DataGenerator.
    7. Prompts the user to enter the git diff and generates the data using generate_data
     method of DataGenerator.
    8. Generates an Excel report using generate_excel_report method of ExcelReport.
    9. Handles KeyboardInterrupt or SystemExit exceptions by printing an error message.

    :return: None
    """
    try:
        project_name = pf.figlet_format("DocAgile APP")
        print(Fore.GREEN + project_name + Style.RESET_ALL)
        branch_action = CommandGenerator()
        data_generator = DataGenerator()
        excel_report = ExcelReport()

        branch_action.get_branch_names()

        output_filename = data_generator.get_output_filename(
            input(
                f"Indica el nombre del archivo de salida "
                f"{Fore.RED + OPTIONAL_PRESS_ENTER + Style.RESET_ALL}"
            )
        )

        path = input(f"Ingresa la ruta donde guardarás el archivo de manera local "
                     f"{Fore.RED + OPTIONAL_PRESS_ENTER + Style.RESET_ALL}")

        final_out_path = data_generator.get_output_path(path, output_filename)

        branch_name = input("ingresa path de la rama en Bitbucket o GitHub... "
                            f"{Fore.RED + OPTIONAL_PRESS_ENTER + Style.RESET_ALL}"
                            )

        data_generator.get_branch_name(branch_name)
        print("\n")
        print("Ingresa el git diff copiado, presiona Enter y escribe "
              + Fore.RED + "'Exit'" + Style.RESET_ALL + " para finalizar.\n")

        data_generator.generate_data()

        excel_report.generate_excel_report(final_out_path)
    except (KeyboardInterrupt, SystemExit) as e:
        print(Fore.RED + "An error occurred. Please try again later. " + Style.RESET_ALL)
        print(str(e))


if __name__ == '__main__':
    run_project()
