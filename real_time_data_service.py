from kafka import KafkaConsumer
import pandas as pd
from src.cyberguardai.anomaly_detection_service import EnhancedAnomalyDetectionService
from src.cyberguardai.response_service import ResponseService

class RealTimeDataService:
    def __init__(self):
        self.consumer = KafkaConsumer('threats', bootstrap_servers=['localhost:9092'])
        self.anomaly_detection_service = EnhancedAnomalyDetectionService()
        self.response_service = ResponseService()

    def process_data_stream(self):
        for message in self.consumer:
            data = pd.read_json(message.value)
            prediction = self.anomaly_detection_service.detect_anomaly(data)
            if prediction > 0.5:
                self.trigger_response(data)

    def trigger_response(self, data):
        self.response_service.automated_response("intrusion", data['ip_address'])
