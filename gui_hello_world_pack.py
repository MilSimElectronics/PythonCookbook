from tkinter import *
from PIL import ImageTk, Image
# To install Pillow use: pip install Pillow

root = Tk()
root.title('GUI Hello World!')

the_title = Label(root, text="Welcome!")
the_title.pack()

user_input = Entry(root, width=50, bg="#336699", fg="#FFFFFF", borderwidth=0)
user_input.pack()


def get_user_entry():
    output_text = "User entry: " + user_input.get()
    entry_output = Label(root, text=output_text)
    entry_output.pack()


btn_get_input = Button(root, text="Get User Input", padx=10, pady=10, command=get_user_entry)
btn_get_input.pack()

my_image = ImageTk.PhotoImage(Image.open("images/Tomahawk1.jpg"))
my_image_container = Label(image=my_image)
my_image_container.pack()

btn_quit = Button(root, text="Quit", padx=10, pady=10, command=root.quit)
btn_quit.pack()

root.mainloop()
