import re

pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

match = pattern.match("192.168.0.1")

if match is not None:
    print(match[0])

else:
    print("errado!")