import math


def mul(mass,velocity):
	momentum = mass*velocity
	return momentum

def output(name, momentum1, mass, velocity, momentum):
	return """
Hey {}!
The momentum of the ball is {}
To find the momentum of the ball you'll need to times the mass of the ball by its velocity: {} * {} = {}
""".format(name, momentum1, mass, velocity, momentum)

def main():
	name= raw_input ("What is you name?:")
	mass = raw_input("Type in the mass of the ball: ")
	velocity = raw_input("Type in the velocity of the ball: ")
	momentum = mul(int(mass), int(velocity))
	print output(name, momentum, mass, velocity, momentum)
main()

