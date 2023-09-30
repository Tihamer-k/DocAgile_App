from colorama import Fore, Style

import src.utils.ValidationData as Validate


class CommandGenerator:
    def __init__(self):
        self.__branch_name_left = None
        self.__branch_name_right = None

    def generate_git_diff_command(self, branch_left, branch_right):
        if branch_left is not None and branch_right is not None:
            self.__branch_name_left = branch_left
            self.__branch_name_right = branch_right
            return (f"git diff --name-status --diff-filter=MRAD "
                    f"origin/{self.__branch_name_left}"
                    f"..origin/{self.__branch_name_right}")
        else:
            return "nombres de ramas no informados"

    def get_branch_names(self):
        message = "¿Desea generar su comando git diff? [s|n]: "
        res: bool = Validate.get_response(message)
        if res:
            path_left = input("Ingrese rama estable: ")
            path_right = input("Ingrese rama modificada: ")
            command = self.generate_git_diff_command(path_left, path_right)
            print(
                f"¡Acá está tú comando!\n" +
                Fore.GREEN + f" {command} \n " +
                Style.RESET_ALL + f"Ejecutalo en la ubicación de tú proyecto y vuelve con la respuesta copiada.")
            print("\n")
        else:
            print("\n")
            pass
