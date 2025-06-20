import spacy

nlp = spacy.load

palabras_clave = {
    "youtube": ["youtube", "vídeos", "videos"],
    "google": ["google", "navegador", "buscar"],
    "hora": ["hora", "tiempo"],
    "musica": ["música", "canción", "reproducir", "sonido"],
    "modo oscuro": ["modo oscuro", "tema oscuro"],
    "whatsapp": ["whatsapp"],
    "saludo": ["hola", "buenos días", "qué tal", "buenas tardes", "buenas noches"],
    "salir": ["salir", "terminar", "cerrar programa", "cerrar orionia", "apagar"]
}

def extraer_entidad(frase):
    doc = nlp(frase.lower())
    for ent in doc.ents:
        return ent.text
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            return token.text
    return "desconocido"