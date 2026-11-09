# 🎨 Planificador de Experiencias Creativas

Aplicativo académico desarrollado con **Python** y **Streamlit** para calcular los materiales que faltan comprar y el dinero que se necesita desembolsar para realizar una experiencia creativa.

---

## 📋 ¿Qué hace esta aplicación?

1. Recibe el nombre de la experiencia y el número de asistentes.
2. Permite registrar materiales con sus unidades disponibles, unidades por participante y precio unitario.
3. Calcula automáticamente cuántas unidades faltan y cuánto cuestan.
4. Suma snack, espacio y otros gastos para obtener el **desembolso total** y el **desembolso por participante**.

---

## 🖥️ Requisitos previos

Necesitas tener instalado en tu computador:

- **Python 3.9 o superior** → [Descargar aquí](https://www.python.org/downloads/)
- **pip** (viene incluido con Python)

Para verificar que ya los tienes, abre una terminal y escribe:

```
python --version
pip --version
```

---

## 🚀 Instalación paso a paso

### 1. Abre una terminal en la carpeta del proyecto

En Windows, puedes hacer clic derecho dentro de la carpeta y elegir **"Abrir en Terminal"** o **"Abrir ventana de PowerShell aquí"**.

### 2. Instala las dependencias

Escribe el siguiente comando y presiona **Enter**:

```
pip install -r requirements.txt
```

Este comando instala Streamlit y pandas, que son las librerías que usa la aplicación.

### 3. Ejecuta la aplicación

Escribe el siguiente comando y presiona **Enter**:

```
streamlit run app.py
```

Después de unos segundos, se abrirá automáticamente tu navegador con la aplicación. Si no se abre, copia la dirección que aparece en la terminal (algo como `http://localhost:8501`) y pégala en tu navegador.

---

## 🛑 Cómo cerrar la aplicación

Ve a la terminal donde está corriendo la aplicación y presiona **Ctrl + C**.

---

## 🧪 Prueba de referencia

Puedes verificar que la aplicación funciona correctamente con estos datos:

| Campo                  | Valor        |
|------------------------|--------------|
| Asistentes             | 18           |
| Material               | Velas        |
| Unidades disponibles   | 20           |
| Unidades por persona   | 7            |
| Precio unitario        | \$700        |
| Snack por persona      | \$22.000     |
| Costo del espacio      | \$80.000     |
| Otros gastos           | \$0          |

**Resultado esperado:**

| Concepto                    | Valor        |
|-----------------------------|--------------|
| Velas necesarias            | 126          |
| Velas faltantes             | 106          |
| Compra de velas             | \$74.200     |
| Total snack                 | \$396.000    |
| **Desembolso total**        | **\$550.200**|
| **Desembolso por persona**  | **\$30.566,67** |

---

## 📁 Archivos del proyecto

```
planificador_experiencias/
│
├── app.py            ← Código principal de la aplicación
├── requirements.txt  ← Lista de librerías necesarias
└── README.md         ← Este archivo de instrucciones
```

---

## 💡 Notas importantes

- Todos los precios están en **pesos colombianos (COP)**.
- Las cantidades de materiales deben ser **números enteros** (sin decimales).
- El número de asistentes debe ser **mayor que cero**.
- Si ya tienes suficientes unidades de un material, el costo de compra es **\$0**.
