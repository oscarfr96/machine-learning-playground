# Machine Learning Playground

Este repositorio contiene prácticas y ejercicios de Machine Learning organizados por tipo de aprendizaje. El objetivo es explorar diferentes técnicas, aprender su implementación práctica y entender cómo resolver problemas reales utilizando estas herramientas.

## 📚 Contenidos

### 1. Supervised Learning (Aprendizaje Supervisado)
- **Regression**:
  - [Electric Consumption Predictor](supervised-learning/regression/electric-consumption-predictor): Predicción del consumo eléctrico basado en datos históricos.

---

## 🧪 Detalles de los Proyectos

### 📂 `supervised-learning/regression/electric-consumption-predictor`

#### **Descripción**
Este proyecto utiliza un modelo de **Regresión Lineal** para predecir el consumo eléctrico de un hogar. El modelo se entrena con datos históricos, analizando variables como el voltaje, la potencia reactiva y la intensidad de corriente, para estimar el consumo eléctrico en kilovatios.

#### **Dataset**
El proyecto emplea el dataset público **"Individual Household Electric Power Consumption"**, disponible en el [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption).

#### **Objetivo**
Predecir la variable **Global Active Power** (consumo eléctrico) basándose en las siguientes características:
- **Voltage**: Voltaje en la red eléctrica.
- **Global Reactive Power**: Potencia reactiva global.
- **Global Intensity**: Intensidad de corriente global.

#### **Tecnologías Usadas**
- **Python**: Lenguaje principal.
- **Pandas**: Para manipulación y análisis de datos.
- **Scikit-learn**: Para escalado de características, entrenamiento y evaluación del modelo.
- **Matplotlib**: Para la visualización de resultados.

#### **Estructura**
electric-consumption-predictor/ │ ├── electric_consumption_predictor.py # Script principal del proyecto

#### **Cómo Ejecutar**
1. Navega a la carpeta del proyecto:
   cd supervised-learning/regression/electric-consumption-predictor
2. Asegúrate de instalar las dependencias necesarias:
  pip install -r requirements.txt
3. Ejecuta el script principal:
  python electric_consumption_predictor.py

#### Resultados
Métricas:
##### Error Cuadrático Medio (MSE): Mide el promedio de los errores al cuadrado.
##### Error Absoluto Medio (MAE): Mide el error promedio absoluto.
Gráfico:
Comparación entre los valores reales y las predicciones del modelo.

## 🔍 Próximos Proyectos
El repositorio se irá ampliando con más ejercicios de Machine Learning, incluyendo:

Clasificación en aprendizaje supervisado.
Clustering y reducción de dimensionalidad en aprendizaje no supervisado.
Implementaciones básicas de aprendizaje por refuerzo.

## 📄 Licencia
Este proyecto está distribuido bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
