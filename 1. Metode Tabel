class fungsi:
    def __init__(self, aa, bb, cc):
        self.aa = aa
        self.bb = bb
        self.cc = cc

    def fx(self, x):
        return self.aa*x**2 + self.bb*x + self.cc

print("ax^2 + bx + c\n")
aa = float(input("masukan nilai a: "))
bb = float(input("masukan nilai b: "))
cc = float(input("masukan nilai c: "))

print(f"\nfungsi: ({aa})x^2 + ({bb})x + ({cc})\n")

def tabel(aa, bb, cc):
    masuk = fungsi(aa, bb, cc)
    a = float(input("Masukkan batas bawah: "))
    b = float(input("Masukkan batas atas: "))
    n = int(input("Masukkan banyak iterasi: "))
    h = (b - a) / n

    print ("\nLoop\tx1\t\tx2\t\tf(x1)\tf(x2)\tf(x1)*f(x2)")

    for i in range(0, n):
        x1 = a + i*h
        x2 = a + (i+1)*h
        y1 = masuk.fx(x1)
        y2 = masuk.fx(x2)
        print("%d\t\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" % (i+1, x1, x2, y1, y2, y1*y2))
        if y1*y2 <= 0:
            break

    if (i+1) == n:
        print("\nHasil tidak ditemukan")
    else:
        if abs(y1) < abs (y2):
            return x1
        else:
            return x2
     
tabel(aa, bb, cc)
