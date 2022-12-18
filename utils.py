import settings as s
import validations as v
import pandas as pd
from pandas import ExcelWriter


def get_and_set_data():
    output_filename = input("Indica el nombre del archivo de salida:\n")
    if output_filename == "":
        output_filename = "nuevo_doc_agil"
    out_path = input("Ingresa la ruta donde guardarás el archivo (opcional):\n")
    if out_path == "":
        out_path = "doc_agil"
    out_path = v.final_out_path(out_path, output_filename)
    branch = input("ingresa path de la rama en Bitbucket (opcional):\n")
    branch = v.branch_path(branch)
    print("\n")
    print("Ingresa el git diff copiado, presiona Enter y escribe 'Exit' para Salir.")
    input_text = v.obtain_diff()
    # input_text = sys.stdin.read().replace(space, "-").split("\n")
    print("\n")
    for i in input_text:
        dato = i.split("-")
        estado = v.format_datatype(dato[0])
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
        s.COMPONENT.append({'Nombre Archivo/Componente': dato3[0]})
        s.COMPONENT_TYPE.append({'Tipo Archivo/Componente': tipo_componente})
        s.COMPONENT_STATUS.append({'Tipo de Acción': estado})
        s.COMPONENT_PATH.append({'Ruta': ruta})
        s.BRANCH_PATH_COMPONENT.append({'URL rama': branch})
        excel_writer(out_path)


def excel_writer(out_path):
    # print(diff_data)
    # df = pd.DataFrame(diff_data)
    df = pd.DataFrame(s.COMPONENT)
    df1 = pd.DataFrame(s.COMPONENT_TYPE)
    df2 = pd.DataFrame(s.COMPONENT_STATUS)
    df3 = pd.DataFrame(s.COMPONENT_PATH)
    df4 = pd.DataFrame(s.BRANCH_PATH_COMPONENT)
    try:
        writer = ExcelWriter(out_path, engine=None)
        df.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=2)
        df1.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=5)
        df2.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=7)
        df3.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=9)
        df4.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=15)
        writer.save()
    except():
        print("Problema guardando la data")
    print("¡Data guardada en el archivo!")