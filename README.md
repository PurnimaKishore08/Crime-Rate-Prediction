# 🔐 Crime Rate Prediction Dashboard

An interactive and intelligent web-based dashboard to **analyze, visualize, and predict** crime trends across Indian states/UTs using historical data and AI models. Built using **Streamlit**, this tool empowers users with insightful visualizations and accurate predictions.

---

## 📌 Features

- 📊 **Trend Analysis**: Year-wise crime rate line graph for each state/UT  
- 🌡️ **Heatmap**: Visual crime intensity map across years and regions  
- 📉 **Bar Chart**: Total crimes per state/UT comparison  
- 🥧 **Pie Chart**: Crime distribution in the latest year  
- 🔮 **AI-Based Prediction**: Forecast next year's crime rate using ARIMA  
- 📁 **CSV Upload**: Load your own dataset for dynamic predictions  
- 🖥️ **Responsive UI**: Clean, modern layout that works on desktop & mobile  

---

## 📷 Demo

![App Screenshot](demo.gif) <!-- Optional: Insert GIF or image -->

---

## 🧠 Tech Stack

- **Frontend & App**: [Streamlit](https://streamlit.io)  
- **Data Handling**: Pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn, Plotly  
- **Forecasting Model**: ARIMA from statsmodels

---

## 📂 File Structure

crime-rate-prediction/
│
├── app.py # Main Streamlit App
├── prediction_model.py # ARIMA Forecasting Logic
├── visualizations.py # All Graphs (Trend, Heatmap, Bar, Pie)
├── requirements.txt # Python Libraries
└── crime_data.csv # Sample CSV (replaceable by user)


---

## 📈 Sample Dataset Format (`crime_data.csv`)

| State/UT         | 2020   | 2021   | 2022   |
|------------------|--------|--------|--------|
| Andhra Pradesh   | 135000 | 140000 | 145000 |
| Bihar            | 120000 | 123000 | 126000 |
| ...              | ...    | ...    | ...    |

> Make sure your CSV has a **`State/UT`** column and at least 3 years of numeric data.

---

## 🚀 How to Run Locally

1. **Clone the Repo**  
   git clone https://github.com/yourusername/crime-rate-prediction.git
   cd crime-rate-prediction

2. ## Install Requirements
   pip install -r requirements.txt

3. ## Run the App
   streamlit run app.py

4. ## Upload your CSV and explore insights!

🌍 Deployment (Streamlit Cloud)
Push your project to GitHub

Go to https://share.streamlit.io

Select your repo > choose app.py > Deploy 🚀

Share the generated link with others!

📱 Mobile Friendly?
Yes! The dashboard is responsive and looks good on both desktop and mobile screens.

💡 Use Cases
Academic AI/ML projects

Government crime analysis

Data journalism

Law enforcement analytics

Research & policy making

🙋‍♀️ Author
Purnima Kishore
🎓 B.Tech | AIML Student
📫 Your Email or LinkedIn