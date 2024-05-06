from temperature_converter import TemperatureConverter

if __name__ == "__main__":
  f = TemperatureConverter.celsius_to_fahrenheit(35)
  print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))
