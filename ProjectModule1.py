listBarang = [
    {
        'nama': 'Telur',
        'stock': 100,
        'harga': 20000
    },
    {
        'nama': 'Beras',
        'stock': 50,
        'harga': 50000
    },
    {
        'nama': 'Minyak',
        'stock': 75,
        'harga': 30000
    }
]

keranjang = []

def menampilkanDaftarBarang():
   print('Daftar Barang\n')
   print('Index\t| Nama\t| Stock\t| Harga')
   for i in range (len(listBarang)):
    print('{}\t| {} \t| {}\t| {}'.format(i, listBarang[i]['nama'], listBarang[i]['stock'], listBarang[i]['harga']))

def menambahBarang():
    namaBarang = input('Masukkan nama barang: ')
    stockBarang = int(input('Masukkan stock barang: '))
    hargaBarang = int(input('Masukkan harga barang: '))
    listBarang.append({
            'nama': namaBarang,
            'stock': stockBarang,
            'harga': hargaBarang   
    })
    menampilkanDaftarBarang()

def menghapusBarang():
    menampilkanDaftarBarang()
    indexBarang = int(input('Masukkan index yang ingin di hapus: '))
    del listBarang[indexBarang]
    menampilkanDaftarBarang()

def membeliBarang():
    menampilkanDaftarBarang()
    while True:
        indexBarang = int(input('Masukkan index  yang ingin di beli: '))
        jumlahBarang = int(input('Masukkan jumlah yang ingin di beli: '))
        if(jumlahBarang>listBarang[indexBarang]['stock']):
            print('Mohon maaf stock tidak mencukupi, stock {} tinggal {}'.format(listBarang[indexBarang]['nama'],listBarang[indexBarang]['stock']))
        else:
            keranjang.append({
                'nama': listBarang[indexBarang]['nama'],
                'jumlah': jumlahBarang,
                'harga': listBarang[indexBarang]['harga'],
                'index': indexBarang
             
            })
        print('Isi keranjang: ')
        print('Nama\t| Jumlah\t| Harga')
        for barang in keranjang:
            print('{}\t| {}\t| {}'.format(barang['nama'], barang['jumlah'], barang['harga']))
        pemeriksa = input('Apakah anda mau membeli barang lain? (yes/no) = ')
        if(pemeriksa == 'no'):
            break

    print('Daftar belanja: ')
    print('Nama\t| Jumlah\t| Harga\t| Jumlah Biaya')
    jumlahBiaya = 0
    for barang in keranjang:
        print('{}\t| {}\t| {}\t| {}'.format(barang['nama'], barang['jumlah'], barang['harga'], barang['jumlah'] * barang['harga']))
        jumlahBiaya += barang['jumlah'] * barang['harga']
    while True:
        print('Jumlah yang harus di bayar = {}'.format(jumlahBiaya))
        jumlahUang = int(input('Masukkan jumlah uang: '))
        if(jumlahUang>jumlahBiaya):
            change = jumlahUang - jumlahBiaya
            print('Terima kasih \n\nUang kembali anda : {}'.format(change))
            for barang in keranjang:
                listBarang[barang['index']]['stock'] -= barang['jumlah']
            keranjang.clear()
            break
        elif(jumlahUang == jumlahBiaya):
            print('Terima kasih')
            for barang in keranjang:
                listBarang[barang['index']]['stock'] -= barang['jumlah']
            keranjang.clear()
            break
        else:
            kurangBayar = jumlahBiaya - jumlahUang
            print('Anda kurang bayar sebesar {}'.format(kurangBayar))

while True:
    menu = input('''
        Selamat datang di Toko Sembako

        List Menu:
        1. Menampilkan Daftar Barang
        2. Menambah Barang
        3. Menghapus Barang
        4. Membeli Barang
        5. Exit

        Masukkan angka menu yang ingin di jalankan: ''')

    if(menu == '1'):
        menampilkanDaftarBarang()
    elif(menu == '2'):
        menambahBarang()
    elif(menu == '3'):
        menghapusBarang()
    elif(menu == '4'):
        membeliBarang()
    elif(menu == '5'):
        break
