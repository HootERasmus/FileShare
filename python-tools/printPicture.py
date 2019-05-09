with open("../Pictures/clock.pgm", "rb") as image:
  f = image.read()
  b = bytearray(f)
  for byte in b:
      print(byte)
  