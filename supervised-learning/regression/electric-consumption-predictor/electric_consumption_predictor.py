from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# ------------ CARGA DE DATOS Y LIMPIEZA DE LOS MISMOS ---------------------
# Cargar datos usando ucimlrepo
dataset = fetch_ucirepo(id=235)  # Individual Household Electric Power Consumption

# Crear un DataFrame con los datos cargados
data = pd.concat([dataset.data.features, dataset.data.targets], axis=1)

# Asegurarse de que todas las columnas relevantes sean numéricas
for col in ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity']:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Eliminar filas con valores NaN
data = data.dropna()
# -------------------------------------------------------------------------

# --------------- SELECCIÓN DE CARACTERÍSTICAS Y OBJETIVO ------------------ 
# Seleccionar características (X) y objetivo (y)
# Variables que utilizamos para predecir el consumo:
X = data[['Voltage', 'Global_reactive_power', 'Global_intensity']]
# Variable que queremos predecir, Global Active Power (consumo eléctrico en kW)
y = data['Global_active_power']

# Dividir los datos en conjuntos de entrenamiento y prueba
    #  El 20% de los datos se asignan al conjunto de prueba, y el 80% se asignan al conjunto de entrenamiento.
    # Con random_state=42, fijamos una semilla para que los datos se dividan de la misma manera cada vez que ejecutemos el código.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# -------------------------------------------------------------------------

# -------------------- ESCALAR LAS CARACTERÍSTICAS -----------------------
# Aplicamos escalado con StandardScaler para normalizar los valores
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# -------------------------------------------------------------------------

# -------------------- ENTRENAMIENTO DEL MODELO -----------------------
# Crear y entrenar el modelo de Regresión Lineal
model = LinearRegression()
model.fit(X_train_scaled, y_train)
# -------------------------------------------------------------------------

# ------------------------ REALIZAR PREDICCIONES --------------------------
# Realizar predicciones
y_pred = model.predict(X_test_scaled)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"\nError Cuadrático Medio (MSE): {mse:.2f}")
print(f"Error Absoluto Medio (MAE): {mae:.2f}")
# -------------------------------------------------------------------------

# Comparar predicciones con valores reales
plt.figure(figsize=(10, 6))
plt.plot(y_test.values[:100], label="Valores Reales", marker='o')
plt.plot(y_pred[:100], label="Predicciones", marker='x')
plt.legend()
plt.xlabel("Muestras")
plt.ylabel("Consumo Eléctrico (kW)")
plt.title("Comparación de Predicciones y Valores Reales")
plt.show()
