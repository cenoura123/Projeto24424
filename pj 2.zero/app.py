import customtkinter
from tkinter import PhotoImage
from pygame import mixer
import sqlite3

class App:
  def __init__(self, window):
    self.window = window
    self.window.geometry("1600x900")
    self.window.title("TDM")
    self.window.resizable(False, False)
    self.ScreenLogin()
    self.player = None    
    
  def ScreenLogin(self):
    self.Som('./_internal/sound/entrada.mp3')
    self.imgLogin = PhotoImage(file="_internal\img/logo.png")
    self.frame_one = customtkinter.CTkFrame(master=window, width=1600, height=900,)
    self.imgLoginn = customtkinter.CTkLabel(master=self.frame_one, image=self.imgLogin, text=None)
    self.frame_one_login = customtkinter.CTkFrame(master=self.frame_one, width=599, height=900, fg_color="#142A0D")
    self.enter_login = customtkinter.CTkEntry(master=self.frame_one_login, width=266, height=65, placeholder_text="Digite Seu Usuario", fg_color="transparent", corner_radius=40)  
    self.enter_login_password = customtkinter.CTkEntry(master=self.frame_one_login, show=".", width=266, height=65, placeholder_text="Digite Sua Senha ⚿", fg_color="transparent", corner_radius=40)  
    self.enter = customtkinter.CTkButton(master=self.frame_one_login, fg_color="#96FF00",font=("Arial", 25), command=self.Click, text="Entrar", text_color="black", width=266, height=65, hover_color="#142A0D", corner_radius=40)
    self.enter_conta = customtkinter.CTkButton(master=self.frame_one_login, command=self.CreatAcount, width=266, height=65, border_color="white", fg_color="#96FF00", font=("arial", 22), text="Criar Conta", text_color="Black", hover_color="#142A0D", corner_radius=40)
    self.enter_conta.place(x=25, y=799)
    self.enter_login.place(x=25, y=66)
    self.enter_login_password.place(x=25, y=144)
    self.enter.place(x=25, y=254)
    self.imgLoginn.place(x=0, y=0)
    self.frame_one.place(x=0, y=0)
    self.frame_one_login.place(x=1289, y=0)

  def Som(self, caminho):
    mixer.init()
    som = mixer.Sound(caminho)
    som.play()
  def Click(self):
    mixer.init()
    click = mixer.Sound('./_internal/sound/click2.mp3')
    click.play()
  
  def Back_Home(self):
    self.Click()
    self.frame_CreatCont.place_forget()
    self.ScreenLogin()

  def CreatAcount(self):
    #self.Click()
    #self.frame_one.place_forget()
    self.frame_CreatCont = customtkinter.CTkFrame(master=window, width=1600, height=900, fg_color="black")
    self.Label_creatCont = customtkinter.CTkLabel(master=self.frame_CreatCont, text="Create Acount", font=("Arial", 55))
    self.frame_CreatCont2 = customtkinter.CTkFrame(master=self.frame_CreatCont, width=1600, height=750, fg_color="#96FF00", corner_radius=55)
    self.Label_Name = customtkinter.CTkLabel(master=self.frame_CreatCont2, text="Name", font=("Arial", 16), text_color="Black")
    self.Entry_Label_Name = customtkinter.CTkEntry(master=self.frame_CreatCont2, placeholder_text="Type your name", font=("Arial", 16), width=299, height=44, corner_radius=15)
    self.Label_Password = customtkinter.CTkLabel(master=self.frame_CreatCont2, text="Password", font=("Arial", 16), text_color="Black")
    self.Entry_Label_password = customtkinter.CTkEntry(master=self.frame_CreatCont2, show=".", placeholder_text="Type your password", font=("Arial", 16), width=299, height=44, corner_radius=15)
    self.Label_Confirm_Password = customtkinter.CTkLabel(master=self.frame_CreatCont2, text="Confirm Password", font=("Arial", 16), text_color="Black")
    self.Entry_Label_confirm_password = customtkinter.CTkEntry(master=self.frame_CreatCont2, show=".", placeholder_text="Confirm your password", font=("Arial", 16), width=299, height=44 , corner_radius=15)
    self.Btn_Creat_Acount = customtkinter.CTkButton(master=self.frame_CreatCont2, command=self.Criar_conta, text="Create", text_color="Black", fg_color="#228B22", width=299, height=44, hover_color="#6B8E23", font=("Arial", 16), corner_radius=15 )

    self.imgBack = PhotoImage(file="_internal/img/back.png")
    self.imgCreatecont = PhotoImage(file="_internal\img/register.png")
    
    self.imgBack = self.imgBack.subsample(5,5)
    self.imgCreatecont = self.imgCreatecont.subsample(3,3)

    self.Img_labelCreatecont = customtkinter.CTkLabel(master=self.frame_CreatCont2, image=self.imgCreatecont, text=None)
    self.Img_Label_Back = customtkinter.CTkButton(master=self.frame_CreatCont, image=self.imgBack, text=None, fg_color="transparent", hover_color="Black", command=self.Back_Home)

    self.frame_CreatCont2.place(x=0, y=210)
    self.Label_creatCont.place(x=55, y=65)
    self.Label_Name.place(x=33, y=44)
    self.Entry_Label_Name.place(x=33, y=75)
    self.Label_Password.place(x=33, y=121)
    self.Entry_Label_password.place(x=33, y=152)
    self.Label_Confirm_Password.place(x=33, y=196)
    self.Entry_Label_confirm_password.place(x=33, y=225)
    self.Btn_Creat_Acount.place(x=33, y=282)
    self.Img_labelCreatecont.place(x=777, y=0)
    self.Img_Label_Back.place(x=1422, y=65)
    self.frame_CreatCont.place(x=0, y=0)
  #BANCO DE DADOS DE CRIAR CONTA E ENTRAR EM CONTA
  def verificar_nome(self, nome):
    # Conectar ao banco de dados
    con = sqlite3.connect("./_internal/bd/tdm.db")
    cursor = con.cursor()

    # Executar a consulta SQL para verificar se o nome existe na tabela
    cursor.execute("SELECT * FROM tdm WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    con.close()

    # Se o resultado não for None, significa que o nome existe na tabela
    if resultado:
        return True
    else:
        return False
  
  def Criar_conta(self):
    self.Click()
    nome = self.Entry_Label_Name.get()
    senha = self.Entry_Label_confirm_password.get()
    senha2 = self.Entry_Label_password.get()
    #conexao com o banco dados ok!
    con = sqlite3.connect("./_internal/bd/tdm.db")
    cursor = con.cursor()
    # verification
    if nome and senha and senha2:
      if self.verificar_nome(nome):
        print("Nome Unico")
      

    #cursor.execute(f"INSERT INTO tdm (nome , senha) VALUES (?, ?)", (nome, senha))

    con.commit()




window = customtkinter.CTk()
app = App(window)
window.mainloop()


