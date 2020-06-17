
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
        print('Under construction - Sebagai Admin\n')
    elif pilihan == 'U':
        print ('Under construction - Sebagai User\n')
    elif pilihan == 'Q':
        program_masih_berjalan = False
    else:
        print('Pilihan tidak sah')
