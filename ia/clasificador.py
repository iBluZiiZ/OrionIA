import joblib
import os

# Ruta segura a /modelos
ruta_base = os.path.dirname(os.path.abspath(__file__))
modelo_path = os.path.join(ruta_base, "..", "modelos", "clasificador.pkl")
vector_path = os.path.join(ruta_base, "..", "modelos", "vectorizador.pkl")

# Cargar modelo y vectorizador
modelo = joblib.load(modelo_path)
vectorizador = joblib.load(vector_path)

def detectar_intencion(frase):
    entrada_vect = vectorizador.transform([frase])
    prediccion = modelo.predict(entrada_vect)
    return prediccion[0]
