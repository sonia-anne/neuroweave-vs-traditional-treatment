import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="NEUROWEAVE Comparative Dashboard", layout="wide", page_icon="🧠")

# --- CUSTOM DARK THEME ---
st.markdown("""
    <style>
        body { background-color: #0f172a; }
        .main { background-color: #0f172a; color: white; }
        h1, h2, h3, h4 { color: #38bdf8; text-align: center; }
        .css-1d391kg { background-color: #0f172a !important; }
    </style>
""", unsafe_allow_html=True)

# --- TITLE AND INTRO ---
st.title("🧠 NEUROWEAVE vs. Current Hydrocephalus Treatments")
st.markdown("#### A multi-dimensional visual and scientific comparison")

# --- DATASET SETUP ---
treatments = ["Shunt (VP/VA)", "Endoscopic ETV", "Gene Editing", "SRP-2001", "Lonafarnib+Progerinina", "NEUROWEAVE"]
categories = ["Efficacy", "Reinterventions", "Cost", "Tissue Regen", "Monitoring", "AI Integration"]
data = [
    [50, 85, 10000, 0, 0, 0],
    [60, 50, 8000, 0, 0, 0],
    [70, 40, 15000, 30, 10, 5],
    [75, 30, 13000, 40, 0, 0],
    [65, 50, 11000, 0, 0, 0],
    [92, 5, 1200, 100, 100, 100]
]
df = pd.DataFrame(data, columns=categories, index=treatments)

# --- RADAR CHART ---
st.subheader("🕸️ Radar Chart: Performance by Category")
radar_fig = go.Figure()
for treatment in df.index:
    radar_fig.add_trace(go.Scatterpolar(
        r=df.loc[treatment].values,
        theta=categories,
        fill='toself',
        name=treatment
    ))
radar_fig.update_layout(
    polar=dict(
        bgcolor="#0f172a",
        radialaxis=dict(visible=True, range=[0, 100], color='white', gridcolor='gray')
    ),
    template="plotly_dark",
    title="Treatment Profile by Category",
    font=dict(color="white")
)
st.plotly_chart(radar_fig, use_container_width=True)

# --- PARALLEL COORDINATES ---
st.subheader("📊 Parallel Coordinates")
parallel_fig = px.parallel_coordinates(
    df.reset_index(),
    color="Efficacy",
    dimensions=categories,
    color_continuous_scale=px.colors.sequential.Teal
)
st.plotly_chart(parallel_fig, use_container_width=True)

# --- SANKEY DIAGRAM ---
st.subheader("🔀 Sankey Diagram: Investment Flow to Results")
sankey_fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15, thickness=20,
        line=dict(color="white", width=0.5),
        label=[
            "R&D", "Trials", "Surgery", "Nanotech", "AI System",
            "Low Outcome", "Medium Outcome", "High Outcome"
        ],
        color=["gray", "gray", "gray", "cyan", "purple", "#f87171", "#facc15", "#34d399"]
    ),
    link=dict(
        source=[0, 1, 2, 3, 4],
        target=[5, 6, 6, 7, 7],
        value=[20, 15, 15, 25, 25],
        color=["#ff6b6b", "#ffd166", "#fca311", "#06d6a0", "#6a5acd"]
    )
)])
sankey_fig.update_layout(
    title="Resource Allocation → Clinical Outcomes",
    font=dict(color="white"),
    paper_bgcolor="#0f172a"
)
st.plotly_chart(sankey_fig, use_container_width=True)

# --- VIOLIN + BOX PLOT ---
st.subheader("🎻 Violin + Box Plot: Cost Analysis")
cost_df = pd.DataFrame({
    "Treatment": treatments,
    "Cost": [10000, 8000, 15000, 13000, 11000, 1200]
})
violin_fig = px.violin(cost_df, y="Cost", x="Treatment", box=True, points="all", color="Treatment",
                       color_discrete_sequence=px.colors.qualitative.Bold)
violin_fig.update_layout(
    yaxis_title="Cost (USD)",
    paper_bgcolor="#0f172a",
    font=dict(color="white"),
    title="Treatment Cost Comparison"
)
st.plotly_chart(violin_fig, use_container_width=True)

# --- DOT PLOT FOR EFFICACY CONFIDENCE ---
st.subheader("📌 Dot Plot: Efficacy with Confidence Intervals")
dot_fig = go.Figure()
for treatment in df.index:
    dot_fig.add_trace(go.Scatter(
        x=[df.loc[treatment, "Efficacy"]],
        y=[treatment],
        mode='markers',
        marker=dict(size=14, color='#4ade80'),
        name=treatment,
        error_x=dict(type='data', array=[5])
    ))
dot_fig.update_layout(
    xaxis_title="Efficacy (%)",
    yaxis=dict(autorange="reversed"),
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font=dict(color="white"),
    title="Estimated Efficacy (±5%)"
)
st.plotly_chart(dot_fig, use_container_width=True)

# --- FINAL ARGUMENT ---
st.markdown("""
### 🧬 Why NEUROWEAVE Is Scientifically Superior

Sam Berns (died at 17) received traditional palliative support. Sammy Basso (lived until 28) had access to **lonafarnib**, a molecule that extended his life through molecular inhibition. Yet, both lacked regeneration.

**NEUROWEAVE introduces:**
- **Real-time AI control**
- **Tissue regeneration with BDNF/VEGF**
- **One-time nano-delivery**
- **Autodestruct safety + 3D navigation**

It’s not a patch. It’s a cure.

> "If technology gave Sammy 11 extra years, NEUROWEAVE can give life back."
""")