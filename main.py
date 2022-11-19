import sys
import pandas as pd
from pandas import ExcelWriter

space = " " * 7
diff_data = []
component = []
component_type = []
component_status = []
component_path = []
branch_path_component = []
out_path = f"./{out_path}/{output_filename}.xlsx"

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


def get_data():
    output_filename = input("Indica el nombre del archivo de salida:\n")
    if output_filename == "":
        output_filename = "nuevo_doc_agil"
    out_path = input("Ingresa la ruta donde guardarás el archivo:\n")
    if out_path == "":
        out_path = "doc_agil"
    branch = input("ingresa path de la rama en Bitbucket (opcional):\n")
    branch = branch_path(branch)
    print("\n")
    print("Ingresa el git diff copiado finalizando con un Ctrl + D\n")
    input_text = sys.stdin.read().replace(space, "-").split("\n")
    print("\n")
    for i in input_text:
        dato = i.split("-")
        estado = format_datatype(dato[0])
        ruta = dato[1]
        dato2 = dato[1].split("/")
        dato2_size = len(dato2)
        componente = dato2[dato2_size - 1]
        dato3 = componente.split(".")
        tipo_componente = dato3[1]
        # diff_data.append({
        #     'Componente': componente,
        #     'Tipo componente': tipo_componente,
        #     'Estado': estado,
        #     'Ruta': ruta,
        #     'URL rama': branch
        # })
        component.append({'Componente': componente})
        component_type.append({'Tipo componente': tipo_componente})
        component_status.append({'Estado': estado})
        component_path.append({'Ruta': ruta})
        branch_path_component.append({'URL rama': branch})


def excel_writer():
    # print(diff_data)
    # df = pd.DataFrame(diff_data)
    df = pd.DataFrame(component)
    df1 = pd.DataFrame(component_type)
    df2 = pd.DataFrame(component_status)
    df3 = pd.DataFrame(component_path)
    df4 = pd.DataFrame(branch_path_component)
    writer = ExcelWriter(out_path, engine=None)
    df.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=2)
    df1.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=5)
    df2.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=7)
    df3.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=9)
    df4.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=15)
    writer.save()
    print("¡Data guardada en el archivo!")


if __name__ == '__main__':
    get_data()
    excel_writer()
