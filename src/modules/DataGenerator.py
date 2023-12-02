from colorama import Fore, Style

import src.utils.ValidationData as Validate
import src.utils.Settings as Settings


class DataGenerator:
    def __init__(self):
        self.output_filename = None
        self.out_path = None
        self.branch = None

    def get_output_filename(self, file_name):
        if file_name == "":
            self.output_filename = "nuevo_doc_agil"
            print(Fore.GREEN + "¡Nombre default guardado!\n" + Style.RESET_ALL)
        else:
            self.output_filename = file_name
        return self.output_filename

    def get_output_path(self, path, output_filename):
        if path == "":
            path = "doc_agil"
        self.out_path = Validate.final_out_path(path, output_filename)
        return self.out_path

    def get_branch_name(self, branch_name):
        self.branch = Validate.branch_path(branch_name)

    def generate_data(self):
        input_text = obtain_diff()
        renamed = "N/A"
        renamed_path = "N/A"
        if len(input_text) > 0:
            for i in input_text:
                dato = i.split("###")
                if "  " in dato[1]:
                    dato_new = i.split("  ")
                    renamed_path = dato_new[1]
                    ruta = dato_new[0].replace("R###", "")
                    dato2 = dato_new[0].split("/")
                    dato2_size = len(dato2)
                    componente = dato2[dato2_size - 1]
                    dato_renamed = dato_new[1].split("/")
                    renamed_size = len(dato_renamed)
                    renamed = dato_renamed[renamed_size - 1]
                else:
                    ruta = dato[1]
                    dato2 = dato[1].split("/")
                    dato2_size = len(dato2)
                    componente = dato2[dato2_size - 1]
                estado = Validate.format_datatype(dato[0])
                if '.' in componente:
                    dato3 = componente.split(".")
                    nombre_componente = dato3[0]
                    tipo_componente = dato3[1]
                else:
                    nombre_componente = componente
                    tipo_componente = "-"
                Settings.DIFF_DATA.append(
                    {
                        'Componente con Tipo Archivo': componente,
                        'Nombre Componente': nombre_componente,
                        'Tipo Componente': tipo_componente,
                        'Tipo de Acción': estado,
                        'Ruta': ruta,
                        'URL rama': self.branch,
                        'renombrado': renamed,
                        'ruta renombrado': renamed_path
                    }
                )
                renamed = "N/A"
                renamed_path = "N/A"
        else:
            print(Fore.RED + "¡Data no informada!" + Fore.RESET + " No se genera Excel.")


def obtain_diff():
    while True:
        data = Validate.valid_diff(input())
        if 'Exit' == data:
            break
        if data is not None:
            Settings.LIST.append(data.replace(Settings.SPACE, "###"))
    return Settings.LIST
