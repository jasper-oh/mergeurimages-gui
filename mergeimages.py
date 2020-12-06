import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import basic_function as b_func
from PIL import Image

root = Tk()
root.title("Merge UR Images")
root.resizable(False, False)

# File Frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,
                      text="ADD FILE", command=b_func.add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12,
                      text="DELETE FILE", command=b_func.del_file)
btn_del_file.pack(side="right")

# List Frame & scrollbar
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand="True")
scrollbar.config(command=list_file.yview)

# Saving path Frame
path_frame = LabelFrame(root, text="SAVING PATH")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="SEARCH",
                       width=10, command=b_func.browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# Option Frame
option_frame = LabelFrame(root, text="OPTION")
option_frame.pack(padx=5, pady=5)

# Width Option
lbl_width = Label(option_frame, text="WIDTH", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# Width Option Combo
opt_width = ["Maintain", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# Margin Option
lbl_margin = Label(option_frame, text="MARGIN", width=8)
lbl_margin.pack(side="left", padx=5, pady=5)
# Margin Option Combo
opt_margin = ["None", "Narrow", "Normal", "Wide"]
cmb_margin = ttk.Combobox(option_frame, state="readonly", values=opt_margin)
cmb_margin.current(0)
cmb_margin.pack(side="left", padx=5, pady=5)

# File Format Option
lbl_format = Label(option_frame, text="FORMAT", width=8)
lbl_format.pack(side="left", padx=5, pady=5)
# File Format Option Combo
opt_format = ["PNG", "JPG", "BNP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", values=opt_format)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress Statue Frame
progress_frame = LabelFrame(root, text="PROGRESS STATUE")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progrss_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progrss_bar.pack(fill="x", padx=5, pady=5)


# Run Frame

run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text="CLOSE",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start = Button(run_frame, padx=5, pady=5, text="START",
                   width=12, command=b_func.start)
btn_start.pack(side="right", padx=5, pady=5)


root.mainloop()
