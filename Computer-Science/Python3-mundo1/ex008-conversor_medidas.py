meter = float(input("Ente the measure: "))
print("""Meter: {}
Milimeters: {:.0f}
Centimeters: {:.0f}
Decimeters: {:.0f}
Decameters: {}
Hectometers: {}
Kilometers: {}

""".format(meter, meter * 1000, meter * 100, meter * 10, meter / 10, meter / 100, meter / 1000)
)