#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sv_ttk
import utils
import locations


def show_file_error():
    messagebox.showerror("Error", "File not found.")


def show_empty_alert():
    messagebox.showerror("Error",
                         f"No data found in the backup file {utils.BACKUP_FILE}")


def show_success_export():
    messagebox.showinfo(
        "Success",
        f"Search Engines exported successfully in {utils.BACKUP_FILE}")


def show_success_import(path):
    messagebox.showinfo(
        "Success",
        f"Search Engines imported successfully in {path}")


def importar():
    """Importa el JSON backup en el navegador seleccionado"""
    path = locations.get_browser_path(bw_sel.get().strip())
    file_path = filedialog.askopenfilename(initialfile="Web Data",
                                           initialdir=path,
                                           filetypes=[("Web Data SQLite",
                                                       "Web\\ Data")])
    if not file_path:
        show_file_error()
        return

    print(f"Importing from {file_path}")
    filas = utils.json_read(utils.BACKUP_FILE)
    if len(filas) == 0:
        show_empty_alert()
        return

    try:
        utils.db_insertar_filas(file_path, filas)
        show_success_import(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"{e}")


def exportar(bw_sel):
    """Exporta Search Engines del navegador seleccionado en un archivo JSON"""
    path = locations.get_browser_path(bw_sel.get().strip())
    file_path = filedialog.askopenfilename(initialfile="Web Data",
                                           initialdir=path,
                                           filetypes=[("Web Data SQLite",
                                                       "Web\\ Data")])
    if not file_path:
        show_file_error()
        return

    filas = utils.db_read_keywords(file_path)
    utils.json_write(filas)
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

# Create a frame that holds both the label and the menu
frame = tk.Frame(win)
frame.pack(pady=10)

# Place label above the menu
label = tk.Label(frame,
                 text="Close Browser before import or export",
                 font=("Arial", 14, "bold"))
label.pack(pady=(0, 10))

label = tk.Label(frame,
                 text=("Export from Browser Web Data SQLite to a JSON file\n"
                       "Import from a JSON file into a Browser Web Data SQLite"))
label.pack(pady=(0, 10))

bws = utils.add_spaces(locations.LOCATIONS.keys())
menu = ttk.OptionMenu(frame,
                      bw_sel, bws[0], *bws, command=lambda _: select_browser)
menu.config(padding=(50, 5))
menu.pack(anchor="center")

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
