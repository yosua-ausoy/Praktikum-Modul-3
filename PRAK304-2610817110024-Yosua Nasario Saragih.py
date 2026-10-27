n = int(input())

if n == 0:
 print("Nol") 
elif 1 <= n <= 9:
 print("Satuan") 
elif 10 <= n <= 19:
 print("Belasan")
elif 20 <= n <= 99: print("Puluhan")
else:
 print("Anda Menginput Melebihi Limit Bilangan")