import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog

prolog = Prolog()
prolog.consult("pakar_motor_gui.pl")

kerusakan = list()
gejala = dict()
index_kerusakan = 0
index_gejala = 0
current_kerusakan = ""
current_gejala = ""

def mulai_deteksi():
    global kerusakan, gejala, index_kerusakan, index_gejala
    prolog.retractall("gejala_pos(_)")
    prolog.retractall("gejala_neg(_)")
    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)
    kerusakan = [p["X"].decode() for p in list(prolog.query("kerusakan(X)"))]
    for p in kerusakan:
        gejala[p] = [g["X"] for g in list(prolog.query(f"gejala(X,\"{p}\")"))]
    index_kerusakan = 0
    index_gejala = -1
    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_kerusakan=False):
    global current_kerusakan, current_gejala, index_kerusakan, index_gejala
    if ganti_kerusakan:
        index_kerusakan += 1
        index_gejala = -1
    if index_kerusakan >= len(kerusakan):
        hasil_deteksi()
        return
    current_kerusakan = kerusakan[index_kerusakan]
    index_gejala += 1
    if index_gejala >= len(gejala[current_kerusakan]):
        hasil_deteksi(current_kerusakan)
        return
    current_gejala = gejala[current_kerusakan][index_gejala]
    if list(prolog.query(f"gejala_pos({current_gejala})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"gejala_neg({current_gejala})")):
        pertanyaan_selanjutnya(ganti_kerusakan=True)
        return
    pertanyaan = list(prolog.query(f"pertanyaan({current_gejala},Y)"))[0]["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"gejala_pos({current_gejala})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"gejala_neg({current_gejala})")
        pertanyaan_selanjutnya(ganti_kerusakan=True)

def hasil_deteksi(masalah=""):
    if masalah:
        messagebox.showinfo("Hasil Deteksi", f"Motor Anda kemungkinan Mengalami Kerusakan : {masalah}.")
    else:
        messagebox.showinfo("Hasil Deteksi", "Tidak ditemukan Kerusakan.")
    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

root = tk.Tk()
root.title("Sistem Pakar Deteksi Kerusakan Motor")
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

ttk.Label(mainframe, text="Deteksi Kerusakan Motor", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Pertanyaan:").grid(column=0, row=1)
kotak_pertanyaan = tk.Text(mainframe, height=4, width=50, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))
no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))
start_btn = ttk.Button(mainframe, text="Mulai Deteksi", command=mulai_deteksi)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
