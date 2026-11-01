import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

# 1. Buat data dummy
X_dummy = np.random.rand(100, 4)
y_dummy = np.random.randint(0, 2, size=100)

# 2. Fit Scaler & Model
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_dummy)

model = XGBClassifier(n_estimators=10, max_depth=3)
model.fit(X_scaled, y_dummy)

# 3. Simpan file pkl
joblib.dump(model, 'best_xgboost_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("✅ File 'best_xgboost_model.pkl' & 'scaler.pkl' berhasil dibuat!")