# Fill_DocAgil_App
<p>Proyecto pensado para facilitar la documentación de los componentes modificados con los datos obtenidos del comando:</p>

```bash
git diff --name-status --diff-filter=MRAD origin/"rama a comparar"..origin/"rama modificada"
```
#### Resultado ejemplo de ejecución del comando anterior:

```text
M       bla/src/main/java/com/exm/ble/mapper/Bla.jspx
M       bla/src/main/java/com/exm/ble/mapper/Ble.java
A       bla/src/main/java/com/exm/ble/mapper/Bli.python
M       bla/src/main/java/com/exm/ble/mapper/impl/Blo.java
A       bla/src/main/java/com/exm/ble/proxy/Blu.js
```
<p>El anterior es el texto que copiaremos y pegaremos en la consola cuando el programa lo solicite.</p>
<p>Requerido tener instalado y actualizado pip y pandas, para ello usaremos lo siguiente:</p>
 
#### Para instalación y actualización de pip:

Te puedes apoyar [acá](https://phoenixnap.com/kb/install-pip-windows) con respecto a la instalación.

Para actualizar pip:
```bash
python -m pip install --upgrade  
```
> Si es requerido validar que versión de python se está usando para asi mismo saber si iniciar con `py`,
> `python` o `python3`. En este caso se usó python 3.9

#### Para instalación de pandas:
```bash
pip install pandas    
```
