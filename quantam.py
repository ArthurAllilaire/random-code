import math
import csv

delta_x = 0.1
x = 0
d1 = 10
d2 = 7
width = 12
n = 1.5
#Speed of light in cm/second
s = 3*(10**10)
#In cm
w1 = 500*(10**-7)
w2 = w1/n

# l1 = (x**2 + d1**2)**0.5
# l2 = ((width-x)**2 + d2**2)**0.5
# # Remainder of the wave left to do
# phasor_l1 = round((l1%w1)/w1,5)

# # print("Phasor 1", phasor_l1)
# # print(l1, l2, w1, w2, l1%w1)
# phasor_l2 = round(((l2+(phasor_l1*w2))%w2)/w2,5)    
# #print(phasor_l2)
# t = l1/s + l2/(s/n)
# phasor = round(2*math.pi*(phasor_l1 + phasor_l2),5)
# print(phasor)
# sin_theta = math.sin(phasor)
# cos_theta = math.cos(phasor)


header = ["x", "time", "Phasor", "Sin_theta", "Cos_theta"]

with open('new_results.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for i in range(int(width/delta_x)):
    x += delta_x
    l1 = (x**2 + d1**2)**0.5
    l2 = ((width-x)**2 + d2**2)**0.5
    # Remainder of the wave left to do
    phasor_l1 = round((l1%w1)/w1,5)

    #print(l1, l2, w1, w2, l1%w1)
    phasor_l2 = round(((l2+(phasor_l1*w2))%w2)/w2,5)    
    
    t = l1/s + l2/(s/n)
    
    phasor = round((phasor_l1 + phasor_l2)/(2*math.pi),5)
    print(phasor)
    sin_theta = math.sin(phasor)
    cos_theta = math.cos(phasor)

    #print(sin_theta, cos_theta)

    writer.writerow([x, t, phasor, sin_theta, cos_theta])
