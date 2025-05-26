import pickle
import os
import sys


FileDirectory = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
DF = os.path.join(FileDirectory, "Data")
os.makedirs(DF, exist_ok=True)
DataDir = os.path.join(DF, "Mahasiswa.pkl")

def LD():
    if os.path.exists(DataDir) and os.path.getsize(DataDir) > 0:
        with open(DataDir, "rb") as f:
            try:
                return pickle.load(f)
            except EOFError:
                print("File kosong. Kembali ke data kosong.")
                return []
    else:
        print("File tidak ditemukan. Membuat data kosong.")
        return []
def SD(Data):
    with open(DataDir, "wb") as f:
        pickle.dump(Data, f)