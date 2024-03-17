#!/bin/bash

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pruebas
python -m unittest discover -s tests
