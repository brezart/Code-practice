print("input height of jar")
h_jar = float(input())
print("input diameter of jar")
d_jar = float(input())

d_lifesaver = 1.0
h_lifesaver = 0.3

lifeSaversPerJar = ((d_jar ** 2) /(d_lifesaver ** 2)) * (h_jar / h_lifesaver)

print(lifeSaversPerJar)
