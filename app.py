import streamlit as st
import random
import math

# Configuración de la página
st.set_page_config(
    page_title="Generador de Ecuaciones de Primer Grado",
    page_icon="🧮",
    layout="wide"
)

# Título principal
st.title("🧮 Generador de Ecuaciones de Primer Grado")
st.markdown("---")

# Función para generar ecuación aleatoria
def generar_ecuacion():
    """Genera una ecuación de primer grado aleatoria del tipo ax + b = c"""
    # Coeficientes aleatorios
    a = random.randint(1, 20)  # Coeficiente de x
    b = random.randint(-50, 50)  # Término independiente lado izquierdo
    c = random.randint(-50, 50)  # Término independiente lado derecho
    
    # Calculamos la solución: x = (c - b) / a
    solucion = (c - b) / a
    
    # Formateamos la ecuación para mostrar
    if b >= 0:
        ecuacion_str = f"{a}x + {b} = {c}"
    else:
        ecuacion_str = f"{a}x - {abs(b)} = {c}"
    
    return ecuacion_str, solucion, a, b, c

# Función para generar ecuación más compleja (opcional)
def generar_ecuacion_compleja():
    """Genera ecuaciones más complejas del tipo ax + b = cx + d"""
    a = random.randint(1, 15)
    b = random.randint(-30, 30)
    c = random.randint(1, 15)
    d = random.randint(-30, 30)
    
    # Aseguramos que a ≠ c para que tenga solución única
    if a == c:
        c += random.choice([-1, 1])
    
    # Solución: x = (d - b) / (a - c)
    solucion = (d - b) / (a - c)
    
    # Formatear ecuación
    def formato_termino(coef, var="", es_primero=False):
        if coef == 0:
            return ""
        elif coef == 1 and var:
            return var if es_primero else f" + {var}"
        elif coef == -1 and var:
            return f"-{var}" if es_primero else f" - {var}"
        elif coef > 0 and not es_primero:
            return f" + {coef}{var}"
        else:
            return f"{coef}{var}"
    
    lado_izq = formato_termino(a, "x", True) + formato_termino(b)
    lado_der = formato_termino(c, "x", True) + formato_termino(d)
    
    ecuacion_str = f"{lado_izq} = {lado_der}"
    
    return ecuacion_str, solucion

# Inicializar estado de la sesión
if 'ecuacion_actual' not in st.session_state:
    st.session_state.ecuacion_actual = None
    st.session_state.solucion_actual = None
    st.session_state.respuesta_mostrada = False
    st.session_state.puntuacion = 0
    st.session_state.intentos = 0

# Sidebar para configuraciones
st.sidebar.header("⚙️ Configuraciones")
tipo_ecuacion = st.sidebar.selectbox(
    "Tipo de ecuación:",
    ["Simple (ax + b = c)", "Compleja (ax + b = cx + d)"]
)

nivel_dificultad = st.sidebar.selectbox(
    "Nivel de dificultad:",
    ["Fácil", "Medio", "Difícil"]
)

# Mostrar estadísticas
st.sidebar.markdown("---")
st.sidebar.header("📊 Estadísticas")
if st.session_state.intentos > 0:
    porcentaje = (st.session_state.puntuacion / st.session_state.intentos) * 100
    st.sidebar.metric("Puntuación", f"{st.session_state.puntuacion}/{st.session_state.intentos}")
    st.sidebar.metric("Porcentaje de aciertos", f"{porcentaje:.1f}%")
else:
    st.sidebar.info("¡Resuelve algunas ecuaciones para ver tus estadísticas!")

# Botón para generar nueva ecuación
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🎲 Generar Nueva Ecuación", type="primary", use_container_width=True):
        if tipo_ecuacion == "Simple (ax + b = c)":
            ecuacion, solucion = generar_ecuacion()[:2]
        else:
            ecuacion, solucion = generar_ecuacion_compleja()
        
        st.session_state.ecuacion_actual = ecuacion
        st.session_state.solucion_actual = solucion
        st.session_state.respuesta_mostrada = False

# Mostrar ecuación actual
if st.session_state.ecuacion_actual:
    st.markdown("## 📝 Ecuación a resolver:")
    
    # Mostrar la ecuación en una caja destacada
    st.markdown(f"""
    <div style="
        background-color: #1e1e1e;
        color: #ffffff;
        border: 2px solid #1f77b4;
        padding: 20px;
        margin: 20px 0;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    ">
        {st.session_state.ecuacion_actual}
    </div>
    """, unsafe_allow_html=True)
    
    # Input para la respuesta del usuario
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        respuesta_usuario = st.number_input(
            "Introduce el valor de x:",
            value=0.0,
            step=0.1,
            format="%.2f",
            key="respuesta_input"
        )
        
        # Botones de acción
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("✅ Verificar Respuesta", use_container_width=True):
                st.session_state.intentos += 1
                tolerancia = 0.01  # Tolerancia para números decimales
                
                if abs(respuesta_usuario - st.session_state.solucion_actual) < tolerancia:
                    st.session_state.puntuacion += 1
                    st.success(f"🎉 ¡Correcto! La respuesta es x = {st.session_state.solucion_actual:.2f}")
                else:
                    st.error(f"❌ Incorrecto. La respuesta correcta es x = {st.session_state.solucion_actual:.2f}")
                
                st.session_state.respuesta_mostrada = True
        
        with col_btn2:
            if st.button("💡 Ver Solución", use_container_width=True):
                st.session_state.respuesta_mostrada = True
                st.info(f"💡 La solución es: x = {st.session_state.solucion_actual:.2f}")
    
    # Mostrar explicación de la solución si se ha mostrado la respuesta
    if st.session_state.respuesta_mostrada:
        with st.expander("📚 Ver explicación paso a paso"):
            st.markdown("### Pasos para resolver la ecuación:")
            if tipo_ecuacion == "Simple (ax + b = c)":
                st.markdown(f"""
                **Ecuación:** {st.session_state.ecuacion_actual}
                
                **Paso 1:** Aislar el término con x
                - Mover el término independiente al lado derecho
                
                **Paso 2:** Despejar x
                - Dividir ambos lados por el coeficiente de x
                
                **Resultado:** x = {st.session_state.solucion_actual:.2f}
                """)
            else:
                st.markdown(f"""
                **Ecuación:** {st.session_state.ecuacion_actual}
                
                **Paso 1:** Mover todos los términos con x a un lado
                
                **Paso 2:** Mover todos los términos independientes al otro lado
                
                **Paso 3:** Factorizar x y despejar
                
                **Resultado:** x = {st.session_state.solucion_actual:.2f}
                """)

else:
    st.info("👆 Haz clic en 'Generar Nueva Ecuación' para comenzar")

# Información adicional
st.markdown("---")
with st.expander("ℹ️ Información sobre ecuaciones de primer grado"):
    st.markdown("""
    ### ¿Qué son las ecuaciones de primer grado?
    
    Las ecuaciones de primer grado son expresiones algebraicas donde la variable (x) tiene exponente 1.
    
    **Formas comunes:**
    - **Simple:** ax + b = c
    - **Compleja:** ax + b = cx + d
    
    **Pasos generales para resolver:**
    1. Simplificar ambos lados si es necesario
    2. Mover todos los términos con x a un lado
    3. Mover todos los números al otro lado
    4. Despejar x dividiendo por su coeficiente
    
    **Ejemplo:**
    - 3x + 5 = 14
    - 3x = 14 - 5
    - 3x = 9
    - x = 3
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 14px;'>"
    "💡 Generador de Ecuaciones de Primer Grado | Creado con Streamlit"
    "</div>", 
    unsafe_allow_html=True
)