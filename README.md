# Fill_DocAgil_App
<p>Proyecto pensado para facilitar la documentación de los componentes modificados con los datos obtenidos del comando:</p>

```bash
git diff --name-status --diff-filter=MRAD origin/"rama a comparar"..origin/"rama modificada"
```

<p>Requerido tener instalado y actualizado pip y pandas, para ello usaremos lo siguiente:</p>
 
### Para instalación y actualización de pip:
```bash
python -m pip install --upgrade  
```
> Si es requerido validar que versión de python se está usando para asi mismo saber si iniciar con `py`,
> `python` o `python3`. En este caso se usó python 3.9

### Para instalación de pandas:
```bash
pip install pandas    
```
