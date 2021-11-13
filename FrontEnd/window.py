import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, Button
from BackEnd.modelo import validaUser, cadastraUser, login, validaBD, resgataLogins, resgataUserID


def limitSizeUser(*args):
    value = userName.get()
    if len(value) > 30: userName.set(value[:30])


def limitSizePass(*args):
    value = userPass.get()
    if len(value) > 16: userName.set(value[:16])

def userScr(name):
    global userWindow
    userWindow = Tk()
    userWindow.title("Gerenciador de Acessos")
    userWindow.geometry("900x500")
    userWindow.configure(bg="#ffffff")
    canvas = Canvas(
        userWindow,
        bg="#ffffff",
        height=9000,
        width=5000,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)


    bg_img = PhotoImage(file=f"FrontEnd/AppScreen.png")
    bg = canvas.create_image(450, 250, image=bg_img)

    welcomeUser = "Welcome " + name
    textLen = len(welcomeUser) + 200
    welcomeText = canvas.create_text(
        textLen,
        50,
        text=welcomeUser,
        font=("Arial", 20),
        fill="white",
        justify=tk.RIGHT
    )

    logins = resgataLogins(resgataUserID(name))

    addLogBtn = Button(
        userWindow,
        text = "Novo Acesso",
        width = 15,
        height = 5,
        command=btnAddLogin,
        relief = "ridge",
        activebackground = "#345",
    )

    addLogBtn.place(
        x=20,
        y=120,
    )

    print(logins)
    # if logins == 0

    userWindow.resizable(False, False)
    userWindow.mainloop()


def loginScr():
    global loginWindow
    loginWindow = Tk()
    loginWindow.title("Gerenciador de Acessos")
    loginWindow.geometry("900x500")
    loginWindow.configure(bg="#ffffff")
    canvas = Canvas(
        loginWindow,
        bg="#ffffff",
        height=9000,
        width=5000,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    bg_img = PhotoImage(file=f"FrontEnd/LoginBg.png")
    bg = canvas.create_image(450, 250, image=bg_img)

    global userName
    userName = StringVar()
    userName.trace("w", limitSizeUser)

    global textBoxUser
    textBoxUser = tk.Entry(
        bd=0,
        bg="#c7c3f9",
        highlightthickness=0,
        justify=CENTER,
        width=30,
        textvariable=userName,
    )

    textBoxUser.place(
        x=560,
        y=200,
        width=230,
        height=48
    )

    global userPass
    userPass = StringVar()
    userPass.trace("w", limitSizePass)

    global textBoxPass
    textBoxPass = tk.Entry(
        bd=0,
        bg="#c7c3f9",
        highlightthickness=0,
        justify=CENTER,
        show="*",
        textvariable=userPass,
    )

    textBoxPass.place(
        x=560,
        y=300,
        width=230,
        height=48
    )

    registerBg = PhotoImage(file=f"FrontEnd/RegisterButton.png")

    global registerBtn
    registerBtn = Button(
        image=registerBg,
        borderwidth=0,
        highlightthickness=0,
        command=btn_register,
        relief="flat",
    )

    registerBtn.place(
        x=570,
        y=360,
        width=102,
        height=50
    )

    loginBg = PhotoImage(file=f"FrontEnd/LoginButton.png")

    global loginBtn
    loginBtn = Button(
        image=loginBg,
        borderwidth=0,
        highlightthickness=0,
        command=btn_login,
        relief="flat"
    )

    loginBtn.place(
        x=694,
        y=360,
        width=102,
        height=50
    )

    loginWindow.resizable(False, False)
    loginWindow.mainloop()


def btn_login():
    userName = textBoxUser.get()
    userPass = textBoxPass.get()

    if valida_campos(userName, userPass) == True:
        if validaUser(userName) == True:
            if login(userName,userPass) == False:
                messagebox.showerror("Erro", "Senha Incorreta!")
            else:
                messagebox.showinfo("Sucesso","Login com Sucesso")
                loginWindow.destroy()
                userScr(userName)
        else:
            messagebox.showerror("Erro", "Usuário não cadastrado")

#Registrar novo usuário
def btn_register():
    userName = textBoxUser.get()
    userPass = textBoxPass.get()

    if valida_campos(userName,userPass) == True:
        validaBD()
        if validaUser(userName) == False:
            cadastraUser(userName,userPass)
            messagebox.showinfo("Sucesso","Usuário registrado com sucesso!")
        else:
            messagebox.showerror("Erro!", "Usuário já existe no sistema!")


def btnAddLogin():

    addWebLogin = tk.Tk()
    addWebLogin.title("Adiciona novo Site")
    addWebLogin.geometry("300x400")

    addWebLogin.resizable(False, False)
    # addWebLogin.mainloop()


#Valida campos de Login
def valida_campos(user,senha):
    if user == "":
        messagebox.showerror("Erro","Informar usuário!")
    elif ' ' in user:
        messagebox.showwarning("Usuário Inválido", "Usuário não deve conter espaços")
    elif not user.isalnum():
        messagebox.showwarning("Usuário Inválido", "Utilizar apenas caracteres alfanuméricos!")
    elif senha == "":
        messagebox.showerror("Senha Inválida", "Informar uma senha!")
    else:
        return True
    return False

