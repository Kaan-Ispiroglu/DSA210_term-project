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
  
> **Note:** Visualizations supporting this analysis (scatter plots, regression plots) are available in the **`plots/`** directory.

---

### 📊 What the Machine Learning Models Tell Us

To explore how geography influences national living standards, several supervised machine learning models were applied to predict each country’s **quality of life score** using only **geographical features** (e.g. latitude, elevation, coastline access, and temperature). These models allow us to go beyond correlation and test whether patterns in geography are strong enough to explain variation in life quality across countries.

All models were framed as **regression tasks**, since the target variable—quality of life—is continuous. Their performance was evaluated using **cross-validated Mean Squared Error (MSE)**, allowing us to measure how closely the predicted values matched actual outcomes.

By comparing results across different algorithms, we gain insight into:
- How much predictive power geography alone can provide,
- Which algorithms are most effective on this type of data,
- Which geographic variables carry the most weight in determining national well-being.

---

### 🎯 Regression Model Performance Summary

To evaluate how well geography alone can predict quality of life, four different regression models were tested using appropriate validation strategies:

| Model               | Validation Method | Mean Squared Error (MSE) | Notes |
|---------------------|-------------------|---------------------------|-------|
| k-Nearest Neighbors | Train/Test Split  | 1222                      | Simple method; sensitive to data partitioning |
| Decision Tree       | Leave-One-Out CV  | 1149                      | Interpretable, tree-based model with moderate error |
| Random Forest       | Leave-One-Out CV  | **1044.67**               | Best overall performance; stable and generalizable |
| XGBoost             | Leave-One-Out CV  | 1124                      | Competitive performance; more sensitive to small sample size |

> All models were trained on geographic features only. Lower MSE indicates better predictive accuracy.

---

### 🔍 Model Interpretations & Insights

#### 📍 k-Nearest Neighbors (k-NN)
- Used as a baseline regression model.
- Achieved an MSE of 1222 under train/test split.
- Performance depended heavily on the choice of `k` and the specific split of data.
- Although not the best-performing model, it provided a useful reference point for spatial similarity-based prediction.

#### 🌳 Decision Tree
- Evaluated using Leave-One-Out Cross Validation (MSE: 1149).
- The tree learned threshold-based splits on features such as **latitude** and **temperature**.
- Depth was manually tuned for simplicity and interpretability.
- Offers clear, rule-based logic that can be visualized and easily communicated.

#### 🌲 Random Forest
- Best performer with an MSE of 1044.67 under Leave-One-Out CV.
- Combines multiple decision trees to reduce overfitting and improve prediction stability.
- Feature importance ranking revealed:
  1. **Latitude** was the most influential predictor
  2. Followed by **Temperature** and **Elevation**
  3. **Longitude** and **Coastline** had minimal impact
- Demonstrated the strongest ability to generalize using geographic features alone.

#### ⚡ XGBoost
- Performed well with an MSE of 1124 under Leave-One-Out CV.
- Although powerful, its performance was slightly less consistent than Random Forest on this dataset.
- More sensitive to hyperparameter tuning and data scale.
- Still confirmed the importance of **latitude** and **temperature** as dominant predictors.

---

### 🎯 Key Takeaways

- **Geographic features alone** can moderately predict a country's quality of life.
- Among all models tested, **Random Forest** delivered the best performance with the lowest MSE (1044.67).
- **Latitude** consistently emerged as the most influential variable across all tree-based models, suggesting spatial location is a strong proxy for development conditions.
- **Temperature** and **elevation** also showed meaningful impact, while **longitude** and **coastline length** contributed minimally.
- The performance of simple models like **k-NN** and **Decision Tree** confirms that even basic geographic thresholds reflect global living standard patterns.
- Models using only physical geography—without any economic or social variables—were still able to uncover clear predictive structure in the data.

---

### 🤖 Ethical Use of Generative AI

This project involved the use of generative AI tools to assist with:

- Structuring and polishing documentation (e.g., this README)
- Summarizing findings and articulating model insights
- Brainstorming next steps and research framing

All code, analysis, and model training were conducted independently by the author. AI assistance was used solely for communication, not for producing results or writing code.

---

### 🚀 Statistical Confidence & Limitations

This project’s findings are supported by consistent model performance, significant correlations, and interpretable patterns across multiple algorithms. However, like any data-driven analysis, several limitations apply:

#### ✅ Strengths
- All results are based on **cross-validation**, reducing the risk of overfitting.
- Multiple models (linear and non-linear) showed agreement on which features mattered most.
- The use of purely **geographical variables** provides a clear and narrowly scoped test of predictive power.

#### ⚠️ Limitations
- **Sample size is small**: only 103 countries with full feature coverage.
- **Geography alone** can’t explain all the variance in quality of life—important economic, cultural, and political variables were excluded to isolate the environmental effect.
- **No time dimension**: the analysis is cross-sectional, so no trends or causal pathways can be inferred.
- **Model performance is dataset-specific**: generalization to other populations may require revalidation with different regions or timeframes.

---

### 🔮 Future Research Directions

This project opens the door to several follow-up studies that could deepen or broaden the insights gained:

- **Add economic and political variables**: Incorporating GDP, education, healthcare access, or governance indices could help compare the influence of geography vs. policy.
- **Explore causal inference**: Use methods like regression with controls, instrumental variables, or longitudinal analysis to move beyond correlation.
- **Time-series analysis**: Investigate how geography-related predictors interact with life quality over time, especially in the face of climate change.
- **Regional modeling**: Build continent-specific models to test whether geographic effects differ in Europe, Asia, Africa, etc.
- **Interaction effects**: Study whether geography moderates the effect of other variables (e.g., “is economic growth less effective in high-temperature regions?”).
- **Granular data**: Expand the dataset to include subnational or city-level analysis where environmental differences are even more pronounced.

These next steps could turn a simple correlation study into a full framework for understanding how location shapes life conditions in a changing world.
