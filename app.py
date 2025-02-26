import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Devok Softwares - versionamento personalizado")
        self.geometry("1300x600")

        # Layout principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Caminho das imagens
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens")

        # Imagens principais
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_sygma.png")), size=(26, 26))
        self.fundo_sygma_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "fundoSygma.png")), size=(800, 195))
        self.fundo_corrida_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "corridaSygma.png")), size=(800, 195))
        self.fundo_eventos_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "eventoSygma.png")), size=(800, 195))
        self.fundo_spotify_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "spotifySygma.png")), size=(800, 195))
        

        # Ícones dos botões de navegação
        self.home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_dark.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "chat_dark.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "add_user_dark.png")), size=(20, 20))
        self.add_spotify_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "spotify_dark.png")), size=(20, 20))

        # Ícones dos botões do frame Corrida
        self.cadastro_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "corredor.png")), size=(25, 25))
        self.gerenciar_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "crono.png")), size=(25, 25))
        self.visualizar_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "tabela.png")), size=(25, 25))
        self.novo_banco_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banco.png")), size=(25, 25))

        # Frame de navegação (menu lateral)
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Sygma Som e Luz", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Botões de navegação
        self.home_button = self.create_nav_button("Centro", self.home_image, self.home_button_event, row=1)
        self.frame_2_button = self.create_nav_button("Corridas", self.chat_image, self.frame_2_button_event, row=2)
        self.frame_3_button = self.create_nav_button("Eventos", self.add_user_image, self.frame_3_button_event, row=3)
        self.frame_4_button = self.create_nav_button("Spotify", self.add_spotify_image, self.frame_4_button_event, row=4)
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # Frames das páginas (pode criar mais um frame)
        self.home_frame = self.create_home_frame()
        self.second_frame = self.create_second_frame()
        self.third_frame = self.create_third_frame()
        self.four_frame = self.create_four_frame()

        # Definir o frame inicial
        self.select_frame_by_name("home")

    def create_nav_button(self, text, image, command, row):
        """Cria um botão de navegação"""
        button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=text, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=image, anchor="w", command=command)
        button.grid(row=row, column=0, sticky="ew")
        return button
# CENTRO NOTICIAS
    def create_home_frame(self):
        """Cria o frame principal (Centro)"""
        frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        # Imagem principal
        label = customtkinter.CTkLabel(frame, text="", image=self.fundo_sygma_image)
        label.grid(row=0, column=0, padx=20, pady=10)

        # Seção de notícias
        news_frame = customtkinter.CTkFrame(frame, fg_color="transparent")
        news_frame.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        title = customtkinter.CTkLabel(news_frame, text="Últimas Atualizações!", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        noticias = [
            (" Novo versionamento 1.0.6 do Devok Software!", "setaVermelha.png"),
            (" Implementação de leitura de banco de dados .SQL!", "setaVermelha.png"),
            (" Personalização própria para o software!", "setaVermelha.png")
        ]

        for i, (noticia, img) in enumerate(noticias):
            img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens", img)
            noticia_imagem = customtkinter.CTkImage(Image.open(img_path), size=(30, 30))

            news_image_label = customtkinter.CTkLabel(news_frame, text="", image=noticia_imagem)
            news_image_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            news_text_label = customtkinter.CTkLabel(news_frame, text=noticia, font=("Arial", 14))
            news_text_label.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")

        return frame
# CORRIDAS
    def create_second_frame(self):
        """Cria o frame Corridas"""
        frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        # Imagem principal
        label = customtkinter.CTkLabel(frame, text="", image=self.fundo_corrida_image)
        label.grid(row=0, column=0, padx=20, pady=10)

        # Título abaixo da imagem
        title = customtkinter.CTkLabel(frame, text="Selecione uma opção abaixo!", font=("Arial", 20, "bold"))
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
            btn = customtkinter.CTkButton(
                frame, text=text, image=img, compound="left", command=command,
                width=250, height=60, fg_color="transparent", hover_color="orange", font=("Arial", 14)
            )
            btn.grid(row=i+2, column=0, padx=20, pady=10)

        return frame

# EVENTOS
    def create_third_frame(self):
        """Cria o frame principal (Centro)"""
        frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        # Imagem principal
        label = customtkinter.CTkLabel(frame, text="", image=self.fundo_eventos_image)
        label.grid(row=0, column=0, padx=20, pady=10)

        # Seção de notícias
        news_frame = customtkinter.CTkFrame(frame, fg_color="transparent")
        news_frame.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        title = customtkinter.CTkLabel(news_frame, text="Últimas Atualizações!", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        noticias = [
            (" Novo versionamento 1.0.6 do Devok Software!", "setaVermelha.png"),
            (" Implementação de leitura de banco de dados .SQL!", "setaVermelha.png"),
            (" Personalização própria para o software!", "setaVermelha.png")
        ]

        for i, (noticia, img) in enumerate(noticias):
            img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens", img)
            noticia_imagem = customtkinter.CTkImage(Image.open(img_path), size=(30, 30))

            news_image_label = customtkinter.CTkLabel(news_frame, text="", image=noticia_imagem)
            news_image_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            news_text_label = customtkinter.CTkLabel(news_frame, text=noticia, font=("Arial", 14))
            news_text_label.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")

        return frame


#SPOTIFY
    def create_four_frame(self):
        """Cria o frame principal (Centro)"""
        frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        # Imagem principal
        label = customtkinter.CTkLabel(frame, text="", image=self.fundo_spotify_image)
        label.grid(row=0, column=0, padx=20, pady=10)

        # Seção de notícias
        news_frame = customtkinter.CTkFrame(frame, fg_color="transparent")
        news_frame.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        title = customtkinter.CTkLabel(news_frame, text="Últimas Atualizações!", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        noticias = [
            (" Novo versionamento 1.0.6 do Devok Software!", "setaVermelha.png"),
            (" Implementação de leitura de banco de dados .SQL!", "setaVermelha.png"),
            (" Personalização própria para o software!", "setaVermelha.png")
        ]

        for i, (noticia, img) in enumerate(noticias):
            img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens", img)
            noticia_imagem = customtkinter.CTkImage(Image.open(img_path), size=(30, 30))

            news_image_label = customtkinter.CTkLabel(news_frame, text="", image=noticia_imagem)
            news_image_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            news_text_label = customtkinter.CTkLabel(news_frame, text=noticia, font=("Arial", 14))
            news_text_label.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")

        return frame




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
        customtkinter.set_appearance_mode(new_mode)

    def cadastro_corredor(self):
        print("Abrir cadastro de corredor")

    def gerenciar_corrida(self):
        print("Abrir gerenciamento de corrida")

    def visualizar_tabela(self):
        print("Abrir tabela de corredores")

    def criar_novo_banco(self):
        print("Criar novo banco de corrida")


if __name__ == "__main__":
    app = App()
    app.mainloop()
