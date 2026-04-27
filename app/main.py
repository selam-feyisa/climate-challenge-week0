import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("🌍 African Climate Dashboard (COP32 Analysis)")

# -------------------------
# LOAD DATA
# -------------------------
data = load_data()

# -------------------------
# SIDEBAR CONTROLS
# -------------------------
st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    data["Country"].unique(),
    default=data["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(data["Year"].min()),
    int(data["Year"].max()),
    (2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M", "WS2M"]
)

# -------------------------
# FILTER DATA
# -------------------------
filtered = data[
    (data["Country"].isin(countries)) &
    (data["Year"].between(year_range[0], year_range[1]))
]

# ======================================================
# 🌡️ TEMPERATURE TREND (FULL TIME SERIES)
# ======================================================
st.subheader("🌡️ Temperature Trend Over Time")

fig, ax = plt.subplots()

for c in countries:
    subset = filtered[filtered["Country"] == c]
    trend = subset.groupby("DATE")["T2M"].mean()
    ax.plot(trend.index, trend.values, label=c)

ax.set_xlabel("Date")
ax.set_ylabel("Temperature (°C)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# ======================================================
# 🌧️ PRECIPITATION TREND
# ======================================================
st.subheader("🌧️ Precipitation Trend Over Time")

fig2, ax2 = plt.subplots()

for c in countries:
    subset = filtered[filtered["Country"] == c]
    trend = subset.groupby("DATE")["PRECTOTCORR"].mean()
    ax2.plot(trend.index, trend.values, label=c)

ax2.set_xlabel("Date")
ax2.set_ylabel("Precipitation (mm)")
ax2.legend()
ax2.grid(True)

st.pyplot(fig2)

# ======================================================
# 📊 VARIABLE DISTRIBUTION
# ======================================================
st.subheader(f"📊 Distribution of {variable}")

fig3, ax3 = plt.subplots()

filtered.boxplot(column=variable, by="Country", ax=ax3)
plt.suptitle("")

st.pyplot(fig3)

# ======================================================
# 📋 DATA PREVIEW
# ======================================================
st.subheader("📋 Filtered Data Preview")
st.dataframe(filtered.head(20))