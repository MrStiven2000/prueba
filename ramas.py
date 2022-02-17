# este programa esta hecho para el cuidado de los pollos
# variables
sensorNivel=3
SensorDeAgua=("bajo")
SensorFotoResistencia=("dia")
SensorDeMovimiento=("sin detectar")
Resistencia=("0") 
# sensor de temperatura
if sensorNivel==5:
    print("el pollo tine una temperatura estable")
if  sensorNivel>=16:
    print("alerta el nivel de temperatura de los pollos subio a 16")
if  sensorNivel<=3:
    print("error, los pollos tienen temperatura baja")
# sensor de agua
if SensorDeAgua ==("normal"):
    print("el nivel de agua esta correctamente, es de 200 litros")
if SensorDeAgua==("mayor"):
    print("error, el agua consumible de los pollos es de 300 litros")
if SensorDeAgua <=("bajo"):
    print("alerta, el agua de los pollos es muy poca, es de 100 litros")