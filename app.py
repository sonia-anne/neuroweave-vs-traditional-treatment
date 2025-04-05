import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="NEUROWEAVE Comparative Visuals", layout="wide", page_icon="🧠")
st.title("🧠 NEUROWEAVE vs. Other Hydrocephalus Treatments")
st.markdown("### A multi-dimensional scientific comparison: Shunts, Endoscopic Surgery, Gene Editing, SRP-2001, Lonafarnib, and NEUROWEAVE")

# --- DATA ---
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

# --- 1. Radar Chart (Spider Chart) ---
st.header("🕸️ Multidimensional Treatment Profile")
radar_fig = go.Figure()
for i, treatment in enumerate(df.index):
    radar_fig.add_trace(go.Scatterpolar(
        r=df.loc[treatment].values,
        theta=categories,
        fill='toself',
        name=treatment
    ))
radar_fig.update_layout(
    polar=dict(
        bgcolor="#0f172a",
        radialaxis=dict(visible=True, range=[0, 100], gridcolor='gray', color='white')
    ),
    template="plotly_dark",
    title="Performance by Category",
    font=dict(color="white")
)
st.plotly_chart(radar_fig, use_container_width=True)

# --- 2. Parallel Coordinates Plot ---
st.header("📊 Evaluation Flow")
parallel_fig = px.parallel_coordinates(
    df.reset_index(),
    color="Efficacy",
    dimensions=categories,
    color_continuous_scale=px.colors.sequential.Viridis
)
st.plotly_chart(parallel_fig, use_container_width=True)

# --- 3. Sankey Diagram ---
st.header("🔀 Resource Flow to Outcomes")
sankey_fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="white", width=0.5),
        label=[
            "R&D Cost", "Trials", "Surgery", "Nanotech", "AI System",
            "Low Result", "Medium Result", "High Result"
        ],
        color=["gray", "gray", "gray", "cyan", "purple", "#ff4c4c", "#f6e58d", "#2ecc71"]
    ),
    link=dict(
        source=[0, 1, 2, 3, 4],
        target=[5, 6, 6, 7, 7],
        value=[20, 10, 15, 30, 25],
        color=["#ff7675", "#ffeaa7", "#fab1a0", "#00cec9", "#6c5ce7"]
    )
)])
sankey_fig.update_layout(
    title="Investments vs Outcomes",
    font=dict(color="white"),
    paper_bgcolor="#0f172a"
)
st.plotly_chart(sankey_fig, use_container_width=True)

# --- 4. Violin + Box Plot ---
st.header("🎻 Cost Distribution")
cost_df = pd.DataFrame({
    "Treatment": treatments,
    "Cost": [10000, 8000, 15000, 13000, 11000, 1200]
})
violin_fig = px.violin(cost_df, y="Cost", x="Treatment", box=True, points="all", color="Treatment",
                       color_discrete_sequence=px.colors.qualitative.Bold)
violin_fig.update_layout(
    title="Treatment Cost Distribution",
    yaxis_title="USD",
    plot_bgcolor='#0f172a',
    paper_bgcolor='#0f172a',
    font=dict(color="white")
)
st.plotly_chart(violin_fig, use_container_width=True)

# --- 5. Treemap ---
st.header("🧩 Value by Category per Treatment")
flat_data = []
for i, treatment in enumerate(treatments):
    for j, cat in enumerate(categories):
        flat_data.append({"Treatment": treatment, "Category": cat, "Score": data[i][j]})
treemap_df = pd.DataFrame(flat_data)
treemap_fig = px.treemap(treemap_df, path=["Treatment", "Category"], values="Score", color="Score",
                         color_continuous_scale="aggrnyl")
treemap_fig.update_layout(
    title="Category Weight by Treatment",
    paper_bgcolor="#0f172a",
    font=dict(color="white")
)
st.plotly_chart(treemap_fig, use_container_width=True)

# --- 6. Dot Plot with Confidence ---
st.header("📌 Efficacy Confidence Intervals")
dot_fig = go.Figure()
for i, treatment in enumerate(treatments):
    dot_fig.add_trace(go.Scatter(
        x=[df.loc[treatment, "Efficacy"]],
        y=[treatment],
        mode='markers',
        marker=dict(size=14, color='lightgreen'),
        name=treatment,
        error_x=dict(type='data', array=[5])
    ))
dot_fig.update_layout(
    title="Estimated Efficacy (±5%)",
    xaxis_title="Efficacy (%)",
    yaxis=dict(autorange="reversed"),
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font=dict(color="white")
)
st.plotly_chart(dot_fig, use_container_width=True)

# --- COMPARATIVE REASONS ---
st.markdown("""
### 🔬 Why NEUROWEAVE Outperforms Traditional Treatments

The comparison between **Sam Berns** (17 years) and **Sammy Basso** (28 years) shows a stark contrast in life expectancy due to different approaches to treatment. **Sam Berns** had limited access to advanced treatments, whereas **Sammy Basso** benefited from **innovative therapies** such as **lonafarnib**, which extended his life significantly.

**NEUROWEAVE**, with its nanotechnology-based approach, outperforms traditional **Shunts** and **Endoscopic Surgeries** by directly addressing the root cause of hydrocephalus, rather than just mitigating symptoms. 

Key advantages of **NEUROWEAVE** include:
- **Nanotech** for precise intervention
- **AI-guided** surgeries for real-time adjustments
- **Tissue regeneration** (BDNF/VEGF) to repair damaged cells
- **Low cost** compared to traditional treatments
- **Minimal reintervention** needed due to its one-time delivery approach

These advancements make **NEUROWEAVE** not just a treatment but a **revolutionary solution** in hydrocephalus management.
""")
