# Descripción

El presente repositorio es una muestra de como se van a manejar todos los proyectos de visión, ya que se están utilizando diferentes librerías y ambientes de trabajo para el uso de diversas herramientas, en algunas tenemos contenedores docker y en otras tenemos ambientes de trabajo generados con anaconda. Esto se realiza con la finalidad de tener las librerías encansuladas y que no entren en conflicto con las demás. Por ejemplo el sistema operativo trae por defecto instalado python pero en su versión 2 (en linux y macOs) para algunas aplñicaciones de visión dicha versión de python es obsoleta, por lo que debemos instalar alguna versión de python 3 y tambien difiere entre aplicaciones.

Para el presente repositorio se utilizó un ambiente llamado visión generado para trabajar con opencv y manejar datos e imagenes con la cpu, por lo que no tenemos ni tensorflow ni paytorch en dicho ambiente.

# Ambiente

El presente ambiente corre dentro del servidor con anaconda, para crear dicho ambiente ejecutamos:

```sh
cd Cursos
conda activate
conda create -n vision python
conda activate vision
```
una vez tenemos activado el ambiente instalamos las dependencias necesarias para que el ambiente pueda correr nuestra aplicación:

```sh
pip3 install -r requirements.txt
```
Ahora ubicados en la carpeta py-project

```sh
cd py-project
```

# Ejecución

para ejecutar el programa debemos estar parados en donde se encuentra nuestro programa y dese la terminal lanzamos el siguiente comando:

```sh
python3 hello.py
```
