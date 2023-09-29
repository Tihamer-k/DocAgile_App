from abc import ABC

import src.utils.Settings as Settings
import pandas as pd
from pandas import ExcelWriter


class ExcelReport():
    def __init__(self):
        self.data_obj = None

    def generate_excel_report(self, final_out_path):
        self.data_obj = pd.DataFrame(Settings.DIFF_DATA)
        # df = pd.DataFrame(s.COMPONENT)
        try:
            writer = ExcelWriter(final_out_path, engine="openpyxl")
            # df.to_excel(writer, sheet_name="hoja1", index=False, startrow=2, startcol=2)
            self.data_obj.to_excel(writer, sheet_name="hoja1", index=False)
            writer._save()
            writer.close()
        except():
            print("Problema guardando la data")
        print("¡Data guardada!")
