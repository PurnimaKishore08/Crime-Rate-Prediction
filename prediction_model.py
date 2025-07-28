### ✅ 3. `prediction_model.py`

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def predict_crime_rate(df, state):
    df_state = df[df['State/UT'] == state]
    data = df_state[[col for col in df.columns if col.isdigit()]].T.squeeze()
    data.index = pd.to_datetime(data.index, format='%Y')
    model = ARIMA(data, order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=1)
    return forecast.iloc[0]