"""Un cerrojo con combinaci?n tiene las siguientes propiedades b?sicas: la combinaci?n (una secuencia de tres n?meros); el cerrojo se puede abrir proporcionando la combinaci?n; y la combinaci?n se puede cambiar, pero solamente por alguien que conoce la combinaci?n actual. Dise?e una clase con m?todos abrir, cerrar y cambiar_combinacion, y atributos para almacenar la combinaci?n y el estado de la puerta, cerrada o abierta. La combinaci?n deber?a asignarse en el constructor."""

class Cerrojo:
	"""Representa un cerrojo que permite abrir y cerrar una puerta dada una combinacion de 3 nros."""

	def __init__(self, combinacion):
		self.combinacion = combinacion
		self.abierto = False

	def __repr__(self):
		return "El cerrojo esta " + str(self.abierto)

	def abrir(self, combinacion):
		if (combinacion == self.combinacion):
			self.abierto = True
			return True
		return False

	def cerrar(self):
		self.abierto = True

	def cambiar_combinacion(self, combinacion):
		self.combinacion = combinacion

if __name__ == "__main__":
	c = Cerrojo([1,2,3])
	print c
