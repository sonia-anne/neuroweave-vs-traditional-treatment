import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from lifelines import KaplanMeierFitter, NelsonAalenFitter

# PAGE CONFIG
st.set_page_config(page_title="NEUROWEAVE: Survival Dashboard", layout="wide", page_icon="🧠")
st.title("🧬 Survival Comparison: Lonafarnib, Trials & NEUROWEAVE")
st.markdown("### Scientific Visualizations on Life Expectancy for Progeria Treatments")

# DATASET
data = pd.DataFrame({
    'Patient': ['Sam Berns', 'Sammy Basso', 'NEUROWEAVE (Projected)'],
    'Treatment': ['Lonafarnib', 'Lonafarnib + Cardio Trials', 'NEUROWEAVE'],
    'Survival Time': [17, 28, 38],
    'Event': [1, 1, 0],
})

# KAPLAN-MEIER
kmf = KaplanMeierFitter()
fig_km = go.Figure()
for i, row in data.iterrows():
    kmf.fit([row['Survival Time']], [row['Event']], label=row['Patient'])
    km_df = kmf.survival_function_.reset_index()
    fig_km.add_trace(go.Scatter(x=km_df['timeline'], y=km_df[row['Patient']],
                                mode='lines+markers', name=row['Patient']))
fig_km.update_layout(title="Kaplan-Meier Survival Curve",
                     xaxis_title="Age (Years)", yaxis_title="Survival Probability",
                     template="plotly_dark", font=dict(color="white"))
st.plotly_chart(fig_km, use_container_width=True)

# NELSON-AALEN
naf = NelsonAalenFitter()
fig_na = go.Figure()
for i, row in data.iterrows():
    naf.fit([row['Survival Time']], [row['Event']], label=row['Patient'])
    ha_df = naf.cumulative_hazard_.reset_index()
    fig_na.add_trace(go.Scatter(x=ha_df['timeline'], y=ha_df[row['Patient']],
                                mode='lines+markers', name=row['Patient']))
fig_na.update_layout(title="Nelson-Aalen Cumulative Hazard",
                     xaxis_title="Age", yaxis_title="Cumulative Hazard",
                     template="plotly_dark", font=dict(color="white"))
st.plotly_chart(fig_na, use_container_width=True)

# DOT PLOT
dot = go.Figure()
dot.add_trace(go.Scatter(x=[17, 28, 38],
                         y=["Sam Berns", "Sammy Basso", "NEUROWEAVE"],
                         mode='markers+text',
                         text=["17 yrs", "28 yrs", "38 yrs (Projected)"],
                         marker=dict(size=[18, 25, 30], color=["red", "orange", "lime"]),
                         textposition="top center"))
dot.update_layout(title="Life Expectancy Comparison",
                  xaxis_title="Years Lived", yaxis=dict(autorange="reversed"),
                  template="plotly_dark", font=dict(color="white"))
st.plotly_chart(dot, use_container_width=True)

# RISK HEATMAP
risk_data = pd.DataFrame({
    "Treatment": ["Shunt", "SRP-2001", "Lonafarnib", "NEUROWEAVE"],
    "Max Age": [15, 20, 28, 38],
    "Hazard Score": [0.9, 0.6, 0.4, 0.1]
})
heatmap = px.imshow(risk_data.set_index("Treatment"),
                    color_continuous_scale="Viridis", text_auto=True)
heatmap.update_layout(title="Hazard vs Life Expectancy",
                      template="plotly_dark", font=dict(color="white"))
st.plotly_chart(heatmap, use_container_width=True)

# TREEMAP CAPABILITY
cap_data = pd.DataFrame({
    "Intervention": ["Lonafarnib", "Trials", "NEUROWEAVE"] * 3,
    "Capability": ["Delays Progression", "Combo Repair", "Nanobot Regeneration",
                   "No Monitoring", "Partial Monitoring", "Full AR-Guided Monitoring",
                   "No AI", "Mild Control", "AI+Autodestruct+BDNF"],
    "Score": [30, 50, 100, 0, 50, 100, 0, 25, 100]
})
treemap = px.treemap(cap_data, path=["Intervention", "Capability"], values="Score",
                     color="Score", color_continuous_scale="Turbo")
treemap.update_layout(title="Technological Depth Comparison",
                      template="plotly_dark", font=dict(color="white"))
st.plotly_chart(treemap, use_container_width=True)

# EXPLANATION CARD
with st.expander("📌 Why Did One Live Longer Than the Other?"):
    st.markdown("""
- **Sam Berns (17 yrs):** Used *Lonafarnib* — slowed cellular damage, no systemic repair.
- **Sammy Basso (28 yrs):** Accessed cardiac therapies + combinations, received multidisciplinary care.
- **NEUROWEAVE (38 yrs projected):** Delivers AI-guided nanorobots that detect, rebalance, regenerate brain systems in real time.
    """)
    st.success("NEUROWEAVE is not a delay mechanism — it's a regenerative cure engineered from biology + nanotechnology + ethical AI.")

# FOOTER
st.markdown("---")
st.caption("Engineered by Annette — Young Scientific Leader from Ecuador. Powered by Science.")