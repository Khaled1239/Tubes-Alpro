class Mahasiswa:
    def __init__(self,NAMA,NIM,P_NUM,BDate,Sems,FACE_EMB=None, PhotoPath=None):
        self.NAMA = NAMA
        self.NIM = NIM
        self.P_NUM = P_NUM
        self.BDate = BDate
        self.Sems = Sems
        self.FACE_EMB = FACE_EMB
        self.PhotoPath = PhotoPath
    def Info(self):
        print(f"Nama     : {self.NAMA}")
        print(f"NIM      : {self.NIM}")
        print(f"P_Num    : {self.P_NUM}")
        print(f"BDate    : {self.BDate}")
        print(f"Semester : {self.Sems}")


    def __str__(self):
        return f"Nama: {self.NAMA}\nNIM: {self.NIM}\nHP: {self.P_NUM}\nTanggal Lahir: {self.BDate}\nSemester: {self.Sems}"