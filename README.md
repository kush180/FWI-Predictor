# 🔥 Forest Fire Weather Index (FWI) Predictor

A Flask web application that predicts the **Fire Weather Index (FWI)** using machine learning, trained on the Algerian Forest Fires dataset.

---

## 📌 About the Project

This project builds an end-to-end ML pipeline to predict the FWI — a numeric rating of fire intensity — based on meteorological and fire danger index inputs. The app takes user inputs through a web form and returns a predicted FWI value in real time.

---

## 📂 Dataset

**Name:** Algerian Forest Fires Dataset  
**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++)

The dataset contains fire observations collected from **two regions of Algeria** between **June and September 2012**:

| Region | Location |
|--------|----------|
| 0 | Bejaia Region (northeast Algeria) |
| 1 | Sidi Bel-Abbes Region (northwest Algeria) |

### Features

| Feature | Description | Type |
|---------|-------------|------|
| Temperature | Temperature at noon (°C) | Integer |
| RH | Relative Humidity (%) | Integer |
| Ws | Wind Speed (km/h) | Integer |
| Rain | Daily rainfall (mm) | Float |
| FFMC | Fine Fuel Moisture Code | Float |
| DMC | Duff Moisture Code | Float |
| ISI | Initial Spread Index | Float |
| Classes | Fire / Not Fire | Binary (0/1) |
| Region | Bejaia / Sidi Bel | Binary (0/1) |

**Target Variable:** `FWI` (Fire Weather Index) — a continuous value representing fire danger level.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML Libraries:** Scikit-learn, NumPy, Pandas
- **Frontend:** HTML, CSS
- **Model Persistence:** Pickle

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fwi-predictor.git
cd fwi-predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:5000
```

---

## 📁 Project Structure

```
fwi-predictor/
│
├── app.py                  # Flask application
├── model.pkl               # Trained ML model
├── scaler.pkl              # Feature scaler
├── templates/
│   ├── home.html           # Home page
│   └── form.html           # Prediction form
├── notebook/
│   └── FWI_model.ipynb     # Model training notebook
└── README.md
```

---

## 📊 Model

The model is trained using regression on the FWI target variable. Input features are scaled using `StandardScaler` before prediction.

---

## 📄 License

This project is for educational purposes. Dataset credit: Faroudja ABID et al., UCI ML Repository.