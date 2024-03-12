# Mendefinisikan a dan b
def perkalian(a, b):
# mengeksekusi
    kali = a * b  
    print(f"{a} * {b} = {kali} ", end="")                
    for i in range(a):   # Menggunakan range untuk mengulang sebanyak a
        if i < a - 1:    
            print(f"{b} + ", end ="")       # memuculkan b dan +
        else :
            print(f"{b}", end ="")          # memuculkan b 

    print(f" = {kali} ")                    # memuculkan kali

# Inputan langsung
perkalian(6,5)           
perkalian(7, 10)
