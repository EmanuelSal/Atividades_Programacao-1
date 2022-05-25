a = int(input())
b = int(input())
c = int(input())
d = int(input())
 
a_str = str(a)
b_str = str(b)
c_str =str(c)
d_str = str(d)

dc = d_str + c_str
ca = c_str + a_str
bb = b_str + b_str
aad = a_str + a_str + d_str

calculo = int(dc) - a - b - int(ca) - d + int(bb) + int(aad)

print(calculo)