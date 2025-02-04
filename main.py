#!/usr/bin/env python3

import tkinter as tk
import sv_ttk
from tkinter import filedialog, messagebox, ttk
import Utils
import Locations


def show_file_error():
    messagebox.showerror("Error", "File not found.")


def show_empty_alert():
    messagebox.showerror("Error",
                         f"No data found in the backup file {Utils.BACKUP_FILE}")


def show_success_export():
    messagebox.showinfo(
        "Success",
        f"Search Engines exported successfully in {Utils.BACKUP_FILE}")


def show_success_import(path):
    messagebox.showinfo(
        "Success",
        f"Search Engines imported successfully in {path}")


def importar():
    """Importa el JSON backup en el navegador seleccionado"""
    path = Locations.get_browser_path(bw_sel.get().strip())
    file_path = filedialog.askopenfilename(initialfile="Web Data",
                                           initialdir=path,
                                           filetypes=[("Web Data SQLite",
                                                       "Web\\ Data")])
    if not file_path:
        show_file_error()
        return

    print(f"Importing from {file_path}")
    filas = Utils.json_read(Utils.BACKUP_FILE)
    if len(filas) == 0:
        show_empty_alert()
        return

    try:
        Utils.db_insertar_filas(file_path, filas)
        show_success_import(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"{e}")


def exportar(bw_sel):
    """Exporta Search Engines del navegador seleccionado en un archivo JSON"""
    path = Locations.get_browser_path(bw_sel.get().strip())
    file_path = filedialog.askopenfilename(initialfile="Web Data",
                                           initialdir=path,
                                           filetypes=[("Web Data SQLite",
                                                       "Web\\ Data")])
    if not file_path:
        show_file_error()
        return

    filas = Utils.db_read_keywords(file_path)
    Utils.json_write(filas)
    show_success_export()


def select_browser():
    print(f"Browser: {bw_sel.get()}")


win = tk.Tk()
sv_ttk.set_theme("dark")
style = ttk.Style()
style.configure("TMenubutton", padding=(10, 5, 10, 5))

win.geometry("400x200")
win.title("Browser Search Engines")

bw_sel = tk.StringVar()

frame = tk.Frame(win)
frame.pack(pady=10)

label = tk.Label(win, text="Close Browser before import or export")
label.pack(pady=10)

bws = Utils.add_spaces(Locations.LOCATIONS.keys())
menu = ttk.OptionMenu(
    frame, bw_sel, bws[0], *bws, command=lambda _: select_browser
)
menu.config(padding=(50, 5))
menu.pack(anchor=tk.W)

frame_botones = tk.Frame(win)
frame_botones.pack(side=tk.BOTTOM, pady=10)

btn_export = ttk.Button(
    frame_botones, text="Export from Browser", command=lambda: exportar(bw_sel)
)
btn_export.pack(side=tk.LEFT, padx=5)

btn_import = ttk.Button(
    frame_botones, text="Import into Browser", command=importar
)
btn_import.pack(side=tk.RIGHT, padx=5)

win.mainloop()
