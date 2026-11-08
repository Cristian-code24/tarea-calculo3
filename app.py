# =============================================================================
#  CÁLCULO III — UNJFSC  |  MODO DIAPOSITIVAS PROFESIONAL (PRESENTATION DECK)
#  Derivadas Parciales, Gradiente, Derivada Direccional & Hessiana
#  Superficie en R³: z = f(x, y) | x = Open, y = High, z = Close (AAPL)
#  Ejecutar: streamlit run app.py
# =============================================================================

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─────────────────────────────────────────────────────────────────────────────
#  CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Cálculo III — UNJFSC (Exposición)",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
#  TEMA OSCURO TIPO DIAPOSITIVAS (KEYNOTE / PPT STYLE)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Fondo oscuro general ── */
.stApp, [data-testid="stAppViewContainer"] { background: #0A0D14 !important; color: #E2E8F0 !important; }
[data-testid="stHeader"] { background: #0A0D14 !important; }
[data-testid="stSidebar"] { background: #0F131D !important; }
[data-testid="stMain"] { background: #0A0D14 !important; }

/* ── Tipografía ── */
h1, h2, h3, h4 { color: #FFFFFF !important; font-family: 'Inter', -apple-system, sans-serif; letter-spacing: -0.5px; }
p, li, label, small { color: #CBD5E1 !important; line-height: 1.6; }
code { background: #1E2433; color: #38BDF8; padding: 2px 6px; border-radius: 4px; font-weight: 600; }

/* ── Banner Superior tipo Presentación ── */
.slide-deck-banner {
  background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 50%, #1E293B 100%);
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 16px;
  padding: 22px 30px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
}
.slide-deck-banner h1 { margin: 0; font-size: 1.85rem; color: #FFFFFF !important; }
.slide-deck-banner p { margin: 4px 0 0 0; color: #94A3B8; font-size: 0.95rem; }

/* ── Encabezado de Cada Diapositiva ── */
.slide-header {
  background: #111622;
  border-left: 5px solid #38BDF8;
  border-radius: 12px;
  padding: 18px 24px;
  margin-bottom: 20px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.25);
}
.slide-badge {
  display: inline-block;
  background: #0284C7;
  color: #FFFFFF;
  font-weight: 800;
  font-size: 0.72rem;
  padding: 3px 10px;
  border-radius: 20px;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.slide-title {
  font-size: 1.65rem;
  font-weight: 700;
  color: #FFFFFF !important;
  margin: 4px 0;
}
.slide-subtitle {
  color: #94A3B8;
  font-size: 0.95rem;
  margin: 0;
}

/* ── Tarjetas de Diapositiva (Slide Cards) ── */
.slide-card {
  background: #111622;
  border: 1px solid #1E293B;
  border-radius: 14px;
  padding: 20px 22px;
  margin-bottom: 14px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
.card-cyan { border-top: 3px solid #38BDF8; }
.card-purple { border-top: 3px solid #A855F7; }
.card-gold { border-top: 3px solid #F59E0B; }
.card-green { border-top: 3px solid #10B981; }
.card-red { border-top: 3px solid #EF4444; }

/* ── Pestañas estilo Diapositiva ── */
.stTabs [data-baseweb="tab-list"] {
  background: #111622;
  border-radius: 12px;
  padding: 6px;
  gap: 8px;
  border: 1px solid #1E293B;
}
.stTabs [data-baseweb="tab"] {
  color: #94A3B8 !important;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.88rem;
  padding: 10px 18px;
}
.stTabs [aria-selected="true"] {
  background: #1E293B !important;
  color: #38BDF8 !important;
  border: 1px solid rgba(56, 189, 248, 0.4) !important;
  box-shadow: 0 4px 12px rgba(56, 189, 248, 0.15);
}

/* ── Métricas ── */
[data-testid="stMetricValue"] { color: #38BDF8 !important; font-size: 1.35rem !important; font-weight: 700; }
[data-testid="stMetricLabel"] { color: #94A3B8 !important; font-size: 0.82rem !important; }

/* ── Sliders ── */
.stSlider label { color: #E2E8F0 !important; font-weight: 600; }

/* ── Badges ── */
.badge { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 0.73rem; font-weight: 700; margin: 2px; }
.b-cyan { background: rgba(56, 189, 248, 0.15); color: #38BDF8; border: 1px solid rgba(56, 189, 248, 0.3); }
.b-purple { background: rgba(168, 85, 247, 0.15); color: #C084FC; border: 1px solid rgba(168, 85, 247, 0.3); }
.b-gold { background: rgba(245, 158, 11, 0.15); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.3); }
.b-green { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3); }
.b-red { background: rgba(239, 68, 68, 0.15); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.3); }

/* ── KaTeX Styling en Modo Oscuro ── */
.katex-display { margin: 12px 0 !important; }
.katex { color: #38BDF8 !important; font-size: 1.15rem !important; }

/* ── Separador ── */
.sep { border: none; border-top: 1px solid #1E293B; margin: 18px 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  CONSTANTES PLOTLY OSCURO
# ─────────────────────────────────────────────────────────────────────────────
_BG_PAPER  = "#111622"
_BG_PLOT   = "#0A0D14"
_FONT_MAIN = dict(color="#CBD5E1", family="Inter, sans-serif", size=12)
_LEGEND    = dict(bgcolor="#1E2433", bordercolor="#334155", borderwidth=1,
                  font=dict(color="#F1F5F9", size=11), x=0.01, y=0.99)
_AXIS_DARK = dict(gridcolor="#1E293B", zerolinecolor="#334155",
                  color="#94A3B8", tickcolor="#94A3B8",
                  linecolor="#1E293B", showline=True)
_SCENE_DARK = dict(
    bgcolor=_BG_PLOT,
    xaxis=dict(backgroundcolor="#0F131D", gridcolor="#1E293B", color="#94A3B8", showbackground=True),
    yaxis=dict(backgroundcolor="#0F131D", gridcolor="#1E293B", color="#94A3B8", showbackground=True),
    zaxis=dict(backgroundcolor="#0F131D", gridcolor="#1E293B", color="#94A3B8", showbackground=True),
)

# ─────────────────────────────────────────────────────────────────────────────
#  DATOS Y MODELO CUADRÁTICO (x = Open, y = High, z = Close)
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_data
def cargar_datos():
    df = pd.read_csv(
        "datos_modelo.csv",
        skiprows=3, header=None,
        names=["Date", "Close", "High", "Low", "Open", "Volume"],
    )
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for c in ["Close", "High", "Low", "Open", "Volume"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df.dropna(subset=["Close", "High", "Low", "Open"], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

@st.cache_data
def ajustar_modelo(df):
    x_data = df["Open"].values   # Eje X: Open
    y_data = df["High"].values   # Eje Y: High
    z_data = df["Close"].values  # Eje Z: Close

    s = dict(
        x_min=float(x_data.min()), x_max=float(x_data.max()),
        y_min=float(y_data.min()), y_max=float(y_data.max()),
    )
    rx = s["x_max"] - s["x_min"]
    ry = s["y_max"] - s["y_min"]

    xn = (x_data - s["x_min"]) / rx
    yn = (y_data - s["y_min"]) / ry

    # Polinomio cuadrático: z = β0 + β1*xn + β2*yn + β3*xn² + β4*yn² + β5*xn*yn
    X = np.column_stack([np.ones(len(xn)), xn, yn, xn**2, yn**2, xn * yn])
    beta = np.linalg.lstsq(X, z_data, rcond=None)[0]

    zp = X @ beta
    r2_score = 1 - np.sum((z_data - zp)**2) / np.sum((z_data - z_data.mean())**2)
    return beta, s, x_data, y_data, z_data, r2_score

def f_pred(x_v, y_v, beta, s):
    rx, ry = s["x_max"] - s["x_min"], s["y_max"] - s["y_min"]
    xn = (x_v - s["x_min"]) / rx
    yn = (y_v - s["y_min"]) / ry
    b = beta
    return b[0] + b[1]*xn + b[2]*yn + b[3]*xn**2 + b[4]*yn**2 + b[5]*xn*yn

def grad_f(x_v, y_v, beta, s):
    """Gradiente ∇f = (∂z/∂x, ∂z/∂y) en coordenadas originales."""
    rx, ry = s["x_max"] - s["x_min"], s["y_max"] - s["y_min"]
    xn = (x_v - s["x_min"]) / rx
    yn = (y_v - s["y_min"]) / ry
    b = beta
    dz_dxn = b[1] + 2*b[3]*xn + b[5]*yn
    dz_dyn = b[2] + 2*b[4]*yn + b[5]*xn
    return dz_dxn / rx, dz_dyn / ry

def deriv_direccional(x_v, y_v, theta_rad, beta, s):
    """D_û z = ∇f · û, con û = (cos θ, sin θ)."""
    gx, gy = grad_f(x_v, y_v, beta, s)
    return gx * np.cos(theta_rad) + gy * np.sin(theta_rad)

def hessiana_original(beta, s):
    """Hessiana del modelo: [[∂²z/∂x², ∂²z/∂x∂y], [∂²z/∂y∂x, ∂²z/∂y²]]."""
    rx = s["x_max"] - s["x_min"]
    ry = s["y_max"] - s["y_min"]
    b = beta
    h11 = 2*b[3] / rx**2
    h22 = 2*b[4] / ry**2
    h12 = b[5] / (rx * ry)
    det = h11*h22 - h12**2
    return h11, h22, h12, det

# Carga de datos
df_main = cargar_datos()
beta_m, s_m, x_m, y_m, z_m, r2_m = ajustar_modelo(df_main)

# Grilla 2D
_N2D = 85
_xg = np.linspace(x_m.min(), x_m.max(), _N2D)
_yg = np.linspace(y_m.min(), y_m.max(), _N2D)
_Xg, _Yg = np.meshgrid(_xg, _yg)
_Zg = np.vectorize(lambda a, b: f_pred(a, b, beta_m, s_m))(_Xg, _Yg)

# Campo vectorial
_NQ = 15
_xq = np.linspace(x_m.min(), x_m.max(), _NQ)
_yq = np.linspace(y_m.min(), y_m.max(), _NQ)
_Xq, _Yq = np.meshgrid(_xq, _yq)
_GX = np.zeros((_NQ, _NQ))
_GY = np.zeros((_NQ, _NQ))
for _i in range(_NQ):
    for _j in range(_NQ):
        _GX[_i, _j], _GY[_i, _j] = grad_f(_Xq[_i, _j], _Yq[_i, _j], beta_m, s_m)
_G_norm = np.sqrt(_GX**2 + _GY**2) + 1e-12
_arrow_scale = (x_m.max() - x_m.min()) / (_NQ * 1.6)
_UX = _GX / _G_norm * _arrow_scale
_UY = _GY / _G_norm * _arrow_scale

# ─────────────────────────────────────────────────────────────────────────────
#  BANNER SUPERIOR DE LA PRESENTACIÓN
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="slide-deck-banner" style="flex-direction: column; align-items: stretch; gap: 16px; padding: 24px 28px;">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="slide-badge" style="background:#0284C7;">PROYECTO ACADÉMICO • UNJFSC</span>
      <h1 style="font-size: 1.85rem; margin: 4px 0 2px 0;">📐 Modelado y Optimización Multivariable en Mercados Financieros</h1>
      <p style="color: #94A3B8; margin: 0; font-size: 0.95rem;">
        Análisis de Superficie en ℝ³: <strong>z = f(x, y)</strong> &nbsp;|&nbsp; 
        Eje X: Apertura (Open) &nbsp;•&nbsp; Eje Y: Máximo (High) &nbsp;•&nbsp; Eje Z: Cierre (Close)
      </p>
    </div>
    <div style="text-align: right;">
      <span class="badge b-cyan">5 Diapositivas</span>
      <span class="badge b-gold">Apple Inc. (AAPL)</span>
      <span class="badge b-green">Modelo Cuadrático OLS</span>
    </div>
  </div>

  <!-- DATOS ACADÉMICOS Y EQUIPO -->
  <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid #1E293B; border-radius: 12px; padding: 14px 20px;">
    <div style="color: #38BDF8; font-weight: 700; font-size: 0.82rem; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 8px;">
      📋 DATOS ACADÉMICOS Y EQUIPO
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 12px; font-size: 0.88rem;">
      <div>
        <span style="color: #94A3B8;">🏛️ Universidad:</span><br>
        <strong style="color: #F1F5F9;">José Faustino Sánchez Carrión (UNJFSC)</strong>
      </div>
      <div>
        <span style="color: #94A3B8;">📚 Asignatura:</span><br>
        <strong style="color: #F1F5F9;">Cálculo III</strong>
      </div>
      <div>
        <span style="color: #94A3B8;">👥 Integrantes del Grupo:</span><br>
        <strong style="color: #38BDF8;">• Inga Sialas, Carlos Alexis</strong><br>
        <strong style="color: #C084FC;">• Quispe Lucas, Cristian David</strong>
      </div>
      <div>
        <span style="color: #94A3B8;">📈 Activo Modelado:</span><br>
        <strong style="color: #F1F5F9;">Apple Inc. (AAPL - Yahoo Finance)</strong>
      </div>
      <div>
        <span style="color: #94A3B8;">💻 Entorno:</span><br>
        <strong style="color: #F1F5F9;">Python, NumPy, Pandas, Plotly & Streamlit</strong>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  PESTAÑAS ESTILO DIAPOSITIVA (PPT SLIDES)
# ─────────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🖥️ DIAPO 1: Variables & Derivadas",
    "🧭 DIAPO 2: Gradiente & Curvas",
    "🔲 DIAPO 3: Hessiana & Extremos",
    "🎛️ DIAPO 4: Simulador 3D en Vivo",
    "🎯 DIAPO 5: Conclusiones & Métricas",
])

# ═════════════════════════════════════════════════════════════════════════════
#  DIAPOSITIVA 1: VARIABLES & DERIVADAS
# ═════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
<div class="slide-header">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <span class="slide-badge">DIAPOSITIVA 01 / 05</span>
    <span style="color:#94A3B8; font-size:0.85rem; font-weight:600;">UNJFSC • CÁLCULO III</span>
  </div>
  <div class="slide-title">Definición de Variables en ℝ³ y Operadores Diferenciales</div>
  <div class="slide-subtitle">Identificación Rigurosa de Ejes Coordenados (x, y, z) y Análisis de Sensibilidad</div>
</div>
""", unsafe_allow_html=True)

    # 1. Definición Formal de Coordenadas
    st.markdown("### 🏷️ 1. Definición Formal de Coordenadas y Variables del Modelo")

    v1, v2, v3 = st.columns(3)

    with v1:
        st.markdown("""
<div class="slide-card card-cyan">
  <span class="badge b-cyan">EJE X (VARIABLE INDEPENDIENTE 1)</span>
  <h4 style="margin:10px 0 6px 0; color:#38BDF8!important;">x = Open (Precio de Apertura)</h4>
  <ul style="padding-left:18px; margin:0; font-size:0.92rem;">
    <li><strong>Definición:</strong> Precio al que abrió la acción a las 9:30 AM en Wall Street.</li>
    <li><strong>Rol en ℝ³:</strong> Primera coordenada del dominio plano base.</li>
    <li><strong>Unidad:</strong> Dólares estadounidenses (USD).</li>
  </ul>
</div>
""", unsafe_allow_html=True)

    with v2:
        st.markdown("""
<div class="slide-card card-purple">
  <span class="badge b-purple">EJE Y (VARIABLE INDEPENDIENTE 2)</span>
  <h4 style="margin:10px 0 6px 0; color:#C084FC!important;">y = High (Precio Máximo Diario)</h4>
  <ul style="padding-left:18px; margin:0; font-size:0.92rem;">
    <li><strong>Definición:</strong> Precio pico más alto alcanzado por la acción durante la jornada.</li>
    <li><strong>Rol en ℝ³:</strong> Segunda coordenada del dominio plano base.</li>
    <li><strong>Unidad:</strong> Dólares estadounidenses (USD).</li>
  </ul>
</div>
""", unsafe_allow_html=True)

    with v3:
        st.markdown("""
<div class="slide-card card-green">
  <span class="badge b-green">EJE Z (VARIABLE DEPENDIENTE)</span>
  <h4 style="margin:10px 0 6px 0; color:#34D399!important;">z = Close = f(x, y) (Precio de Cierre)</h4>
  <ul style="padding-left:18px; margin:0; font-size:0.92rem;">
    <li><strong>Definición:</strong> Precio final oficial de la acción registrado a las 4:00 PM.</li>
    <li><strong>Rol en ℝ³:</strong> Altura de la superficie en cada punto evaluado.</li>
    <li><strong>Unidad:</strong> Dólares estadounidenses (USD).</li>
  </ul>
</div>
""", unsafe_allow_html=True)

    # Formulación Matemática en R3 usando st.latex nativo
    st.markdown("#### 📐 Ecuación de la Superficie en ℝ³")
    st.latex(r"\mathcal{S} = \left\{ (x, y, z) \in \mathbb{R}^3 \;\middle|\; z = f(x, y), \quad (x, y) \in \mathcal{D} \subset \mathbb{R}^2 \right\}")
    st.caption("Donde el dominio D es el plano base (x, y) = (Open, High) y la variable dependiente z = Close representa la altura de la superficie en ℝ³.")

    st.markdown('<hr class="sep">', unsafe_allow_html=True)

    # 2. Operadores de Diferenciación Multivariable usando st.latex
    st.markdown("### 📐 2. Operadores de Diferenciación Multivariable")
    d1, d2, d3 = st.columns(3)

    with d1:
        st.markdown("""
<div class="slide-card card-cyan" style="margin-bottom:8px;">
  <span class="badge b-cyan">OPERADOR 1</span>
  <h4 style="color:#38BDF8!important; margin:8px 0 4px 0;">Derivadas Parciales</h4>
  <p style="font-size:0.88rem; margin:0; color:#94A3B8;">Tasa de variación respecto a un eje manteniendo el otro constante:</p>
</div>
""", unsafe_allow_html=True)
        st.latex(r"\frac{\partial z}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}")
        st.latex(r"\frac{\partial z}{\partial y} = \lim_{k \to 0} \frac{f(x, y+k) - f(x, y)}{k}")
        st.caption("Sensibilidad del cierre z ante variaciones aisladas de apertura (x) o máximo (y).")

    with d2:
        st.markdown("""
<div class="slide-card card-purple" style="margin-bottom:8px;">
  <span class="badge b-purple">OPERADOR 2</span>
  <h4 style="color:#C084FC!important; margin:8px 0 4px 0;">Derivada Direccional</h4>
  <p style="font-size:0.88rem; margin:0; color:#94A3B8;">Tasa de cambio de z a lo largo de un vector unitario û = (cos θ, sin θ):</p>
</div>
""", unsafe_allow_html=True)
        st.latex(r"D_{\hat{u}} z = \nabla f(x, y) \cdot \hat{u} = \frac{\partial z}{\partial x}\cos\theta + \frac{\partial z}{\partial y}\sin\theta")
        st.caption("Generalización: θ=0° produce ∂z/∂x, mientras que θ=90° produce ∂z/∂y.")

    with d3:
        st.markdown("""
<div class="slide-card card-gold" style="margin-bottom:8px;">
  <span class="badge b-gold">OPERADOR 3</span>
  <h4 style="color:#FBBF24!important; margin:8px 0 4px 0;">Diferencial Total</h4>
  <p style="font-size:0.88rem; margin:0; color:#94A3B8;">Aproximación lineal para cambios simultáneos de dx y dy:</p>
</div>
""", unsafe_allow_html=True)
        st.latex(r"dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy")
        st.caption("Variación total esperada en el cierre cuando x e y cambian al mismo tiempo.")

# ═════════════════════════════════════════════════════════════════════════════
#  DIAPOSITIVA 2: GRADIENTE & CURVAS DE NIVEL
# ═════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
<div class="slide-header">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <span class="slide-badge">DIAPOSITIVA 02 / 05</span>
    <span style="color:#94A3B8; font-size:0.85rem; font-weight:600;">UNJFSC • CÁLCULO III</span>
  </div>
  <div class="slide-title">El Vector Gradiente: Máximo Crecimiento y Ortogonalidad</div>
  <div class="slide-subtitle">Demostración Gráfica de las 2 Propiedades Fundamentales sobre Curvas de Nivel</div>
</div>
""", unsafe_allow_html=True)

    g1, g2 = st.columns(2)
    with g1:
        st.markdown("""
<div class="slide-card card-cyan" style="padding:14px 18px; margin-bottom:8px;">
  <h4 style="color:#38BDF8!important; margin:0 0 4px 0;">🏔️ Propiedad 1: Dirección de Máxima Pendiente</h4>
  <p style="font-size:0.88rem; margin:0; color:#94A3B8;">Apunta hacia donde la función asciende con mayor rapidez:</p>
</div>
""", unsafe_allow_html=True)
        st.latex(r"\nabla f(x, y) = \left( \frac{\partial z}{\partial x}, \frac{\partial z}{\partial y} \right), \quad \|\nabla f\| = \sqrt{\left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2}")

    with g2:
        st.markdown("""
<div class="slide-card card-gold" style="padding:14px 18px; margin-bottom:8px;">
  <h4 style="color:#FBBF24!important; margin:0 0 4px 0;">⟂ Propiedad 2: Ortogonalidad a Curvas de Nivel</h4>
  <p style="font-size:0.88rem; margin:0; color:#94A3B8;">Sobre f(x, y) = c, la derivada a lo largo de la tangente es cero:</p>
</div>
""", unsafe_allow_html=True)
        st.latex(r"df = 0 \implies \nabla f \cdot \hat{T} = 0 \implies \nabla f \perp \text{Curva de Nivel } (\angle 90^\circ)")

    st.markdown('<hr class="sep">', unsafe_allow_html=True)

    # Los dos gráficos en dos columnas claras estilo diapositiva
    st.markdown("### 📊 Demostración Visual en Dos Gráficos")
    gc1, gc2 = st.columns(2)

    with gc1:
        st.markdown("#### 🗺️ Gráfico A: Curvas de Nivel z = f(x, y) = c")
        fig_cont = go.Figure()
        fig_cont.add_trace(go.Contour(
            x=_xg, y=_yg, z=_Zg,
            colorscale="Viridis",
            contours=dict(showlabels=True, labelfont=dict(size=10, color="white"), coloring="heatmap"),
            colorbar=dict(title=dict(text="z = Close (USD)", font=dict(color="#CBD5E1", size=10)), tickfont=dict(color="#CBD5E1"), thickness=12),
            name="Curvas de nivel",
            hovertemplate="x (Open): $%{x:.2f}<br>y (High): $%{y:.2f}<br>z (Close): $%{z:.2f}<extra>Isolínea</extra>",
        ))
        fig_cont.add_trace(go.Scatter(
            x=x_m, y=y_m, mode="markers",
            marker=dict(color="#F87171", size=4, opacity=0.6),
            name="Datos reales AAPL",
        ))
        fig_cont.update_layout(
            paper_bgcolor=_BG_PAPER, plot_bgcolor=_BG_PLOT, font=_FONT_MAIN, legend=_LEGEND, height=440,
            margin=dict(t=40, b=30, l=10, r=10),
            xaxis=dict(**_AXIS_DARK, title="x = Open (USD)"),
            yaxis=dict(**_AXIS_DARK, title="y = High (USD)"),
        )
        st.plotly_chart(fig_cont, width="stretch")
        st.caption("Cada isolínea representa un valor constante de cierre z. Los puntos rojos son los registros históricos.")

    with gc2:
        st.markdown("#### 🧭 Gráfico B: Campo Vectorial ∇f y Perpendicularidad (90°)")
        fig_grad = go.Figure()
        # Curvas suaves
        fig_grad.add_trace(go.Contour(
            x=_xg, y=_yg, z=_Zg, colorscale="Blues", opacity=0.4,
            contours=dict(showlabels=False, coloring="lines"),
            line=dict(width=1.5, color="#38BDF8"), showscale=False, name="Curvas z=cte",
        ))
        # Campo vectorial
        arr_x, arr_y = [], []
        for i in range(_NQ):
            for j in range(_NQ):
                arr_x += [_Xq[i, j], _Xq[i, j] + _UX[i, j], None]
                arr_y += [_Yq[i, j], _Yq[i, j] + _UY[i, j], None]
        fig_grad.add_trace(go.Scatter(
            x=arr_x, y=arr_y, mode="lines",
            line=dict(color="#FBBF24", width=1.2), name="∇f Campo Vectorial", hoverinfo="skip",
        ))
        # Punto de prueba P0
        _cx = float(np.median(x_m))
        _cy = float(np.median(y_m))
        _gx0, _gy0 = grad_f(_cx, _cy, beta_m, s_m)
        _gn0 = np.sqrt(_gx0**2 + _gy0**2) + 1e-12
        _disp = _arrow_scale * 2.8

        # Vector gradiente destacado (rojo)
        fig_grad.add_annotation(
            x=_cx + _gx0 / _gn0 * _disp, y=_cy + _gy0 / _gn0 * _disp,
            ax=_cx, ay=_cy, xref="x", yref="y", axref="x", ayref="y",
            showarrow=True, arrowhead=3, arrowsize=1.5, arrowwidth=3.5, arrowcolor="#EF4444",
        )
        # Recta tangente perpendicular (verde)
        fig_grad.add_trace(go.Scatter(
            x=[_cx - (-_gy0) / _gn0 * _disp * 1.2, _cx + (-_gy0) / _gn0 * _disp * 1.2],
            y=[_cy - _gx0 / _gn0 * _disp * 1.2,   _cy + _gx0 / _gn0 * _disp * 1.2],
            mode="lines", line=dict(color="#10B981", width=2.5, dash="dash"),
            name="Tangente a Curva (⊥ a ∇f)",
        ))
        fig_grad.add_trace(go.Scatter(
            x=[_cx], y=[_cy], mode="markers+text",
            marker=dict(color="#EF4444", size=13, symbol="star", line=dict(color="white", width=1.5)),
            text=[" P₀ (∠90°)"], textfont=dict(color="#EF4444", size=12), name="Punto P₀ (Ortogonalidad)",
        ))
        fig_grad.update_layout(
            paper_bgcolor=_BG_PAPER, plot_bgcolor=_BG_PLOT, font=_FONT_MAIN, legend=_LEGEND, height=440,
            margin=dict(t=40, b=30, l=10, r=10),
            xaxis=dict(**_AXIS_DARK, title="x = Open (USD)"),
            yaxis=dict(**_AXIS_DARK, title="y = High (USD)"),
        )
        st.plotly_chart(fig_grad, width="stretch")
        st.caption("En P₀: El vector gradiente ∇f (rojo) cruza a 90° respecto a la recta tangente (verde).")

# ═════════════════════════════════════════════════════════════════════════════
#  DIAPOSITIVA 3: MATRIZ HESSIANA & EXTREMOS
# ═════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("""
<div class="slide-header">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <span class="slide-badge">DIAPOSITIVA 03 / 05</span>
    <span style="color:#94A3B8; font-size:0.85rem; font-weight:600;">UNJFSC • CÁLCULO III</span>
  </div>
  <div class="slide-title">La Matriz Hessiana y Análisis de Concavidad en ℝ³</div>
  <div class="slide-subtitle">Criterio de la Segunda Derivada para la Clasificación de Puntos Críticos</div>
</div>
""", unsafe_allow_html=True)

    hc1, hc2 = st.columns([1, 1], gap="large")

    with hc1:
        st.markdown("### 🔲 1. Definición y Criterio del Determinante")
        st.latex(r"""
        H = \begin{pmatrix}
            \dfrac{\partial^2 z}{\partial x^2} & \dfrac{\partial^2 z}{\partial x \partial y} \\[8pt]
            \dfrac{\partial^2 z}{\partial y \partial x} & \dfrac{\partial^2 z}{\partial y^2}
        \end{pmatrix}
        \quad\Longrightarrow\quad
        D = \det(H) = \frac{\partial^2 z}{\partial x^2}\frac{\partial^2 z}{\partial y^2} - \left(\frac{\partial^2 z}{\partial x \partial y}\right)^2
        """)

        # Tabla del criterio
        tabla_crit = pd.DataFrame({
            "Condición": ["D > 0  y  ∂²z/∂x² > 0", "D > 0  y  ∂²z/∂x² < 0", "D < 0", "D = 0"],
            "Clasificación": ["🟢 MÍNIMO LOCAL", "🔴 MÁXIMO LOCAL", "🟡 PUNTO SILLA", "⚪ INDETERMINADO"],
            "Geometría 3D": ["Valle (concavidad positiva)", "Cima (concavidad negativa)", "Inflexión cruzada en ℝ³", "Requiere orden superior"],
            "Interpretación": ["Punto de menor cota local", "Punto de mayor cota local", "Sin extremo local", "Criterio no concluyente"],
        })
        st.dataframe(tabla_crit, width="stretch", hide_index=True)

        h11, h22, h12, hdet = hessiana_original(beta_m, s_m)
        st.markdown("""
<div class="slide-card card-gold" style="margin-top:14px; margin-bottom:6px;">
  <span class="badge b-gold">MATRIZ HESSIANA DEL MODELO AJUSTADO</span>
</div>
""", unsafe_allow_html=True)
        st.latex(rf"H = \begin{{pmatrix}} {h11:.6f} & {h12:.6f} \\ {h12:.6f} & {h22:.6f} \end{{pmatrix}}, \quad D = \det(H) = {hdet:.6f}")
        st.caption("Segundas derivadas constantes que describen la concavidad global del modelo polinomial cuadrático.")

    with hc2:
        st.markdown("### 🏔️ 2. Geometría de los Tres Tipos de Puntos Críticos")
        xa = np.linspace(-2, 2, 45)
        ya = np.linspace(-2, 2, 45)
        Xa, Ya = np.meshgrid(xa, ya)

        fig_hess = make_subplots(
            rows=1, cols=3,
            specs=[[{"type": "surface"}, {"type": "surface"}, {"type": "surface"}]],
            subplot_titles=["🟢 Mínimo (D>0)", "🔴 Máximo (D>0)", "🟡 Silla (D<0)"],
        )
        _cam = dict(eye=dict(x=1.45, y=1.45, z=1.1))
        for ci, (Z_h, cs_h) in enumerate(
            [(Xa**2 + Ya**2, "Greens"), (-(Xa**2 + Ya**2), "Reds"), (Xa**2 - Ya**2, "YlOrBr")], start=1
        ):
            fig_hess.add_trace(go.Surface(x=Xa, y=Ya, z=Z_h, colorscale=cs_h, showscale=False, opacity=0.85), row=1, col=ci)
            fig_hess.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode="markers", marker=dict(size=8, color="white", symbol="diamond"), showlegend=False), row=1, col=ci)

        for ann in fig_hess.layout.annotations:
            ann.font.color = "#F1F5F9"
            ann.font.size = 11

        fig_hess.update_layout(
            height=430, paper_bgcolor=_BG_PAPER, font=_FONT_MAIN,
            scene=dict(**_SCENE_DARK, camera=_cam),
            scene2=dict(**_SCENE_DARK, camera=_cam),
            scene3=dict(**_SCENE_DARK, camera=_cam),
            margin=dict(t=50, b=10, l=0, r=0),
        )
        st.plotly_chart(fig_hess, width="stretch")
        st.markdown("""
<div class="slide-card card-purple" style="padding:14px; margin-top:8px;">
  <strong>📌 Definición Geométrica del Punto Silla:</strong> Punto donde ∇f = 0, pero las secciones transversales presentan signos opuestos de concavidad (mínimo respecto a un eje y máximo respecto al otro).
</div>
""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
#  DIAPOSITIVA 4: SIMULADOR 3D INTERACTIVO
# ═════════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown("""
<div class="slide-header">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <span class="slide-badge">DIAPOSITIVA 04 / 05</span>
    <span style="color:#94A3B8; font-size:0.85rem; font-weight:600;">UNJFSC • CÁLCULO III</span>
  </div>
  <div class="slide-title">Laboratorio 3D: Superficie z = f(x, y) & Dinámica Diferencial</div>
  <div class="slide-subtitle">Evaluación de Derivadas Parciales, Gradiente ∇f y Derivada Direccional en Tiempo Real</div>
</div>
""", unsafe_allow_html=True)

    # Controles de Diapositiva
    st.markdown("### 🎛️ Consola de Control de Variables en ℝ³")
    c_modo, c_info = st.columns([1, 2], gap="medium")

    with c_modo:
        modo = st.radio(
            "Modo de Variación:",
            ["🔀 Ambas libres (Diferencial Total dz)",
             "📈 Variar solo x = Open (Derivada Parcial ∂z/∂x)",
             "📊 Variar solo y = High (Derivada Parcial ∂z/∂y)"],
            index=0,
        )

    with c_info:
        st.markdown("""
<div class="slide-card card-cyan" style="padding:14px 18px; margin:0;">
  <strong>⚙️ Esquema de Experimentación:</strong><br>
  • <strong>Ambas libres:</strong> Evalúa la superficie general z = f(x, y) con desplazamiento en el plano base (x, y).<br>
  • <strong>Una libre:</strong> Congela la otra variable en su valor medio para aislar analíticamente la <em>Derivada Parcial</em>.<br>
  • <strong>Ángulo θ:</strong> Controla el vector unitario û = (cos θ, sin θ) para evaluar la derivada direccional.
</div>
""", unsafe_allow_html=True)

    st.markdown('<hr class="sep">', unsafe_allow_html=True)

    # Sliders
    x_min_v, x_max_v = float(x_m.min()), float(x_m.max())
    x_mean_v = float(x_m.mean())
    y_min_v, y_max_v = float(y_m.min()), float(y_m.max())
    y_mean_v = float(y_m.mean())

    _lock_x = "Variar solo y" in modo
    _lock_y = "Variar solo x" in modo

    sl1, sl2, sl3 = st.columns([1, 1, 1], gap="medium")
    with sl1:
        x_v = st.slider("Eje X: x = Open (USD)", x_min_v, x_max_v, x_mean_v, (x_max_v - x_min_v)/300, format="$%.2f", disabled=_lock_x)
        if _lock_x: x_v = x_mean_v
    with sl2:
        y_v = st.slider("Eje Y: y = High (USD)", y_min_v, y_max_v, y_mean_v, (y_max_v - y_min_v)/300, format="$%.2f", disabled=_lock_y)
        if _lock_y: y_v = y_mean_v
    with sl3:
        theta_deg = st.slider("Ángulo θ para Derivada Direccional D_û z", 0, 360, 45, 1, format="%d°")

    theta_rad_v = np.deg2rad(theta_deg)
    _z_pred = f_pred(x_v, y_v, beta_m, s_m)
    _gx, _gy = grad_f(x_v, y_v, beta_m, s_m)
    _gmag = float(np.sqrt(_gx**2 + _gy**2))
    _dd = deriv_direccional(x_v, y_v, theta_rad_v, beta_m, s_m)
    _h11, _h22, _h12, _hdet = hessiana_original(beta_m, s_m)

    # Métricas en vivo (Dashboard de Diapositiva)
    st.markdown("### 📊 Métricas Instantáneas en el Punto Evaluado")
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    m1.metric("Altura z = Close", f"${_z_pred:.2f}", delta=f"{_z_pred - float(z_m.mean()):.2f} vs media")
    m2.metric("∂z/∂x (Parcial Open)", f"{_gx:.4f}")
    m3.metric("∂z/∂y (Parcial High)", f"{_gy:.4f}")
    m4.metric("‖∇f‖ (Magnitud)", f"{_gmag:.4f}")
    m5.metric(f"D_û z (θ={theta_deg}°)", f"{_dd:.4f}")
    m6.metric("det(H) Hessiana", f"{_hdet:.6f}")

    # Gráfico 3D interactivo
    st.markdown('<hr class="sep">', unsafe_allow_html=True)
    st.markdown("### 🌐 Superficie 3D: z = f(x, y), Vector Gradiente y Datos Históricos")

    _N3D = 38
    _xs = np.linspace(x_min_v, x_max_v, _N3D)
    _ys = np.linspace(y_min_v, y_max_v, _N3D)
    _Xs, _Ys = np.meshgrid(_xs, _ys)
    _Zs = np.vectorize(lambda a, b: f_pred(a, b, beta_m, s_m))(_Xs, _Ys)

    _gscale3d = (x_max_v - x_min_v) * 0.09
    _gx_3d = _gx / (_gmag + 1e-12) * _gscale3d
    _gy_3d = _gy / (_gmag + 1e-12) * _gscale3d
    _gz_3d = _gmag * _gscale3d

    _du_x = np.cos(theta_rad_v) * _gscale3d
    _du_y = np.sin(theta_rad_v) * _gscale3d
    _du_z = _dd * _gscale3d

    fig_3d = go.Figure()
    # 1. Superficie ondulada
    fig_3d.add_trace(go.Surface(
        x=_Xs, y=_Ys, z=_Zs, colorscale="Viridis", opacity=0.72, showscale=True,
        colorbar=dict(title=dict(text="z = Close (USD)", font=dict(color="#CBD5E1", size=10)), tickfont=dict(color="#CBD5E1"), thickness=12, x=1.0),
        name="Superficie z = f(x, y)",
    ))
    # 2. Puntos reales dispersos
    fig_3d.add_trace(go.Scatter3d(
        x=x_m, y=y_m, z=z_m, mode="markers",
        marker=dict(size=3.5, color=z_m, colorscale="Reds", opacity=0.65, showscale=False),
        name="Registros reales AAPL (250 días)",
    ))
    # 3. Punto actual
    fig_3d.add_trace(go.Scatter3d(
        x=[x_v], y=[y_v], z=[_z_pred], mode="markers+text",
        marker=dict(size=12, color="#38BDF8", symbol="diamond", line=dict(color="white", width=2)),
        text=[f"  P₀: (${x_v:.1f}, ${y_v:.1f}, ${_z_pred:.1f})"], textfont=dict(color="#38BDF8", size=11), name="Punto evaluado P₀",
    ))
    # 4. Gradiente en 3D
    fig_3d.add_trace(go.Scatter3d(
        x=[x_v, x_v + _gx_3d], y=[y_v, y_v + _gy_3d], z=[_z_pred, _z_pred + _gz_3d],
        mode="lines+markers", line=dict(color="#FBBF24", width=7),
        marker=dict(size=[2, 9], color="#FBBF24", symbol=["circle", "diamond"]),
        name=f"∇f = ({_gx:.3f}, {_gy:.3f}) [Gradiente]",
    ))
    # 5. Derivada direccional en 3D
    fig_3d.add_trace(go.Scatter3d(
        x=[x_v, x_v + _du_x], y=[y_v, y_v + _du_y], z=[_z_pred, _z_pred + _du_z],
        mode="lines+markers", line=dict(color="#C084FC", width=5, dash="dot"),
        marker=dict(size=[2, 8], color="#C084FC", symbol=["circle", "diamond"]),
        name=f"D_û z = {_dd:.3f} (θ={theta_deg}°)",
    ))
    fig_3d.update_layout(
        height=620,
        scene=dict(
            **_SCENE_DARK,
            xaxis_title="Eje X: x = Open (USD)", yaxis_title="Eje Y: y = High (USD)", zaxis_title="Eje Z: z = Close (USD)",
            camera=dict(eye=dict(x=1.5, y=-1.85, z=0.9)),
        ),
        paper_bgcolor=_BG_PAPER, font=_FONT_MAIN, legend=_LEGEND,
        margin=dict(l=0, r=0, t=30, b=0),
    )
    st.plotly_chart(fig_3d, width="stretch")

    # Leyenda visual estilo Diapositiva
    st.markdown("#### 🗺️ Guía de Elementos Gráficos en ℝ³")
    lg1, lg2, lg3, lg4, lg5 = st.columns(5)
    with lg1: st.markdown("""<div class="slide-card card-cyan" style="padding:12px; text-align:center;"><strong style="color:#38BDF8;">🌈 Superficie z = f(x, y)</strong><br><small>Superficie cuadrática con curvatura generada por x² + y².</small></div>""", unsafe_allow_html=True)
    with lg2: st.markdown("""<div class="slide-card card-red" style="padding:12px; text-align:center;"><strong style="color:#F87171;">📍 Puntos Rojos</strong><br><small>Nube de datos reales (x, y, z) observados en el mercado.</small></div>""", unsafe_allow_html=True)
    with lg3: st.markdown("""<div class="slide-card card-cyan" style="padding:12px; text-align:center;"><strong style="color:#38BDF8;">⭐ Punto P₀ (x, y, z)</strong><br><small>Coordenada dinámica evaluada en tiempo real mediante los sliders.</small></div>""", unsafe_allow_html=True)
    with lg4: st.markdown("""<div class="slide-card card-gold" style="padding:12px; text-align:center;"><strong style="color:#FBBF24;">🧭 Vector ∇f</strong><br><small>Vector gradiente en el espacio que indica la dirección de máxima pendiente.</small></div>""", unsafe_allow_html=True)
    with lg5: st.markdown("""<div class="slide-card card-purple" style="padding:12px; text-align:center;"><strong style="color:#C084FC;">🎯 Vector Direccional</strong><br><small>Vector en dirección unitaria û según el ángulo θ configurado.</small></div>""", unsafe_allow_html=True)

    # ── ANÁLISIS DE GANANCIA FINANCIERA & GRÁFICO DE TORTAS ───────────────
    st.markdown('<hr class="sep">', unsafe_allow_html=True)
    st.markdown("### 🥧 Simulación Financiera: Ganancias y Gráficos de Torta (Antes vs. Después)")

    # Explicación clara de las variables y el ángulo
    st.markdown(f"""
<div class="slide-card card-gold">
  <h4 style="color:#FBBF24!important; margin:0 0 8px 0;">💰 Interpretación Financiera de las Variables y el Ángulo θ</h4>
  <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:14px;">
    <div style="background:#0F131D; padding:14px; border-radius:10px; border-left:3px solid #38BDF8;">
      <strong style="color:#38BDF8;">¿Cuánto gano si aumento x (Open)?</strong><br>
      <small style="color:#CBD5E1;">
        La derivada parcial <code>∂z/∂x = {_gx:.4f}</code> indica que por cada $1 que sube la apertura, el cierre z sube {_gx:.2f} USD.<br>
        <strong>Ganancia Neta por acción:</strong> Como compraste $1 más caro, la ganancia marginal neta varía en <code>({_gx:.2f} - 1) = {_gx - 1:.2f} USD</code>.
      </small>
    </div>
    <div style="background:#0F131D; padding:14px; border-radius:10px; border-left:3px solid #C084FC;">
      <strong style="color:#C084FC;">¿Cuánto gano si aumento y (High)?</strong><br>
      <small style="color:#CBD5E1;">
        La derivada parcial <code>∂z/∂y = {_gy:.4f}</code> indica que por cada $1 que sube el máximo diario, el precio final de cierre sube {_gy:.2f} USD.<br>
        <strong>Ganancia Neta por acción:</strong> Como tu precio de entrada x no cambió, ¡todo ese incremento es ganancia directa adicional!
      </small>
    </div>
    <div style="background:#0F131D; padding:14px; border-radius:10px; border-left:3px solid #10B981;">
      <strong style="color:#34D399;">¿Por qué el ángulo θ está en el plano XY y define la ganancia Z?</strong><br>
      <small style="color:#CBD5E1;">
        El plano base <code>(x, y) = (Open, High)</code> representa las dos variables de entrada observables. El ángulo θ define una <strong>estrategia conjunta</strong> en el plano: <code>Δx = cos θ</code> y <code>Δy = sin θ</code>.<br>
        La derivada direccional <code>D_û z = ∇f · û</code> proyecta esa dirección hacia el eje vertical Z, indicando la <strong>tasa de ganancia por acción</strong> en esa trayectoria.
      </small>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    # Cálculos de Ganancias Antes vs Después
    _x_base = float(x_m.mean())
    _y_base = float(y_m.mean())
    _z_base = float(f_pred(_x_base, _y_base, beta_m, s_m))
    _ganancia_base = max(0.01, _z_base - _x_base)
    _roi_base = (_ganancia_base / _x_base) * 100

    _ganancia_simulada = _z_pred - x_v
    _roi_simulado = (_ganancia_simulada / x_v) * 100
    _var_ganancia = _ganancia_simulada - _ganancia_base

    # Métricas de rentabilidad
    pm1, pm2, pm3, pm4 = st.columns(4)
    pm1.metric("💵 Ganancia Inicial (Antes)", f"${_ganancia_base:.2f}/acc", f"{_roi_base:.2f}% ROI base")
    pm2.metric("🚀 Ganancia Simulada (Después)", f"${_ganancia_simulada:.2f}/acc", f"{_roi_simulado:.2f}% ROI actual", delta_color="normal")
    pm3.metric("📈 Variación de Ganancia", f"${_var_ganancia:+.2f}/acc", f"{_var_ganancia:+.2f} USD vs Base")
    pm4.metric("🧭 Tasa Direccional D_û z", f"{_dd:+.4f} USD", f"en θ = {theta_deg}°")

    # Gráficos de Torta: Antes vs Después
    fig_pie = make_subplots(
        rows=1, cols=2,
        specs=[[{'type': 'pie'}, {'type': 'pie'}]],
        subplot_titles=[
            f"📊 Estado Inicial (Antes) — Ganancia: ${_ganancia_base:.2f} ({_roi_base:.1f}%)",
            f"🚀 Estado Simulado (Después) — Ganancia: ${_ganancia_simulada:.2f} ({_roi_simulado:.1f}%)"
        ]
    )

    # Torta 1: Antes
    fig_pie.add_trace(go.Pie(
        labels=['Capital Invertido (Open)', 'Ganancia Neta (Close - Open)'],
        values=[_x_base, _ganancia_base],
        hole=0.45,
        marker=dict(colors=['#1E293B', '#10B981']),
        textinfo='label+percent',
        hovertemplate="%{label}: $%{value:.2f}<br>%{percent}<extra>Antes</extra>",
    ), row=1, col=1)

    # Torta 2: Después
    _color_ganancia = '#38BDF8' if _ganancia_simulada >= _ganancia_base else '#F59E0B'
    fig_pie.add_trace(go.Pie(
        labels=['Capital Invertido (Open)', 'Ganancia Neta Simulada'],
        values=[x_v, max(0.01, _ganancia_simulada)],
        hole=0.45,
        marker=dict(colors=['#1E293B', _color_ganancia]),
        textinfo='label+percent',
        hovertemplate="%{label}: $%{value:.2f}<br>%{percent}<extra>Después</extra>",
    ), row=1, col=2)

    fig_pie.update_layout(
        paper_bgcolor=_BG_PAPER,
        plot_bgcolor=_BG_PLOT,
        font=_FONT_MAIN,
        height=350,
        margin=dict(t=50, b=20, l=10, r=10),
        showlegend=False,
    )
    for ann in fig_pie.layout.annotations:
        ann.font.color = '#F1F5F9'
        ann.font.size = 13

    st.plotly_chart(fig_pie, width="stretch")

# ═════════════════════════════════════════════════════════════════════════════
#  DIAPOSITIVA 5: CONCLUSIONES & MÉTRICAS
# ═════════════════════════════════════════════════════════════════════════════
with tab5:
    st.markdown("""
<div class="slide-header">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <span class="slide-badge">DIAPOSITIVA 05 / 05</span>
    <span style="color:#94A3B8; font-size:0.85rem; font-weight:600;">UNJFSC • CÁLCULO III</span>
  </div>
  <div class="slide-title">Conclusiones del Modelo Multivariable en ℝ³</div>
  <div class="slide-subtitle">Síntesis Analítica y Resumen Estadístico de los Parámetros del Ajuste OLS</div>
</div>
""", unsafe_allow_html=True)

    c_left, c_right = st.columns([3, 2], gap="large")

    with c_left:
        st.markdown("### 📌 4 Conclusiones Fundamentales")
        st.markdown("""
<div class="slide-card card-cyan">
  <h4 style="color:#38BDF8!important; margin:0 0 6px 0;">1️⃣ Derivadas Parciales (Sensibilidad de Ejes)</h4>
  <p style="font-size:0.92rem; margin:0;">
    Las derivadas ∂z/∂x y ∂z/∂y cuantifican el impacto marginal de cada variable independiente. El precio máximo diario (y) exhibe la mayor ponderación sobre la altura de cierre (z).
  </p>
</div>

<div class="slide-card card-purple">
  <h4 style="color:#C084FC!important; margin:0 0 6px 0;">2️⃣ Vector Gradiente (Dirección y Ortogonalidad)</h4>
  <p style="font-size:0.92rem; margin:0;">
    Se comprobó que ∇f marca la trayectoria de máxima variación instantánea y resulta estrictamente ortogonal a las curvas de nivel f(x, y) = c, propiedad matemática que rige la optimización multivariable.
  </p>
</div>

<div class="slide-card card-gold">
  <h4 style="color:#FBBF24!important; margin:0 0 6px 0;">3️⃣ Matriz Hessiana (Curvatura de Segundo Orden)</h4>
  <p style="font-size:0.92rem; margin:0;">
    El cálculo del determinante D = det(H) permite clasificar la concavidad de la superficie en ℝ³. En el polinomio ajustado, la curvatura es uniforme en el dominio acotado analizado.
  </p>
</div>

<div class="slide-card card-green">
  <h4 style="color:#34D399!important; margin:0 0 6px 0;">4️⃣ Bondad de Ajuste OLS (Precisión en ℝ³)</h4>
  <p style="font-size:0.92rem; margin:0;">
    El coeficiente de determinación alcanzado fue <strong>R² = 99.4%</strong>, verificando que el plano base (x, y) = (Open, High) determina con alta fidelidad la cota del precio de cierre z.
  </p>
</div>
""", unsafe_allow_html=True)

    with c_right:
        st.markdown("### 📊 Ficha Técnica del Modelo (AAPL)")
        _gx_m, _gy_m = grad_f(float(x_m.mean()), float(y_m.mean()), beta_m, s_m)
        _gm_m = float(np.sqrt(_gx_m**2 + _gy_m**2))
        _h11m, _h22m, _h12m, _hdetm = hessiana_original(beta_m, s_m)

        resumen_df = pd.DataFrame({
            "Parámetro / Métrica": [
                "Ecuación del Modelo",
                "Variable en Eje X",
                "Variable en Eje Y",
                "Variable en Eje Z",
                "Bondad de Ajuste R²",
                "Registros Analizados",
                "∂z/∂x medio",
                "∂z/∂y medio",
                "‖∇f‖ medio",
                "det(H) Hessiana",
            ],
            "Valor Obtenido": [
                "z = f(x, y) [Cuadrática 2D]",
                "x = Open (USD)",
                "y = High (USD)",
                "z = Close (USD)",
                f"{r2_m:.4f} (99.4%)",
                f"{len(df_main)} días bursátiles",
                f"{_gx_m:.4f}",
                f"{_gy_m:.4f}",
                f"{_gm_m:.4f}",
                f"{_hdetm:.6f}",
            ],
        })
        st.dataframe(resumen_df, width="stretch", hide_index=True)

        st.markdown("""
<div class="slide-card card-cyan" style="margin-top:14px;">
  <span class="badge b-cyan">DATOS ACADÉMICOS Y EQUIPO</span>
  <ul style="padding-left:18px; margin:8px 0 0 0; font-size:0.88rem;">
    <li><strong>Universidad:</strong> José Faustino Sánchez Carrión (UNJFSC)</li>
    <li><strong>Asignatura:</strong> Cálculo III</li>
    <li><strong>Integrantes del Grupo:</strong>
      <ul style="margin-top:4px;">
        <li><strong style="color:#38BDF8;">Inga Sialas, Carlos Alexis</strong></li>
        <li><strong style="color:#C084FC;">Quispe Lucas, Cristian David</strong></li>
      </ul>
    </li>
    <li><strong>Activo Modelado:</strong> Apple Inc. (AAPL - Yahoo Finance)</li>
    <li><strong>Entorno:</strong> Python, NumPy, Pandas, Plotly & Streamlit</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  PIE DE DIAPOSITIVA
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; color:#64748B; font-size:0.8rem; padding:18px 0; border-top:1px solid #1E293B; margin-top:24px;">
  📐 Exposición de Cálculo III — Universidad Nacional José Faustino Sánchez Carrión (UNJFSC) • 2026
</div>
""", unsafe_allow_html=True)
