"""
Module CommandGenerator

This module contains the CommandGenerator class, which is used to generate git diff commands
based on the branch names provided by the user.

Classes:
    CommandGenerator: Class to generate git diff commands.
"""

from colorama import Fore, Style
import src.utils.validation_data as validate_data


class CommandGenerator:
    """
    CommandGenerator

    This class represents a command generator for generating git diff commands.

    Attributes:
        __branch_name_left (str): The name of the left branch.
        __branch_name_right (str): The name of the right branch.

    Methods:
        generate_git_diff_command(branch_left, branch_right)
            Generates a git diff command based on the provided branch names.

        get_branch_names()
            Prompts the user to enter the branch names and generates the git diff command.

    """

    def __init__(self):
        self.__branch_name_left = None
        self.__branch_name_right = None

    def generate_git_diff_command(self, branch_left, branch_right):
        """
        Generates a git diff command based on the provided branch names.

        Args:
            branch_left (str): The name of the left branch.
            branch_right (str): The name of the right branch.

        Returns:
            str: The git diff command or an error message if branch names are not provided.
        """
        if branch_left is not None and branch_right is not None:
            self.__branch_name_left = branch_left
            self.__branch_name_right = branch_right
            return (f"git diff --name-status --diff-filter=MRAD "
                f"origin/{self.__branch_name_left}"
                f"..origin/{self.__branch_name_right}")
        return "nombres de ramas no informados"

    def get_branch_names(self):
        """
        Prompts the user to enter the branch names and generates the git diff command.

        This method asks the user if they want to generate a git diff command.
        If the user agrees, it prompts for the names of the stable and modified branches,
        generates the git diff command, and prints it.

        Returns:
            None
        """
        message = "¿Desea generar su comando git diff? [s|n]: "
        res: bool = validate_data.get_response(message)
        if res:
            path_left = input("Ingrese rama estable: ")
            path_right = input("Ingrese rama modificada: ")
            command = self.generate_git_diff_command(path_left, path_right)
            print(
                "¡Acá está tú comando!\n" +
                Fore.GREEN + f" {command} \n " +
                Style.RESET_ALL +
                "Ejecutalo en la ubicación de tú proyecto y vuelve con la respuesta copiada.\n")
