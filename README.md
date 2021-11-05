# Precios Spot de Chicago

Proyecto diseñado con el fin de tener toda la data histórica de los precios spot de Chicago.

Se compone de diversas carpetas:

- **Data**
    - *Cbot.xlsx*: Data descargada para soja, maíz y trigo.

- **Scripts/Update**
    - *Update_Data*: Extracción de datos, transformación a usd/tn, cálculo de nuevas variables y actualización de base y gráficos.


- **Grafs**
    - Linechart de precios 1990 hasta la actualidad.
    - Histograma con línea punteada del último precio y el porcentaje de días que supera ese valor.
    - Linechart de la volatilidad intradiaria: Diferencia entre máximo y mínimo.
    - Linechart de un índice de precios base 100 = 01/01/1990

## Proceso para actualizar el proyecto
Para correr el proyecto solamente se debería:
1. Correr el script de *CBOT/Scripts/Update/Update_Data.py*

## Vizualiación de resultados
Se puede: 
1. Ver la base entera en *CBOT\Data\Cbot.xlsx*
2. Ver los gráficos en *CBOT/Grafs*

