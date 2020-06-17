
class Paparan:
    def paparan_utama(self):
        program_masih_berjalan = True

        while program_masih_berjalan:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            print('.............. Sistem Tempahan .................\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

            print('Sebagai Admin: Tekan \'A\'')
            print('\n')
            print('Sebagai Pengguna: Tekan \'U\'')
            print('\n')
            print('Keluar dari program: Tekan \'Q\'')
            print('\n')
            pilihan = input()
            if pilihan == 'A':
                self.paparan_admin()
            elif pilihan == 'U':
                print ('Under construction - Sebagai User\n')
            elif pilihan == 'Q':
                program_masih_berjalan = False
            else:
                print('Pilihan tidak sah')

    def paparan_admin(self):

        program_masih_berjalan = True

        while program_masih_berjalan:
        
            print('........... Menu ADMINISTRATOR ...........\n')
            print('1.Bina penyimpanan data\n')
            print('2.Tambah maklumat\n')
            print('3.Papar maklumat terperinci\n')
            print('4.Pengurusan Pengguna\n')
            print('5.Papar maklumat terperinci penumpang\n')
            print('6.Kembali ke menu utama\n')
            print('Pilihan anda: ')

            pilihan = input()
            if pilihan == '1':
                print('Under construction - Sebagai Admin\n')
            elif pilihan == '2':
                print ('Under construction - Sebagai User\n')
            elif pilihan == '6':
                program_masih_berjalan = False
                self.paparan_utama()
            else:
                print('Pilihan tidak sah')
