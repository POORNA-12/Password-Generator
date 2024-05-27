import random
import string
import tkinter as tk

def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def generate_password_and_show():
        try:
            length = int(entry_length.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer")
            password = generate_password(length)
            password_label.config(text=f"Your password is: {password}")
        except ValueError as e:
            password_label.config(text=str(e))
app = tk.Tk()
app.title("Password Generator")

app_width = 300
app_height = 150
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
a = (screen_width / 2) - (app_width / 2)
b = (screen_height / 2) - (app_height / 2)
app.geometry(f"{app_width}x{app_height}+{int(a)}+{int(b)}")

label_length = tk.Label(app, text="Enter the desired length of the password:")
label_length.pack()
entry_length = tk.Entry(app)
entry_length.pack()

button_generate = tk.Button(app, text="Generate Password", command=generate_password_and_show)
button_generate.pack()

password_label = tk.Label(app, text="")
password_label.pack()

app.mainloop()
