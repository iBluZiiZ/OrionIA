# 🧠 Roadmap de Desarrollo – OrionIA

OrionIA es un asistente virtual inspirado en JARVIS, diseñado para evolucionar paso a paso desde un sistema básico hasta una inteligencia artificial personal avanzada. Este documento resume los niveles de desarrollo planificados y alcanzados.

---

## 🔹 Nivel 1 – OrionIA Básico ✅

> Estado: **COMPLETADO**

- Entrada de voz (speech_recognition)
- Salida de voz (pyttsx3)
- Clasificación de intención (saludo, orden, pregunta)
- Detección de entidad por palabras clave
- Acciones simples (abrir navegador, decir hora, salir)
- Proyecto modular: `main.py`, `ia/`, `modelos/`, `datos/`
- Dataset `.csv` editable para entrenamiento
- Versionado en GitHub

---

## 🔸 Nivel 2 – OrionIA Interactiva 🟡

> Estado: **EN DESARROLLO**

- Confirmación de acciones críticas (ej: salir)
- Historial simple de interacción
- Generación de respuestas dinámicas por intención
- Dataset ampliado con sinónimos y frases reales
- Reconocimiento de frases similares o parafraseadas

---

## 🔸 Nivel 3 – OrionIA Semántica (NLP) 🔜

> Objetivo: Comprensión real del lenguaje

- Integrar `spaCy` o `transformers` para análisis semántico
- Detección automática de entidades sin palabras clave
- Comprensión de frases fuera del dataset

---

## 🔸 Nivel 4 – OrionIA Sensorial (Emocional) 🔜

> Objetivo: Detectar emociones y tono en la voz

- Clasificación de emociones (feliz, triste, molesto, etc.)
- Respuestas empáticas o adaptativas
- Reconocimiento facial (opcional, con cámara)
- Control de volumen/velocidad de voz según emoción

---

## 🔸 Nivel 5 – OrionIA Multimodal 🔜

> Objetivo: Integración con entorno físico y visual

- Control de luces, sensores o dispositivos reales (Raspberry Pi / Arduino)
- Dashboard visual o interfaz gráfica
- Recordatorios, alarmas, calendario personal
- Integración con servicios: clima, correo, agenda

---

## 🔸 Nivel 6 – OrionIA Aprendizaje Continuo 🔜

> Objetivo: Una IA que evoluciona contigo

- Aprender nuevas frases a partir del uso
- Reentrenamiento incremental con feedback del usuario
- Personalización progresiva
- Memoria de hábitos, gustos y rutina

---

## 🏁 Futuro

- Reconocimiento de voz de usuario
- Voz personalizada (con ElevenLabs, TTS neural)
- API ChatGPT opcional (controlado por modo)
- App móvil o cliente visual conectado

---

✍️ Desarrollado por [@iBluZiiZ](https://github.com/iBluZiiZ/)

