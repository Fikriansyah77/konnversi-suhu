#Fungsi untuk mengkonversui suhu

def Ctof(celsius):
    return (celsius * 9/5) + 32
def Ftoc(fahrenheit):
    return (fahrenheit - 32) * 5/9
def Ctok(celsius):
    return celsius + 273.15
while True:
    try:
        # Meminta untuk memasukan input suhu dari pengguna
        suhu = float(input("Masukkan suhu: "))
        
        # Meminta input jenis konversi
        print("Pilih konversi : ")
        print("1    : Celsius ke Fahrenheit")
        print("2    : Fahrenheit ke Celsius")
        print("3    : Celsius ke Kelvin")
        print("4    : Keluar")
        pilihan = input("Masukkan nomor pilihan (1/2/3/4): ")

        # kontrol alur  konversi suhu
        if pilihan == '1':
            hasil = Ctof(suhu)
            print(f"Hasil konversi  : {hasil} Fahrenheit")
        elif pilihan == '2':
            hasil = Ftoc(suhu)
            print(f"Hasil konversi  : {hasil} Celsius")
        elif pilihan == '3':
            hasil = Ctok(suhu)
            print(f"Hasil konversi  : {hasil} Kelvin")
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Harap pilih yang ada!!!")
    
    except ValueError:
        print("nilai suhu tidak valid...masukkan angka yang benar donkkk!!!")
