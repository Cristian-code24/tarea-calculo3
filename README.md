# 📐 Modelado y Optimización Multivariable en Mercados Financieros

**Universidad Nacional José Faustino Sánchez Carrión (UNJFSC)**  
**Facultad de Ingeniería / Ciencias** • **Asignatura:** Cálculo III  

---

## 👥 Integrantes del Grupo
- **Inga Sialas, Carlos Alexis**
- **Quispe Lucas, Cristian David**

---

## 📌 Descripción del Proyecto
Aplicación web interactiva desarrollada en **Python** con **Streamlit**, **NumPy**, **Pandas** y **Plotly** para el análisis multivariable en $\mathbb{R}^3$ del mercado de valores, tomando como activo de estudio las acciones de **Apple Inc. (AAPL)** descargadas de Yahoo Finance.

El modelo ajusta una **superficie polinomial cuadrática $z = f(x, y)$** mediante Mínimos Cuadrados Ordinarios (OLS) con un coeficiente de determinación $R^2 \approx 99.4\%$.

### 🏷️ Definición de Variables:
- **Eje X (Variable Independiente 1):** $x = \text{Open}$ (Precio de Apertura en USD a las 9:30 AM).
- **Eje Y (Variable Independiente 2):** $y = \text{High}$ (Precio Máximo Diario en USD).
- **Eje Z (Variable Dependiente):** $z = \text{Close} = f(x, y)$ (Precio de Cierre oficial en USD a las 4:00 PM).

---

## 📑 Estructura de la Presentación (Modo Diapositivas)

1. **🖥️ Diapositiva 1: Variables & Derivadas**
   - Coordenadas formales en $\mathbb{R}^3$ y ecuación de la superficie $\mathcal{S}$.
   - Operadores diferenciales en KaTeX: Derivadas Parciales $\left(\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}\right)$, Derivada Direccional $D_{\hat{u}} z$ y Diferencial Total $dz$.

2. **🧭 Diapositiva 2: Gradiente & Curvas de Nivel**
   - Las 2 propiedades clave: Máxima pendiente $(\|\nabla f\|)$ y Ortogonalidad a curvas de nivel ($\angle 90^\circ$).
   - Gráfico 2D de isolíneas y campo vectorial interactivo con demostración geométrica en $P_0$.

3. **🔲 Diapositiva 3: Matriz Hessiana & Extremos**
   - Matriz $H$ de segundas derivadas y criterio del determinante $D = \det(H)$.
   - Clasificación de puntos críticos (Mínimo, Máximo, Punto Silla e Indeterminado) con superficies 3D comparativas.

4. **🎛️ Diapositiva 4: Simulador 3D en Vivo & Análisis Financiero**
   - Consola con selector de modo (Derivada Total vs. Derivada Parcial congelando un eje).
   - Sliders en tiempo real para $x$ (Open), $y$ (High) y $\theta$ (ángulo de la derivada direccional).
   - Superficie cuadrática 3D interactiva con nube de puntos reales, punto $P_0$, gradiente $\nabla f$ y vector direccional.
   - **Simulación Financiera y Gráficos de Torta (Antes vs. Después):** Desglose de Capital Invertido vs. Ganancia Neta y retorno de inversión ($ROI\%$).

5. **🎯 Diapositiva 5: Conclusiones & Métricas**
   - Síntesis analítica de las 4 conclusiones del proyecto.
   - Ficha técnica completa con coeficientes, derivadas promedio y métricas de ajuste.

---

## 🚀 Instalación y Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Cristian-code24/tarea-calculo3.git
   cd tarea-calculo3
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Iniciar la aplicación:**
   ```bash
   streamlit run app.py
   ```
   Abre tu navegador en `http://localhost:8501`.

---

## ☁️ Despliegue en Streamlit Community Cloud
1. Ve a [share.streamlit.io](https://share.streamlit.io/) e inicia sesión con tu cuenta de GitHub (`Cristian-code24`).
2. Haz clic en **"New app"**.
3. Selecciona el repositorio: `Cristian-code24/tarea-calculo3`.
4. Rama: `main`.
5. Archivo principal: `app.py`.
6. Haz clic en **"Deploy!"**.
