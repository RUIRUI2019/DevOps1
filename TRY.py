import re
time_1='07/17/19 11:22:04'
m1 = time_1.strip().split("/")
m2=m1[2].split()
time2="20"+str(m2[0])+"-"+str(m1[0])+"-"+str(m1[1])+" "+str(m2[1])
