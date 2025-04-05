import streamlit as st import pandas as pd import numpy as np import plotly.graph_objects as go import plotly.express as px from lifelines import KaplanMeierFitter, NelsonAalenFitter import streamlit_lottie as st_lottie import requests

--- PAGE CONFIG ---

st.set_page_config(page_title="NEUROWEAVE Survival Dashboard", layout="wide", page_icon="🧬")

--- HEADER WITH LOTTIE ---

st.title("\U0001f9ec Life Expectancy in Progeria: NEUROWEAVE vs Historical Interventions") st.markdown(""" This interactive dashboard compares Sam Berns, Sammy Basso, and a projected patient treated with NEUROWEAVE. It uses advanced medical statistics and visual tools to model the future of neuroregeneration in rare genetic diseases. """)

def load_lottieurl(url): r = requests.get(url) if r.status_code != 200: return None return r.json()

lottie_robot = load_lottieurl("https://lottie.host/1b4ccf44-56ed-4421-9c8c-2bb1556f93ed/3eaZ1BAwbn.json") st_lottie.st_lottie(lottie_robot, speed=1, height=200)

--- DATA ---

data = pd.DataFrame({ 'Patient': ['Sam Berns', 'Sammy Basso', 'Projected NEUROWEAVE Patient'], 'Treatment': ['Lonafarnib', 'Lonafarnib + Trials', 'NEUROWEAVE (Hypothetical)'], 'Survival Time': [17, 28, 38], 'Event': [1, 1, 0], 'Supportive Therapy': ['None', 'Cardiac Support', 'Neuroregenerative AI Nanobots'] })

--- Kaplan-Meier ---

kmf = KaplanMeierFitter() fig_km = go.Figure() for index, row in data.iterrows(): kmf.fit([row['Survival Time']], [row['Event']], label=row['Patient']) surv_df = kmf.survival_function_.reset_index() fig_km.add_trace(go.Scatter(x=surv_df['timeline'], y=surv_df[row['Patient']], mode='lines+markers', name=row['Patient'], line=dict(width=3))) fig_km.update_layout(title="Kaplan-Meier Survival Curves", xaxis_title="Age (Years)", yaxis_title="Survival Probability", template="plotly_dark", plot_bgcolor="#0f172a", paper_bgcolor="#0f172a", font=dict(color="white")) st.plotly_chart(fig_km, use_container_width=True)

--- Nelson-Aalen Cumulative Hazard ---

naf = NelsonAalenFitter() fig_naf = go.Figure() for index, row in data.iterrows(): naf.fit([row['Survival Time']], [row['Event']], label=row['Patient']) hazard_df = naf.cumulative_hazard_.reset_index() fig_naf.add_trace(go.Scatter(x=hazard_df['timeline'], y=hazard_df[row['Patient']], mode='lines+markers', name=row['Patient'], line=dict(width=3))) fig_naf.update_layout(title="Cumulative Hazard (Nelson-Aalen Estimation)", xaxis_title="Age (Years)", yaxis_title="Cumulative Hazard", template="plotly_dark", plot_bgcolor="#1e1e2f", paper_bgcolor="#1e1e2f", font=dict(color="white")) st.plotly_chart(fig_naf, use_container_width=True)

--- Risk Heatmap ---

heatmap_df = pd.DataFrame({ "Treatment": ["Shunt", "SRP-2001", "Lonafarnib", "NEUROWEAVE"], "Expected Max Age": [15, 20, 28, 38], "Risk Level": [0.9, 0.6, 0.4, 0.1] }) heatmap = px.imshow(heatmap_df.set_index("Treatment")[["Expected Max Age", "Risk Level"]], text_auto=True, color_continuous_scale="Viridis", title="Expected Survival & Risk Level") heatmap.update_layout(paper_bgcolor="#0f172a", plot_bgcolor="#0f172a", font=dict(color='white')) st.plotly_chart(heatmap, use_container_width=True)

--- Dot Plot ---

dot_fig = go.Figure() dot_fig.add_trace(go.Scatter(x=[17, 28, 38], y=["Sam Berns", "Sammy Basso", "NEUROWEAVE"], mode='markers+text', marker=dict(size=[18, 24, 30], color=['red', 'orange', 'limegreen']), text=["Lonafarnib", "Lonafarnib+Support", "Neuro-AI Regeneration"], textposition="top center")) dot_fig.update_layout(title="Expected Lifespan Based on Intervention", xaxis_title="Years of Life", yaxis=dict(autorange='reversed'), paper_bgcolor="#0f172a", plot_bgcolor="#0f172a", font=dict(color="white")) st.plotly_chart(dot_fig, use_container_width=True)

--- Explanation ---

with st.expander("\U0001f52c Scientific Explanation"): st.markdown(""" Why did Sammy live longer than Sam? - Sammy received additional cardiac therapies and had continuous Italian support. - Sam relied solely on Lonafarnib, which slowed but did not stop progression.

**Why NEUROWEAVE could exceed both:**
- Combines **real-time detection**, **AI correction**, and **neuroregeneration**.
- Designed to **reverse** cellular damage, not just delay symptoms.
- Projects +10 years of survival by restoring and restructuring brain function.
""")

--- Footer ---

st.markdown("---") st.success("NEUROWEAVE is not a drug. It’s a platform for rewiring survival.") st.caption("Created by Annette — Global Young Scientist from Ecuador. \U0001f9e0")

