import os

from openpyxl.reader.excel import load_workbook

import src.utils.Settings as Settings
import pandas as pd
from pandas import ExcelWriter


class ExcelReport:
    def __init__(self):
        self.data_obj = None

    def generate_excel_report(self, final_out_path: str):
        if len(Settings.DIFF_DATA) > 0:
            self.data_obj = pd.DataFrame(Settings.DIFF_DATA)
            # df = pd.DataFrame(s.COMPONENT)
            try:
                # validar si existe o no el folder de salida:
                os.makedirs(os.path.dirname(final_out_path), exist_ok=True)

                writer = ExcelWriter(final_out_path, engine=None)
                # df.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=2)
                self.data_obj.to_excel(writer, sheet_name="hoja1", index=False)
                writer.close()
            except():
                print("Problema guardando la data")
            print("¡Data guardada!")
            modify_excel_report(final_out_path)
            os.startfile(final_out_path)


def modify_excel_report(final_out_path: str):
    wb = load_workbook(final_out_path)
    ws = wb['hoja1']
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        max_width = 0

        for row_num in range(1, ws.max_row + 1):
            if len(ws[f"{letter}{row_num}"].value) > max_width:
                max_width = len(ws[f"{letter}{row_num}"].value)

        ws.column_dimensions[letter].width = max_width + 1
    wb.save(final_out_path)
