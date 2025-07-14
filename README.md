
# 🔋 CU-BEMS Energy Forecasting

This project focuses on forecasting hourly building energy consumption using the **CU-BEMS (Chulalongkorn University Building Energy Management System)** dataset. We compare various deep learning models such as CNN-GRU, CNN-LSTM, and Bidirectional GRU, along with traditional linear regression methods.

---

## 📊 Dataset: CU-BEMS

**CU-BEMS** is a real-world dataset that captures energy consumption data from a university building. The dataset includes:

- Per-floor electrical usage in kilowatts (kW)
- High-resolution timestamps (minute-level)
- Data collected from 7 floors (Floor1–Floor7)
- Time range: **July 2018 to December 2019**

### 🔧 Preprocessing Steps

- **Date conversion** and invalid date removal
- **Hourly aggregation** of minute-level readings
- **Missing values** filled using forward and backward fill
- **Feature engineering**:
  - Hour of day
  - Day of week
  - Month
- **Z-score normalization** using `StandardScaler`

---

## 🧠 Models Compared

| Model                           | Type            | Input Type   |
|--------------------------------|------------------|--------------|
| CNN-GRU Hybrid                 | Deep Learning    | Multivariate |
| CNN-GRU                        | Deep Learning    | Univariate   |
| CNN-LSTM                       | Deep Learning    | Uni/Multivariate |
| Bidirectional GRU             | Deep Learning    | Multivariate |
| Linear Regression             | Traditional ML   | Uni/Multivariate |

---

## 📈 Evaluation Metrics

We used the following metrics to evaluate model performance:

- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)
- **R² Score** (Coefficient of Determination)

---

## ✅ Results Summary

| Model                           | MAE    | RMSE   | R² Score |
|--------------------------------|--------|--------|----------|
| CNN-GRU Hybrid Multivariate    | **953.6**  | **2303.9** | **0.920**   |
| CNN-GRU Univariate             | 872.9  | 3058.4 | 0.878    |
| Linear Regression Multivariate | 1156.8 | 3008.9 | 0.878    |
| Linear Regression Univariate   | 1204.8 | 3016.7 | 0.880    |
| CNN-LSTM Univariate            | 895.1  | 3064.1 | 0.859    |
| CNN-LSTM Multivariate          | 918.5  | 2558.2 | 0.914    |
| Bidirectional GRU Multivariate | 997.0  | 2386.8 | 0.914    |

---

## 📊 Visualizations

### MAE Comparison
![MAE Comparison](./output/mae_comparison.png)

### RMSE Comparison
![RMSE Comparison](./output/rmse_comparison.png)

### R² Score Comparison
![R2 Score Comparison](./output/r2_score_comparison.png)

### Actual vs Predicted (Example)
![Actual vs Predicted](./output/actual_vs_predicted.png)

---

## 🛠️ Technologies Used

- Python 3
- Pandas, NumPy
- Scikit-learn
- PyTorch / TensorFlow
- Matplotlib, Seaborn
- Google Colab

---

## 📁 Folder Structure

```

CU\_BEMS\_Energy\_Forecasting/
│
├── data/
│   ├── 2018Floor1.csv
│   ├── ...
│
├── models/
│   ├── cnn\_gru.py
│   ├── cnn\_lstm.py
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── Training\_Evaluation.ipynb
│
├── output/
│   ├── mae\_comparison.png
│   ├── rmse\_comparison.png
│   ├── r2\_score\_comparison.png
│   ├── actual\_vs\_predicted.png
│
├── utils/
│   └── preprocessing.py
│
└── README.md



---

## ✍️ Author

This project was built using real energy data to demonstrate forecasting methods in smart buildings using deep learning.
