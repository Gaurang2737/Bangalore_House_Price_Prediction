# 🏠 Bangalore House Price Prediction

A full-stack Machine Learning web application that predicts housing prices in Bangalore using Linear Regression.  
This project covers data preprocessing, feature engineering, EDA, model training, and deployment using Flask.

---

## 🚀 Demo

👉 **Live App**: https://bangalore-house-price-prediction-glpl.onrender.com/

---

## 📌 Features

- 📊 **Performed detailed Exploratory Data Analysis (EDA)**
- 🧹 **Cleaned and transformed real-world housing data**
- 🧠 **Built a Linear Regression model for price prediction**
- 💡 **Feature engineering based on location, BHK, square footage, etc.**
- 🌐 **Developed a REST API using Flask**
- 🎨 **Designed a responsive frontend using HTML, CSS, JS**
- ☁️ **Deployed using Render and monitored via UptimeRobot**

---

## 🛠 Tech Stack

**Languages**: Python, HTML/CSS, JavaScript  
**Libraries**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn  
**Framework**: Flask  
**Deployment**: Render  
**Monitoring**: UptimeRobot

---

## 📁 Project Structure

```text
House_price_prediction/
│
├── Model/
│   ├── Bengaluru_price_prediction.ipynb   # EDA, preprocessing, modeling
│   ├── Bengaluru_House_Data.csv           # Dataset
│   └── bengaluru_home_price_model.pkl     # Trained model
│
├── Server/
│   ├── server.py                          # Flask backend
│   ├── util.py                            # Helper functions
│   ├── templates/
│   │   └── app.html                       # HTML frontend
│   └── static/
│       ├── app.css                        # Styles
│       └── app.js                         # Frontend logic
│
├── requirements.txt                       # Python dependencies
└── Procfile                               # Render deployment config
```

---

## 🧑‍💻 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/Gaurang2737/Bangalore_House_Price_Prediction.git
cd Bangalore_House_Price_Prediction

2. **Create a virtual environment and activate it**

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask server**

```bash
cd Server
python server.py
```

5. **Open in browser**

Go to: `http://127.0.0.1:5000/`

---


## 📬 Contact

For any questions or feedback, feel free to reach out:

**Gaurang Sane**  
📧 [LinkedIn](linkedin.com/in/gaurang-sane-84b5b1254)  
📫 Email: gaurangtech9@gmail.com

---

## ⭐ Show Your Support

If you like this project, don’t forget to ⭐ the repo!




