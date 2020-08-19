#!/usr/bin/python
from gpiozero import LED

codes = {
        "2963": LED(20),
        "8246": LED(21)
}

for pin in codes:
    codes[pin].off()

while True:
    val = ""
    try:
        val = input()
    except Exception as e:
        print("no input")
    pin = codes.get(val)
    if pin is not None:
        pin.on()
        print("on")
    else:
        print("no match")
