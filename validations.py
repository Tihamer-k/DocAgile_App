import re

from colorama import Fore, Style

import settings as s


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
    return res


def valid_out_path(param):
    return re.search("^C:..\\w", param)


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
            data = input(Style.RESET_ALL + "\nIntenta de nuevo:\n")


def final_out_path(out_path, output_filename):
    x = False
    if out_path == "doc_agil":
        return f"./{out_path}/{output_filename}.xlsx"
    else:
        while not x:
            data = valid_out_path(out_path)
            if data:
                return f"{out_path}/{output_filename}.xlsx"
            else:
                print("¡Formato de ruta no es correcto!")
                out_path = input("Ingresa la ruta donde guardarás el archivo (opcional):\n")


def obtain_diff():
    while True:
        data = valid_diff(input())
        if 'Exit' == data:
            break
        s.LIST.append(data.replace(s.SPACE, "###"))
    return s.LIST
