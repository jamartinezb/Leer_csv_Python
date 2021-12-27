import pandas as pd

df = pd.read_csv("archivos.csv")

data = df.values

# for i in data:
if data[1, 2] == 1:
    suma1 = data[0, 1]+data[1, 1]+data[2, 1]+data[3, 1]
    vPorc1 = data[0, 1]/suma1
    vPorc2 = data[1, 1]/suma1
    vPorc3 = data[2, 1]/suma1
    vPorc4 = data[3, 1]/suma1
    print(1, vPorc1,vPorc2,vPorc3,vPorc4, suma1)
if data[5, 2] == 2:
    suma2 = data[4, 1]+data[5, 1]+data[6, 1]+data[7, 1]
    vPorc1 = data[4, 1]/suma2
    vPorc2 = data[5, 1]/suma2
    vPorc3 = data[6, 1]/suma2
    vPorc4 = data[7, 1]/suma2
    print(2, vPorc1,vPorc2,vPorc3,vPorc4, suma2)
if data[9, 2] == 3:
    suma3 = data[8, 1]+data[9, 1]+data[10, 1]+data[11, 1]
    vPorc1 = data[8, 1]/suma3
    vPorc2 = data[9, 1]/suma3
    vPorc3 = data[10, 1]/suma3
    vPorc4 = data[11, 1]/suma3
    print(3, vPorc1,vPorc2,vPorc3,vPorc4, suma3)
if data[13, 2] == 4:
    suma4 = data[12, 1]+data[13, 1]+data[14, 1]+data[15, 1]
    vPorc1 = data[12, 1]/suma4
    vPorc2 = data[13, 1]/suma4
    vPorc3 = data[14, 1]/suma4
    vPorc4 = data[15, 1]/suma4
    print(4, vPorc1,vPorc2,vPorc3,vPorc4, suma4)


