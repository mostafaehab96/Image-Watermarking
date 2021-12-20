from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

file_name = ""
image = None
canvas_image = None


############################### IMAGE WATERMARKING #########################
def add_watermark():
    # Create an Image Object from an Image
    global image
    global canvas_image
    width, height = image.size
    draw = ImageDraw.Draw(image)
    text = watermark.get()

    font = ImageFont.truetype("Arial.ttf", 22)
    text_width, text_height = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - text_width - margin
    y = height - text_height - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    canvas_image = ImageTk.PhotoImage(image)
    canvas.create_image(300, 300, image=canvas_image)
    save_button['state'] = 'normal'
    window.focus()


############################### FILES FUNCTIONS ############################

def upload_image():
    global file_name
    global image
    save_button['state'] = 'disabled'
    file_name = filedialog.askopenfilename()
    print("Selected", file_name)
    if file_name != "":
        image = Image.open(file_name)
        image.thumbnail((600, 600), Image.ANTIALIAS)
        present_image()


def save_image():
    # Save watermarked image
    extension = file_name.split(".")[1]
    file = filedialog.asksaveasfilename(defaultextension=f"{extension}")
    if file != "":
        image.save(f'{file}')


############################### UI SETUP ################################

def present_image():
    global image
    global canvas_image
    canvas_image = ImageTk.PhotoImage(image)
    canvas.create_image(300, 300, image=canvas_image)
    watermark_btn['state'] = 'normal'


window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=500)
window.config(pady=20)
upload_button = Button(text="Upload Image", command=upload_image)
upload_button.pack()
canvas = Canvas(width=600, height=600)
canvas.pack()
watermark = Entry(width=20)
watermark.pack()
watermark_btn = Button(text="Add Watermark", state="disabled", command=add_watermark)
watermark_btn.pack()
save_button = Button(text="Save Image", command=save_image, state="disabled")
save_button.pack()
window.mainloop()
