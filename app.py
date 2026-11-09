# ============================================================
# PLANIFICADOR DE EXPERIENCIAS CREATIVAS
# Aplicativo académico desarrollado con Python y Streamlit
# ============================================================
# Este programa calcula cuántos materiales faltan comprar
# y cuánto dinero se necesita desembolsar para realizar
# una experiencia creativa.
# ============================================================

import streamlit as st  # Importamos Streamlit para construir la interfaz web

# ------------------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# ------------------------------------------------------------
# set_page_config() debe ser la primera instrucción de Streamlit
st.set_page_config(
    page_title="Planificador de Experiencias Creativas",
    page_icon="🎨",
    layout="centered"
)

# ------------------------------------------------------------
# ESTILOS PERSONALIZADOS (CSS)
# Aplicamos fondo claro y detalles morados y verdes
# ------------------------------------------------------------
st.markdown("""
    <style>
        /* Fondo general de la aplicación */
        .stApp {
            background-color: #f8f6ff;
        }

        /* Título principal */
        h1 {
            color: #6a0dad;
            text-align: center;
        }

        /* Subtítulos (h2, h3) */
        h2, h3 {
            color: #5b2d8e;
        }

        /* Línea divisoria decorativa */
        hr {
            border: 1px solid #c9a0f5;
        }

        /* Botón principal */
        div.stButton > button {
            background-color: #6a0dad;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-size: 1em;
            border: none;
        }

        /* Botón al pasar el cursor */
        div.stButton > button:hover {
            background-color: #4b0082;
            color: white;
        }

        /* Etiquetas de los campos */
        label {
            color: #3d005e;
            font-weight: bold;
        }

        /* Cuadro de resultados */
        .resultado-box {
            background-color: #eaf5ea;
            border-left: 5px solid #2e7d32;
            padding: 1em;
            border-radius: 6px;
            margin-top: 1em;
        }

        /* Texto de aclaración */
        .aclaracion {
            color: #555;
            font-size: 0.9em;
            font-style: italic;
        }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# TÍTULO Y DESCRIPCIÓN
# ============================================================
st.title("🎨 Planificador de Experiencias Creativas")
st.markdown("---")
st.markdown(
    "Completa los datos de tu experiencia para conocer **qué materiales "
    "te faltan comprar** y **cuánto dinero necesitas desembolsar**."
)
st.markdown("---")

# ============================================================
# SECCIÓN 1: DATOS GENERALES
# ============================================================
st.subheader("📋 Datos generales")

# Campo de texto para el nombre de la experiencia
nombre_experiencia = st.text_input(
    "Nombre de la experiencia",
    placeholder="Ej.: Taller de velas aromáticas"
)

# Campo numérico para el número de asistentes
# min_value=1 evita que se ingrese cero o un número negativo
numero_asistentes = st.number_input(
    "Número de asistentes",
    min_value=1,          # Mínimo permitido: 1 persona
    max_value=10000,      # Máximo razonable
    value=1,              # Valor inicial
    step=1,               # Solo enteros (pasos de 1)
    help="Debe ser un número entero mayor que cero."
)

st.markdown("---")

# ============================================================
# SECCIÓN 2: TABLA DE MATERIALES (EDITABLE)
# ============================================================
st.subheader("🛒 Materiales")
st.markdown(
    "Agrega cada material que necesitas. "
    "Puedes usar el botón ➕ para añadir filas y 🗑️ para eliminarlas."
)

# Usamos st.session_state para recordar las filas entre interacciones.
# session_state es como la "memoria" de la aplicación mientras está abierta.
if "materiales" not in st.session_state:
    # Si todavía no existe la lista, la creamos con una fila vacía de ejemplo
    st.session_state.materiales = [
        {
            "nombre": "",
            "disponibles": 0,
            "por_participante": 1,
            "precio_unitario": 0
        }
    ]

# ---- Encabezados de la tabla ----
# Usamos columnas de Streamlit para simular las celdas de la tabla
col1, col2, col3, col4, col5 = st.columns([3, 1.5, 2, 2, 1])
col1.markdown("**Material**")
col2.markdown("**Disponibles**")
col3.markdown("**Und. por persona**")
col4.markdown("**Precio (COP)**")
col5.markdown("**Eliminar**")

# ---- Filas editables ----
# Usamos enumerate() para obtener el índice (i) y el valor (mat) de cada fila
for i, mat in enumerate(st.session_state.materiales):

    # Creamos 5 columnas: nombre, disponibles, por participante, precio, botón
    c1, c2, c3, c4, c5 = st.columns([3, 1.5, 2, 2, 1])

    # Columna 1: Nombre del material
    # key="..." hace que cada campo tenga un identificador único
    st.session_state.materiales[i]["nombre"] = c1.text_input(
        f"Material {i + 1}",
        value=mat["nombre"],
        key=f"nombre_{i}",
        label_visibility="collapsed"    # Ocultamos la etiqueta para que se vea como tabla
    )

    # Columna 2: Unidades disponibles (entero, mínimo 0)
    st.session_state.materiales[i]["disponibles"] = c2.number_input(
        "Disponibles",
        min_value=0,
        value=int(mat["disponibles"]),
        step=1,
        key=f"disponibles_{i}",
        label_visibility="collapsed"
    )

    # Columna 3: Unidades necesarias por participante (entero, mínimo 1)
    st.session_state.materiales[i]["por_participante"] = c3.number_input(
        "Por persona",
        min_value=1,
        value=int(mat["por_participante"]),
        step=1,
        key=f"por_participante_{i}",
        label_visibility="collapsed"
    )

    # Columna 4: Precio unitario en pesos colombianos (mínimo 0)
    st.session_state.materiales[i]["precio_unitario"] = c4.number_input(
        "Precio",
        min_value=0,
        value=int(mat["precio_unitario"]),
        step=100,
        key=f"precio_{i}",
        label_visibility="collapsed"
    )

    # Columna 5: Botón para eliminar esta fila
    if c5.button("🗑️", key=f"eliminar_{i}"):
        # Eliminamos la fila con el índice i de la lista
        st.session_state.materiales.pop(i)
        st.rerun()  # Recargamos la pantalla para reflejar el cambio

# ---- Botón para añadir una fila nueva ----
if st.button("➕ Agregar material"):
    # Añadimos una fila vacía al final de la lista
    st.session_state.materiales.append(
        {
            "nombre": "",
            "disponibles": 0,
            "por_participante": 1,
            "precio_unitario": 0
        }
    )
    st.rerun()

st.markdown("---")

# ============================================================
# SECCIÓN 3: OTROS COSTOS
# ============================================================
st.subheader("💰 Otros costos")

# Snack por persona (costo del refrigerio de cada asistente)
snack_por_persona = st.number_input(
    "Snack por persona (COP)",
    min_value=0,
    value=0,
    step=1000,
    help="Costo del refrigerio de cada asistente."
)

# Costo total del espacio o lugar donde se realiza la experiencia
costo_espacio = st.number_input(
    "Costo del espacio (COP)",
    min_value=0,
    value=0,
    step=5000,
    help="Valor del alquiler o reserva del lugar."
)

# Otros gastos varios que no encajan en las categorías anteriores
otros_gastos = st.number_input(
    "Otros gastos (COP)",
    min_value=0,
    value=0,
    step=1000,
    help="Cualquier otro gasto adicional."
)

st.markdown("---")

# ============================================================
# SECCIÓN 4: BOTÓN CALCULAR Y LÓGICA PRINCIPAL
# ============================================================
if st.button("🧮 Calcular presupuesto"):

    # ----------------------------------------------------------
    # PASO A: VALIDAR LAS FILAS DE MATERIALES
    # Usamos un while con índice para recorrer la lista
    # ----------------------------------------------------------

    # Lista donde guardaremos solo las filas válidas (con datos completos)
    materiales_validos = []

    # Lista donde guardaremos los errores encontrados
    errores = []

    # Índice para el ciclo while
    i = 0

    # El while recorre cada fila de materiales usando un índice manual
    while i < len(st.session_state.materiales):
        fila = st.session_state.materiales[i]

        # Leemos los valores de la fila actual
        nombre       = fila["nombre"].strip()           # .strip() elimina espacios al inicio y al final
        disponibles  = int(fila["disponibles"])
        por_persona  = int(fila["por_participante"])
        precio       = int(fila["precio_unitario"])

        # Determinamos si la fila está completamente vacía:
        # nombre vacío, disponibles = 0, por_persona = 1 (valor mínimo) y precio = 0
        fila_vacia = (nombre == "" and disponibles == 0 and por_persona == 1 and precio == 0)

        if fila_vacia:
            # Si la fila está vacía, la ignoramos y pasamos a la siguiente
            i = i + 1
            continue  # Saltamos al siguiente ciclo del while

        elif nombre == "":
            # La fila tiene datos numéricos pero le falta el nombre
            errores.append(f"• Fila {i + 1}: el nombre del material está vacío.")
            i = i + 1

        elif disponibles < 0:
            # La cantidad disponible no puede ser negativa
            errores.append(f"• Fila {i + 1} ({nombre}): las unidades disponibles no pueden ser negativas.")
            i = i + 1

        elif por_persona < 1:
            # Se necesita al menos 1 unidad por participante
            errores.append(f"• Fila {i + 1} ({nombre}): las unidades por participante deben ser al menos 1.")
            i = i + 1

        elif precio < 0:
            # El precio no puede ser negativo
            errores.append(f"• Fila {i + 1} ({nombre}): el precio no puede ser negativo.")
            i = i + 1

        else:
            # Si la fila es válida, la añadimos a la lista de materiales válidos
            materiales_validos.append(
                {
                    "nombre": nombre,
                    "disponibles": disponibles,
                    "por_participante": por_persona,
                    "precio_unitario": precio
                }
            )
            i = i + 1

    # ----------------------------------------------------------
    # PASO B: VERIFICAR QUE HAYA AL MENOS UN MATERIAL COMPLETO
    # ----------------------------------------------------------
    if len(materiales_validos) == 0 and len(errores) == 0:
        # No se ingresó ningún material
        errores.append("• Debes agregar al menos un material completo.")

    # ----------------------------------------------------------
    # PASO C: MOSTRAR ERRORES (SI LOS HAY) Y DETENER EL CÁLCULO
    # ----------------------------------------------------------
    if len(errores) > 0:
        st.error("⚠️ Corrige los siguientes problemas antes de calcular:")
        for mensaje in errores:
            st.markdown(mensaje)

    else:
        # ----------------------------------------------------------
        # PASO D: CALCULAR LOS RESULTADOS
        # Usamos un for para recorrer cada material válido
        # ----------------------------------------------------------

        # Lista donde guardaremos los resultados de cada material
        resultados_materiales = []

        # Acumulador para el total de compras de materiales
        total_compras_materiales = 0

        # El for recorre cada diccionario en la lista de materiales válidos
        for material in materiales_validos:

            # Cantidad total necesaria para todos los asistentes
            cantidad_necesaria = numero_asistentes * material["por_participante"]

            # Cantidad faltante (lo que hay que comprar)
            # Si hay más disponibles de los que se necesitan, el faltante es 0
            diferencia = cantidad_necesaria - material["disponibles"]

            if diferencia > 0:
                cantidad_faltante = diferencia   # Hacen falta unidades
            else:
                cantidad_faltante = 0            # No hacen falta unidades

            # Costo de compra de este material
            costo_compra = cantidad_faltante * material["precio_unitario"]

            # Sumamos al acumulador general
            total_compras_materiales = total_compras_materiales + costo_compra

            # Guardamos el resultado de este material como un diccionario
            resultados_materiales.append(
                {
                    "Material":             material["nombre"],
                    "Necesarias":           cantidad_necesaria,
                    "Disponibles":          material["disponibles"],
                    "Faltantes":            cantidad_faltante,
                    "Costo de compra (COP)": costo_compra
                }
            )

        # ----------------------------------------------------------
        # PASO E: CALCULAR SUBTOTALES Y TOTAL GENERAL
        # ----------------------------------------------------------

        # Total del snack para todos los asistentes
        total_snack = numero_asistentes * snack_por_persona

        # Desembolso total = materiales + snack + espacio + otros
        desembolso_total = (
            total_compras_materiales
            + total_snack
            + costo_espacio
            + otros_gastos
        )

        # Desembolso por participante
        desembolso_por_participante = desembolso_total / numero_asistentes

        # ----------------------------------------------------------
        # PASO F: MOSTRAR RESULTADOS EN PANTALLA
        # ----------------------------------------------------------
        st.markdown("---")
        st.subheader("📊 Resultados")

        # Aclaración sobre qué significa el cálculo
        st.markdown(
            '<p class="aclaracion">'
            "ℹ️ Se calcula el dinero que hace falta desembolsar, "
            "considerando únicamente las unidades que ya tienes disponibles. "
            "Si ya cuentas con suficientes existencias de un material, "
            "su costo de compra es $0."
            "</p>",
            unsafe_allow_html=True
        )

        # Mostramos el nombre de la experiencia si fue ingresado
        if nombre_experiencia.strip() != "":
            st.markdown(f"**Experiencia:** {nombre_experiencia.strip()}")

        st.markdown(f"**Asistentes:** {numero_asistentes}")
        st.markdown(" ")

        # ---- Tabla de materiales ----
        st.markdown("**Detalle por material:**")

        # Importamos pandas aquí para crear la tabla de resultados.
        # pandas es una librería que facilita trabajar con tablas de datos.
        import pandas as pd

        # Creamos un DataFrame (tabla) a partir de la lista de resultados
        df_resultados = pd.DataFrame(resultados_materiales)

        # Formateamos la columna de costo con símbolo de pesos
        df_resultados["Costo de compra (COP)"] = df_resultados["Costo de compra (COP)"].apply(
            lambda x: f"${x:,.0f}".replace(",", ".")
        )

        # Mostramos la tabla en la pantalla (sin índice de fila)
        st.dataframe(df_resultados, use_container_width=True, hide_index=True)

        # ---- Subtotales y total ----
        st.markdown(" ")
        st.markdown("**Resumen de costos:**")

        # Función auxiliar para formatear valores en pesos colombianos
        def formato_pesos(valor):
            """Convierte un número en cadena con formato de pesos colombianos."""
            # Formateamos con separador de miles (.) y dos decimales (,)
            entero = int(valor)
            decimal = round((valor - entero) * 100)
            if decimal == 0:
                return f"${entero:,}".replace(",", ".")
            else:
                return f"${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Mostramos cada subtotal en una caja de color verde
        st.markdown(
            f"""
            <div class="resultado-box">
                <p>🛒 <b>Compras de materiales:</b> {formato_pesos(total_compras_materiales)}</p>
                <p>🍎 <b>Total snack ({numero_asistentes} × {formato_pesos(snack_por_persona)}):</b> {formato_pesos(total_snack)}</p>
                <p>🏠 <b>Costo del espacio:</b> {formato_pesos(costo_espacio)}</p>
                <p>📦 <b>Otros gastos:</b> {formato_pesos(otros_gastos)}</p>
                <hr>
                <p style="font-size:1.1em;">💵 <b>Desembolso total:</b> {formato_pesos(desembolso_total)}</p>
                <p style="font-size:1.1em;">👤 <b>Desembolso por participante:</b> {formato_pesos(desembolso_por_participante)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# PIE DE PÁGINA
# ============================================================
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#9b59b6; font-size:0.85em;">'
    "Planificador de Experiencias Creativas · Hecho con 💜 en Python y Streamlit"
    "</p>",
    unsafe_allow_html=True
)
