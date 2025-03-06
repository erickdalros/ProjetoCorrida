from tkinter import messagebox
import customtkinter
import os
from PIL import Image
import sqlite3
import shutil
import pandas as pd


# CLASSE DA JANELA PRINCIAL
class App(customtkinter.CTk):
    def __init__(self): 
        super().__init__()
        self.title("Solution Business - version 1.0.1")
        self.geometry("1920x1080")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagens")
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(700, 200))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")), dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Sygma Som e Luz", compound="left", font=customtkinter.CTkFont(size=11, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # MENU INTERATIVO CANTO ESQUERDO
        self.home_button = customtkinter.CTkButton(self.navigation_frame, text="Centro", image=self.home_image, command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, text="Corridas", image=self.home_image, command=self.corridas_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, text="Manutenção", image=self.home_image, command=self.manutencao_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.create_central_buttons()

        # select default frame
        self.select_frame_by_name("home")
    #Botões da Home
    def create_central_buttons(self):
        buttons_data = [
            ("Criar novo banco", self.acao_1),
            ("Lista de corredores", self.acao_2),
            ("Inserir novo corredor", self.acao_3),
            ("Remover corredor", self.acao_4),
            ("Fazer Backup", self.acao_5)
        ]

        for i, (text, command) in enumerate(buttons_data, start=1):
            btn = customtkinter.CTkButton(self.home_frame, text=text, command=command)
            btn.grid(row=i, column=0, padx=20, pady=5)

    def select_frame_by_name(self, name):
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def corridas_button_event(self):
        self.select_frame_by_name("home")

    def manutencao_button_event(self):
        self.select_frame_by_name("home")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)



    
    def acao_1(self):
        dialog = customtkinter.CTkInputDialog(text="Digite o nome do novo banco de Carrida:", title="Criar Novo Banco de Corrida")
        nome_banco = dialog.get_input()
        if nome_banco:
            nome_banco = nome_banco.strip() + ".sql"
            try:
                conn = sqlite3.connect(nome_banco)
                cursor = conn.cursor()
                # Criar a tabela
                cursor.execute("""
                    CREATE TABLE corredores (
                        Numero INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nome_Completo TEXT NOT NULL,
                        Data_Nascimento DATE NOT NULL,
                        Genero TEXT CHECK(Genero IN ('Masculino', 'Feminino')) NOT NULL,
                        Equipe TEXT,
                        Telefone TEXT
                );
                """)                
                messagebox.showinfo('Sucesso', message="Banco Criado com Sucesso!")
                conn.commit()
            except sqlite3.Error as e:
                messagebox.showerror('Atenção', message=f"Erro ao criar o Banco: {e}")
            finally:
                conn.close()

    def acao_2(self):
        # Diálogo para inserir o nome do banco de dados
        dialog = customtkinter.CTkInputDialog(text="Digite o nome do banco para visualizar:", title="Visualizar Corredores")
        banco = dialog.get_input().strip() + ".sql"

        # Verifica se o banco de dados existe
        if not os.path.exists(banco):
            messagebox.showerror('Atenção', message="O banco não existe, verifique se você digitou corretamente o nome do banco!")
            return

        try:
            # Conectar ao banco de dados
            conn = sqlite3.connect(banco)
 
            # Consultar os dados da tabela 'corredores' utilizando pandas
            query = "SELECT * FROM corredores"
            df = pd.read_sql_query(query, conn)

            # Criar a estrutura da tabela na interface se não existir
            if not hasattr(self, 'frame_tabela'):
                self.frame_tabela = customtkinter.CTkFrame(self.home_frame)
                self.frame_tabela.grid(row=1, column=0, padx=20, pady=20)

            # Limpar qualquer dado anterior na interface
            for widget in self.frame_tabela.winfo_children():
                widget.destroy()

            # Exibir os cabeçalhos das colunas
            for col, cabecalho in enumerate(df.columns):
                customtkinter.CTkLabel(self.frame_tabela, text=cabecalho, font=("Arial", 10, "bold")).grid(row=0, column=col, padx=5, pady=5)

            # Exibir os dados das linhas
            for i, row in df.iterrows():
                for j, valor in enumerate(row):
                    customtkinter.CTkLabel(self.frame_tabela, text=str(valor), width=20).grid(row=i + 1, column=j, padx=5, pady=5)

            conn.close()

        except sqlite3.Error as e:
            messagebox.showerror('Atenção', message=f"Erro ao acessar o banco '{banco}': {e}")



    def acao_3(self):
        dialog = customtkinter.CTkInputDialog(text="Digite o nome do banco para inserir o corredor:", title="Inserir Corredor")
        banco = dialog.get_input().strip() + ".sql"

        if not os.path.exists(banco):
            messagebox.showerror("Atenção", message=f"Não existe nenhum banco com o nome {banco}")
            return

        try:
            conn = sqlite3.connect(banco)
            cursor = conn.cursor()


            # Captura os dados do corredor
            nome_dialog = customtkinter.CTkInputDialog(text="Digite o nome do corredor:", title="Nome Corredor")
            nome = nome_dialog.get_input().strip()

            idade_dialog = customtkinter.CTkInputDialog(text="Digite a idade do corredor:", title="Idade Corredor")
            idade = int(idade_dialog.get_input().strip())

            ano_nascimento_dialog = customtkinter.CTkInputDialog(text="Digite o ano de nascimento do corredor:", title="Ano de Nascimento")
            ano_nascimento = int(ano_nascimento_dialog.get_input().strip())

            genero_dialog = customtkinter.CTkInputDialog(text="Digite o gênero (Masculino, Feminino, Outro):", title="Gênero")
            genero = genero_dialog.get_input().strip()

            tipo_sanguineo_dialog = customtkinter.CTkInputDialog(text="Digite o tipo sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-):", title="Tipo Sanguíneo")
            tipo_sanguineo = tipo_sanguineo_dialog.get_input().strip()

            altura_dialog = customtkinter.CTkInputDialog(text="Digite a altura (em metros):", title="Altura")
            altura = float(altura_dialog.get_input().strip())

            peso_dialog = customtkinter.CTkInputDialog(text="Digite o peso (em kg):", title="Peso")
            peso = float(peso_dialog.get_input().strip())

            cpf_rg_dialog = customtkinter.CTkInputDialog(text="Digite o CPF ou RG:", title="CPF ou RG")
            cpf_rg = cpf_rg_dialog.get_input().strip()

            contato_emergencia_dialog = customtkinter.CTkInputDialog(text="Digite o contato de emergência:", title="Contato Emergência")
            contato_emergencia = contato_emergencia_dialog.get_input().strip()

            problemas_saude_dialog = customtkinter.CTkInputDialog(text="Digite os problemas de saúde (se houver):", title="Problemas de Saúde")
            problemas_saude = problemas_saude_dialog.get_input().strip()

            categoria_dialog = customtkinter.CTkInputDialog(text="Digite a categoria (Amador, Profissional, Maratonista, Velocista):", title="Categoria")
            categoria = categoria_dialog.get_input().strip()

            tempo_corrida_dialog = customtkinter.CTkInputDialog(text="Digite o tempo total de corrida (HH:MM:SS):", title="Tempo Corrida")
            tempo_corrida = tempo_corrida_dialog.get_input().strip()

            cidade_dialog = customtkinter.CTkInputDialog(text="Digite a cidade:", title="Cidade")
            cidade = cidade_dialog.get_input().strip()

            telefone_dialog = customtkinter.CTkInputDialog(text="Digite o telefone:", title="Telefone")
            telefone = telefone_dialog.get_input().strip()

            email_dialog = customtkinter.CTkInputDialog(text="Digite o email:", title="Email")
            email = email_dialog.get_input().strip()


            cursor.execute("""
                INSERT INTO corredores (Nome, Idade, Ano_Nascimento, Genero, Tipo_Sanguineo, Altura, Peso, CPF_RG, Contato_Emergencia, 
                                       Problemas_Saude, Categoria, Tempo_Total_Corrida, Cidade, Telefone, Email)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nome, idade, ano_nascimento, genero, tipo_sanguineo, altura, peso, cpf_rg, contato_emergencia, problemas_saude, categoria, tempo_corrida, cidade, telefone, email))

            conn.commit()
            print("Corredor inserido com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao inserir corredor: {e}")
        finally:
            conn.close()

    def acao_4(self):
        dialog = customtkinter.CTkInputDialog(text="Digite o nome do banco para remover o corredor:", title="Remover Corredor")
        banco = dialog.get_input().strip() + ".sql"

        if not os.path.exists(banco):
            print(f"O banco '{banco}' não existe!")
            return

        try:
            conn = sqlite3.connect(banco)
            cursor = conn.cursor()

            corredor_id = int(input("Digite o ID do corredor a ser removido: "))

            cursor.execute("SELECT * FROM corredores WHERE ID = ?", (corredor_id,))
            if cursor.fetchone() is None:
                print(f"Corredor com ID {corredor_id} não encontrado.")
                return

            cursor.execute("DELETE FROM corredores WHERE ID = ?", (corredor_id,))
            conn.commit()
            print(f"Corredor ID {corredor_id} removido com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao remover corredor: {e}")
        finally:
            conn.close()

    def acao_5(self):
        pasta_origem = os.getcwd()
        pasta_backup = os.path.join(pasta_origem, "backupBancos")

        if not os.path.exists(pasta_backup):
            os.makedirs(pasta_backup)

        arquivos_sql = [f for f in os.listdir(pasta_origem) if f.endswith(".sql")]

        if not arquivos_sql:
            print("Não há arquivos do banco para fazer backup.")
            return

        for arquivo in arquivos_sql:
            origem = os.path.join(pasta_origem, arquivo)
            destino = os.path.join(pasta_backup, arquivo)
            shutil.copy2(origem, destino)
            print(f"Arquivo '{arquivo}' copiado para o backup.")

        print(f"Backup concluído. {len(arquivos_sql)} arquivos foram copiados para '{pasta_backup}'.")


if __name__ == "__main__":
    app = App()
    app.mainloop()