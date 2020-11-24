# WILLAC UMU API
API Rest de Willac Umu, donde se hace uso de algoritmos de machine learning para el entrenamiento del sistema y predicción de datos

## Requerimientos para la instalación y uso del API

#### Interprete
- Python 3~

#### Instalación
Abrir la terminar y clonar los archivos en la carpeta deseada

    $ git clone https://github.com/JeielLovera/willac_umu_api.git

Moverse a la carpeta donde se clonaron los archivos e instalar un virtual enviroment de python

    $ python -m venv venv

Cambiar el interprete por el venv

    $ source venv/bin/activate
    $ export PYTHONPATH=$PWD

Instalar las extenxiones necesarias para el funcionamiento del api desde el archivo requirements.txt

    (venv)$ pip install -r requirements.txt

#### Uso del API
Teniendo ya el venv activado y las extensiones instaladas desde el requirements.txt, ya se puede iniciar la aplicación

    (venv)$ python app/main.py
    

## Archivos core
#### Data_Standarization.py
Contiene todas las funciones para estandarizar el archivo de los datos de entrenamiento. El resultado es que los datos contienen los datos de entrada con los cinco cursos de Matemática, Comunicación, Persona Familia y Relaciones Humanas, Ciencias Sociales y Ciencia y Ambiente.
#### Multilayer_Perceptron_Trainer.py
### Willaq_Umu_Prediction.py
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

