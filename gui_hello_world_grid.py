# New from last
# Added sticky and anchor to allow full with labels

from tkinter import *
from PIL import ImageTk, Image
# To install Pillow use: pip install Pillow

root = Tk()
root.title('GUI Hello World!')

the_title = Label(root, text="Welcome!")
the_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W+E)

user_input = Entry(root, width=50, bg="#336699", fg="#FFFFFF", borderwidth=0)
user_input.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


def get_user_entry():
    output_text = "User entry: " + user_input.get()
    entry_output = Label(root, text=output_text, anchor=W)
    entry_output.grid(row=2, column=0, columnspan=2, sticky=W+E)


btn_get_input = Button(root, text="Get User Input", padx=10, pady=10, command=get_user_entry)
btn_get_input.grid(row=3, column=0, padx=10, pady=10)

my_image1 = ImageTk.PhotoImage(Image.open("images/Tomahawk1.jpg"))
my_image_container1 = Label(image=my_image1)
my_image_container1.grid(row=4, column=0, padx=1, pady=10)

my_image2 = ImageTk.PhotoImage(Image.open("images/Tomahawk2.jpg"))
my_image_container2 = Label(image=my_image2)
my_image_container2.grid(row=4, column=1, padx=1, pady=10)

btn_quit = Button(root, text="Quit", padx=10, pady=10, command=root.quit)
btn_quit.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
