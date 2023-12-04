import os
import re
from colorama import Fore, Style

from src.utils import Settings


def format_datatype(param):
    mapping = {
        "M": "Modificado",
        "A": "Nuevo",
        "R": "Renombrado",
        "D": "Eliminado"
    }
    return mapping.get(param, "")


def branch_path(param):
    res = param
    if res == "":
        res = "path no informado"
        print(Fore.GREEN + "¡Nombre default guardado!\n" + Style.RESET_ALL)
    return res


def valid_out_path(param):
    if param != "":
        # RegExp to match Mac/Linux file paths
        mac_linux_regexp = r'^(\/[^/ ]*)+\/?$'
        # Regexp to match Windows file path
        windows_regexp = r'^[a-zA-Z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*$'

        match_unix = re.search(mac_linux_regexp, param)
        match_windows = re.search(windows_regexp, param)

        if match_unix:
            return match_unix.group()
        elif match_windows:
            return match_windows.group()
        else:
            return None
    else:
        return param


def valid_input(input_text):
    regexp = r'(M|A|R|D|R090)\s{4}|\s{7}[\w/.-]+|Exit'
    if re.match(regexp, input_text):
        return re.search(regexp, input_text)


def valid_res(param):
    if param.__contains__("R090"):
        return param.replace("R090    ", "R" + Settings.SPACE)
    else:
        return param


def valid_diff(data):
    x = False
    while not x:
        input_txt = valid_input(data)
        if input_txt:
            return valid_res(data)
        else:
            print("\n¡Formato de entrada no es correcto!" + Fore.RED + f" ({data})\n")
            print("Debe iniciar con M, D, A, seguido por 7 espacios (o R090, seguido por 4 espacios) "
                  "y texto con o sin slash entre el. "
                  "Finalizando con el nombre de el archivo junto con su tipo de archivo (si lo tiene).")
            print("También puedes escribir 'Exit' para finalizar.")
            data = input(Style.RESET_ALL + "\nIntenta de nuevo:\n")


def final_out_path(out_path, output_filename):
    x = False
    project_path = os.getcwd()
    if out_path == "doc_agil" or out_path is None:
        if out_path is None:
            out_path = "doc_agil"
        # print(f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx")
        print(Fore.GREEN + "¡Ruta default añadida!\n" + Style.RESET_ALL)
        return f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx"
    else:
        while not x:
            data = valid_out_path(out_path)
            if data:
                print(Fore.GREEN + "¡Ruta indicada guardada!\n" + Style.RESET_ALL)
                return f"{data}\\{output_filename}.xlsx"
            elif data == "":
                print(Fore.GREEN + "¡Se añadió ruta default!\n" + Style.RESET_ALL)
                return f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx"
            else:
                print("¡Formato de ruta no es correcto!")
                out_path = input("Ingresa la ruta donde guardarás el archivo (opcional):\n")


def get_response(message):
    x = False
    print(message)
    res = input().lower()
    while not x:
        if res == 's':
            return True
        elif res == 'n':
            return False
        else:
            print("¡Respuesta ingresada no es correcta!" + Fore.RED + f" ({res})\n")
            res = input(Style.RESET_ALL + "\nIntenta de nuevo [s|n]:\n").lower()
