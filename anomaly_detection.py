from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

class EnhancedAnomalyDetectionService:
    def __init__(self):
        self.model = Sequential([
            Dense(64, activation='relu', input_shape=(10,)),  # Assuming 10 features
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train_model(self, data_path):
        df = pd.read_csv(data_path)
        X = df.drop(columns=['label'])
        y = df['label']
        self.model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

    def detect_anomaly(self, data):
        df = pd.read_csv(data)
        predictions = self.model.predict(df)
        return predictions
