# ===============================================================================
# DAY 27: Project - Miles to KM Converter
# ===============================================================================
import tkinter as tk
from tkinter import messagebox


def calc_miles_to_km():
    val_miles = input_miles.get()
    try:
        val_km = float(val_miles) * 1.609
    except Exception as err:
        val_km = 0
        show_warning(
            title="Convert Error",
            msg="Unable to complete conversion due to KM input value.",
        )
    return round(val_km, 3)


def show_result(*args):
    input_km.delete(
        first=0,
        last=tk.END
    )
    input_km.insert(
        index=0,
        string=calc_miles_to_km()
    )
    # Select all from MILES ready for new value
    input_miles.select_range(
        start=0,
        end=tk.END
    )


def show_warning(title: str, msg: str):
    messagebox.showwarning(
        icon=messagebox.ERROR,
        message=msg,
        title=title,
    )


main_window = tk.Tk()
main_window.title("Miles to KM Converter")
main_window.minsize(
    width=300,
    height=150
)
main_window.config(
    padx=40,
    pady=40,
)
main_window.resizable(
    width=False,
    height=False
)

# Layout widgets in 3x3 grid
# [Input] Miles
input_miles = tk.Entry(
    width=10,
)
input_miles.insert(
    index=0,
    string="0.0"
)
input_miles.bind(
    sequence="<Return>",
    func=show_result
)
input_miles.bind(
    sequence="<KP_Enter>",
    func=show_result
)
input_miles.bind(
    sequence="<Return>",
    func=show_result
)
input_miles.bind(
    sequence="<KP_Enter>",
    func=show_result
)

input_miles.grid(
    column=1,
    row=0,
)
input_miles.focus_force()

# [Label] Miles
label_miles = tk.Label(
    text="Miles",
)
label_miles.grid(
    column=2,
    row=0,
)

# [Label] is equal to
label_isequalto = tk.Label(
    text="is equal to",
)
label_isequalto.grid(
    column=0,
    row=1,
)

# [Input] KM
input_km = tk.Entry(
    justify="center",
    # state="readonly",
    width=10,
)
input_km.lower()
input_km.grid(
    column=1,
    row=1,
)

# [Label] Km
label_km = tk.Label(
    text="Km",
)
label_km.grid(
    column=2,
    row=1,
)

# [Button] Calculate
btn_calculate = tk.Button(
    text="Calculate",
    command=show_result,
)
btn_calculate.grid(
    column=1,
    row=2,
)

# Keep window open
main_window.mainloop()
