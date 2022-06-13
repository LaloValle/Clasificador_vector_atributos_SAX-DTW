# Clasificador de gestos motrices utilizando vectores de atributos distancia DTW sobre series de tiempo en representación SAX

Este trabajo presenta un análisis de la efectividad en términos de precisión y tiempo de ejecución, para 3 modelos que implementan el algoritmo DTW, la técnica SAX y modelos clásicos de *machine learning* como *k-NN* y *SVC*, en la tarea de clasificación de series de tiempo. Bajo el contexto de reconocimiento de gestos motrices, se utilizan patrones en términos de fuerzas de aceleración, muestreados en los ejes tridimensionales usando el sensor acelerómetro integrado en dispositivos *wearable* o *smartphones*. Se analiza el desempeño de los modelos con el conjunto de datos *Gesture Pebble*, publicamente disponible en *UCR Time Series Archive*, que se compone por 304 patrones procedente de 4 participantes distintos, representados como series de tiempo de longitud variable de las mediciones de la acelaración en el eje Z para 6 gestos únicos.

## Dependencias
El lenguaje de programación utilizado para la implementación es Python en su versión 3.
Las bibliotecas requeridas para la ejecución de los modelos o archivos de prueba son:
* Numpy
* Matplotlib
* Pandas
* scikit-learn
* dtaidistance

## Estructura del repositorio
- **Artículo**
  
  Este apartado almacena el artículo del proyecto y los archivos requeridos para la compilación del documento en LaTex
  
- **Código**
  
  Archivos fuente y carpetas relacionadas con la ejecución de las funciones y métodos reportados en el artículo
  
  - **Data**
    
    Archivos con los datos utilizados durante el desarrollo y pruebas de las técnicas y modelos
    
  - **Libraries**
    
    Archivos fuentes que implementa los algoritmo y técnicas usadas en los modelos(DTW,SAX,Optimización del parámetro *w*,...)
    > > *Particularmente esta biblioteca es funcional cuando se manejan arreglos numpy(secuencias temporales de longitud fija)*
    
  - **LLibraries**
    
    Archivos fuentes que implementa los algoritmo y técnicas usadas en los modelos(DTW,SAX,Optimización del parámetro *w*,...)
    > > *Particularmente esta biblioteca es funcional cuando se manejan listas de arreglos numpy(secuencias temporales de longitud variable)*
    
  - **Results**
    
    Hojas de cálculo utilizadas para realizar el registro de los resultados de cada modelo
    
  - **Tests**
    
    Archivo fuentes utilizados durante el desarrollo como sencillos programas que prueban la funcionalidad de las funciones
