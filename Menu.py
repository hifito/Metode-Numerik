ordo = int(input("Masukkan ordo matrix : "))
baris = ordo
kolom = ordo+1

A = []
for i in range(baris):
    matrix=[]
    for j in range(kolom):
        matrix.append(0)
    A.append(matrix)

for i in range(baris):
    print("Masukkan persamaan ke-%d" % (i + 1))
    for j in range(0, kolom):
        A[i][j] = int(input(f"Masukkan angka baris-{i+1} kolom-{j+1}: "))

for i in range(baris):
    diag = A[i][i]
    for j in range(kolom):
        A[i][j] /= diag
    for k in range(i + 1, kolom):
        if k != baris:
            diag1 = A[k][i]
            for j in range(0, kolom):
                A[k][j] = A[k][j] - diag1 * A[i][j]

for i in range(0, baris):
    for j in range(0, kolom):
            print("%4.2f" % (A[i][j]), end=" ")
    print("\n")

x3 = A[2][3]
x2 = A[1][3] - A[1][2]*x3
x1 = A[0][3] - A[0][2]*x3 - A[0][1]*x2
print("x1= %4.2f \nx2= %4.2f \nx3= %4.2f" % (x1, x2, x3))
