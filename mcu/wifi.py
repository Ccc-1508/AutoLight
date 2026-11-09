import network
import time
import config

class WiFi:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self, max_retry=3, wait_timeout=10) -> bool:
        self.wlan.active(True)

        for _ in range(max_retry):
            self.wlan.connect(config.SSID, config.PASSWORD)
            if self.wlan.isconnected(): return True
            for _ in range(wait_timeout):
                if self.wlan.isconnected():
                    return True
                time.sleep(1)
        return False

    def clear(self) -> None:
        try:
            self.wlan.disconnect()
        except OSError:
            pass
        self.wlan.active(False)

    def status(self) -> bool:
        return self.wlan.isconnected()

    def ip(self) -> str:
        return self.wlan.ifconfig()[0]