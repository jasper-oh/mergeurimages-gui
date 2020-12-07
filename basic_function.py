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
    if folder_selected == '':
        return
    mi.txt_dest_path.delete(0, END)
    mi.txt_dest_path.insert(0, folder_selected)


def start():

    if mi.list_file.size() == 0:
        msgbox.showwarning("Warning!", "Add image file")
        return
    if len(mi.txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning!", "Select Saving Folder")
        return
    merge_image()


def merge_image():
    # Get option
    img_width = mi.cmb_width.get()
    if img_width == "Maintain":
        img_width = -1
    else:
        img_width = int(img_width)

    img_margin = mi.cmb_margin.get()
    if img_margin == "Narrow":
        img_margin = 30
    elif img_margin == "Normal":
        img_margin = 60
    elif img_margin == "Wide":
        img_margin = 90
    else:
        img_margin = 0

    images = [Image.open(x) for x in mi.list_file.get(0, END)]

    img_format = mi.cmb_format.get().lower()

    image_sizes = []
    if img_width > -1:
        image_sizes = [(int(img_width), int(
            img_width * x.size[1] / x.size[0])) for x in images]
    else:
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]

    widths, heights = zip(*(image_sizes))

    max_width, total_heights = max(widths), sum(heights)

    if img_margin > 0:
        total_heights += (img_margin * (len(images)-1))

    result_img = Image.new("RGB", (max_width, total_heights), (255, 255, 255))
    y_offset = 0  # 연속적으로 붙여주기 위해서
    # for img in images:
    #     result_img.paste(img, (0, y_offset))
    #     y_offset += img.size[1]

    for idx, img in enumerate(images):
        if img_width > -1:
            img = img.resize(image_sizes[idx])

        result_img.paste(img, (0, y_offset))
        y_offset += (img.size[1] + img_margin)

        progress = (idx + 1)/len(images) * 100
        mi.p_var.set(progress)
        mi.progrss_bar.update()

    file_name = "jasper." + img_format
    dest_path = os.path.join(mi.txt_dest_path.get(), file_name)
    result_img.save(dest_path)
    msgbox.showinfo("Alarm", "Merging is  Complete")
