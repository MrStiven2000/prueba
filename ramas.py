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
    print("alerta, el agua de los pollos es baja, es de 100 litros")
# sensor de luz 
if SensorFotoResistencia ==("dia"):
   print("la puerta se ha abierto ya se hizo de dia")
if SensorFotoResistencia ==("noche"):
   print("las puertas se ceraron, los pollos estan adentro")
# sensor de movimientos hostiles
if SensorDeMovimiento ==("detectando"):
   print("se detecta movimiento de un gato, metiendo a los pollos")
if SensorDeMovimiento ==("sin detectar"):
   print("no se detectan movimientos de otros animales")
# sensor de calefaccion
if Resistencia ==("0") and SensorFotoResistencia==("dia"):
    print("la temperatura esta apagada y la puerta esta abierta")
if Resistencia ==("1") and SensorFotoResistencia==("noche"):
   print("la temepratura esta encendida y las puertas se cerraron")