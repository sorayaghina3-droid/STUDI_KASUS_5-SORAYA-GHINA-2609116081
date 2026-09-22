#menghitung biaya hotel  
  
def hitung_biaya(jenis_kamar, lama_menginap):  
  
    if jenis_kamar == "Standard":  
        tarif = 200000  
  
    elif jenis_kamar == "Deluxe":  
        tarif = 350000  
  
    else:  
        tarif = 0  
  
    total = tarif * lama_menginap  
    return total  
  
  
#menampilkan pemesanan  
  
def pesan_hotel():  
  
    jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")  
    check_in = input("Masukkan tanggal check-in: ")  
    check_out = input("Masukkan tanggal check-out: ")  
    lama_menginap = (input("Masukkan lama menginap (malam): "))  
  
    total_biaya = hitung_biaya(jenis_kamar, lama_menginap)  
  
    print("== PEMESANAN HOTEL ==")  
    print("Jenis kamar    :", jenis_kamar)  
    print("Check-in       :", check_in)  
    print("Check-out      :", check_out)  
    print("Lama menginap  :", lama_menginap, "malam")  
    print("Total biaya    : Rp", total_biaya)  
  
  
#menu  
  
while True:  
    print("== MENU HOTEL ==")  
    print("1. Pesan Kamar")  
    print("2. Keluar")  
  
    pilihan = input("Masukkan pilihan: ")  
  
    if pilihan == "1":  
        pesan_hotel()  
  
    elif pilihan == "2":  
        print("Sampai bertemu kembali")  
        break  
  
    else:  
        print("Pilihan tidak valid")