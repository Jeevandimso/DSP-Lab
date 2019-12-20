import numpy as ak
r=input("no.of Rows=")
c=input("no.of columns=")
m=[]
for i in range(r):
	m.append([0]*c)
for j in range(r):
	for k in range(c):
		print("enter the elements in matrix=",[j+1,k+1])
		m[j][k]=int(input())
print("The Matrix is=")
print(ak.matrix(m))
er="\t\t\t*********   99.EXIT   no operation perform    *********\n\t\t\t*********   1.Determinant   *********\n\t\t\t*********   2.Transpose   *********\n\t\t\t*********   3.Inverse   *********\n\t\t\t*********   4.Eigenvalues   *********\n\t\t\t*********   5.Trace   *********\n\t\t\t*********   6.Matrix based to Power   *********\n\t\t\t*********   7.Norm   *********\n\t\t\t*********   8.Rank of Matrix   *********\n\t\t\t*********   9.Pseudo Inverse   *********\n\t\t\t*********   10.Maximum and Minimim of Matrix   *********\n"
print(er)
while True:
	d=input("\nENTER THE OPERATION=")
	if d==1:
		if r==c:
			print("\nDETERMINANT OF MATRIX IS="),
			print(ak.linalg.det(m))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==2:
		print("\nTRANSPOSE OF MATRIX IS=")
		print(ak.transpose(m))
	elif d==3:
		if r==c:
			print("\nINVERSE MATRIX IS=")
			print(ak.linalg.inv(m))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==4:
		if r==c:
			print("\nEIGEN VALUES=")
			print(ak.linalg.eigvals(m))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==5:
		if r==c:
			print("\nTRACE OF MATRIX IS="),
			print(ak.trace(m))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==6:
		if r==c:
			p=input("ENTER POWER=")
			print("\nTHE RESULT MATRIX IS=")
			print(ak.linalg.matrix_power(m,p))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==7:
		print("\nNORM OF MATRIX IS=")
		print(ak.linalg.norm(m))
	elif d==8:
		 print("\nRANK OF THE GIVEN MATRIX IS=")
		 print(ak.linalg.matrix_rank(m))
	elif d==9:
		print("\nPSEUDO INVERSE OF MATRIX IS=")
		print(ak.linalg.pinv(m))
	elif d==10:
			print("MAXIMUM IN MATRIX=")
			print(ak.max(m))
			print("MINIMUM IN MATRIX=")
			print(ak.min(m))
	elif(d==99):
		print("\nPROGRAM ENDED")
		break

	else:
		print("ENTER VALID OPTION")

	
 
