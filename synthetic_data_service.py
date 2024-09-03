import pandas as pd
from faker import Faker

class SyntheticDataService:
    def generate_synthetic_data(self):
        fake = Faker()
        data = []
        for _ in range(1000):
            data.append({
                'feature1': fake.random_number(),
                'feature2': fake.random_number(),
                'label': fake.random_element(elements=(0, 1))
            })
        return pd.DataFrame(data)

    def update_model(self, anomaly_detection_service):
        synthetic_data = self.generate_synthetic_data()
        anomaly_detection_service.train_model(synthetic_data)
