# WILLAC UMU API
API Rest de Willac Umu, donde se hace uso de algoritmos de machine learning para el entrenamiento del sistema y predicción de datos.

## Requerimientos para la instalación y uso del API

#### Interprete
- Python 3~

#### Instalación
Para toda la instalación usar el Command Prompt de Windows.

Abrir la terminal y clonar los archivos en la carpeta deseada.

    $ git clone https://github.com/JeielLovera/willac_umu_api.git

Moverse a la carpeta donde se clonaron los archivos e instalar un virtual environment de python.

    $ cd willac_umu_api
    $ python -m venv venv

Activar el virtual environment.

    $ cd venv/Scripts
    $ activate

Instalar las extensiones necesarias para el funcionamiento del api desde el archivo requirements.txt

    cd ../..
    (venv)$ pip install -r requirements.txt

Si tuvo algún error durante la instalación, realice los siguientes pasos:
- Abra el Editor de Registro (Registry Editor) con el buscador de Windows.
- Acceda a la ruta 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem'
- Cambie el valor de la variable 'LongPathsEnabled' a 1
- Elimine la carpeta Codigo/willac_umu_api/venv
- Vuelva a realizar los pasos desde la instalación del virtual environment.

#### Uso del API
Teniendo ya el venv activado y las extensiones instaladas desde el requirements.txt, ya se puede iniciar la aplicación.

    (venv)$ python app/main.py

Para ver la documentación y prueba de los endpoints debe ir a la siguiente url

    http://localhost:8000/docs
    

## Archivos core
#### Data_Standarization.py
Contiene todas las funciones para estandarizar los datos de un archivo. El resultado es un dataset que contiene únicamente 5 áreas de evaluación: Matemática, Comunicación, Persona Familia y Relaciones Humanas, Ciencias Sociales, y Ciencia y Ambiente.

#### Multilayer_Perceptron_Trainer.py
Contiene las funciones que recibirán el dataset para entrenar a la red neuronal mediante backpropagation. El resultado son los pesos y bias finales de cada capa de la red.

#### Willaq_Umu_Prediction.py
Willaq_Umu_Prediction.py: Contiene las funciones para predecir el dataset ingresado por el usuario. El resultado es la predicción del ingreso o no ingreso de los estudiantes a cualquiera de las 2 universidades.

## Estructura de archivos
```
willac_umu_api
├──app
│   ├── server
│   │   ├── code
│   │   │   ├── Data_Standardization.py
│   │   │   ├── Multilayer_Perceptron_Trainer.py
│   │   │   └── Willaq_Umu_Prediction.py
│   │   ├── files
│   │   ├── models
│   │   │   └── weights_bias.py
│   │   ├── routes
│   │   │   ├── training.py
│   │   │   └── predict.py
│   │   ├── app.py
│   │   └── database.py
│   ├── __init__.py
│   └── main.py
├── .gitignore
├── README.md
└── requirements.txt
```