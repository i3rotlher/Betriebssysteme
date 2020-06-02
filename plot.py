import matplotlib.pyplot as plt

file = open("data.txt","r")

data = []
Line = file.readline() #1 1
data.append(int(Line))
Line = file.readline() #2 2
Line = file.readline() #3 4
data.append(int(Line))
Line = file.readline()
Line = file.readline() #5 16
data.append(int(Line))
Line = file.readline()
Line = file.readline() #7 64
data.append(int(Line))
Line = file.readline()
Line = file.readline() #9 256
data.append(int(Line))
Line = file.readline()
Line = file.readline() #11 1024
data.append(int(Line))
Line = file.readline() #12 2048
data.append(int(Line))
Line = file.readline() #12 4096
data.append(int(Line))



names = ["1","4","16","64","256"," 1024", 2048, 4096]
plt.title("TLB Size Measurement")
plt.plot(names, data)
plt.ylim(0,200)
plt.ylabel("Time Per Access (ns)")
plt.xlabel("Number Of Pages")
plt.show()