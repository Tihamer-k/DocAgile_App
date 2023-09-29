import os
import re
from colorama import Fore, Style
import src.utils.Settings as s


def format_datatype(param):
    res = ""
    if param == "M":
        res = "Modificado"
    elif param == "A":
        res = "Nuevo"
    return res


def branch_path(param):
    res = param
    if res == "":
        res = "path no informado"
        print("¡Nombre default guardado!\n")
    return res


def valid_out_path(param):
    regexp = r'^[a-zA-Z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*$'
    match = re.search(regexp, param)
    return match.group() if match else None


def valid_input(input_text):
    regexp = r'(M|A)\s{7}[\w/.-]+|Exit'
    if re.match(regexp, input_text):
        return re.search(regexp, input_text)


def valid_diff(data):
    x = False
    while not x:
        input_txt = valid_input(data)
        if input_txt:
            return data
        else:
            print("\n¡Formato de entrada no es correcto!" + Fore.RED + f" ({data})\n")
            print("Debe iniciar con M o A, seguido por 7 espacios y texto con o sin slash entre el. "
                  "Finalizando con el nombre de el archivo junto con su extención.")
            data = input(Style.RESET_ALL + "\nIntenta de nuevo o solo presiona Enter:\n")


def final_out_path(out_path, output_filename):
    x = False
    if out_path == "doc_agil" or out_path == "":
        if out_path == "":
            out_path = "doc_agil"
        project_path = os.getcwd()
        # print(f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx")
        return f"{project_path}\\resources\\{out_path}\\{output_filename}.xlsx"
    else:
        while not x:
            data = valid_out_path(out_path)
            if data:
                return f"{data}\\{output_filename}.xlsx"
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