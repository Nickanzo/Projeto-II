from tkinter import *
from tkinter import messagebox


def btn_login():
    userName = entry0.get()
    userPass = entry1.get()


def btn_register():
    userName = entry0.get()
    userPass = entry1.get()

    if userName is "":
        messagebox.showerror("Erro","Informar usuário")
    elif ' ' in userName:
        messagebox.showwarning("Usuário Inválido", "Usuário não deve conter espaços")
    elif not userName.isalnum():
        messagebox.showwarning("Usuário Inválido", "Utilizar apenas caracteres alfanuméricos!")
    elif userPass is "":
        messagebox.showerror("Senha Inválida", "Informar uma senha!")
    else:
        messagebox.showinfo("Sucesso","Usuário registrado com sucesso!")


def limitSizeUser(*args):
    value = userName.get()
    if len(value) > 30: userName.set(value[:30])


def limitSizePass(*args):
    value = userPass.get()
    if len(value) > 16: userName.set(value[:16])


window = Tk()
window.title("Gerenciador de Acessos")
window.geometry("900x500")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=9000,
    width=5000,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(450, 250, image=background_img)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(680, 225, image=entry0_img)

userName = StringVar()
userName.trace("w", limitSizeUser)

entry0 = Entry(
    bd=0,
    bg="#c7c3f9",
    highlightthickness=0,
    justify=CENTER,
    width=30,
    textvariable=userName,
)

entry0.place(x=560, y=200, width=230, height=48)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(680, 325, image=entry1_img)

userPass = StringVar()
userPass.trace("w", limitSizePass)

entry1 = Entry(
    bd=0,
    bg="#c7c3f9",
    highlightthickness=0,
    justify=CENTER,
    show="*",
    textvariable=userPass,
)

entry1.place(
    x=560,
    y=300,
    width=230,
    height=48
)

img0 = PhotoImage(file=f"img0.png")

b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_register,
    relief="flat",
)

b0.place(
    x=570,
    y=360,
    width=102,
    height=50
)

img1 = PhotoImage(file=f"img1.png")

b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_login,
    relief="flat"
)

b1.place(
    x=694,
    y=360,
    width=102,
    height=50
)

window.resizable(False, False)
window.mainloop()
