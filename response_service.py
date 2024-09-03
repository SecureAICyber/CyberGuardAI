class ResponseService:
    @staticmethod
    def isolate_system(ip_address):
        # Logic to isolate the system
        print(f"Isolating system with IP: {ip_address}")

    @staticmethod
    def block_traffic(ip_address):
        # Logic to block traffic from a specific IP
        print(f"Blocking traffic from IP: {ip_address}")

    @staticmethod
    def notify_security_team(threat_details):
        # Logic to notify the security team
        print(f"Notifying security team: {threat_details}")

    def automated_response(self, threat_type, ip_address):
        if threat_type == "intrusion":
            self.isolate_system(ip_address)
        elif threat_type is "malware":
            self.block_traffic(ip_address)
        self.notify_security_team({"type": threat_type, "ip": ip_address})
