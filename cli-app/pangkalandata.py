from perincian import Perincian

class PangkalanData:
    def __init__(self, katalaluan):
        self.katalaluan = katalaluan

    def paparan_pangkalan_data(self):
        with open('pangkalandata.txt', mode='w') as k:
            perincian = Perincian()
            perincian.data_perincian_baharu()
            k.write()