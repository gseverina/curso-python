class Persona:
	def __init__(self,nombre):
		self.nombre = nombre

	def __repr__(self):
		return str(self.nombre)

def upper_name(self):
	return (self.nombre).upper()

if __name__ == "__main__":
	p = Persona("Pepo")
	c = Persona("Coti")
	print p
	print c
	p.upper_name = upper_name
	print p.upper_name(p)
	#print c.upper_name(c)
