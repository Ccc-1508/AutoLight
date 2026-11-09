import machine

# 初始化 GPIO2 为输出（大多数 ESP32 开发板的板载 LED 接在 GPIO2）

if connected:
    blue_light = machine.PWM(machine.Pin(2), freq=1000)
    blue_light.duty(10)