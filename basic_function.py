import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import mergeimages as mi
from PIL import Image
import os


def add_file():
    files = filedialog.askopenfilenames(title="Select Image File", filetypes=(
        ("PNG File", "*.png"), ("Every file", "*.*")), initialdir="C:/")

    for file in files:
        mi.list_file.insert(END, file)


def del_file():
    for index in reversed(mi.list_file.curselection()):
        mi.list_file.delete(index)


def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        return
    mi.txt_dest_path.delete(0, END)
    mi.txt_dest_path.insert(0, folder_selected)


def start():
    print("Width : ", mi.cmb_width.get())
    print("mergin : ", mi.cmb_margin.get())
    print("format : ", mi.cmb_format.get())
    if mi.list_file.size() == 0:
        msgbox.showwarning("Warning!", "Add image file")
        return
    if len(mi.txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning!", "Select Saving Folder")
        return
    merge_image()


def merge_image():
    # Get option
    img_widths = mi.cmb_width.get()

    images = [Image.open(x) for x in mi.list_file.get(0, END)]
    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]

    # widths , heights = zip(*(x.size for x in images)) above two code could be change to this one code

    max_width, total_heights = max(widths), sum(heights)

    result_img = Image.new("RGB", (max_width, total_heights), (255, 255, 255))
    y_offset = 0  # 연속적으로 붙여주기 위해서
    # for img in images:
    #     result_img.paste(img, (0, y_offset))
    #     y_offset += img.size[1]

    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx + 1)/len(images) * 100
        mi.p_var.set(progress)
        mi.progrss_bar.update()

    dest_path = os.path.join(mi.txt_dest_path.get(), "jasper.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("Alarm", "Merging is  Complete")
