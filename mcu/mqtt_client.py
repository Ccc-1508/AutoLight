import umqtt.simple
import time

class MQTTManager:
    def __init__(self, client_id, server, port=1883, user="", password="", keepalive=60, ssl=False):
            self.online = False
            self.client = umqtt.simple.MQTTClient(
                client_id=client_id,
                server=server,
                port=port,
                user=user or None,
                password=password or None,
                keepalive=keepalive,
                ssl=ssl,
            )

    def connect(self, clean_session=True) -> bool:
        try:
            self.client.connect(clean_session)
            self.online = True
            return True
        except Exception:
            self.online = False
            return False

    def disconnect(self):
        try:
            self.client.disconnect()
        except Exception:
            pass
        self.online = False

    def publish(self, topic, msg, retain=False, qos=0):
        if not self.online:  return False
        try:
            self.client.publish(topic, msg, retain, qos)
            return True
        except Exception:
            self.online = False
            return False

    def subscribe(self, topic, qos=0):
        try:
            self.client.subscribe(topic, qos)
            return True
        except Exception:
            self.online = False
            return False

    def unsubscribe(self, topic, qos=0):
        try:
            self.client.unsubscribe(topic)
            return True
        except Exception:
            self.online = False
            return False

    def set_callback(self, func):
        self.client.set_callback(func)

    def set_last_will(self, topic, msg, retain=False, qos=0):
        self.client.set_last_will(topic, msg, retain, qos)

    def check_msg(self):
        try:
            self.client.check_msg()
            return True
        except Exception:
            self.online = False
            return False

    def ping(self):
        try:
            self.client.ping()
            return True
        except Exception:
            self.online = False
            return False