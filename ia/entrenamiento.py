import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# 1. Cargar dataset.csv
ruta_base = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(ruta_base, "..", "datos", "dataset.csv")
df = pd.read_csv(csv_path)
if "frase" not in df.columns or "intencion" not in df.columns:
    raise ValueError("El CSV debe tener columnas 'frase' e 'intencion'")
frases = df["frase"]
intenciones = df["intencion"]


# 2. Convertir texto a vectores
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(frases)

# 3. Entrenar modelo
modelo = MultinomialNB()
modelo.fit(X, intenciones)

# 4. Guardar modelo y vectorizador
modelo_dir = os.path.join(ruta_base, "..", "modelos")
os.makedirs(modelo_dir, exist_ok=True)
joblib.dump(modelo, os.path.join(modelo_dir, "clasificador.pkl"))
joblib.dump(vectorizador, os.path.join(modelo_dir, "vectorizador.pkl"))

print("✅ Modelo entrenado y guardado correctamente.")
