import machine

class StatusLED:
    def __init__(self, pin=2, duty=10, period_ms=1500):
        self.led = machine.PWM(pin, freq=1000)
        self.duty = duty
        self.enabled = True
        self.led.duty(self.duty)
        self.timer = machine.Timer(0)
        self.timer.init(period=period_ms, mode=machine.Timer.PERIODIC,callback=self._toggle)

    def _toggle(self, t):
        if not self.enabled:
            self.led.duty(0)
            return
        self.led.duty(0 if self.led.duty() > 0 else self.duty)

    def on(self):
        self.enabled = True
        self.led.duty(self.duty)

    def off(self):
        self.enabled = False
        self.led.duty(0)