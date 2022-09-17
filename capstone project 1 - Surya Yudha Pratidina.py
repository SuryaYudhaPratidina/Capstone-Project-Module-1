print("\nSELAMAT DATANG DI SISTEM INFORMASI PEGAWAI PT. POHON MANGGA")
kolom = "\nkode  |nama                     |cabang         |posisi         |tanggal lahir  |gaji           |"
bulan = {"01":["JAN",list(range(1,32))],"02":["FEB",list(range(1,30))],
"03":["MAR",list(range(1,32))],"04":["APR",list(range(1,31))],
"05":["MEI",list(range(1,32))],"06":["JUN",list(range(1,31))],
"07":["JUL",list(range(1,32))],"08":["AUG",list(range(1,32))],
"09":["SEP",list(range(1,31))],"10":["OCT",list(range(1,32))],
"11":["NOV",list(range(1,31))],"12":["DEC",list(range(1,32))]}
db = {
"000112":{"nama":"Surya Yudha","cabang":"Pusat","posisi":"CEO","tanggal lahir":"20101998","gaji":40000000},
"000212":{"nama":"Jim Jimbo","cabang":"Jagakarsa","posisi":"Manager","tanggal lahir":"23071995","gaji":20000000},
"000123":{"nama":"Ani Anabel","cabang":"Kebayoran","posisi":"Staff","tanggal lahir":"01071999","gaji":10000000}
}

cek_nik = lambda x:True if x in db.keys() else False
def masuk_nama():
    nama = input("Masukan Nama(Hanya karakter alphabet)\t:")
    if (nama.replace(" ","")).isalpha():
        return nama.title()
    else:
        print("nama tidak sesuai format")
        return masuk_nama()
def masuk_tl():
    tl = input("Masukan Tanggal Lahir(ddmmyyyy)\t\t:")
    if len(tl)==8 and tl[2:4] in bulan.keys() and int(tl[:2]) in bulan[tl[2:4]][1] and int(tl[4:])%4==0:
        return tl
    elif len(tl)==8 and tl[2:4] in bulan.keys() and int(tl[:2]) in bulan[tl[2:4]][1] and int(tl[4:])%4!=0:
        if (tl[2:4]!="02") or (tl[2:4]=="02" and int(tl[:2])!=29):    
            return tl
        else:
            print("Tanggal Lahir tidak sesuai format")
            return masuk_tl()            
    else:
        print("Tanggal Lahir tidak sesuai format")
        return masuk_tl()
def masuk_gaji():
    gaji = input("Masukan Gaji (Hanya angka)\t\t:")
    if gaji.isdigit():
        return int(gaji)
    else:
        print("gaji tidak sesuai format")
        return masuk_gaji()
def konfirmasi(x):
    b = input(f"apakah anda ingin {x} informasi pada database (1.ya 2.tidak):")
    if b == "1":
        print(f"berhasil {x} data")
        return True
    elif b == "2":
        print(f"gagal {x} data")
        return False
    else:
        return konfirmasi(x)
print_tl = lambda x:f"{x[:2]} {bulan[x[2:4]][0]} {x[4:]}" if len(x) == 8 and x[2:4] in bulan.keys() else None
print_data = lambda x,i : print(f"{i:6}|{(x[i]['nama']):25}|{x[i]['cabang']:15}|{(x[i]['posisi']):15}|{print_tl(x[i]['tanggal lahir']):15}|Rp{x[i]['gaji']:13}|")
def baca():
    while True:
        print('''
Menu Menampilkan INFORMASI PEGAWAI :
1. Tampilakan Seluruh Informasi Pegawai
2. Tampilkan Informasi pegawai
3. Kembali Ke Menu Utama\n''')
        mn = input("Pilih Menu :")
        if mn == "1":
            if db == {}:
                print("Database masih kosong")
            else:
                print(kolom)
                for i in db:
                    print_data(db,i)
        elif mn == "2":
            if db == {}:
                print("Database masih kosong")
            else:
                nik = input("masukan nik\t\t\t:")
                if cek_nik(nik):
                    print(kolom)
                    print_data(db,nik)
                else:
                    print("\ndata tidak ditemukan")
        elif mn == "3":
            break
def tambah():
    while True:
        print('''
Menu Menambah INFORMASI PEGAWAI :
1. Tambah Informasi Pegawai
2. Kembali Ke Menu Utama\n''')
        mn = input("Pilih Menu :")
        if mn == "1":
            nik = input("masukan nik\t\t\t:")
            if cek_nik(nik) == False:
                x = {nik:{}}
                x[nik]["nama"] = masuk_nama()
                x[nik]["cabang"] = input("Masukan cabang\t\t\t\t:")
                x[nik]["posisi"] = input("Masukan posisi\t\t\t\t:")
                x[nik]["tanggal lahir"] = masuk_tl()
                x[nik]["gaji"] = masuk_gaji()
                print(kolom)
                print_data(x,nik)
                if konfirmasi("menambah"):
                    db.update(x)                    
            else:
                print("\ndata sudah ada")
        elif mn == "2":
            break
def ubah():
    while True:
        print('''
Menu Mengubah INFORMASI PEGAWAI :
1. Ubah Informasi Pegawai
2. Kembali Ke Menu Utama\n''')
        mn = input("Pilih Menu :")
        if mn == "1":
            nik = input("masukan nik\t\t\t:")
            if cek_nik(nik):
                while True:
                    print(kolom)
                    print_data(db,nik)
                    print('''
Menu data yang diubah :
1. Nama
2. Cabang
3. Posisi
4. Tanggal lahir
5. Gaji
6. Kembali''')
                    mn = input("Pilih data yang ingin diubah\t\t:")
                    if mn == "1":
                        nama = masuk_nama()
                        if konfirmasi("mengubah"):
                            db[nik]["nama"]=nama
                    elif mn == "2":
                        cabang = input("Masukan cabang\t\t\t\t:")
                        if konfirmasi("mengubah"):
                            db[nik]["cabang"]=cabang
                    elif mn == "3":
                        posisi= input("Masukan posisi\t\t\t\t:")
                        if konfirmasi("mengubah"):
                            db[nik]["posisi"]=posisi
                    elif mn == "4":
                        tl = masuk_tl()
                        if konfirmasi("mengubah"):
                            db[nik]["tanggal lahir"]=tl
                    elif mn == "5":
                        gaji = masuk_gaji()
                        if konfirmasi("mengubah"):
                            db[nik]["gaji"]=gaji
                    elif mn == "6":
                        break
            else:
                print("\ndata tidak ditemukan")
        elif mn == "2":
            break
def hapus():
 while True:
        print('''
Menu Menghapus INFORMASI PEGAWAI :
1. Hapus Informasi Pegawai
2. Kembali Ke Menu Utama\n''')
        mn = input("Pilih Menu :")
        if mn == "1":
            nik = input("masukan nik\t\t\t:")
            if cek_nik(nik):
                print(kolom)
                print_data(db,nik)
                if konfirmasi("menghapus"):
                    del db[nik]
            else:
                print("\ndata tidak ditemukan")
        elif mn == "2":
            break


while True:
    print('''
Menu Utama  :
1. Tampilkan Informasi Pegawai
2. Tambah Informasi Pegawai
3. Ubah Informasi Pegawai
4. Hapus Informasi Pegawai
5. Exit\n''')
    menu = input("Pilih Menu :")
    if menu == "1":
        baca()
    elif menu == "2":
        tambah()
    elif menu == "3":
        ubah()
    elif menu == "4":
        hapus()
    elif menu == "5":
        print("Terima Kasih")
        break