class PangkalanData:
    def __init__(self, katalaluan):
        self.katalaluan = katalaluan

    def tambahan_baharu(self):
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
        tarikh_perjalanan = { 'Tahun' : '', 'Bulan' : '', 'Hari' : ''}

    def paparan_pangkalan_data(self):
        with open('pangkalandata.txt', mode='w') as k:
            self.tambahan_baharu()
            k.write()