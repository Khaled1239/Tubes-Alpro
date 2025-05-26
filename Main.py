import cv2
from deepface import DeepFace
from tkinter import simpledialog, messagebox
from Mahasiswa import Mahasiswa
from DataBase import LD, SD
import sys
import numpy as np
import os
import ttkbootstrap as ttk
import tkinter as tk
import time
import traceback


def resource_path(relative_path):
    try:
        BasePath = sys._MEIPASS
    except Exception:
        BasePath = os.path.abspath(".")

    abs_path = os.path.join(BasePath, relative_path)

    if not os.path.exists(abs_path):
        abs_path = os.path.join(os.getcwd(), relative_path)

    return abs_path

os.environ['DEEPFACE_HOME'] = resource_path(".deepface")


def FRSearch(Data):
    cap = cv2.VideoCapture(0)
    recognized = False
    threshold = 0.25

    ST = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for mahasiswa in Data:
            if mahasiswa.PhotoPath and os.path.exists(mahasiswa.PhotoPath):
                try:
                    TempPath = os.path.join(os.getcwd(), "TempFrame.jpg")
                    cv2.imwrite(TempPath, frame)
                    cv2.waitKey(5)
                    result = DeepFace.verify(
                        img1_path=TempPath,
                        img2_path=mahasiswa.PhotoPath,
                        model_name="VGG-Face",
                        enforce_detection=False
                    )
                    if result["distance"] <= threshold:
                        recognized = True
                        cap.release()
                        cv2.destroyAllWindows()
                        if os.path.exists(TempPath):
                            os.remove(TempPath)
                        messagebox.showinfo("Wajah Dikenali",
                                            f"Data Mahasiswa:\nNama: {mahasiswa.NAMA}\nNIM: {mahasiswa.NIM}\nHP: {mahasiswa.P_NUM}\nTanggal Lahir: {mahasiswa.BDate}\nSemester: {mahasiswa.Sems}")
                        return
                except Exception as e:
                    print("Error DeepFace:", e)
                    traceback.print_exc()

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time.time() - ST > 20 :
            break

    cap.release()
    cv2.destroyAllWindows()

    if not recognized:
        print("Wajah tidak dikenali.")
        messagebox.showwarning("Tidak Dikenali", "Wajah tidak dikenali.")


def SNim(Data):
    key = simpledialog.askstring("Input", "Masukkan NIM : (Ketik exit untuk keluar)")
    if key is None:
        return "Pencarian dibatalkan."
    key = key.lower()
    for m in Data:
        if key in m.NIM.lower():
            return messagebox.showinfo("Data Mahasiswa Terurut",m)
        elif key == "exit":
            return "See You!"
    return "Data Not Found"

def AddMahasiswa(parent,Data):
    def simpan():
        name = entry_name.get()
        nim = entry_nim.get()
        phone = entry_phone.get()
        bdate = entry_bdate.get()
        sems = entry_sems.get()

        if not name or not nim:
            messagebox.showwarning("Input Tidak Lengkap", "Nama dan NIM wajib diisi.")
            return

        top.destroy()

        cap = cv2.VideoCapture(0)
        messagebox.showinfo("Ambil Foto", "Tekan 's' untuk mengambil gambar...")

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Ambil Wajah", frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                IMGDIR = str(resource_path("DataImg"))
                os.makedirs(IMGDIR, exist_ok=True)
                filename = f"{name}_{nim}.jpg"
                filepath = os.path.join(IMGDIR, filename)
                cv2.imwrite(filepath, frame)
                mhs = Mahasiswa(name, nim, phone, bdate, sems, PhotoPath=filepath)
                Data.append(mhs)
                SD(Data)
                messagebox.showinfo("Sukses", f"Mahasiswa {name} ditambahkan.")
                break
        cap.release()
        cv2.destroyAllWindows()

    top = tk.Toplevel(parent)
    top.title("Tambah Mahasiswa")
    top.geometry("300x480")
    top.grab_set()  # Supaya window modal

    ttk.Label(top, text="Nama:").pack(pady=(10, 0))
    entry_name = ttk.Entry(top)
    entry_name.pack(pady=5)

    ttk.Label(top, text="NIM:").pack(pady=(10, 0))
    entry_nim = ttk.Entry(top)
    entry_nim.pack(pady=5)

    ttk.Label(top, text="No. HP:").pack(pady=(10, 0))
    entry_phone = ttk.Entry(top)
    entry_phone.pack(pady=5)

    ttk.Label(top, text="Tanggal Lahir (dd/mm/yyyy):").pack(pady=(10, 0))
    entry_bdate = ttk.Entry(top)
    entry_bdate.pack(pady=5)

    ttk.Label(top, text="Semester:").pack(pady=(10, 0))
    entry_sems = ttk.Entry(top)
    entry_sems.pack(pady=5)

    ttk.Button(top, text="OK", command=simpan).pack(pady=(15, 5))
    ttk.Button(top, text="Batal", command=top.destroy).pack()

def EditData(parent,Data):
    nim = simpledialog.askstring("Input", "Masukkan NIM mahasiswa yang ingin diedit:")
    if not nim:
        return

    for m in Data:
        if m.NIM == nim:
            def simpan():
                name = entry_name.get()
                nim = entry_nim.get()
                phone = entry_phone.get()
                bdate = entry_bdate.get()
                sems = entry_sems.get()

                if not name or not nim:
                    messagebox.showwarning("Input Tidak Lengkap", "Nama dan NIM wajib diisi.")
                    return

                m.NAMA = name
                m.NIM = nim
                m.P_NUM = phone
                m.BDate = bdate
                m.Sems = sems

                SD(Data)
                messagebox.showinfo("Sukses", "Data berhasil diperbarui.")
                top.destroy()

            top = tk.Toplevel(parent)
            top.title("Tambah Mahasiswa")
            top.geometry("300x480")
            top.grab_set()  # Supaya window modal

            ttk.Label(top, text="Nama:").pack(pady=(10, 0))
            entry_name = ttk.Entry(top)
            entry_name.pack(pady=5)

            ttk.Label(top, text="NIM:").pack(pady=(10, 0))
            entry_nim = ttk.Entry(top)
            entry_nim.pack(pady=5)

            ttk.Label(top, text="No. HP:").pack(pady=(10, 0))
            entry_phone = ttk.Entry(top)
            entry_phone.pack(pady=5)

            ttk.Label(top, text="Tanggal Lahir (dd/mm/yyyy):").pack(pady=(10, 0))
            entry_bdate = ttk.Entry(top)
            entry_bdate.pack(pady=5)

            ttk.Label(top, text="Semester:").pack(pady=(10, 0))
            entry_sems = ttk.Entry(top)
            entry_sems.pack(pady=5)

            ttk.Button(top, text="OK", command=simpan).pack(pady=(15, 5))
            ttk.Button(top, text="Batal", command=top.destroy).pack()

            return

    messagebox.showerror("Gagal", "Mahasiswa dengan NIM tersebut tidak ditemukan.")


def RemoveData(Data):
    nim = simpledialog.askstring(title="Input", prompt="Masukkan NIM mahasiswa yang ingin dihapus:")
    if nim is None:
        messagebox.showinfo("Batal", "Penghapusan dibatalkan.")
        return

    for i, m in enumerate(Data):
        if m.NIM == nim:
            konfirmasi = messagebox.askyesno("Konfirmasi", f"Apakah kamu yakin ingin menghapus {m.NAMA}?")
            if konfirmasi:
                if m.PhotoPath and os.path.exists(m.PhotoPath):
                    try:
                        os.remove(m.PhotoPath)
                        print(f"File gambar {m.PhotoPath} berhasil dihapus.")
                    except Exception as e:
                        print(f"Gagal menghapus file gambar: {e}")
                del Data[i]
                SD(Data)
                messagebox.showinfo("Berhasil", "Data berhasil dihapus.")
            else:
                messagebox.showinfo("Dibatalkan", "Penghapusan dibatalkan.")
            return

    messagebox.showerror("Tidak Ditemukan", "Mahasiswa dengan NIM tersebut tidak ditemukan.")

def SS(Data, key='NIM'):
    n = len(Data)
    for i in range(1, n):
        current = Data[i]
        j = i - 1
        while j >= 0 and getattr(current, key).lower() < getattr(Data[j], key).lower():
            Data[j + 1] = Data[j]
            j -= 1
        Data[j + 1] = current

    result = f"=== Data Mahasiswa diurutkan berdasarkan {key.upper()} ===\n\n"
    for mhs in Data:
        result += f"{mhs}\n" + "-" * 40 + "\n"

    messagebox.showinfo("Data Mahasiswa Terurut", result)