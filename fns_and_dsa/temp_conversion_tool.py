# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
	global FAHRENHEIT_TO_CELSIUS_FACTOR
	
	"""Convert Fahrenheit to Celsius using the global factor."""
	return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
	global CELSIUS_TO_FAHRENHEIT_FACTOR
	
	"""Convert Celsius to Fahrenheit using the global factor."""
	return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
	try:
		temp_input = input("Enter the temperature value: ")
		temp_value = float(temp_input)
		scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
		if scale == 'C':
			converted = convert_to_fahrenheit(temp_value)
			print(f"{temp_value}°C is {converted:.2f}°F")
		elif scale == 'F':
			converted = convert_to_celsius(temp_value)
			print(f"{temp_value}°F is {converted:.2f}°C")
		else:
			raise ValueError("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
	except ValueError as e:
		print(f"Invalid temperature. Please enter a numeric value. ({e})")

