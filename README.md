# 📊 DSA210 Term Project: **Analyzing the Relationship Between Geography and Living Standards**

## 🌍 Project Overview

This project investigates how a country's **geographical characteristics** (such as climate, elevation, and proximity to coastlines) correlate with its **living standards**.

By analyzing multiple datasets, we aim to uncover **patterns and relationships** between geography and indicators of quality of life, contributing to a broader understanding of how environment shapes economic and social well-being.

---

### 🔍 Key Research Questions

- Do geographical features significantly impact living standards?
- Which geographical factors show the strongest correlations with quality of life?
- Are regions at certain latitudes or elevations advantaged in living standards?

---

## 📌 Hypothesis

- **Null Hypothesis (H₀):** Geographical features have no significant relationship with living standards.
- **Alternative Hypothesis (Hₐ):** Certain geographical features (e.g., temperature, latitude) significantly influence living standards.

Statistical testing was conducted to determine whether we can reject the null hypothesis.

---

## 🎯 Objectives

- Analyze correlations between geographical metrics and quality of life values.
- Identify geographical trends affecting well-being.
- Provide insights for policymakers and researchers interested in geography-driven development factors.

---

## 📈 Datasets Used

- **Primary Dataset:** [Quality of Life for Each Country (Kaggle)](https://www.kaggle.com/datasets/ahmedmohamed2003/quality-of-life-for-each-country)
- **Supplementary Geographical Data:**
  - Average Annual Temperature
  - Elevation Data (meters, feet)
  - Latitude and Longitude
  - Coastline Length (World Factbook, WRI sources)

Merging and cleaning operations were performed using custom Python scripts (`merge.py`, `mergeNsort.py`, and `remove.py`).

---

## 🔧 Tools & Technologies

- **Programming Language:** Python
- **Data Libraries:** Pandas, NumPy, SciPy
- **Statistical Analysis:** Pearson Correlation, Permutation Testing
- **Visualization:** (Plots available in the `plots` directory)

---

## 📊 Descriptive Statistics

| Metric                | Mean     | Std Dev  | Min     | Max       |
| --------------------- | -------- | -------- | ------- | --------- |
| coastline\_wf         | 6226.33  | 21380.21 | 0.00    | 202080.00 |
| coastline\_wri        | 12908.90 | 34082.79 | 0.00    | 265523.00 |
| latitude              | 27.11    | 25.59    | -40.90  | 64.96     |
| longitude             | 22.34    | 58.20    | -106.35 | 174.89    |
| Quality of Life Value | 131.68   | 48.45    | 0.00    | 224.31    |
| Elevation (m)         | 587.46   | 505.31   | 15.00   | 2988.00   |
| Elevation (ft)        | 1927.35  | 1657.83  | 49.00   | 9803.00   |
| Temperature (°C)      | 16.14    | 8.33     | -4.03   | 28.17     |

---

## 📊 Correlation Analysis Summary

| Variable         | Pearson r  | Traditional p-value | Permutation p-value |
| ---------------- | ---------- | ------------------- | ------------------- |
| coastline\_wf    | 0.106      | 0.2850              | 0.2783              |
| coastline\_wri   | 0.136      | 0.1764              | 0.1755              |
| Elevation (m)    | **-0.362** | **0.0002**          | **0.0001**          |
| Temperature (°C) | **-0.440** | **0.0000**          | **0.0000**          |
| latitude         | **0.448**  | **0.0000**          | **0.0000**          |
| longitude        | -0.014     | 0.8868              | 0.8926              |

### 📊 Key Observations

- 🔥 **Higher temperatures are associated with lower living standards.**
- 🌄 **Higher elevations negatively correlate with living standards.**
- 🌎 **Latitude is positively correlated with quality of life**, suggesting regions farther from the equator may have better living standards.
- 🌊 **Coastline lengths show no significant relationship with living standards.**
- 🔄 **Longitude does not significantly affect living standards.**

> **Important Note:** These analyses alone are not sufficient to definitively prove a causal relationship, even when slight correlations are observed. Preliminary results suggest that **subregion** (e.g., continental or regional divisions) may have a stronger association with living standards. Therefore, **further research** will continue to focus on analyzing subregional patterns in greater detail.

---

## 📅 Conclusion

- There is **very limited evidence** that geographical features such as **temperature, elevation, and latitude** are related to living standards.
- **Longitude and coastline proximity** appear to have little to no influence based on the data analyzed.
- Overall, geography alone shows only **slight associations** with quality of life, and stronger relations are suspected at the **subregional** level.

---

## 🔍 Next Steps

- Deeper investigation into **regional patterns** (e.g., continent-level analysis).
- Explore **multivariate models** combining geography with economic and social factors.
- Expand datasets to include more refined geographical variables like precipitation, land use, and natural disaster risk.
- Focus future analysis on the influence of **subregions** on living standards.

---

> **Note:** Visualizations supporting this analysis (scatter plots, regression plots) are available in the **`plots/`** directory.

