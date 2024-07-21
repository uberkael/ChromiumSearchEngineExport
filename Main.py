import tkinter as tk
import sv_ttk
from tkinter import filedialog, messagebox, ttk
import Utils
import Locations


def importar():
    print("Import")


def exportar(bw_sel):
    path = Locations.get_browser_path(bw_sel.get().strip())
    file_path = filedialog.askopenfilename(initialfile="Web Data",
                                           initialdir=path,
                                           filetypes=[("Web Data SQLite",
                                                       "Web\\ Data")])
    if file_path:
        filas = Utils.db_read_keywords(file_path)
        Utils.json_write(filas)
        show_success_alert()


def show_success_alert():
    messagebox.showinfo(
        "Success",
        f"Search Engines exported successfully in {Utils.BACKUP_FILE}")


def select_bw():
    print(f"Browser: {bw_sel.get()}")


# Crear la ventana principal
win = tk.Tk()
sv_ttk.set_theme("dark")
style = ttk.Style()
style.configure("TMenubutton", padding=(10, 5, 10, 5))

win.geometry("400x200")
win.title("Browser Search Engines")

# Variable para almacenar la opción seleccionada
bw_sel = tk.StringVar()

# Frame for Menu
frame = tk.Frame(win)
frame.pack(pady=10)

label = tk.Label(win, text="Close Browser before import or export")
label.pack(pady=10)

# Crear y agregar las opciones del menú radio
bws = ["chrome    ", "chromium    ", "brave    ", "edge    ", "firefox    "]
menu = ttk.OptionMenu(frame, bw_sel, bws[0], *bws, command=lambda _: select_bw)
menu.config(padding=(50, 5))
menu.pack(anchor=tk.W)

# Crear el frame para los botones
frame_botones = tk.Frame(win)
frame_botones.pack(side=tk.BOTTOM, pady=10)

# Buttons
btn_export = ttk.Button(
    frame_botones, text="Export from Browser", command=lambda: exportar(bw_sel)
)
btn_export.pack(side=tk.LEFT, padx=5)

btn_import = ttk.Button(frame_botones, text="Import into Browser", command=importar)
btn_import.pack(side=tk.RIGHT, padx=5)

# Ejecutar la win
win.mainloop()
