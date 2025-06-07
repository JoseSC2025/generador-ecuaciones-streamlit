# 🧮 Generador de Ecuaciones de Primer Grado

Una aplicación web interactiva creada con Streamlit para practicar la resolución de ecuaciones de primer grado.

## ✨ Características

- **Generación aleatoria** de ecuaciones de primer grado
- **Dos tipos de ecuaciones**:
  - Simple: `ax + b = c`
  - Compleja: `ax + b = cx + d`
- **Verificación automática** de respuestas
- **Sistema de puntuación** y estadísticas
- **Explicaciones paso a paso** de las soluciones
- **Interfaz intuitiva** y responsive

## 🚀 Cómo usar

1. Haz clic en "Generar Nueva Ecuación"
2. Resuelve la ecuación mentalmente o en papel
3. Introduce tu respuesta en el campo de texto
4. Haz clic en "Verificar Respuesta" para comprobar si es correcta
5. Si necesitas ayuda, usa el botón "Ver Solución"

## 🛠️ Instalación local

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/generador-ecuaciones.git
cd generador-ecuaciones
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run app.py
```

4. Abre tu navegador en `http://localhost:8501`

## 🌐 Despliegue en Streamlit Cloud

1. Sube tu código a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio de GitHub
4. Selecciona el archivo `app.py`
5. ¡Tu aplicación estará disponible en línea!

## 📁 Estructura del proyecto

```
generador-ecuaciones/
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias
└── README.md          # Este archivo
```

## 🎯 Funcionalidades

### Tipos de ecuaciones
- **Ecuaciones simples**: Del tipo `3x + 5 = 17`
- **Ecuaciones complejas**: Del tipo `2x + 3 = 5x - 9`

### Sistema de puntuación
- Tracking de respuestas correctas e incorrectas
- Porcentaje de aciertos
- Estadísticas en tiempo real

### Ayuda educativa
- Explicaciones paso a paso
- Información sobre ecuaciones de primer grado
- Ejemplos ilustrativos

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la aplicación:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Creado con ❤️ usando Streamlit

---

¿Tienes alguna pregunta o sugerencia? ¡Abre un issue!