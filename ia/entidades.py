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
    frase = frase.lower()
    for entidad, palabras in palabras_clave.items():
        if any(palabra in frase for palabra in palabras):
            return entidad
    return "desconocido"