def v(s, t):
  speed = s / t
  return speed;

v1 = v(100, 1)
v2 = v(50, 2)
v3 = v(67, 0.7)
print(f'velocity 1: {v1}')
print(f'velocity 2: {v2}')
print(f'velocity 3: {v3}')

# Начало задания round(number, digits=0)
# avarage funcion
def avarage(speed1, speed2):
    middlevelocity = round((speed1 + speed2) / 2, 2)
    return str(middlevelocity) + ' km/h';

#  pass
# str(arg) int(arg) int(1213)
# результат среденй скорости v1 и v2
avarage1 = str(avarage(v1, v2))
# результат среденй скорости v1 и v3
avarage2 = avarage(v1, v3)
# результат среденй скорости v2 и v3
avarage3 = avarage(v2, v3)

print(f'avarage 1 velocity: {avarage1}')
print(f'avarage 2 velocity: {avarage2}')
print(f'avarage 3 velocity: {avarage3}')