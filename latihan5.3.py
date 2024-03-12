jmlh_matkul = int(input('Berapa jumlah mata kuliah : ', ))
for i in range (1, jmlh_matkul+1):
    nilai_matkul = str(input(f"Nilai MK {i} :"))    
bobot = 0
for i in range (jmlh_matkul):   
    if nilai_matkul == 'A' or nilai_matkul == 'a':
        bobot += 4 
    elif nilai_matkul == 'B' or nilai_matkul == 'b':
        bobot +=3 
    elif nilai_matkul == 'C' or nilai_matkul == 'c':
        bobot +=2 
    elif nilai_matkul == 'D' or nilai_matkul == 'd':
        bobot +=1 
indks_prs_mhs =  bobot / jmlh_matkul
    
print("rata-rata : ", indks_prs_mhs)


