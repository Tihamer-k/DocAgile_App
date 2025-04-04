"""
Module DataGenerator

This module contains the DataGenerator class,
which is responsible for generating data for Excel files.

Classes:
    DataGenerator: Class to generate data for Excel files.

Functions:
    obtain_diff: Function to obtain the difference values and add them to the settings.LIST.
"""

from colorama import Fore, Style
import src.utils.validation_data as validate
import src.utils.settings_definitions as settings

class DataGenerator:
    """
    The `DataGenerator` class is responsible for generating data for Excel files.

    Attributes:
        - output_filename: A string representing the name of the output file.
        - out_path: A string representing the output path for the generated file.
        - branch: A string representing the branch name.

    Methods:
        - get_output_filename(file_name): Sets the output filename.
            - Params:
                - file_name: A string representing the desired output filename.
            - Returns:
                - output_filename: A string representing the output filename.

        - get_output_path(path, output_filename): Sets the output path.
            - Params:
                - path: A string representing the desired output path.
                - output_filename: A string representing the output filename.
            - Returns:
                - out_path: A string representing the output path.

        - get_branch_name(branch_name): Sets the branch name.
            - Params:
                - branch_name: A string representing the branch name.

        - generate_data(): Generates the data for the Excel file.
            - Returns:
                - None
    """
    def __init__(self):
        self.output_filename = None
        self.out_path = None
        self.branch = None

    def get_output_filename(self, file_name):
        """
        Sets the output filename.

        Args:
            file_name (str): The desired output filename.

        Returns:
            str: The output filename.
        """
        if file_name == "":
            self.output_filename = "nuevo_doc_agil"
            print(Fore.GREEN + "¡Nombre default guardado!\n" + Style.RESET_ALL)
        else:
            self.output_filename = file_name
        return self.output_filename

    def get_output_path(self, path, output_filename):
        """
        Sets the output path.

        Args:
            path (str): The desired output path.
            output_filename (str): The output filename.

        Returns:
            str: The output path.
        """
        if path == "":
            path = "doc_agil"
        self.out_path = validate.final_out_path(path, output_filename)
        return self.out_path

    def get_branch_name(self, branch_name):
        """
        Sets the branch name.

        Args:
            branch_name (str): The branch name.
        """
        self.branch = validate.branch_path(branch_name)

    def generate_data(self):
        """
        Generates the data for the Excel file.

        This method processes the git diff input, extracts relevant information,
        and appends it to the settings.DIFF_DATA list. It handles renamed files
        and formats the data accordingly.

        Returns:
            None
        """
        input_text = obtain_diff()
        input_text = obtain_diff()
        default_values = {
            "renamed": "N/A",
            "renamed_path": "N/A"
        }
        if len(input_text) > 0:
            for i in input_text:
                dato = i.split("###")
                if "  " in dato[1]:
                    dato_new = i.split("  ")
                    default_values["renamed_path"] = dato_new[1]
                    ruta = dato_new[0].replace("R###", "")
                    dato2 = dato_new[0].split("/")
                    dato2_size = len(dato2)
                    componente = dato2[dato2_size - 1]
                    dato_renamed = dato_new[1].split("/")
                    renamed_size = len(dato_renamed)
                    default_values["renamed"] = dato_renamed[renamed_size - 1]
                else:
                    ruta = dato[1]
                    dato2 = dato[1].split("/")
                    dato2_size = len(dato2)
                    componente = dato2[dato2_size - 1]
                estado = validate.format_datatype(dato[0])
                if '.' in componente:
                    nombre_componente, tipo_componente = componente.split(".")
                else:
                    nombre_componente = componente
                    tipo_componente = "-"
                settings.DIFF_DATA.append(
                    {
                        'Componente con Tipo Archivo': componente,
                        'Nombre Componente': nombre_componente,
                        'Tipo Componente': tipo_componente,
                        'Tipo de Acción': estado,
                        'Ruta': ruta,
                        'renombrado': default_values["renamed"],
                        'ruta renombrado': default_values["renamed_path"],
                        'URL rama': self.branch
                    }
                )
                default_values["renamed"] = "N/A"
                default_values["renamed_path"] = "N/A"
        else:
            print(Fore.RED + "¡Data no informada!" + Fore.RESET + " No se genera Excel.")


def obtain_diff():
    """
    Obtain the difference values and add them to the settings.LIST.

    :return: The updated settings.LIST.
    """
    while True:
        data = validate.valid_diff(input())
        if 'Exit' == data:
            break
        if data is not None:
            settings.LIST.append(data.replace(settings.SPACE, "###"))
    return settings.LIST
