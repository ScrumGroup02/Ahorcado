
import DarIncongnita
import PedirLetra
import MeterGuiones
import ImprimirEspaciado
import MeterLetra
import Control_LetraEnPalabra

incognitaSolucion = DarIncongnita.DarIncognita()
incognitaGuion = ""





print(incognitaSolucion)


print("")
print("")
letra = PedirLetra.PedirLetra()

print("")
print("")
print(letra)

print("")
print("")


incognitaGuion = MeterGuiones.MeterGuiones(incognitaSolucion)


ImprimirEspaciado.ImprimirEspaciado(incognitaGuion)

print("")
print("")


incognitaGuion = MeterLetra.MeterLetra(incognitaGuion,letra, Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion))

print("")
print("")
ImprimirEspaciado.ImprimirEspaciado(incognitaGuion)

print(Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion))