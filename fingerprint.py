import time
import colorsys

colors = ['red', 'green', 'blue',]
print ("""
      /      Fingerprint Scanner           /
     /____________________________________/
""")


input("Place your finger on the scanner and press Enter to continue... : ")

steps = ['Scanning.', 'Reading your biometrics...', 'Analyzing data...', 
         'Verifying identity...' , 'Access Granted! Welcome back!']

for step in steps:
    print(step.center(40))
    time.sleep(1.5)