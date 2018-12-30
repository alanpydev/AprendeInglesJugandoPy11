file = open("sustantivos.txt", "r+")
sw = True
palabras = []
while sw:
    st = file.readline()
    if st != '':
        st = st.replace("\n", "")
        ele = st.split("\t")
        ele.append("0\n")
        palabras.append(ele)
    else:
        sw = False
print(palabras)
file.close()
stre = ""
for i in range(0, len(palabras)):
    stre = stre + palabras[i][0] + "," + palabras[i][1] + "," + palabras[i][2]
# procedemos a escribir
file = open("sustantivos.txt", "w")
file.write(stre)
file.close()
