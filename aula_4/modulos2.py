import datetime

agora = datetime.datetime.now()
print(agora)
data_nasc = datetime.datetime.now(1997, 2 ,21, 11, 11, 0)

delta = agora - data_nasc

print(delta)
print(delta.total_seconds())