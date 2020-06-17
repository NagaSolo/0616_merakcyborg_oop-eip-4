from paparan_admin import PaparanAdmin
class PaparanUtama:
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
                paparan_untuk_admin = PaparanAdmin()
                paparan_untuk_admin.paparan_admin
            elif pilihan == 'U':
                print ('Under construction - Sebagai User\n')
            elif pilihan == 'Q':
                program_masih_berjalan = False
            else:
                print('Pilihan tidak sah')
