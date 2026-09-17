import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = {
    'user_length': [5, 10, 4, 12, 5, 3, 15, 4],
    'pass_length': [3, 12, 4, 14, 5, 2, 10, 1],
    'is_hacker':   [1, 0,  1, 0,  1, 1, 0,  1]  
}

df = pd.DataFrame(data)

X = df[['user_length', 'pass_length']]
y = df['is_hacker']

print("Model Training Started...")
model = DecisionTreeClassifier()
model.fit(X, y)

with open('decision_tree_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Decision Tree Model Successfully Trained and Saved!")