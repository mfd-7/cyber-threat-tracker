import pickle
import pandas as pd
import os
from django.conf import settings

def predict_threat(username, password):
    try:
        model_path = os.path.join(settings.BASE_DIR, 'decision_tree_model.pkl')
        with open(model_path, 'rb') as file:
            ml_model = pickle.load(file)

        # Our original model was trained on length of user and pass
        input_data = pd.DataFrame([[len(username), len(password)]], columns=['user_length', 'pass_length'])
        prediction = ml_model.predict(input_data)[0]

        if prediction == 1:
            return "High Threat"
        else:
            return "Low Threat"
    except Exception as e:
        print(f"ML Model Error: {e}")
        return "Unknown"
