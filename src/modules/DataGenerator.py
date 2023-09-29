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
            print("¡Nombre default guardado!\n")
        else:
            self.output_filename = file_name
        return self.output_filename

    def get_output_path(self, path, output_filename):
        if path == "":
            path = "doc_agil"
            print("¡Nombre default guardado!\n")
        self.out_path = Validate.final_out_path(path, output_filename)
        return self.out_path

    def get_branch_name(self, branch_name):
        self.branch = Validate.branch_path(branch_name)

    def generate_data(self):
        input_text = obtain_diff()
        for i in input_text:
            dato = i.split("###")
            estado = Validate.format_datatype(dato[0])
            ruta = dato[1]
            dato2 = dato[1].split("/")
            dato2_size = len(dato2)
            componente = dato2[dato2_size - 1]
            dato3 = componente.split(".")
            tipo_componente = dato3[1]
            Settings.DIFF_DATA.append(
                {
                    'Nombre Archivo/Componente con Tipo Archivo/Componente': componente,
                    'Nombre Archivo/Componente': dato3[0],
                    'Tipo Archivo/Componente': tipo_componente,
                    'Tipo de Acción': estado,
                    'Ruta': ruta,
                    'URL rama': self.branch
                }
            )


def obtain_diff():
    while True:
        data = Validate.valid_diff(input())
        if 'Exit' == data:
            break
        Settings.LIST.append(data.replace(Settings.SPACE, "###"))
    return Settings.LIST
