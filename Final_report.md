# DSA210 Final Project Report

## Abstract

This project explores whether geographic features—such as latitude, temperature, and elevation—can meaningfully predict a country’s quality of life. Using data from 103 countries, I merged environmental metrics (including average climate, elevation, and proximity to coastlines) and applied machine learning models to investigate whether geography alone can explain living standard variations.

Correlation analysis revealed that:

* Latitude (r = 0.45), Temperature (°C) (r = –0.44), and Elevation (m) (r = –0.36) have statistically significant associations with quality of life.
* Longitude and coastline length showed no meaningful relationship.

Several classification models were trained, including k-Nearest Neighbors, Decision Trees, Random Forests, and XGBoost, to predict the Quality of Life Category. The best performance came from a Random Forest model using Leave-One-Out Cross Validation (LOO-CV), which achieved a mean MSE of 1044.67. This indicates that geography alone provides modest but nontrivial predictive power.

XGBoost’s feature importance results further emphasized the role of spatial variables in predicting quality of life. Latitude was by far the most influential predictor, followed by sub-region encoding, temperature, and longitude. Elevation and coastline length contributed less to the model’s decisions.

These findings suggest that even in the absence of economic or political data, natural geography can serve as a useful predictor of national well-being. Regional and latitudinal factors appear particularly important, pointing to broader spatial patterns worthy of further investigation.

## 1. Introduction

### Motivation

This project was inspired by a broader question: can geography alone explain or predict how well people live in different countries? While most discussions around development focus on economic or political conditions, I wanted to test whether purely environmental data could already provide some predictive power.

### Research Questions

* Do geographical features significantly impact living standards?
* Which geographical factors show the strongest correlations with quality of life?
* Can we build a predictive model of living standards using only geography-related features?

### Hypothesis

* Null Hypothesis (H₀): Geographical features have no significant relationship with living standards.
* Alternative Hypothesis (Hₐ): Certain geographical features significantly influence living standards.

## 2. Data Collection and Preprocessing

### Sources

* Primary Dataset: Kaggle - "Quality of Life for Each Country"
* Supplementary Geographical Data:

  * Average Annual Temperature
  * Elevation (meters)
  * Latitude and Longitude
  * Coastline length from World Factbook/WRI

### Final Dataset

* 103 countries
* Features:

  * Latitude, Longitude
  * Elevation (m)
  * Coastline length (weighted factor)
  * Average temperature (C)
  * Sub-region (encoded)
  * Quality of Life Score and Category (label)

### Cleaning Steps

* Harmonized country names across sources
* Dropped rows with missing data
* Encoded sub-regions numerically

## 3. Methods

### Statistical Analysis

* Pearson correlation coefficients were computed between geographic features and the Quality of Life value.
* P-values and permutation testing were used to confirm significance.

### Machine Learning Models

* **k-Nearest Neighbors (KNN)**
* **Decision Tree Classifier**
* **Random Forest Classifier**
* **XGBoost Classifier**

### Validation Techniques

* Train/Test split
* K-Fold Cross Validation (k = 5)
* Leave-One-Out Cross Validation (LOO-CV)

### Evaluation Metrics

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)
* R-squared (R²)

## 4. Results

### Correlation Analysis

| Variable         | Pearson r | p-value (perm.) |
| ---------------- | --------- | --------------- |
| Latitude         | 0.448     | < 0.001         |
| Temperature (°C) | -0.440    | < 0.001         |
| Elevation (m)    | -0.362    | 0.0001          |
| Coastline length | 0.106     | 0.278           |
| Longitude        | -0.014    | 0.893           |

### Model Performance (Best MSE Values)

| Model         | Validation Method | Best Mean MSE |
| ------------- | ----------------- | ------------- |
| KNN           | Train/Test Split  | 1222          |
| Decision Tree | LOO-CV            | 1149          |
| Random Forest | LOO-CV            | **1044.67**   |
| XGBoost       | LOO-CV            | 1124          |

### Feature Importance (XGBoost)

Top contributing features:

1. Latitude
2. Sub-region (encoded)
3. Temperature
4. Longitude
5. Coastline length
6. Elevation

Latitude stood out as the most informative predictor, with other spatial features contributing to varying degrees.

## 5. Discussion

The statistical and ML analysis shows that geography plays a detectable but limited role in determining living standards. Latitude, in particular, stands out as a robust predictor, potentially due to its association with climate and global development patterns.

Despite the absence of direct economic or governance indicators, models trained on just six geographical features could predict quality-of-life categories with decent accuracy, especially under leave-one-out validation.

## 6. Limitations

* Dataset size is small (n = 103 countries)
* Only a subset of possible environmental variables was included
* No economic, political, or social indicators were considered
* Causal conclusions cannot be drawn from correlation and predictive performance alone

## 7. Conclusion and Future Work

Geography alone offers some predictive value in estimating the quality of life across countries. While not sufficient to explain all variance, geographic factors like latitude, temperature, and elevation do show consistent statistical and predictive relationships with well-being scores.

Future work may include:

* Incorporating economic, health, and governance indicators
* Running time-series or longitudinal studies
* Performing region-specific clustering and analysis
* Testing models on larger, more granular datasets

The results support the idea that where we live matters—sometimes in ways that are deeply encoded in the land itself.
