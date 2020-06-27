"""
    Kelas untuk perincian/details
"""

class Perincian:
    def __init__(self, nombor_kenderaan, nama_kenderaan, tempat_berlepas, destinasi, bilangan_kelas_pertama, tambang_kelas_pertama, bilangan_kelas_kedua, tambang_kelas_kedua):
        self.nombor_kenderaan = nombor_kenderaan
        self.nama_kenderaan = nama_kenderaan
        self.tempat_berlepas = tempat_berlepas
        self.destinasi = destinasi
        self.bilangan_kelas_pertama = bilangan_kelas_pertama
        self.tambang_kelas_pertama = tambang_kelas_pertama
        self.bilangan_kelas_kedua = bilangan_kelas_kedua
        self.tambang_kelas_kedua = tambang_kelas_kedua
        self.tarikh_perjalanan = { 'Tahun' : '', 'Bulan' : '', 'Hari' : ''}

    def data_perincian_baharu(self):
        print('Masukkan perincian baharu data :\n')
        print('Nombor keretapi/pesawat/bas')
        nombor_kenderaan = input()
        print('Nama keretapi/pesawat/bas: ')
        nama_kenderaan = input()
        print('Tempat pelepasan')
        tempat_berlepas = input()
        print('Destinasi')
        destinasi = input()
        print('Bilangan tempat duduk kelas pertama dan tambang untuk setiap tiket')
        bilangan_kelas_pertama = input()
        tambang_kelas_pertama = input()
        print('Bilangan tempat duduk kelas kedua dan tambang untuk setiap tiket')
        bilangan_kelas_pertama = input()
        tambang_kelas_pertama = input()
        print('Tarikh perjalanan: ')
        tahun = input()
        bulan = input()
        hari = input()
        tarikh_perjalanan = { 'Tahun' : tahun, 'Bulan' : bulan, 'Hari' : hari}
