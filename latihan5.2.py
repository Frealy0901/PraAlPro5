# Mendefinisikan
def ganjil(batas_bawah, batas_atas):
    if batas_bawah < batas_atas:                                # Menggunakan percabangan untuk kemungkinan jika batas bawah lebih kecil
        # Memunculkan batas
        print("bawah = ",batas_bawah, end=", ")
        print("bawah = ",batas_atas, end=". ")
        print("Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya :")
        # Menggunakan for untuk mengeksekusi program
        for i in range(batas_bawah+1, batas_atas,2):
            if i < batas_atas-1:
                print(i, end=",")
            else :
               print(i,'.')
        
    elif batas_bawah > batas_atas:                              # Menggunakan percabangan untuk kemungkinan jika batas bawah lebih besar
         # Memunculkan batas
        print("bawah = ",batas_bawah, end=", ")                
        print("bawah = ",batas_atas, end=". ")
        print("Karena bawah > atas, berarti dari kecil ke besar, maka hasilnya :")
         # Menggunakan for untuk mengeksekusi program
        for i in range(batas_bawah, batas_atas, -2):
            if i > batas_atas+1:
               print(i, end=",")
            else :
                print(i,end=".")
#meninput program secara langsung 
ganjil(10,30)
ganjil(97, 82)