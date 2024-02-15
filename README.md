# maper-back-chall

## Backend Challenge jan-2024

## Objetivo

Este challenge evalúa su capacidad para interpretar requerimientos, pensar lógicamente,
diseñar software con criterio y escribir código limpio y modular.

## Instrucciones

El sistema MAPER procesa y almacena mediciones de 10000 sensores que envían un valor
al servidor en la nube cada 15’. El servidor tiene una base de datos Postgres y la API y
algoritmos están implementados en Python, usando Django. En la base de datos hay
información de 5 años de estos 10000 sensores.

1. Diseñar una tabla de la DB para almacenar los valores que llegan de los 10000
sensores, cada 15’. Además, diseñar una API que sería implementada con Django
para que el Frontend pida mediciones de hasta 16 sensores simultáneamente, por
un periodo de tiempo máximo de 1 año. No se pide implementar el diseño, sino:
a. Definir el formato del Request y el Response, incluyendo detalle del formato
de los datos que serán transmitidos al Frontend.
b. Definir columnas y otros parámetros de diseño de la tabla de la DB.
c. Enunciar las consideraciones generales de cómo funcionaría la API ante un
GET del Frontend.

2. Se deberá implementar un “horímetro” (medidor de horas de “máquina encendida”).
Cada máquina monitoreada tiene instalada 4 sensores. Los sensores instalados en
una máquina determinada miden la vibración de la máquina simultáneamente. Se
provee un CSV con valores de vibración reportado por cada sensor y timestamp.

    - Diseñar y crear una tabla en la DB para almacenar el tiempo de
funcionamiento por día de cada máquina. Utilice el motor de DB que prefiera.

    - Diseñar e implementar un algoritmo que mida las horas de funcionamiento de
la máquina (es decir, el tiempo en que la máquina estuvo encendida, en
horas). En producción, este algoritmo correría una vez por día, y “miraría” los
datos de vibración del día anterior, calculando las horas de funcionamiento.
No se pide implementar el mecanismo de ejecución periódica de este
algoritmo, pero sí diseñar e implementar el algoritmo de manera aislada. El
input del algoritmo es los datos del CSV, pero el output deberá escribirse en
la tabla de la DB.

    - Diseñar e implementar con Django una API para que el Frontend pida las
horas encendidas de una máquina específica en un día específico.