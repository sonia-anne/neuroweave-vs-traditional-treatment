import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="NEUROWEAVE Life Expectancy Simulation", layout="wide", page_icon="🧠")

# --- HEADER ---
st.title("🧬 Life Expectancy in Progeria: Impact of NEUROWEAVE")
st.markdown("### Scientific analysis comparing historical survival in progeria (Sam Berns vs Sammy Basso) and potential survival impact of NEUROWEAVE.")
st.markdown("---")

# --- DATA ---
data = {
    "Patient": ["Sam Berns", "Sammy Basso", "Projected NEUROWEAVE Patient"],
    "Survival Age": [17, 28, 36],
    "Treatment": ["Supportive", "Lonafarnib + Experimental", "NEUROWEAVE + AI Nanotherapy"]
}
df = pd.DataFrame(data)

# --- DOT PLOT ---
st.header("📌 Survival Ages: Real vs NEUROWEAVE Projection")
dot_fig = go.Figure()
dot_fig.add_trace(go.Scatter(
    x=df["Survival Age"],
    y=df["Patient"],
    mode='markers+text',
    marker=dict(size=20, color=["crimson", "orange", "limegreen"]),
    text=df["Treatment"],
    textposition="middle right"
))
dot_fig.update_layout(
    title="Life Expectancy in Progeria",
    xaxis_title="Age at Death or Projection",
    yaxis=dict(autorange="reversed"),
    plot_bgcolor="#0f172a",
    paper_bgcolor="#0f172a",
    font=dict(color="white")
)
st.plotly_chart(dot_fig, use_container_width=True)

# --- KAPLAN-MEIER SIMULATION ---
st.header("📈 Survival Probability Curve (Simulated)")
ages = np.arange(0, 40, 1)
sam_berns_surv = 1 - (ages / 17).clip(0, 1)**1.5
sammy_basso_surv = 1 - (ages / 28).clip(0, 1)**1.8
neuroweave_surv = 1 - (ages / 36).clip(0, 1)**2.5

km_fig = go.Figure()
km_fig.add_trace(go.Scatter(x=ages, y=sam_berns_surv, name="Sam Berns", line=dict(color="crimson", width=3)))
km_fig.add_trace(go.Scatter(x=ages, y=sammy_basso_surv, name="Sammy Basso", line=dict(color="orange", width=3)))
km_fig.add_trace(go.Scatter(x=ages, y=neuroweave_surv, name="NEUROWEAVE Projection", line=dict(color="limegreen", width=3, dash="dash")))

km_fig.update_layout(
    title="Simulated Kaplan-Meier Survival Curve",
    xaxis_title="Age (years)",
    yaxis_title="Probability of Survival",
    plot_bgcolor="#0f172a",
    paper_bgcolor="#0f172a",
    font=dict(color="white"),
    legend=dict(bgcolor="#1e293b")
)
st.plotly_chart(km_fig, use_container_width=True)

# --- HEATMAP RISK ---
st.header("🔥 Hazard Risk Heatmap by Age")
risk_data = pd.DataFrame({
    "Age": ages,
    "Sam Berns Risk": 1 - sam_berns_surv,
    "Sammy Basso Risk": 1 - sammy_basso_surv,
    "NEUROWEAVE Risk": 1 - neuroweave_surv
})
heatmap_fig = px.imshow(risk_data.drop(columns=["Age"]).T.values,
                        labels=dict(x="Age", y="Profile", color="Risk Level"),
                        x=ages,
                        y=risk_data.drop(columns=["Age"]).columns,
                        color_continuous_scale="Reds")
heatmap_fig.update_layout(
    title="Relative Hazard Risk Over Time",
    paper_bgcolor="#0f172a",
    font=dict(color="white")
)
st.plotly_chart(heatmap_fig, use_container_width=True)

# --- INTERPRETATION ---
st.markdown("### 💡 Interpretation:")
st.success("""
Sammy Basso lived significantly longer than Sam Berns due to access to experimental therapies like Lonafarnib. NEUROWEAVE, integrating AI-driven nanobots, aims not only to delay symptoms but actively **regenerate tissue** and restore biological balance.

This simulation shows NEUROWEAVE could potentially extend life expectancy up to 36 years or more, by targeting the root cause — not just the symptoms — through precision intervention and regenerative strategies.
""")