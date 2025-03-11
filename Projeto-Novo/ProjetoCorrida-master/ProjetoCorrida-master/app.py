
# AQUI NOS IMPORTAMOS AS BIBLIOTECAS USADAS
import sqlite3 #leitor de sql
from tkinter import messagebox #mensagens em caixas quando feitas ações
import customtkinter as ctk #a interface gráfica
import os #Lê arquivos internos do computador
from PIL import Image #imagens que aparecem






#  C O N F I G U R A Ç Õ E S     B Á S I C A S     D A     J A N E L A

class App(ctk.CTk): #Classe padrão da interface gráfica
    def __init__(self): #função básica da interface gráfica
        super().__init__() #init básico da interface gráfica

        self.title("Devok Softwares - versionamento personalizado") #Título na janela do windows
        self.geometry("1300x600") #Tamanho da página

        # Layout principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Caminho das imagens (pastas das imagens tem o nome 'imagens') Para nao colocar toda vez o caminha declaramos a imagem como uma variavel, daí sí chamar a variável
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens")
        # Imagens principais | self.nome_imagem = ctk.CTkImage(Image.open(os.path.join(image_path, "nome_da_imagem.png/jpeg")), size=(tamanoX por tamanhoY))
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo_sygma.png")), size=(26, 26))
        self.fundo_sygma_image = ctk.CTkImage(Image.open(os.path.join(image_path, "fundoSygma.png")), size=(800, 195))
        self.fundo_corrida_image = ctk.CTkImage(Image.open(os.path.join(image_path, "corridaSygma.png")), size=(800, 195))
        self.fundo_eventos_image = ctk.CTkImage(Image.open(os.path.join(image_path, "eventoSygma.png")), size=(800, 195))
        self.fundo_spotify_image = ctk.CTkImage(Image.open(os.path.join(image_path, "spotifySygma.png")), size=(800, 195))
        

        # Ícones dos botões de navegação (Mesmo esquema das imagens!)
        self.home_image = ctk.CTkImage(Image.open(os.path.join(image_path, "home_dark.png")), size=(20, 20))
        self.chat_image = ctk.CTkImage(Image.open(os.path.join(image_path, "chat_dark.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(Image.open(os.path.join(image_path, "add_user_dark.png")), size=(20, 20))
        self.add_spotify_image = ctk.CTkImage(Image.open(os.path.join(image_path, "spotify_dark.png")), size=(20, 20))

        # Ícones dos botões do frame Corrida (Mesmo esquema das imagens!)
        self.cadastro_image = ctk.CTkImage(Image.open(os.path.join(image_path, "corredor.png")), size=(25, 25))
        self.gerenciar_image = ctk.CTkImage(Image.open(os.path.join(image_path, "crono.png")), size=(25, 25))
        self.visualizar_image = ctk.CTkImage(Image.open(os.path.join(image_path, "tabela.png")), size=(25, 25))
        self.novo_banco_image = ctk.CTkImage(Image.open(os.path.join(image_path, "banco.png")), size=(25, 25))

        # Frame de navegação (menu lateral) COnfiguração na navegação dos frames do lado esquerdo!
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)
        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Sygma Som e Luz", image=self.logo_image, compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Botões de navegação do lado esquerdo
        self.home_button = self.create_nav_button("Centro", self.home_image, self.home_button_event, row=1)
        self.frame_2_button = self.create_nav_button("Corridas", self.chat_image, self.frame_2_button_event, row=2)
        self.frame_3_button = self.create_nav_button("Eventos", self.add_user_image, self.frame_3_button_event, row=3)
        self.frame_4_button = self.create_nav_button("Spotify", self.add_spotify_image, self.frame_4_button_event, row=4)
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # Frames das páginas (pode criar mais um frame)
        self.home_frame = self.create_home_frame()
        self.second_frame = self.create_second_frame()
        self.third_frame = self.create_third_frame()
        self.four_frame = self.create_four_frame() 

        # Definir o frame inicial (default)
        self.select_frame_by_name("home")

    def create_nav_button(self, text, image, command, row):
        """Cria um botão de navegação"""
        button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=text, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=image, anchor="w", command=command)
        button.grid(row=row, column=0, sticky="ew")
        return button
    
#------------------------------------------------------------------------------------------------------------------------   



# C R I A Ç Ã O     D A    I N T E R F A C E    G R Á F I C A 

# CENTRO NOTICIAS (OPCÃO 1)
    def create_home_frame(self):
        """Cria o frame principal (Centro)"""
        frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        # Imagem principal
        label = ctk.CTkLabel(frame, text="", image=self.fundo_sygma_image)
        label.grid(row=0, column=0, padx=20, pady=10)

        # Seção de notícias
        news_frame = ctk.CTkFrame(frame, fg_color="transparent")
        news_frame.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        title = ctk.CTkLabel(news_frame, text="Últimas Atualizações!", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        noticias = [
            (" Novo versionamento 1.0.6 do Devok Software!", "setaVermelha.png"),
            (" Implementação de leitura de banco de dados .SQL!", "setaVermelha.png"),
            (" Personalização própria para o software!", "setaVermelha.png")
        ]

        for i, (noticia, img) in enumerate(noticias):
            img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens", img)
            noticia_imagem = ctk.CTkImage(Image.open(img_path), size=(30, 30))

            news_image_label = ctk.CTkLabel(news_frame, text="", image=noticia_imagem)
            news_image_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            news_text_label = ctk.CTkLabel(news_frame, text=noticia, font=("Arial", 14))
            news_text_label.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")

        return frame
    
# CORRIDAS (OPCAO 2)
    def create_second_frame(self):
        """Cria o frame Corridas"""
        frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        # Imagem principal
        label = ctk.CTkLabel(frame, text="", image=self.fundo_corrida_image)
        label.grid(row=0, column=0, padx=20, pady=10)

        # Título abaixo da imagem
        title = ctk.CTkLabel(frame, text="Selecione uma opção abaixo!", font=("Arial", 20, "bold"))
        title.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        # Lista de opções
        options = [
            ("Cadastro de Corredor", self.cadastro_image, self.cadastro_corredor),
            ("Gerenciamento de Corrida", self.gerenciar_image, self.gerenciar_corrida),
            ("Visualizar Tabela de Corredores", self.visualizar_image, self.visualizar_tabela),
            ("Criar Novo Banco de Corrida", self.novo_banco_image, self.criar_novo_banco),
        ]

        # Criando botões com retângulos para cada opção
        for i, (text, img, command) in enumerate(options):
            # Criando botão com fundo de cor (simulando retângulo)
            btn = ctk.CTkButton(
                frame, text=text, image=img, compound="left", command=command,
                width=250, height=60, fg_color="transparent", hover_color="orange", font=("Arial", 14)
            )
            btn.grid(row=i+2, column=0, padx=20, pady=10)

        return frame

# EVENTOS (OPCAO 3)
    def create_third_frame(self):
        """Cria o frame principal (Centro)"""
        frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        # Imagem principal
        label = ctk.CTkLabel(frame, text="", image=self.fundo_eventos_image)
        label.grid(row=0, column=0, padx=20, pady=10)

        # Seção de notícias
        news_frame = ctk.CTkFrame(frame, fg_color="transparent")
        news_frame.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        title = ctk.CTkLabel(news_frame, text="Últimas Atualizações!", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        noticias = [
            (" Novo versionamento 1.0.6 do Devok Software!", "setaVermelha.png"),
            (" Implementação de leitura de banco de dados .SQL!", "setaVermelha.png"),
            (" Personalização própria para o software!", "setaVermelha.png")
        ]

        for i, (noticia, img) in enumerate(noticias):
            img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens", img)
            noticia_imagem = ctk.CTkImage(Image.open(img_path), size=(30, 30))

            news_image_label = ctk.CTkLabel(news_frame, text="", image=noticia_imagem)
            news_image_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            news_text_label = ctk.CTkLabel(news_frame, text=noticia, font=("Arial", 14))
            news_text_label.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")

        return frame


#SPOTIFY (OPCAO 4)
    def create_four_frame(self):
        """Cria o frame principal (Centro)"""
        frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        # Imagem principal
        label = ctk.CTkLabel(frame, text="", image=self.fundo_spotify_image)
        label.grid(row=0, column=0, padx=20, pady=10)

        # Seção de notícias
        news_frame = ctk.CTkFrame(frame, fg_color="transparent")
        news_frame.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        title = ctk.CTkLabel(news_frame, text="Últimas Atualizações!", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        noticias = [
            (" Novo versionamento 1.0.6 do Devok Software!", "setaVermelha.png"),
            (" Implementação de leitura de banco de dados .SQL!", "setaVermelha.png"),
            (" Personalização própria para o software!", "setaVermelha.png")
        ]

        for i, (noticia, img) in enumerate(noticias):
            img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens", img)
            noticia_imagem = ctk.CTkImage(Image.open(img_path), size=(30, 30))

            news_image_label = ctk.CTkLabel(news_frame, text="", image=noticia_imagem)
            news_image_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            news_text_label = ctk.CTkLabel(news_frame, text=noticia, font=("Arial", 14))
            news_text_label.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")

        return frame


#----------------------------------------------------------------------------------------------------------------------------------------------





# C R I A Ç Ã O     D A S     F U N Ç Õ E S    B Á S I C A S ( P O R    T R Á S    D O S   P A N O S    D A    I N T E R F A C E)
    # aqui a graxa veia come solta, pode criar a função que quiser e usar da forma que quiser




    def select_frame_by_name(self, name):
        """Alterna entre os frames"""
        for frame in [self.home_frame, self.second_frame, self.third_frame, self.four_frame]:
            frame.grid_forget()

        getattr(self, f"{name}_frame").grid(row=0, column=1, sticky="nsew")

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("second")

    def frame_3_button_event(self):
        self.select_frame_by_name("third")

    def frame_4_button_event(self):
        self.select_frame_by_name("four")

    def change_appearance_mode_event(self, new_mode):
        ctk.set_appearance_mode(new_mode)

    def cadastro_corredor(self):
        # Função para verificar se o banco de dados existe
        def banco_existe(nome_banco):
            return os.path.exists(nome_banco)   

        # Perguntar ao usuário o nome do banco de dados
        def pedir_nome_banco():
            banco_janela = ctk.CTkToplevel()  # Criar uma janela secundária
            banco_janela.geometry("400x200")
            banco_janela.title("Nome do Banco de Dados")    

            # Label e campo para o nome do banco
            label_banco = ctk.CTkLabel(banco_janela, text="Digite o nome do banco de dados:")
            label_banco.pack(pady=10)
            nome_banco = ctk.CTkEntry(banco_janela, width=300, placeholder_text="Nome do banco (ex: meu_banco.db)")
            nome_banco.pack(pady=10)    


            # Função para verificar e abrir o banco
            def verificar_banco():
                banco = nome_banco.get()
                if banco_existe(banco):
                    banco_janela.destroy()  # Fechar a janela do banco
                    cadastro(banco)  # Chamar a função de cadastro passando o nome do banco
                else:
                    aviso_label.config(text="Banco de dados não encontrado!", text_color="red") 

            # Botões de confirmação e cancelamento
            confirm_button = ctk.CTkButton(banco_janela, text="Confirmar", command=verificar_banco)
            confirm_button.pack(pady=10)    

            aviso_label = ctk.CTkLabel(banco_janela, text="", text_color="red")
            aviso_label.pack()  

            banco_janela.protocol("WM_DELETE_WINDOW", lambda: banco_janela.destroy())  # Lidar com o fechamento da janela   

            banco_janela.mainloop()  # Espera o fechamento da janela antes de continuar 

        # Função de cadastro
        def cadastro(nome_banco):
            # Criar a janela principal de cadastro
            root = ctk.CTk()
            root.geometry("800x680")
            root.title("Cadastrar o Corredor")  

            # Título principal
            titulo = ctk.CTkLabel(root, text="Cadastro de Corredor", font=("Arial", 20, "bold"))
            titulo.pack(pady=(20, 10))  

            # Número do Corredor
            titulo = ctk.CTkLabel(root, text="Número do Corredor:")
            titulo.pack(pady=(10, 0))
            numero = ctk.CTkEntry(root, width=350, placeholder_text="Digite o número do corredor...")
            numero.pack(pady=(0, 20))   

            titulo = ctk.CTkLabel(root, text="Nome do Corredor:")
            titulo.pack(pady=(10, 0))
            nome = ctk.CTkEntry(root, width=350, placeholder_text="Digite o nome do corredor...")
            nome.pack(pady=(0, 20))  


            # Data de Nascimento
            titulo = ctk.CTkLabel(root, text="Data de Nascimento do Corredor:")
            titulo.pack(pady=(10, 0))
            data_nascimento = ctk.CTkEntry(root, width=350, placeholder_text="Digite a data de nascimento... (10112005)")
            data_nascimento.pack(pady=(0, 20))  

            # Gênero
            titulo = ctk.CTkLabel(root, text="Escolha o seu gênero:")
            titulo.pack(pady=(10, 0))
            genero_var = ctk.StringVar()
            radio_masculino = ctk.CTkRadioButton(root, text="Masculino", variable=genero_var, value="Masculino")
            radio_feminino = ctk.CTkRadioButton(root, text="Feminino", variable=genero_var, value="Feminino")
            radio_masculino.pack(pady=(5, 5))
            radio_feminino.pack(pady=(0, 20))   

            # Equipe
            titulo = ctk.CTkLabel(root, text="Equipe:")
            titulo.pack(pady=(10, 0))
            equipe = ctk.CTkEntry(root, width=350, placeholder_text="Digite a equipe do corredor...")
            equipe.pack(pady=(0, 20))   

            # Número de telefone
            titulo = ctk.CTkLabel(root, text="Número de telefone:")
            titulo.pack(pady=(10, 0))
            telefone = ctk.CTkEntry(root, width=350, placeholder_text="Digite o número de telefone do corredor...")
            telefone.pack(pady=(0, 20)) 

            # Função para salvar os dados no banco de dados
            def salvar_no_banco():
                conn = sqlite3.connect(nome_banco)
                cursor = conn.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS corredores (
                    numero INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_completo TEXT NOT NULL,
                    data_nascimento DATE NOT NULL,
                    genero TEXT NOT NULL CHECK(genero IN ('Masculino', 'Feminino')),
                    equipe TEXT,
                    telefone NUMBER,
                )
                """)
                cursor.execute("INSERT INTO corredores (numero, nome, data_nascimento, genero, equipe, telefone) VALUES (?, ?, ?, ?, ?, ?)",
                               (numero.get(), data_nascimento.get(), genero_var.get(), equipe.get(), telefone.get()))
                conn.commit()
                conn.close()
                root.destroy()  # Fecha a janela após salvar    

            # Botões
            frame_botoes = ctk.CTkFrame(root)  # Usar um frame para organizar os botões
            botao_confirmar = ctk.CTkButton(frame_botoes, text="Confirmar", fg_color="blue", width=150, command=salvar_no_banco)
            botao_cancelar = ctk.CTkButton(frame_botoes, text="Cancelar", fg_color="transparent", width=150, command=root.destroy)  

            botao_confirmar.pack(side="left", padx=10)
            botao_cancelar.pack(side="left", padx=10)
            frame_botoes.pack(pady=(20, 20))    

            # Iniciar o loop principal
            root.mainloop() 

        # Chama a função para pedir o nome do banco de dados
        pedir_nome_banco()
        
    def gerenciar_corrida(self):
        print("Abrir gerenciamento de corrida")

    def visualizar_tabela(self):
        print("Abrir tabela de corredores")
    # Criação de um novo banco de corrida
    def criar_novo_banco(self):
        dialog = ctk.CTkInputDialog(text="Digite o nome do novo banco de Corrida:", title="Criar Novo Banco de Corrida")
        nome_banco = dialog.get_input()
        if nome_banco:
            nome_banco = nome_banco.strip() + ".db"
            try:
                conn = sqlite3.connect(nome_banco)
                cursor = conn.cursor()
                # Criar a tabela
                cursor.execute("""
            CREATE TABLE IF NOT EXISTS participantes (
                numero INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_completo TEXT NOT NULL,
                data_nascimento DATE NOT NULL,
                genero TEXT NOT NULL CHECK(genero IN ('Masculino', 'Feminino')),
                equipe TEXT,
                telefone TEXT,
                tempo TEXT
                );
                """)                
                messagebox.showinfo('Sucesso', message="Banco Criado com Sucesso!")
                conn.commit()
            except sqlite3.Error as e:
                messagebox.showerror('Atenção', message=f"Erro ao criar o Banco: {e}")
            finally:
                conn.close()

    
#Deixar a janela em loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
