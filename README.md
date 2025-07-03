# 🚗 Old Car Price Estimator

A machine learning-based regression project to estimate the **resale value of used cars** based on specifications like brand, engine, mileage, power, and ownership history.  
The final model is deployed as a web application using **Flask**, allowing users to input car details and get an estimated price instantly.

---

## 📊 Problem Statement

With the rapidly growing second-hand car market, it's important to estimate a fair price for used vehicles. This project aims to build a predictive system that can accurately estimate a car's selling price based on its attributes.

---

## 🗂 Dataset

- 📌 **Source:** [Car Price Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset)
- 💾 **Rows:** 8,000+
- 🧾 **Features Used:**
  - `brand`, `fuel`, `transmission`, `owner`
  - `year`, `km_driven`, `mileage`, `engine`, `max_power`, `seats`
  - `seller_type`, and more (after encoding)

---

## 🧪 Exploratory Data Analysis & Preprocessing

- Missing values handled using **mean/mode imputation**
- `max_power`, `engine`, and `mileage` cleaned and converted to numerical formats
- One-Hot Encoding applied to categorical features
- Outliers detected using distribution plots and removed for key numeric columns
- Final feature matrix was scaled for certain models

---

## 🧠 Modeling

- Several regression models were tested:
  - Linear Regression
  - Decision Tree Regressor
  - **Random Forest Regressor (Best Performance)**
- Feature importance used for selection
- Cross-validation (`ShuffleSplit`) for reliable evaluation
- Hyperparameter tuning using `GridSearchCV`

---

## 🏆 Model Performance

| Model             | Test R² Score | Notes                     |
| ----------------- | ------------- | ------------------------- |
| Linear Regression | ~0.78         | Simple but underfit       |
| Decision Tree     | ~0.81         | Slight overfitting        |
| **Random Forest** | **~0.89**     | ✅ Best performer (final) |

- Final model saved using `pickle`

---

## 🌐 Deployment

The trained model was integrated into a **Flask web application**, allowing users to enter car details like:

- Brand
- Fuel Type
- Transmission
- Mileage
- Engine (cc)
- Max Power
- Year, Ownership, Seats, etc.

➡️ On submit, the app returns a **predicted price** instantly using the trained model.

---

## 📌 Future Improvements

- Add Streamlit version for easier UI

- Integrate scraping for live car listings

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/IAmHarshit0/OldCarPriceEstimator.git

# Navigate into the folder
cd OldCarPriceEstimator

# Install dependencies
pip install -r requirements.txt

# Change Directories
cd Server

# Run the app
python server.py
```
