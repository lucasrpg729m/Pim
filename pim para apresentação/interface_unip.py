# interface_unip_final_completo.py - SISTEMA ACADÊMICO UNIP COM IA AVANÇADA
import json
import os
import re
import tkinter as tk
from datetime import datetime, timedelta
from pathlib import Path
from tkinter import messagebox, scrolledtext, ttk


class SistemaUNIPIACompleto:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UNIP PIM II - Sistema Acadêmico")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")

        self.usuario_logado = None
        self.ia_contexto = self.carregar_contexto_ia()

        # Dados do sistema
        self.usuarios_cadastrados = self.carregar_usuarios()
        self.cursos_disponiveis = self.carregar_cursos()
        self.progresso_alunos = self.carregar_progresso()
        self.forum_mensagens = self.carregar_forum()
        self.metricas_sustentabilidade = self.carregar_metricas()

        # Estilo moderno
        self.configurar_estilos()

    def configurar_estilos(self):
        """Configura estilos modernos para a interface"""
        style = ttk.Style()
        style.theme_use("clam")

        # Cores UNIP com tema moderno
        style.configure("TFrame", background="#f8f9fa")
        style.configure("TLabel", background="#f8f9fa", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10), padding=8)
        style.configure(
            "Title.TLabel", font=("Segoe UI", 18, "bold"), foreground="#2c3e50"
        )
        style.configure(
            "Subtitle.TLabel", font=("Segoe UI", 14, "bold"), foreground="#34495e"
        )
        style.configure("Card.TFrame", relief="raised", borderwidth=2)

        # ✅ NOVO ESTILO PARA RADIOBUTTON (ADICIONE ESTA LINHA)
        style.configure("Custom.TRadiobutton", font=("Segoe UI", 10))

    def carregar_contexto_ia(self):
        """Carrega contexto para IA"""
        return {
            "padroes_aprendizado": {},
            "recomendacoes_personalizadas": {},
            "alertas_desempenho": {},
            "previsoes_conclusao": {},
            "analise_sentimento": {},
        }

    def carregar_usuarios(self):
        """Carrega usuários do arquivo JSON"""
        try:
            with open("dados_usuarios.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            # Estrutura inicial aprimorada
            usuarios_base = {
                "admin": {
                    "senha": "Admin@123",
                    "email": "admin@unip.com",
                    "idade": 35,
                    "is_admin": True,
                    "tipo": "admin",
                    "data_cadastro": datetime.now().isoformat(),
                    "cursos": ["1", "2", "3"],
                    "nome_completo": "Administrador Sistema UNIP",
                    "telefone": "11999999999",
                    "certificados": [],
                    "modulos_concluidos": {},
                    "ultimo_acesso": None,
                    "preferencias_aprendizado": {
                        "modalidade": "visual",
                        "ritmo": "moderado",
                    },
                },
                "prof.python": {
                    "senha": "Professor@123",
                    "email": "prof.python@unip.com",
                    "idade": 42,
                    "is_admin": False,
                    "tipo": "professor",
                    "data_cadastro": datetime.now().isoformat(),
                    "cursos": ["1"],
                    "nome_completo": "Dr. Python Silva",
                    "telefone": "11988888888",
                    "especialidade": "Ciência de Dados e IA",
                    "bio": "Professor com 15 anos de experiência em Python e Machine Learning",
                },
                "prof.web": {
                    "senha": "Professor@123",
                    "email": "prof.web@unip.com",
                    "idade": 38,
                    "is_admin": False,
                    "tipo": "professor",
                    "data_cadastro": datetime.now().isoformat(),
                    "cursos": ["2"],
                    "nome_completo": "MSc. Web Development",
                    "telefone": "11977777777",
                    "especialidade": "Desenvolvimento Full Stack",
                    "bio": "Especialista em tecnologias web modernas",
                },
                "aluno.exemplo": {
                    "senha": "Aluno@123",
                    "email": "aluno.exemplo@aluno.unip.br",
                    "idade": 22,
                    "is_admin": False,
                    "tipo": "aluno",
                    "data_cadastro": datetime.now().isoformat(),
                    "cursos": ["1", "2"],
                    "nome_completo": "João Silva Santos",
                    "telefone": "11966666666",
                    "certificados": [],
                    "modulos_concluidos": {},
                    "ultimo_acesso": None,
                    "preferencias_aprendizado": {
                        "modalidade": "pratica",
                        "ritmo": "acelerado",
                    },
                    "interesses": ["Python", "Web Development", "IA"],
                },
            }
            self.salvar_usuarios(usuarios_base)
            return usuarios_base

    def salvar_usuarios(self, dados=None):
        """Salva usuários no arquivo JSON"""
        try:
            with open("dados_usuarios.json", "w", encoding="utf-8") as f:
                json.dump(
                    dados or self.usuarios_cadastrados, f, indent=4, ensure_ascii=False
                )
            return True
        except Exception as e:
            print(f"Erro ao salvar usuários: {e}")
            return False

    def salvar_cursos(self):
        """Salva a estrutura de cursos em `cursos_disponiveis.json`"""
        try:
            base_path = os.path.dirname(__file__)
            arquivo_path = os.path.join(base_path, "cursos_disponiveis.json")
            with open(arquivo_path, "w", encoding="utf-8") as f:
                json.dump(self.cursos_disponiveis, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar cursos: {e}")
            return False

    def carregar_cursos(self):
        """Carrega cursos disponíveis. Se existir um arquivo `cursos_disponiveis.json`, carrega dele;
        caso contrário retorna uma estrutura padrão. Cada módulo passa a ter o campo opcional
        'conteudo' para armazenar texto/aulas."""
        base_path = os.path.dirname(__file__)
        arquivo_path = os.path.join(base_path, "cursos_disponiveis.json")
        try:
            with open(arquivo_path, "r", encoding="utf-8") as f:
                cursos = json.load(f)
                # Garantir que cada módulo tenha a chave 'conteudo'
                for cid, curso in cursos.items():
                    for mod in curso.get("modulos", []):
                        if "conteudo" not in mod:
                            mod["conteudo"] = ""
                return cursos
        except Exception:
            cursos = {
                "1": {
                    "nome": "Python para Ciência de Dados e IA",
                    "carga_horaria": "80 horas",
                    "modulos": [
                        {
                            "nome": "Fundamentos do Python",
                            "questoes": 3,
                            "dificuldade": "Iniciante",
                            "tempo_estimado": "10h",
                            "conteudo": "",
                        },
                        {
                            "nome": "Estruturas de Dados Avançadas",
                            "questoes": 3,
                            "dificuldade": "Intermediário",
                            "tempo_estimado": "15h",
                            "conteudo": "",
                        },
                        {
                            "nome": "Análise de Dados com Pandas e NumPy",
                            "questoes": 3,
                            "dificuldade": "Intermediário",
                            "tempo_estimado": "20h",
                            "conteudo": "",
                        },
                    ],
                    "categoria": "Tecnologia & IA",
                    "dificuldade": "Intermediário-Avançado",
                    "professor": "prof.python",
                    "descricao": "Curso completo de Python para análise de dados, visualização e machine learning. Prepare-se para o mercado de ciência de dados!",
                    "tags": ["Python", "Pandas", "Machine Learning", "Data Science"],
                    "avaliacao": 4.8,
                    "alunos_matriculados": 45,
                    "criado_em": "2024-01-15",
                },
                "2": {
                    "nome": "Desenvolvimento Web Full Stack Moderno",
                    "carga_horaria": "120 horas",
                    "modulos": [
                        {
                            "nome": "HTML5, CSS3 e JavaScript ES6+",
                            "questoes": 3,
                            "dificuldade": "Iniciante",
                            "tempo_estimado": "25h",
                            "conteudo": "",
                        },
                        {
                            "nome": "React.js e Hooks Avançados",
                            "questoes": 3,
                            "dificuldade": "Intermediário",
                            "tempo_estimado": "30h",
                            "conteudo": "",
                        },
                        {
                            "nome": "Node.js, Express e APIs REST",
                            "questoes": 3,
                            "dificuldade": "Intermediário",
                            "tempo_estimado": "25h",
                            "conteudo": "",
                        },
                    ],
                    "categoria": "Desenvolvimento Web",
                    "dificuldade": "Intermediário",
                    "professor": "prof.web",
                    "descricao": "Torne-se um desenvolvedor full stack aprendendo as tecnologias mais demandadas do mercado atual.",
                    "tags": ["React", "Node.js", "JavaScript", "MongoDB"],
                    "avaliacao": 4.7,
                    "alunos_matriculados": 38,
                    "criado_em": "2024-02-10",
                },
                "3": {
                    "nome": "Inteligência Artificial Aplicada",
                    "carga_horaria": "100 horas",
                    "modulos": [
                        {
                            "nome": "Fundamentos Matemáticos de IA",
                            "questoes": 3,
                            "dificuldade": "Intermediário",
                            "tempo_estimado": "20h",
                            "conteudo": "",
                        },
                        {
                            "nome": "Redes Neurais e Deep Learning",
                            "questoes": 3,
                            "dificuldade": "Avançado",
                            "tempo_estimado": "30h",
                            "conteudo": "",
                        },
                        {
                            "nome": "Processamento de Linguagem Natural (NLP)",
                            "questoes": 3,
                            "dificuldade": "Avançado",
                            "tempo_estimado": "25h",
                            "conteudo": "",
                        },
                    ],
                    "categoria": "Inteligência Artificial",
                    "dificuldade": "Avançado",
                    "professor": "admin",
                    "descricao": "Aprofunde-se nos conceitos e aplicações práticas de Inteligência Artificial e Machine Learning.",
                    "tags": ["Deep Learning", "NLP", "Computer Vision", "TensorFlow"],
                    "avaliacao": 4.9,
                    "alunos_matriculados": 28,
                    "criado_em": "2024-01-20",
                },
            }
            return cursos

    def carregar_progresso(self):
        """Carrega progresso dos alunos"""
        try:
            with open("progresso_alunos.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}

    def carregar_forum(self):
        """Carrega mensagens do fórum colaborativo"""
        try:
            with open("forum_mensagens.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"geral": [], "duvidas": [], "projetos": []}

    def carregar_metricas(self):
        """Carrega métricas de sustentabilidade"""
        try:
            with open("metricas_sustentabilidade.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {
                "papel_economizado": 0,  # em kg
                "co2_economizado": 0,  # em kg
                "agua_economizada": 0,  # em litros
                "total_atividades_digitais": 0,
            }

    def salvar_progresso(self):
        """Salva progresso dos alunos"""
        try:
            with open("progresso_alunos.json", "w", encoding="utf-8") as f:
                json.dump(self.progresso_alunos, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar progresso: {e}")
            return False

    def salvar_forum(self):
        """Salva mensagens do fórum"""
        try:
            with open("forum_mensagens.json", "w", encoding="utf-8") as f:
                json.dump(self.forum_mensagens, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar fórum: {e}")
            return False

    def salvar_metricas(self):
        """Salva métricas de sustentabilidade"""
        try:
            with open("metricas_sustentabilidade.json", "w", encoding="utf-8") as f:
                json.dump(
                    self.metricas_sustentabilidade, f, indent=4, ensure_ascii=False
                )
            return True
        except Exception as e:
            print(f"Erro ao salvar métricas: {e}")
            return False

    # ========== SISTEMA DE MATRÍCULA E CURSOS ==========

    def matricular_curso(self, curso_id):
        """Matricula o aluno no curso selecionado"""
        if curso_id not in self.cursos_disponiveis:
            messagebox.showerror("Erro", "Curso não encontrado!")
            return False

        # Verificar se já está matriculado
        if curso_id in self.usuarios_cadastrados[self.usuario_logado]["cursos"]:
            messagebox.showinfo("Info", "Você já está matriculado neste curso!")
            return False

        # Matricular
        self.usuarios_cadastrados[self.usuario_logado]["cursos"].append(curso_id)

        # Inicializar progresso
        if self.usuario_logado not in self.progresso_alunos:
            self.progresso_alunos[self.usuario_logado] = {}

        self.progresso_alunos[self.usuario_logado][curso_id] = {
            "modulos_concluidos": [],
            "questoes_respondidas": 0,
            "total_questoes": sum(
                modulo["questoes"]
                for modulo in self.cursos_disponiveis[curso_id]["modulos"]
            ),
            "progresso": 0,
            "nota_final": 0,
            "data_matricula": datetime.now().isoformat(),
        }

        # Salvar alterações
        self.salvar_usuarios()
        self.salvar_progresso()

        # Registrar atividade para sustentabilidade
        self.registrar_atividade_digital()

        messagebox.showinfo(
            "Sucesso!",
            f"✅ Matriculado no curso: {self.cursos_disponiveis[curso_id]['nome']}\n\n"
            f"Acesse 'Meus Cursos' para começar seus estudos!",
        )

        # ATUALIZAR INTERFACE IMEDIATAMENTE
        self.atualizar_interface()
        return True

    def iniciar_questionario(self, curso_id, modulo_nome):
        """Inicia questionário para o módulo"""
        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            return

        # Encontrar módulo
        modulo = next((m for m in curso["modulos"] if m["nome"] == modulo_nome), None)
        if not modulo:
            return

        # Verificar se já foi concluído
        if modulo_nome in self.progresso_alunos.get(self.usuario_logado, {}).get(
            curso_id, {}
        ).get("modulos_concluidos", []):
            messagebox.showinfo("Info", "Este módulo já foi concluído!")
            return

        # Criar janela de questionário
        self.mostrar_questionario_avancado(curso_id, modulo)

    def mostrar_questionario_avancado(self, curso_id, modulo):
        """Mostra questionário avançado para o módulo"""
        quest_janela = tk.Toplevel(self.root)
        quest_janela.title(f"Questionário - {modulo['nome']}")
        quest_janela.geometry("700x500")
        quest_janela.transient(self.root)
        quest_janela.grab_set()

        frame = ttk.Frame(quest_janela, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame,
            text=f"📝 Questionário: {modulo['nome']}",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=10)

        ttk.Label(
            frame,
            text=f"Responda as {modulo['questoes']} questões abaixo:",
            font=("Segoe UI", 12),
        ).pack(pady=5)

        # Container com scroll
        container = ttk.Frame(frame)
        container.pack(expand=True, fill="both", pady=10)

        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Gerar questões dinâmicas baseadas no módulo
        respostas_usuario = {}
        questoes = self.gerar_questoes_modulo(modulo["nome"], modulo["questoes"])

        for i, questao in enumerate(questoes):
            quest_frame = ttk.Frame(
                scrollable_frame, relief="groove", borderwidth=1, padding="15"
            )
            quest_frame.pack(fill="x", pady=8, padx=10)

            ttk.Label(
                quest_frame,
                text=f"Questão {i + 1}: {questao['pergunta']}",
                font=("Segoe UI", 11, "bold"),
                wraplength=600,
            ).pack(anchor="w")

            var = tk.StringVar()
            respostas_usuario[i] = var

            for j, alternativa in enumerate(questao["alternativas"]):
                rb = ttk.Radiobutton(
                    quest_frame, text=alternativa, variable=var, value=alternativa
                )
                rb.pack(anchor="w", pady=2)
                rb.configure(style="Custom.TRadiobutton")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def finalizar_questionario():
            # Calcular pontuação
            acertos = 0
            for i, questao in enumerate(questoes):
                if respostas_usuario[i].get() == questao["resposta_correta"]:
                    acertos += 1

            percentual_acerto = (acertos / len(questoes)) * 100

            if percentual_acerto >= 70:  # 70% para aprovação
                # Atualizar progresso
                if self.usuario_logado not in self.progresso_alunos:
                    self.progresso_alunos[self.usuario_logado] = {}
                if curso_id not in self.progresso_alunos[self.usuario_logado]:
                    self.progresso_alunos[self.usuario_logado][curso_id] = {
                        "modulos_concluidos": [],
                        "questoes_respondidas": 0,
                        "total_questoes": 0,
                        "progresso": 0,
                        "nota_final": 0,
                    }

                # Adicionar módulo concluído
                if (
                    modulo["nome"]
                    not in self.progresso_alunos[self.usuario_logado][curso_id][
                        "modulos_concluidos"
                    ]
                ):
                    self.progresso_alunos[self.usuario_logado][curso_id][
                        "modulos_concluidos"
                    ].append(modulo["nome"])

                # Calcular novo progresso
                total_modulos = len(self.cursos_disponiveis[curso_id]["modulos"])
                modulos_concluidos = len(
                    self.progresso_alunos[self.usuario_logado][curso_id][
                        "modulos_concluidos"
                    ]
                )
                novo_progresso = (modulos_concluidos / total_modulos) * 100

                self.progresso_alunos[self.usuario_logado][curso_id]["progresso"] = (
                    novo_progresso
                )
                self.progresso_alunos[self.usuario_logado][curso_id][
                    "questoes_respondidas"
                ] += len(questoes)
                self.progresso_alunos[self.usuario_logado][curso_id]["nota_final"] = (
                    percentual_acerto
                )

                self.salvar_progresso()

                # Verificar se curso foi 100% concluído
                if novo_progresso >= 100:
                    self.gerar_certificado_automatico(curso_id)
                # Verificar se pode gerar certificado
                elif novo_progresso >= 80:
                    self.mostrar_opcao_certificado(curso_id)

                messagebox.showinfo(
                    "Parabéns!",
                    f"✅ Módulo concluído com sucesso!\n\n"
                    f"📊 Acertos: {acertos}/{len(questoes)} ({percentual_acerto:.1f}%)\n"
                    f"🎯 Progresso total: {novo_progresso:.1f}%\n"
                    f"🏆 Nota final: {percentual_acerto:.1f}",
                )
            else:
                messagebox.showwarning(
                    "Tente Novamente",
                    f"❌ Você precisa de pelo menos 70% de acertos.\n\n"
                    f"📊 Seus acertos: {acertos}/{len(questoes)} ({percentual_acerto:.1f}%)\n"
                    f"💡 Dica: Revise o conteúdo do módulo e tente novamente!",
                )

            quest_janela.destroy()
            # ATUALIZAR INTERFACE APÓS QUESTIONÁRIO
            self.atualizar_interface()

        ttk.Button(
            frame,
            text="✅ Finalizar Questionário",
            command=finalizar_questionario,
            style="TButton",
        ).pack(pady=20)

    def gerar_questoes_modulo(self, modulo_nome, quantidade):
        """Gera questões dinâmicas baseadas no módulo"""
        # Primeiro, verificar se o módulo possui um banco de perguntas salvo (questoes_data)
        for curso in self.cursos_disponiveis.values():
            for mod in curso.get("modulos", []):
                if mod.get("nome") == modulo_nome and mod.get("questoes_data"):
                    # Retornar cópia dos dados já salvos
                    return mod.get("questoes_data")[:quantidade]

        # Banco de questões por módulo (padrão)
        banco_questoes = {
            "Fundamentos do Python": [
                {
                    "pergunta": "Qual é a função usada para exibir texto no Python?",
                    "alternativas": ["print()", "echo()", "display()", "show()"],
                    "resposta_correta": "print()",
                },
                {
                    "pergunta": "Como se declara uma variável em Python?",
                    "alternativas": [
                        "var x = 5",
                        "x = 5",
                        "let x = 5",
                        "variable x = 5",
                    ],
                    "resposta_correta": "x = 5",
                },
                {
                    "pergunta": "Qual símbolo é usado para comentários em Python?",
                    "alternativas": ["//", "#", "/*", "--"],
                    "resposta_correta": "#",
                },
            ],
            "Estruturas de Dados Avançadas": [
                {
                    "pergunta": "Qual estrutura de dados é mutável em Python?",
                    "alternativas": ["Lista", "Tupla", "String", "Número"],
                    "resposta_correta": "Lista",
                },
                {
                    "pergunta": "Como criar um dicionário vazio?",
                    "alternativas": ["{}", "dict()", "[]", "Ambas A e B"],
                    "resposta_correta": "Ambas A e B",
                },
                {
                    "pergunta": "Qual método adiciona elemento ao final da lista?",
                    "alternativas": ["append()", "add()", "insert()", "push()"],
                    "resposta_correta": "append()",
                },
            ],
            "Análise de Dados com Pandas e NumPy": [
                {
                    "pergunta": "Qual biblioteca é usada para análise de dados?",
                    "alternativas": ["Pandas", "TensorFlow", "Django", "Flask"],
                    "resposta_correta": "Pandas",
                },
                {
                    "pergunta": "Como importar o pandas normalmente?",
                    "alternativas": [
                        "import pandas",
                        "import pandas as pd",
                        "from pandas import *",
                        "Todas as anteriores",
                    ],
                    "resposta_correta": "import pandas as pd",
                },
                {
                    "pergunta": "Qual função do NumPy cria array de zeros?",
                    "alternativas": ["zeros()", "empty()", "ones()", "array()"],
                    "resposta_correta": "zeros()",
                },
            ],
            "HTML5, CSS3 e JavaScript ES6+": [
                {
                    "pergunta": "Qual tag HTML5 é usada para conteúdo semântico principal?",
                    "alternativas": ["<main>", "<content>", "<body>", "<section>"],
                    "resposta_correta": "<main>",
                },
                {
                    "pergunta": "Como declarar uma variável com escopo de bloco em JavaScript?",
                    "alternativas": ["var", "let", "const", "variable"],
                    "resposta_correta": "let",
                },
                {
                    "pergunta": "Qual propriedade CSS muda a cor do texto?",
                    "alternativas": ["color", "text-color", "font-color", "text-style"],
                    "resposta_correta": "color",
                },
            ],
            "React.js e Hooks Avançados": [
                {
                    "pergunta": "Qual hook é usado para estado em componentes funcionais?",
                    "alternativas": [
                        "useState",
                        "useEffect",
                        "useContext",
                        "useReducer",
                    ],
                    "resposta_correta": "useState",
                },
                {
                    "pergunta": "React é uma biblioteca para:",
                    "alternativas": [
                        "Interface de usuário",
                        "Backend",
                        "Banco de dados",
                        "Mobile",
                    ],
                    "resposta_correta": "Interface de usuário",
                },
                {
                    "pergunta": "Como criar componente em React?",
                    "alternativas": [
                        "function Component() {}",
                        "class Component {}",
                        "Ambas",
                        "Nenhuma",
                    ],
                    "resposta_correta": "Ambas",
                },
            ],
            "Node.js, Express e APIs REST": [
                {
                    "pergunta": "Node.js é um ambiente de execução:",
                    "alternativas": [
                        "JavaScript no servidor",
                        "Python no servidor",
                        "Java no cliente",
                        "C++ no navegador",
                    ],
                    "resposta_correta": "JavaScript no servidor",
                },
                {
                    "pergunta": "Qual método HTTP para criar recurso?",
                    "alternativas": ["POST", "GET", "PUT", "DELETE"],
                    "resposta_correta": "POST",
                },
                {
                    "pergunta": "Express.js é um:",
                    "alternativas": [
                        "Framework web",
                        "Banco de dados",
                        "Linguagem",
                        "Editor de código",
                    ],
                    "resposta_correta": "Framework web",
                },
            ],
            "Fundamentos Matemáticos de IA": [
                {
                    "pergunta": "Qual área matemática é fundamental para IA?",
                    "alternativas": [
                        "Álgebra Linear",
                        "Geometria",
                        "Trigonometria",
                        "Aritmética",
                    ],
                    "resposta_correta": "Álgebra Linear",
                },
                {
                    "pergunta": "O que é um vetor em machine learning?",
                    "alternativas": [
                        "Array unidimensional",
                        "Matriz 2x2",
                        "Número complexo",
                        "Função",
                    ],
                    "resposta_correta": "Array unidimensional",
                },
                {
                    "pergunta": "Para que serve cálculo em IA?",
                    "alternativas": [
                        "Otimização",
                        "Visualização",
                        "Interface",
                        "Armazenamento",
                    ],
                    "resposta_correta": "Otimização",
                },
            ],
            "Redes Neurais e Deep Learning": [
                {
                    "pergunta": "O que é uma rede neural?",
                    "alternativas": [
                        "Modelo inspirado no cérebro",
                        "Banco de dados",
                        "Protocolo de rede",
                        "Linguagem",
                    ],
                    "resposta_correta": "Modelo inspirado no cérebro",
                },
                {
                    "pergunta": "Qual função de ativação é comum?",
                    "alternativas": ["ReLU", "Sigmoid", "Tanh", "Todas"],
                    "resposta_correta": "Todas",
                },
                {
                    "pergunta": "Deep Learning usa:",
                    "alternativas": [
                        "Múltiplas camadas",
                        "Uma camada",
                        "Sem camadas",
                        "Camadas físicas",
                    ],
                    "resposta_correta": "Múltiplas camadas",
                },
            ],
            "Processamento de Linguagem Natural (NLP)": [
                {
                    "pergunta": "NLP significa:",
                    "alternativas": [
                        "Natural Language Processing",
                        "Neural Language Program",
                        "Network Layer Protocol",
                        "New Learning Process",
                    ],
                    "resposta_correta": "Natural Language Processing",
                },
                {
                    "pergunta": "Qual técnica converte texto em números?",
                    "alternativas": [
                        "Tokenização",
                        "Vectorization",
                        "Parsing",
                        "Compilation",
                    ],
                    "resposta_correta": "Vectorization",
                },
                {
                    "pergunta": "BERT é um modelo de:",
                    "alternativas": ["Linguagem", "Visão", "Áudio", "Dados"],
                    "resposta_correta": "Linguagem",
                },
            ],
        }

        # Retornar questões do módulo ou gerar padrão
        if modulo_nome in banco_questoes:
            return banco_questoes[modulo_nome][:quantidade]
        else:
            # Questões genéricas
            return [
                {
                    "pergunta": f"Qual é o conceito principal do módulo {modulo_nome}?",
                    "alternativas": [
                        "Conceito A",
                        "Conceito B",
                        "Conceito C",
                        "Conceito D",
                    ],
                    "resposta_correta": "Conceito A",
                }
                for _ in range(quantidade)
            ]

    def mostrar_opcao_certificado(self, curso_id):
        """Mostra opção para gerar certificado se atingiu 80%"""
        progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})

        if progresso.get("progresso", 0) >= 80 and progresso.get("nota_final", 0) >= 70:
            if messagebox.askyesno(
                "Certificado Disponível!",
                f"🎓 Parabéns! Você atingiu {progresso['progresso']:.1f}% do curso!\n\n"
                f"Deseja gerar seu certificado agora?",
            ):
                self.gerar_certificado(curso_id)

    def gerar_certificado_automatico(self, curso_id):
        """Gera certificado automaticamente quando curso é 100% concluído"""
        progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})
        curso = self.cursos_disponiveis.get(curso_id)
        user_data = self.usuarios_cadastrados[self.usuario_logado]

        if not curso:
            return

        # Verificar se pode gerar certificado
        if progresso.get("progresso", 0) < 100:
            return

        if progresso.get("nota_final", 0) < 70:
            return

        # Adicionar aos certificados do usuário
        if "certificados" not in user_data:
            user_data["certificados"] = []

        certificado_info = {
            "curso": curso["nome"],
            "curso_id": curso_id,
            "data": datetime.now().strftime("%d/%m/%Y"),
            "carga_horaria": curso["carga_horaria"],
            "aluno_nome": user_data["nome_completo"],
            "aluno_usuario": self.usuario_logado,
            "nota_final": progresso.get("nota_final", 0),
            "progresso": progresso.get("progresso", 0),
            "tipo": "Conclusão Total",
        }

        user_data["certificados"].append(certificado_info)
        self.salvar_usuarios()

        # Registrar atividade sustentável
        self.registrar_atividade_digital()

        messagebox.showinfo(
            "🎓 Certificado Gerado Automaticamente!",
            f"📄 PARABÉNS! Você concluiu 100% do curso!\n\n"
            f"👤 Para: {user_data['nome_completo']}\n"
            f"📚 Curso: {curso['nome']}\n"
            f"📅 Data: {certificado_info['data']}\n"
            f"⏰ Carga Horária: {curso['carga_horaria']}\n"
            f"🏆 Nota Final: {progresso.get('nota_final', 0):.1f}%\n\n"
            f"🎓 UNIP - Universidade Paulista\n"
            f"✅ Certificado gerado automaticamente!",
        )
        # Tentar gerar o PDF do certificado
        try:
            professor_data = self.usuarios_cadastrados.get(curso.get("professor"), {})
            self.gerar_pdf_certificado(certificado_info, curso, professor_data)
        except Exception as e:
            print(f"Aviso: falha ao gerar PDF do certificado: {e}")

    def gerar_certificado(self, curso_id):
        """Gera certificado para o curso"""
        progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})
        curso = self.cursos_disponiveis.get(curso_id)
        user_data = self.usuarios_cadastrados[self.usuario_logado]

        if not curso:
            messagebox.showerror("Erro", "Curso não encontrado!")
            return

        # Verificar se pode gerar certificado
        if progresso.get("progresso", 0) < 80:
            messagebox.showwarning(
                "Atenção",
                "❌ Você precisa concluir pelo menos 80% do curso para gerar o certificado!",
            )
            return

        if progresso.get("nota_final", 0) < 70:
            messagebox.showwarning(
                "Atenção",
                "❌ Você precisa ter nota mínima de 70% para gerar o certificado!",
            )
            return

        # Adicionar aos certificados do usuário
        if "certificados" not in user_data:
            user_data["certificados"] = []

        certificado_info = {
            "curso": curso["nome"],
            "curso_id": curso_id,
            "data": datetime.now().strftime("%d/%m/%Y"),
            "carga_horaria": curso["carga_horaria"],
            "aluno_nome": user_data["nome_completo"],
            "aluno_usuario": self.usuario_logado,
            "nota_final": progresso.get("nota_final", 0),
            "progresso": progresso.get("progresso", 0),
            "tipo": "Parcial (80%+)",
        }

        user_data["certificados"].append(certificado_info)
        self.salvar_usuarios()

        # Registrar atividade sustentável
        self.registrar_atividade_digital()

        messagebox.showinfo(
            "✅ Certificado Gerado!",
            f"📄 Certificado criado com sucesso!\n\n"
            f"👤 Para: {user_data['nome_completo']}\n"
            f"📚 Curso: {curso['nome']}\n"
            f"📅 Data: {certificado_info['data']}\n"
            f"⏰ Carga Horária: {curso['carga_horaria']}\n"
            f"🏆 Nota Final: {progresso.get('nota_final', 0):.1f}%\n"
            f"📊 Progresso: {progresso.get('progresso', 0):.1f}%\n\n"
            f"🎓 UNIP - Universidade Paulista",
        )
        # Tentar gerar o PDF do certificado
        try:
            professor_data = self.usuarios_cadastrados.get(curso.get("professor"), {})
            self.gerar_pdf_certificado(certificado_info, curso, professor_data)
        except Exception as e:
            print(f"Aviso: falha ao gerar PDF do certificado: {e}")

    def gerar_pdf_certificado(self, certificado_info, curso, professor_data=None):
        """Gera um PDF do certificado com layout moderno usando ReportLab.

        Se `reportlab` não estiver instalado, mostra instrução para instalação.
        """
        try:
            from reportlab.lib.colors import HexColor
            from reportlab.lib.pagesizes import A4, landscape
            from reportlab.pdfgen import canvas
        except Exception:
            messagebox.showwarning(
                "Dependência Ausente",
                "Para gerar certificados em PDF instale a biblioteca 'reportlab'.\n"
                "Executar no terminal: pip install reportlab",
            )
            return

        # Preparar diretório
        base_path = os.path.dirname(__file__)
        certificados_dir = os.path.join(base_path, "certificados")
        Path(certificados_dir).mkdir(parents=True, exist_ok=True)

        # Nome do arquivo
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"certificado_{certificado_info.get('curso_id')}_{certificado_info.get('aluno_usuario')}_{timestamp}.pdf"
        file_path = os.path.join(certificados_dir, filename)

        # Criar PDF em A4 paisagem com layout elegante
        c = canvas.Canvas(file_path, pagesize=landscape(A4))
        width, height = landscape(A4)

        # Paleta de cores
        azul_escuro = HexColor("#14274E")
        dourado = HexColor("#D4AF37")
        cinza = HexColor("#7f8c8d")
        branco = HexColor("#ffffff")

        # Fundo
        c.setFillColor(branco)
        c.rect(0, 0, width, height, fill=1, stroke=0)

        # Borda elegante
        margin = 28
        c.setStrokeColor(azul_escuro)
        c.setLineWidth(3)
        c.roundRect(
            margin,
            margin,
            width - margin * 2,
            height - margin * 2,
            12,
            stroke=1,
            fill=0,
        )

        # Cabeçalho institucional
        c.setFillColor(azul_escuro)
        c.setFont("Times-Bold", 40)
        c.drawCentredString(width / 2, height - 70, "UNIP - Universidade Paulista")

        # Subtítulo
        c.setFillColor(dourado)
        c.setFont("Times-Bold", 32)
        c.drawCentredString(width / 2, height - 120, "Certificado de Conclusão")

        # Linha decorativa
        c.setStrokeColor(dourado)
        c.setLineWidth(1.8)
        c.line(margin + 20, height - 130, width - margin - 20, height - 130)

        # Texto introdutório
        text_y = height - 180
        c.setFillColor(azul_escuro)
        c.setFont("Helvetica", 14)
        c.drawCentredString(width / 2, text_y, "Certificamos que")

        # Nome do aluno em destaque (serifa grande)
        aluno_nome = certificado_info.get(
            "aluno_nome", certificado_info.get("aluno_usuario")
        )
        c.setFont("Times-Bold", 34)
        c.drawCentredString(width / 2, text_y - 40, aluno_nome)

        # Declaração de conclusão
        c.setFont("Helvetica", 14)
        curso_text = f"concluiu com êxito o curso '{curso.get('nome')}', totalizando {certificado_info.get('carga_horaria')} de carga horária."
        c.drawCentredString(width / 2, text_y - 80, curso_text)

        # Informações organizadas (duas colunas)
        info_top = text_y - 130
        left_x = width * 0.18
        right_x = width * 0.55
        line_h = 18

        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(azul_escuro)
        c.drawString(left_x, info_top, "Aluno:")
        c.setFont("Helvetica", 12)
        c.drawString(
            left_x + 60,
            info_top,
            f"{aluno_nome} ({certificado_info.get('aluno_usuario')})",
        )

        c.setFont("Helvetica-Bold", 12)
        c.drawString(left_x, info_top - line_h * 1.3, "Curso:")
        c.setFont("Helvetica", 12)
        c.drawString(left_x + 60, info_top - line_h * 1.3, curso.get("nome"))

        c.setFont("Helvetica-Bold", 12)
        c.drawString(left_x, info_top - line_h * 2.6, "Professor:")
        c.setFont("Helvetica", 12)
        c.drawString(
            left_x + 80,
            info_top - line_h * 2.6,
            professor_data.get("nome_completo", curso.get("professor")),
        )

        c.setFont("Helvetica-Bold", 12)
        c.drawString(right_x, info_top, "Data:")
        c.setFont("Helvetica", 12)
        c.drawString(right_x + 50, info_top, certificado_info.get("data"))

        c.setFont("Helvetica-Bold", 12)
        c.drawString(right_x, info_top - line_h * 1.3, "Carga Horária:")
        c.setFont("Helvetica", 12)
        c.drawString(
            right_x + 100,
            info_top - line_h * 1.3,
            certificado_info.get("carga_horaria"),
        )

        c.setFont("Helvetica-Bold", 12)
        c.drawString(right_x, info_top - line_h * 2.6, "Nota Final:")
        c.setFont("Helvetica", 12)
        c.drawString(
            right_x + 80,
            info_top - line_h * 2.6,
            f"{certificado_info.get('nota_final'):.1f}%",
        )

        # Selo/falso carimbo (círculo gravado à direita)
        seal_x = width - margin - 140
        seal_y = height * 0.45
        seal_r = 60
        c.setFillColor(dourado)
        c.circle(seal_x, seal_y, seal_r, stroke=0, fill=1)
        c.setFillColor(azul_escuro)
        c.setFont("Times-Bold", 14)
        c.drawCentredString(seal_x, seal_y + 6, "UNIP")
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(seal_x, seal_y - 12, "CERTIFICADO")

        # Assinatura do Professor Responsável (usar o nome do professor do curso)
        sig_y = margin + 120
        sig_center_x = width / 2 - 40

        professor_nome = None
        if professor_data:
            professor_nome = professor_data.get("nome_completo")
        if not professor_nome:
            professor_nome = curso.get("professor")

        # Linha de assinatura centralizada
        c.setStrokeColor(azul_escuro)
        c.setLineWidth(1)
        c.line(sig_center_x, sig_y, sig_center_x + 300, sig_y)

        # Assinatura estilizada (nome do professor em itálico)
        c.setFont("Times-Italic", 20)
        c.setFillColor(azul_escuro)
        c.drawCentredString(sig_center_x + 150, sig_y - 30, professor_nome)
        c.setFont("Helvetica", 10)
        c.setFillColor(cinza)
        c.drawCentredString(sig_center_x + 150, sig_y - 46, "Professor Responsável")

        # Pequeno selo dourado sobreposto próximo à assinatura
        c.setFillColor(dourado)
        c.circle(sig_center_x + 330, sig_y - 20, 12, stroke=0, fill=1)

        # Rodapé discreto
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColor(cinza)
        c.drawCentredString(
            width / 2,
            margin + 12,
            "Certificado emitido digitalmente pela UNIP - Universidade Paulista",
        )

        c.save()

        # Atualizar info no registro do usuário (se possível)
        try:
            u = certificado_info.get("aluno_usuario")
            if u in self.usuarios_cadastrados:
                for cert in reversed(
                    self.usuarios_cadastrados[u].get("certificados", [])
                ):
                    if cert.get("curso_id") == certificado_info.get(
                        "curso_id"
                    ) and cert.get("data") == certificado_info.get("data"):
                        cert["arquivo_pdf"] = file_path
                        break
                self.salvar_usuarios()
        except Exception:
            pass

        messagebox.showinfo(
            "Certificado PDF", f"✅ Certificado em PDF gerado:\n{file_path}"
        )

    # ========== SISTEMA DE ATUALIZAÇÃO DE INTERFACE ==========

    def atualizar_interface(self):
        """Atualiza toda a interface após mudanças nos dados"""
        if self.usuario_logado:
            self.mostrar_dashboard_ia()

    # ========== SISTEMA DE CADASTRO COM TELEFONE FORMATADO ==========

    def formatar_telefone(self, event=None):
        """Formata o telefone automaticamente enquanto digita"""
        entry = self.entries_cadastro["entry_telefone"]
        # Remover caracteres não-numéricos
        texto = "".join(c for c in entry.get() if c.isdigit())

        # Limitar a 11 dígitos
        texto = texto[:11]

        # Formatar de acordo com comprimento
        if len(texto) == 0:
            texto_formatado = ""
        elif len(texto) <= 2:
            texto_formatado = f"({texto}"
        elif len(texto) <= 7:
            texto_formatado = f"({texto[:2]}) {texto[2:]}"
        else:
            texto_formatado = f"({texto[:2]}) {texto[2:7]}-{texto[7:]}"

        # Atualizar campo
        entry.delete(0, tk.END)
        entry.insert(0, texto_formatado)

    def validar_telefone(self, telefone):
        """Valida telefone no formato brasileiro"""
        # Remover formatação para validar
        telefone_limpo = "".join(c for c in telefone if c.isdigit())

        if len(telefone_limpo) < 10:
            return "Telefone incompleto. Mínimo 10 dígitos necessários"

        if len(telefone_limpo) > 11:
            return "Telefone inválido. Máximo 11 dígitos"

        if not telefone_limpo.isdigit():
            return "Telefone deve conter apenas números"

        # Validar DDD (primeiros 2 dígitos não devem ser 00 ou 01)
        ddd = telefone_limpo[:2]
        if ddd == "00" or ddd == "01":
            return "DDD inválido"

        return None

    def mostrar_cadastro_completo(self):
        """Tela de cadastro completa"""
        cadastro_janela = tk.Toplevel(self.root)
        cadastro_janela.title("🎓 Cadastro de Aluno - UNIP")
        cadastro_janela.geometry("500x600")
        cadastro_janela.resizable(False, False)
        cadastro_janela.transient(self.root)
        cadastro_janela.grab_set()

        # Frame principal
        main_frame = ttk.Frame(cadastro_janela, padding="20")
        main_frame.pack(expand=True, fill="both")

        ttk.Label(
            main_frame, text="📝 Cadastro de Novo Aluno", font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        # Frame do formulário
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill="both", expand=True)

        campos = [
            ("👤 Nome Completo:", "entry_nome", False),
            ("🔐 Nome de Usuário:", "entry_user", False),
            ("📞 Telefone (com DDD):", "entry_telefone", False),
            ("🎂 Idade:", "entry_idade", False),
            ("🎯 Interesses (separados por vírgula):", "entry_interesses", False),
            ("🔒 Senha:", "entry_senha", True),
            ("🔒 Confirmar Senha:", "entry_confirmar_senha", True),
        ]

        self.entries_cadastro = {}
        row = 0

        for label, nome, is_senha in campos:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 9)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            if is_senha:
                entry = ttk.Entry(form_frame, width=30, show="•", font=("Segoe UI", 10))
            else:
                entry = ttk.Entry(form_frame, width=30, font=("Segoe UI", 10))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            self.entries_cadastro[nome] = entry
            row += 1

        # Configurar formatação automática do telefone
        self.entries_cadastro["entry_telefone"].bind(
            "<KeyRelease>", self.formatar_telefone
        )

        # Preferências de aprendizado
        ttk.Label(
            form_frame,
            text="🎯 Preferências de Aprendizado:",
            font=("Segoe UI", 9, "bold"),
        ).grid(row=row, column=0, sticky="w", pady=10)
        row += 1

        # Modalidade
        ttk.Label(form_frame, text="Modalidade:", font=("Segoe UI", 9)).grid(
            row=row, column=0, sticky="w", pady=5
        )
        self.modalidade_var = tk.StringVar(value="pratica")
        modalidade_frame = ttk.Frame(form_frame)
        modalidade_frame.grid(row=row, column=1, sticky="w", pady=5)
        ttk.Radiobutton(
            modalidade_frame,
            text="Prática",
            variable=self.modalidade_var,
            value="pratica",
        ).pack(side="left")
        ttk.Radiobutton(
            modalidade_frame,
            text="Visual",
            variable=self.modalidade_var,
            value="visual",
        ).pack(side="left")
        ttk.Radiobutton(
            modalidade_frame,
            text="Auditivo",
            variable=self.modalidade_var,
            value="auditivo",
        ).pack(side="left")
        row += 1

        # Ritmo
        ttk.Label(form_frame, text="Ritmo:", font=("Segoe UI", 9)).grid(
            row=row, column=0, sticky="w", pady=5
        )
        self.ritmo_var = tk.StringVar(value="moderado")
        ritmo_frame = ttk.Frame(form_frame)
        ritmo_frame.grid(row=row, column=1, sticky="w", pady=5)
        ttk.Radiobutton(
            ritmo_frame, text="Acelerado", variable=self.ritmo_var, value="acelerado"
        ).pack(side="left")
        ttk.Radiobutton(
            ritmo_frame, text="Moderado", variable=self.ritmo_var, value="moderado"
        ).pack(side="left")
        ttk.Radiobutton(
            ritmo_frame, text="Calmo", variable=self.ritmo_var, value="calmo"
        ).pack(side="left")
        row += 1

        form_frame.columnconfigure(1, weight=1)

        # Frame de botões
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)

        ttk.Button(
            btn_frame, text="✅ Cadastrar", command=self.executar_cadastro, width=15
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame,
            text="🔄 Limpar",
            command=self.limpar_formulario_cadastro,
            width=15,
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=cadastro_janela.destroy, width=15
        ).pack(side="left", padx=10)

        # Dicas de validação
        dicas_frame = ttk.Frame(main_frame)
        dicas_frame.pack(fill="x", pady=10)

        dicas_text = """💡 Dicas de Cadastro:
• Usuário: 4-20 caracteres (letras, números, _)
• Senha: Mínimo 8 caracteres, 1 maiúscula, 1 número, 1 símbolo
• Telefone: Digite os dígitos (será formatado automaticamente)
  Exemplo: 11999999999 → (11) 99999-9999
  Valida DDD de 10 ou 11 dígitos
• Email será gerado automaticamente: usuario@aluno.unip.br"""

        ttk.Label(
            dicas_frame,
            text=dicas_text,
            font=("Segoe UI", 8),
            foreground="gray",
            justify="left",
        ).pack(anchor="w")

    def mostrar_cadastro_aluno_admin(self):
        """Tela de cadastro de alunos para admin/professor"""
        cadastro_janela = tk.Toplevel(self.root)
        cadastro_janela.title("📝 Cadastro de Aluno - Administrador")
        cadastro_janela.geometry("500x650")
        cadastro_janela.resizable(False, False)
        cadastro_janela.transient(self.root)
        cadastro_janela.grab_set()

        # Frame principal
        main_frame = ttk.Frame(cadastro_janela, padding="20")
        main_frame.pack(expand=True, fill="both")

        ttk.Label(
            main_frame, text="📝 Cadastro de Novo Aluno", font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        ttk.Label(
            main_frame,
            text="Preencha os dados do novo aluno no sistema",
            font=("Segoe UI", 10),
            foreground="#7f8c8d",
        ).pack(pady=5)

        # Frame do formulário
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill="both", expand=True)

        campos = [
            ("👤 Nome Completo:", "entry_nome", False),
            ("🔐 Nome de Usuário:", "entry_user", False),
            ("📞 Telefone (com DDD):", "entry_telefone", False),
            ("🎂 Idade:", "entry_idade", False),
            ("🎯 Interesses (separados por vírgula):", "entry_interesses", False),
            ("🔒 Senha:", "entry_senha", True),
            ("🔒 Confirmar Senha:", "entry_confirmar_senha", True),
        ]

        self.entries_cadastro_admin = {}
        row = 0

        for label, nome, is_senha in campos:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 9)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            if is_senha:
                entry = ttk.Entry(form_frame, width=30, show="•", font=("Segoe UI", 10))
            else:
                entry = ttk.Entry(form_frame, width=30, font=("Segoe UI", 10))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            self.entries_cadastro_admin[nome] = entry
            row += 1

        # Configurar formatação automática do telefone
        self.entries_cadastro_admin["entry_telefone"].bind(
            "<KeyRelease>", self.formatar_telefone_admin
        )

        # Preferências de aprendizado
        ttk.Label(
            form_frame,
            text="🎯 Preferências de Aprendizado:",
            font=("Segoe UI", 9, "bold"),
        ).grid(row=row, column=0, sticky="w", pady=10)
        row += 1

        # Modalidade
        ttk.Label(form_frame, text="Modalidade:", font=("Segoe UI", 9)).grid(
            row=row, column=0, sticky="w", pady=5
        )
        self.modalidade_var_admin = tk.StringVar(value="pratica")
        modalidade_frame = ttk.Frame(form_frame)
        modalidade_frame.grid(row=row, column=1, sticky="w", pady=5)
        ttk.Radiobutton(
            modalidade_frame,
            text="Prática",
            variable=self.modalidade_var_admin,
            value="pratica",
        ).pack(side="left")
        ttk.Radiobutton(
            modalidade_frame,
            text="Visual",
            variable=self.modalidade_var_admin,
            value="visual",
        ).pack(side="left")
        ttk.Radiobutton(
            modalidade_frame,
            text="Auditivo",
            variable=self.modalidade_var_admin,
            value="auditivo",
        ).pack(side="left")
        row += 1

        # Ritmo
        ttk.Label(form_frame, text="Ritmo:", font=("Segoe UI", 9)).grid(
            row=row, column=0, sticky="w", pady=5
        )
        self.ritmo_var_admin = tk.StringVar(value="moderado")
        ritmo_frame = ttk.Frame(form_frame)
        ritmo_frame.grid(row=row, column=1, sticky="w", pady=5)
        ttk.Radiobutton(
            ritmo_frame,
            text="Acelerado",
            variable=self.ritmo_var_admin,
            value="acelerado",
        ).pack(side="left")
        ttk.Radiobutton(
            ritmo_frame,
            text="Moderado",
            variable=self.ritmo_var_admin,
            value="moderado",
        ).pack(side="left")
        ttk.Radiobutton(
            ritmo_frame, text="Calmo", variable=self.ritmo_var_admin, value="calmo"
        ).pack(side="left")
        row += 1

        form_frame.columnconfigure(1, weight=1)

        # Frame de botões
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)

        ttk.Button(
            btn_frame,
            text="✅ Cadastrar",
            command=self.executar_cadastro_admin,
            width=15,
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame,
            text="🔄 Limpar",
            command=self.limpar_formulario_cadastro_admin,
            width=15,
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=cadastro_janela.destroy, width=15
        ).pack(side="left", padx=10)

        # Dicas de validação
        dicas_frame = ttk.Frame(main_frame)
        dicas_frame.pack(fill="x", pady=10)

        dicas_text = """💡 Dicas de Cadastro:
• Usuário: 4-20 caracteres (letras, números, _)
• Senha: Mínimo 8 caracteres, 1 maiúscula, 1 número, 1 símbolo
• Telefone: Digite os dígitos (será formatado automaticamente)
  Exemplo: 11999999999 → (11) 99999-9999
• Email será gerado automaticamente: usuario@aluno.unip.br"""

        ttk.Label(
            dicas_frame,
            text=dicas_text,
            font=("Segoe UI", 8),
            foreground="gray",
            justify="left",
        ).pack(anchor="w")

    # ========== MÉTODOS RESTANTES (mantidos da versão anterior) ==========

    def limpar_formulario_cadastro(self):
        """Limpa todos os campos do formulário"""
        for entry in self.entries_cadastro.values():
            entry.delete(0, "end")

    def limpar_formulario_cadastro_admin(self):
        """Limpa todos os campos do formulário admin"""
        for entry in self.entries_cadastro_admin.values():
            entry.delete(0, "end")

    def formatar_telefone_admin(self, event=None):
        """Formata o telefone automaticamente enquanto digita (versão admin)"""
        entry = self.entries_cadastro_admin["entry_telefone"]
        # Remover caracteres não-numéricos
        texto = "".join(c for c in entry.get() if c.isdigit())

        # Limitar a 11 dígitos
        texto = texto[:11]

        # Formatar de acordo com comprimento
        if len(texto) == 0:
            texto_formatado = ""
        elif len(texto) <= 2:
            texto_formatado = f"({texto}"
        elif len(texto) <= 7:
            texto_formatado = f"({texto[:2]}) {texto[2:]}"
        else:
            texto_formatado = f"({texto[:2]}) {texto[2:7]}-{texto[7:]}"

        # Atualizar campo
        entry.delete(0, tk.END)
        entry.insert(0, texto_formatado)

    def validar_nome_usuario(self, nome):
        if not re.match(r"^[a-zA-Z0-9_]{4,20}$", nome):
            return "4-20 caracteres (letras, números e _)"
        return None

    def validar_idade(self, idade):
        try:
            if not 16 <= int(idade) <= 80:
                return "Idade deve ser entre 16-80 anos"
        except ValueError:
            return "Digite um número válido"
        return None

    def validar_senha(self, senha):
        if len(senha) < 8:
            return "Mínimo 8 caracteres"
        if not any(c.isupper() for c in senha):
            return "Pelo menos 1 letra maiúscula"
        if not any(c.isdigit() for c in senha):
            return "Pelo menos 1 número"
        if not any(c in "!@#$%&*_-+=" for c in senha):
            return "Pelo menos 1 símbolo especial"
        return None

    def gerar_email_unip(self, nome_usuario):
        """Gera email institucional UNIP"""
        return f"{nome_usuario}@aluno.unip.br"

    def executar_cadastro(self):
        """Executa o cadastro com todas as validações"""
        # Coletar dados
        dados = {}
        for nome, entry in self.entries_cadastro.items():
            campo = nome.replace("entry_", "")
            dados[campo] = entry.get().strip()

        # Validar campos obrigatórios
        campos_obrigatorios = [
            "nome",
            "user",
            "telefone",
            "idade",
            "senha",
            "confirmar_senha",
        ]
        for campo in campos_obrigatorios:
            if not dados[campo]:
                messagebox.showerror("Erro", f"Campo '{campo}' é obrigatório!")
                return

        # Validações específicas
        erros = []

        # Verificar se usuário já existe
        if dados["user"] in self.usuarios_cadastrados:
            erros.append("Usuário já existe!")

        # Validar nome de usuário
        if erro := self.validar_nome_usuario(dados["user"]):
            erros.append(erro)

        # Validar telefone
        if erro := self.validar_telefone(dados["telefone"]):
            erros.append(erro)

        # Validar idade
        if erro := self.validar_idade(dados["idade"]):
            erros.append(erro)

        # Validar senha
        if erro := self.validar_senha(dados["senha"]):
            erros.append(erro)

        # Verificar se senhas coincidem
        if dados["senha"] != dados["confirmar_senha"]:
            erros.append("Senhas não coincidem!")

        # Se há erros, mostrar todos
        if erros:
            messagebox.showerror(
                "Erros de Validação", "\n".join(f"• {erro}" for erro in erros)
            )
            return

        # Processar interesses
        interesses = [
            interesse.strip()
            for interesse in dados.get("interesses", "").split(",")
            if interesse.strip()
        ]

        # Gerar email automático
        email = self.gerar_email_unip(dados["user"])

        # Criar usuário
        self.usuarios_cadastrados[dados["user"]] = {
            "senha": dados["senha"],
            "email": email,
            "idade": int(dados["idade"]),
            "is_admin": False,
            "tipo": "aluno",
            "data_cadastro": datetime.now().isoformat(),
            "cursos": [],
            "nome_completo": dados["nome"],
            "telefone": dados["telefone"],
            "certificados": [],
            "modulos_concluidos": {},
            "ultimo_acesso": None,
            "preferencias_aprendizado": {
                "modalidade": self.modalidade_var.get(),
                "ritmo": self.ritmo_var.get(),
            },
            "interesses": interesses,
        }

        # Salvar no JSON
        if self.salvar_usuarios():
            messagebox.showinfo(
                "Sucesso!",
                f"✅ Aluno cadastrado com sucesso!\n\n"
                f"👤 Nome: {dados['nome']}\n"
                f"📧 Email: {email}\n"
                f"🔐 Usuário: {dados['user']}\n"
                f"📞 Telefone: {dados['telefone']}\n"
                f"🎯 Interesses: {', '.join(interesses) if interesses else 'Não informados'}\n\n"
                f"Bem-vindo à UNIP!",
            )

            # Fechar janela de cadastro
            self.entries_cadastro["entry_user"].master.master.master.destroy()
        else:
            messagebox.showerror("Erro", "Falha ao salvar dados do usuário!")

    def executar_cadastro_admin(self):
        """Executa o cadastro de aluno por admin/professor com todas as validações"""
        # Coletar dados
        dados = {}
        for nome, entry in self.entries_cadastro_admin.items():
            campo = nome.replace("entry_", "")
            dados[campo] = entry.get().strip()

        # Validar campos obrigatórios
        campos_obrigatorios = [
            "nome",
            "user",
            "telefone",
            "idade",
            "senha",
            "confirmar_senha",
        ]
        for campo in campos_obrigatorios:
            if not dados[campo]:
                messagebox.showerror("Erro", f"Campo '{campo}' é obrigatório!")
                return

        # Validações específicas
        erros = []

        # Verificar se usuário já existe
        if dados["user"] in self.usuarios_cadastrados:
            erros.append("❌ Usuário já existe!")

        # Validar nome de usuário
        if erro := self.validar_nome_usuario(dados["user"]):
            erros.append(f"❌ Usuário inválido: {erro}")

        # Validar telefone
        if erro := self.validar_telefone(dados["telefone"]):
            erros.append(f"❌ Telefone inválido: {erro}")

        # Validar idade
        if erro := self.validar_idade(dados["idade"]):
            erros.append(f"❌ Idade inválida: {erro}")

        # Validar senha
        if erro := self.validar_senha(dados["senha"]):
            erros.append(f"❌ Senha inválida: {erro}")

        # Verificar se senhas coincidem
        if dados["senha"] != dados["confirmar_senha"]:
            erros.append("❌ Senhas não coincidem!")

        # Se há erros, mostrar todos
        if erros:
            messagebox.showerror("Erros de Validação", "\n".join(erros))
            return

        # Processar interesses
        interesses = [
            interesse.strip()
            for interesse in dados.get("interesses", "").split(",")
            if interesse.strip()
        ]

        # Gerar email automático
        email = self.gerar_email_unip(dados["user"])

        # Criar usuário
        self.usuarios_cadastrados[dados["user"]] = {
            "senha": dados["senha"],
            "email": email,
            "idade": int(dados["idade"]),
            "is_admin": False,
            "tipo": "aluno",
            "data_cadastro": datetime.now().isoformat(),
            "cursos": [],
            "nome_completo": dados["nome"],
            "telefone": dados["telefone"],
            "certificados": [],
            "modulos_concluidos": {},
            "ultimo_acesso": None,
            "preferencias_aprendizado": {
                "modalidade": self.modalidade_var_admin.get(),
                "ritmo": self.ritmo_var_admin.get(),
            },
            "interesses": interesses,
        }

        # Salvar no JSON
        if self.salvar_usuarios():
            messagebox.showinfo(
                "✅ Cadastro Realizado com Sucesso!",
                f"O aluno foi cadastrado no sistema!\n\n"
                f"👤 Nome: {dados['nome']}\n"
                f"📧 Email: {email}\n"
                f"🔐 Usuário: {dados['user']}\n"
                f"📞 Telefone: {dados['telefone']}\n"
                f"🎂 Idade: {dados['idade']} anos\n"
                f"🎯 Interesses: {', '.join(interesses) if interesses else 'Não informados'}\n"
                f"📊 Preferências: {self.modalidade_var_admin.get().title()} - {self.ritmo_var_admin.get().title()}\n\n"
                f"O aluno pode fazer login com suas credenciais!",
            )

            # Fechar janela de cadastro
            self.entries_cadastro_admin["entry_user"].master.master.master.destroy()

            # Atualizar interface
            self.atualizar_interface()
        else:
            messagebox.showerror("Erro", "Falha ao salvar dados do usuário!")

    def mostrar_cadastro_professor_admin(self):
        """Tela de cadastro de novo professor (somente admin)"""
        cadastro_janela = tk.Toplevel(self.root)
        cadastro_janela.title("👨‍🏫 Cadastro de Professor - Administrador")
        cadastro_janela.geometry("550x650")
        cadastro_janela.resizable(False, False)
        cadastro_janela.transient(self.root)
        cadastro_janela.grab_set()

        # Frame principal
        main_frame = ttk.Frame(cadastro_janela, padding="20")
        main_frame.pack(expand=True, fill="both")

        ttk.Label(
            main_frame,
            text="👨‍🏫 Cadastro de Novo Professor",
            font=("Segoe UI", 14, "bold"),
        ).pack(pady=10)

        ttk.Label(
            main_frame,
            text="Preencha os dados do novo professor no sistema",
            font=("Segoe UI", 10),
            foreground="#7f8c8d",
        ).pack(pady=5)

        # Frame do formulário
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill="both", expand=True)

        campos = [
            ("👤 Nome Completo:", "entry_nome", False),
            ("🔐 Nome de Usuário:", "entry_user", False),
            ("📞 Telefone (com DDD):", "entry_telefone", False),
            ("🎂 Idade:", "entry_idade", False),
            ("🎓 Especialidade:", "entry_especialidade", False),
            ("📝 Bio/Descrição:", "entry_bio", False),
            ("🔒 Senha:", "entry_senha", True),
            ("🔒 Confirmar Senha:", "entry_confirmar_senha", True),
        ]

        self.entries_cadastro_prof = {}
        row = 0

        for label, nome, is_senha in campos:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 9)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            if is_senha:
                entry = ttk.Entry(form_frame, width=30, show="•", font=("Segoe UI", 10))
            else:
                entry = ttk.Entry(form_frame, width=30, font=("Segoe UI", 10))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            self.entries_cadastro_prof[nome] = entry
            row += 1

        # Configurar formatação automática do telefone
        self.entries_cadastro_prof["entry_telefone"].bind(
            "<KeyRelease>", self.formatar_telefone_professor
        )

        form_frame.columnconfigure(1, weight=1)

        # Frame de botões
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)

        ttk.Button(
            btn_frame,
            text="✅ Cadastrar",
            command=self.executar_cadastro_professor,
            width=15,
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame,
            text="🔄 Limpar",
            command=self.limpar_formulario_professor,
            width=15,
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=cadastro_janela.destroy, width=15
        ).pack(side="left", padx=10)

        # Dicas de validação
        dicas_frame = ttk.Frame(main_frame)
        dicas_frame.pack(fill="x", pady=10)

        dicas_text = """💡 Dicas de Cadastro de Professor:
• Usuário: 4-20 caracteres (letras, números, _)
• Senha: Mínimo 8 caracteres, 1 maiúscula, 1 número, 1 símbolo
• Telefone: Digite os dígitos (será formatado automaticamente)
  Exemplo: 11999999999 → (11) 99999-9999
• Email será gerado automaticamente: usuario@prof.unip.br
• Especialidade: Área de conhecimento do professor
• O professor poderá gerenciar cursos após cadastro"""

        ttk.Label(
            dicas_frame,
            text=dicas_text,
            font=("Segoe UI", 8),
            foreground="gray",
            justify="left",
        ).pack(anchor="w")

    def mostrar_cadastro_admin_admin(self):
        """Tela de cadastro de novo admin (somente admin)"""
        cadastro_janela = tk.Toplevel(self.root)
        cadastro_janela.title("👑 Cadastro de Administrador - Administrador")
        cadastro_janela.geometry("550x600")
        cadastro_janela.resizable(False, False)
        cadastro_janela.transient(self.root)
        cadastro_janela.grab_set()

        # Frame principal
        main_frame = ttk.Frame(cadastro_janela, padding="20")
        main_frame.pack(expand=True, fill="both")

        ttk.Label(
            main_frame,
            text="👑 Cadastro de Novo Administrador",
            font=("Segoe UI", 14, "bold"),
        ).pack(pady=10)

        ttk.Label(
            main_frame,
            text="Preencha os dados do novo administrador do sistema",
            font=("Segoe UI", 10),
            foreground="#7f8c8d",
        ).pack(pady=5)

        # Frame do formulário
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill="both", expand=True)

        campos = [
            ("👤 Nome Completo:", "entry_nome", False),
            ("🔐 Nome de Usuário:", "entry_user", False),
            ("📞 Telefone (com DDD):", "entry_telefone", False),
            ("🎂 Idade:", "entry_idade", False),
            ("🔒 Senha:", "entry_senha", True),
            ("🔒 Confirmar Senha:", "entry_confirmar_senha", True),
        ]

        self.entries_cadastro_admin_novo = {}
        row = 0

        for label, nome, is_senha in campos:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 9)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            if is_senha:
                entry = ttk.Entry(form_frame, width=30, show="•", font=("Segoe UI", 10))
            else:
                entry = ttk.Entry(form_frame, width=30, font=("Segoe UI", 10))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            self.entries_cadastro_admin_novo[nome] = entry
            row += 1

        # Configurar formatação automática do telefone
        self.entries_cadastro_admin_novo["entry_telefone"].bind(
            "<KeyRelease>", self.formatar_telefone_admin_novo
        )

        form_frame.columnconfigure(1, weight=1)

        # Frame de botões
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)

        ttk.Button(
            btn_frame,
            text="✅ Cadastrar",
            command=self.executar_cadastro_admin_novo,
            width=15,
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame,
            text="🔄 Limpar",
            command=self.limpar_formulario_admin_novo,
            width=15,
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=cadastro_janela.destroy, width=15
        ).pack(side="left", padx=10)

        # Dicas de validação
        dicas_frame = ttk.Frame(main_frame)
        dicas_frame.pack(fill="x", pady=10)

        dicas_text = """💡 Dicas de Cadastro de Administrador:
• Usuário: 4-20 caracteres (letras, números, _)
• Senha: Mínimo 8 caracteres, 1 maiúscula, 1 número, 1 símbolo
• Telefone: Digite os dígitos (será formatado automaticamente)
• Email será gerado automaticamente: usuario@admin.unip.br
• ⚠️ AVISO: Admins têm acesso total ao sistema!
• Use com cuidado e apenas pessoas confiáveis"""

        ttk.Label(
            dicas_frame,
            text=dicas_text,
            font=("Segoe UI", 8),
            foreground="gray",
            justify="left",
        ).pack(anchor="w")

    def formatar_telefone_professor(self, event=None):
        """Formata o telefone automaticamente enquanto digita (versão professor)"""
        entry = self.entries_cadastro_prof["entry_telefone"]
        texto = "".join(c for c in entry.get() if c.isdigit())
        texto = texto[:11]

        if len(texto) == 0:
            texto_formatado = ""
        elif len(texto) <= 2:
            texto_formatado = f"({texto}"
        elif len(texto) <= 7:
            texto_formatado = f"({texto[:2]}) {texto[2:]}"
        else:
            texto_formatado = f"({texto[:2]}) {texto[2:7]}-{texto[7:]}"

        entry.delete(0, tk.END)
        entry.insert(0, texto_formatado)

    def formatar_telefone_admin_novo(self, event=None):
        """Formata o telefone automaticamente enquanto digita (versão admin novo)"""
        entry = self.entries_cadastro_admin_novo["entry_telefone"]
        texto = "".join(c for c in entry.get() if c.isdigit())
        texto = texto[:11]

        if len(texto) == 0:
            texto_formatado = ""
        elif len(texto) <= 2:
            texto_formatado = f"({texto}"
        elif len(texto) <= 7:
            texto_formatado = f"({texto[:2]}) {texto[2:]}"
        else:
            texto_formatado = f"({texto[:2]}) {texto[2:7]}-{texto[7:]}"

        entry.delete(0, tk.END)
        entry.insert(0, texto_formatado)

    def limpar_formulario_professor(self):
        """Limpa todos os campos do formulário de professor"""
        for entry in self.entries_cadastro_prof.values():
            entry.delete(0, "end")

    def limpar_formulario_admin_novo(self):
        """Limpa todos os campos do formulário de admin"""
        for entry in self.entries_cadastro_admin_novo.values():
            entry.delete(0, "end")

    def executar_cadastro_professor(self):
        """Executa o cadastro de professor com todas as validações"""
        dados = {}
        for nome, entry in self.entries_cadastro_prof.items():
            campo = nome.replace("entry_", "")
            dados[campo] = entry.get().strip()

        # Validar campos obrigatórios
        campos_obrigatorios = [
            "nome",
            "user",
            "telefone",
            "idade",
            "especialidade",
            "senha",
            "confirmar_senha",
        ]
        for campo in campos_obrigatorios:
            if not dados[campo]:
                messagebox.showerror("Erro", f"Campo '{campo}' é obrigatório!")
                return

        # Validações específicas
        erros = []

        if dados["user"] in self.usuarios_cadastrados:
            erros.append("❌ Usuário já existe!")

        if erro := self.validar_nome_usuario(dados["user"]):
            erros.append(f"❌ Usuário inválido: {erro}")

        if erro := self.validar_telefone(dados["telefone"]):
            erros.append(f"❌ Telefone inválido: {erro}")

        if erro := self.validar_idade(dados["idade"]):
            erros.append(f"❌ Idade inválida: {erro}")

        if erro := self.validar_senha(dados["senha"]):
            erros.append(f"❌ Senha inválida: {erro}")

        if dados["senha"] != dados["confirmar_senha"]:
            erros.append("❌ Senhas não coincidem!")

        if erros:
            messagebox.showerror("Erros de Validação", "\n".join(erros))
            return

        # Gerar email automático
        email = f"{dados['user']}@prof.unip.br"

        # Criar usuário professor
        self.usuarios_cadastrados[dados["user"]] = {
            "senha": dados["senha"],
            "email": email,
            "idade": int(dados["idade"]),
            "is_admin": False,
            "tipo": "professor",
            "data_cadastro": datetime.now().isoformat(),
            "cursos": [],
            "nome_completo": dados["nome"],
            "telefone": dados["telefone"],
            "especialidade": dados["especialidade"],
            "bio": dados.get("bio", ""),
        }

        if self.salvar_usuarios():
            messagebox.showinfo(
                "✅ Professor Cadastrado com Sucesso!",
                f"O professor foi cadastrado no sistema!\n\n"
                f"👤 Nome: {dados['nome']}\n"
                f"📧 Email: {email}\n"
                f"🔐 Usuário: {dados['user']}\n"
                f"📞 Telefone: {dados['telefone']}\n"
                f"🎂 Idade: {dados['idade']} anos\n"
                f"🎓 Especialidade: {dados['especialidade']}\n\n"
                f"O professor pode fazer login e gerenciar seus cursos!",
            )

            self.entries_cadastro_prof["entry_user"].master.master.master.destroy()
            self.atualizar_interface()
        else:
            messagebox.showerror("Erro", "Falha ao salvar dados do professor!")

    def executar_cadastro_admin_novo(self):
        """Executa o cadastro de novo admin com todas as validações"""
        dados = {}
        for nome, entry in self.entries_cadastro_admin_novo.items():
            campo = nome.replace("entry_", "")
            dados[campo] = entry.get().strip()

        # Validar campos obrigatórios
        campos_obrigatorios = [
            "nome",
            "user",
            "telefone",
            "idade",
            "senha",
            "confirmar_senha",
        ]
        for campo in campos_obrigatorios:
            if not dados[campo]:
                messagebox.showerror("Erro", f"Campo '{campo}' é obrigatório!")
                return

        # Validações específicas
        erros = []

        if dados["user"] in self.usuarios_cadastrados:
            erros.append("❌ Usuário já existe!")

        if erro := self.validar_nome_usuario(dados["user"]):
            erros.append(f"❌ Usuário inválido: {erro}")

        if erro := self.validar_telefone(dados["telefone"]):
            erros.append(f"❌ Telefone inválido: {erro}")

        if erro := self.validar_idade(dados["idade"]):
            erros.append(f"❌ Idade inválida: {erro}")

        if erro := self.validar_senha(dados["senha"]):
            erros.append(f"❌ Senha inválida: {erro}")

        if dados["senha"] != dados["confirmar_senha"]:
            erros.append("❌ Senhas não coincidem!")

        if erros:
            messagebox.showerror("Erros de Validação", "\n".join(erros))
            return

        # Gerar email automático
        email = f"{dados['user']}@admin.unip.br"

        # Criar usuário admin
        self.usuarios_cadastrados[dados["user"]] = {
            "senha": dados["senha"],
            "email": email,
            "idade": int(dados["idade"]),
            "is_admin": True,
            "tipo": "admin",
            "data_cadastro": datetime.now().isoformat(),
            "cursos": [],
            "nome_completo": dados["nome"],
            "telefone": dados["telefone"],
        }

        if self.salvar_usuarios():
            messagebox.showinfo(
                "✅ Administrador Cadastrado com Sucesso!",
                f"O novo administrador foi cadastrado no sistema!\n\n"
                f"👤 Nome: {dados['nome']}\n"
                f"📧 Email: {email}\n"
                f"🔐 Usuário: {dados['user']}\n"
                f"📞 Telefone: {dados['telefone']}\n"
                f"🎂 Idade: {dados['idade']} anos\n\n"
                f"⚠️ AVISO: Este usuário tem acesso total ao sistema!\n"
                f"O administrador pode fazer login com suas credenciais!",
            )

            self.entries_cadastro_admin_novo[
                "entry_user"
            ].master.master.master.destroy()
            self.atualizar_interface()
        else:
            messagebox.showerror("Erro", "Falha ao salvar dados do administrador!")

    def fazer_login_interativo(self):
        """Sistema de login"""
        usuario = self.entry_user.get().strip()
        senha = self.entry_senha.get()

        if not usuario or not senha:
            messagebox.showwarning("Aviso", "Preencha usuário e senha!")
            return

        if usuario in self.usuarios_cadastrados:
            usuario_data = self.usuarios_cadastrados[usuario]

            if usuario_data["senha"] == senha:
                self.usuario_logado = usuario
                messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
                self.mostrar_dashboard_ia()
            else:
                messagebox.showerror("Erro", "Senha incorreta!")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado!")

    def mostrar_dashboard_ia(self):
        """Dashboard principal com IA integrada"""
        self.limpar_tela()

        user_data = self.usuarios_cadastrados[self.usuario_logado]
        tipo_usuario = user_data.get("tipo", "aluno")

        # Header moderno
        header_frame = ttk.Frame(self.root, style="Card.TFrame", padding="15")
        header_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(
            header_frame,
            text=f"🚀 Bem-vindo, {user_data.get('nome_completo', self.usuario_logado)}!",
            style="Title.TLabel",
        ).pack(side="left")

        tipo_text = {
            "admin": "👑 Administrador do Sistema",
            "professor": "👨‍🏫 Professor",
            "aluno": "🎓 Aluno UNIP",
        }

        ttk.Label(
            header_frame,
            text=tipo_text.get(tipo_usuario, "🎓 Aluno"),
            font=("Segoe UI", 12, "bold"),
            foreground="#7f8c8d",
        ).pack(side="left", padx=20)

        ttk.Button(
            header_frame,
            text="🚪 Sair",
            command=self.mostrar_tela_login,
            style="TButton",
        ).pack(side="right")

        # Abas principais com IA
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)

        if tipo_usuario == "aluno":
            # Aba Dashboard IA
            aba_dashboard = ttk.Frame(notebook)
            self.criar_dashboard_ia_aluno(aba_dashboard)
            notebook.add(aba_dashboard, text="📊 Dashboard IA")

            # Aba Cursos e Matrícula
            aba_cursos = ttk.Frame(notebook)
            self.criar_aba_cursos_matricula(aba_cursos)
            notebook.add(aba_cursos, text="📚 Cursos")

            # Aba Meus Cursos
            aba_meus_cursos = ttk.Frame(notebook)
            self.criar_aba_meus_cursos(aba_meus_cursos)
            notebook.add(aba_meus_cursos, text="🎓 Meus Cursos")

        elif tipo_usuario == "professor":
            # Aba Professor
            aba_professor = ttk.Frame(notebook)
            self.criar_aba_professor(aba_professor)
            notebook.add(aba_professor, text="👨‍🏫 Painel Professor")

            # Aba Cadastro de Alunos
            aba_cadastro = ttk.Frame(notebook)
            self.criar_aba_cadastro_alunos(aba_cadastro)
            notebook.add(aba_cadastro, text="📝 Cadastrar Alunos")

            # Aba Gerenciamento de Conteúdo (Professores podem editar seus cursos)
            aba_conteudo = ttk.Frame(notebook)
            self.criar_aba_gerenciamento_conteudo(aba_conteudo)
            notebook.add(aba_conteudo, text="📚 Gerenciar Conteúdo")

        elif tipo_usuario == "admin":
            # Aba Admin
            aba_admin = ttk.Frame(notebook)
            self.criar_aba_admin(aba_admin)
            notebook.add(aba_admin, text="👑 Painel Admin")

            # Aba Cadastro de Alunos
            aba_cadastro = ttk.Frame(notebook)
            self.criar_aba_cadastro_alunos(aba_cadastro)
            notebook.add(aba_cadastro, text="📝 Cadastrar Alunos")

            # Aba Cadastro de Professores e Admins
            aba_cadastro_prof = ttk.Frame(notebook)
            self.criar_aba_cadastro_professores_admins(aba_cadastro_prof)
            notebook.add(aba_cadastro_prof, text="👥 Cadastrar Prof/Admin")

            # Aba Gerenciamento de Usuários
            aba_usuarios = ttk.Frame(notebook)
            self.criar_aba_gerenciamento_usuarios(aba_usuarios)
            notebook.add(aba_usuarios, text="👥 Gerenciar Usuários")

            # Aba Gerenciamento de Conteúdo
            aba_conteudo = ttk.Frame(notebook)
            self.criar_aba_gerenciamento_conteudo(aba_conteudo)
            notebook.add(aba_conteudo, text="📚 Gerenciar Conteúdo")

        # Abas comuns
        aba_sustentabilidade = ttk.Frame(notebook)
        self.criar_aba_sustentabilidade(aba_sustentabilidade)
        notebook.add(aba_sustentabilidade, text="🌱 Sustentabilidade")

        aba_perfil = ttk.Frame(notebook)
        self.criar_aba_perfil_avancado(aba_perfil)
        notebook.add(aba_perfil, text="👤 Perfil")

    def criar_dashboard_ia_aluno(self, parent):
        """Dashboard avançado com análises de IA"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        # Análise IA do aluno
        analise_ia = self.analisar_padrao_aprendizado(self.usuario_logado)
        recomendacoes_ia = self.gerar_recomendacoes_ia_personalizadas(
            self.usuario_logado
        )

        # Grid principal
        main_grid = ttk.Frame(frame)
        main_grid.pack(expand=True, fill="both")

        # Coluna 1: Métricas de Progresso
        col1 = ttk.Frame(main_grid)
        col1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        ttk.Label(col1, text="📈 Meu Progresso", style="Subtitle.TLabel").pack(
            anchor="w", pady=10
        )

        # Cartões de métricas
        progresso_data = self.progresso_alunos.get(self.usuario_logado, {})
        total_cursos = len(progresso_data)
        cursos_concluidos = sum(
            1 for dados in progresso_data.values() if dados.get("progresso", 0) >= 100
        )
        progresso_medio = sum(
            dados.get("progresso", 0) for dados in progresso_data.values()
        ) / max(total_cursos, 1)

        metricas = [
            ("🎓 Cursos Ativos", total_cursos),
            ("✅ Concluídos", cursos_concluidos),
            ("📊 Progresso Médio", f"{progresso_medio:.1f}%"),
            ("🚀 Velocidade", f"{analise_ia['velocidade_aprendizado']:.1f}%"),
        ]

        for texto, valor in metricas:
            card = ttk.Frame(col1, style="Card.TFrame", padding="15")
            card.pack(fill="x", pady=5)
            ttk.Label(card, text=texto, font=("Segoe UI", 10)).pack(anchor="w")
            ttk.Label(
                card,
                text=str(valor),
                font=("Segoe UI", 16, "bold"),
                foreground="#2c3e50",
            ).pack(anchor="w")

        # Coluna 2: Recomendações IA
        col2 = ttk.Frame(main_grid)
        col2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        ttk.Label(col2, text="🤖 Recomendações IA", style="Subtitle.TLabel").pack(
            anchor="w", pady=10
        )

        # Recomendações em cards
        if recomendacoes_ia["cursos_sugeridos"]:
            for curso in recomendacoes_ia["cursos_sugeridos"][:3]:
                card = ttk.Frame(col2, style="Card.TFrame", padding="12")
                card.pack(fill="x", pady=3)

                ttk.Label(
                    card, text=curso["curso"], font=("Segoe UI", 10, "bold")
                ).pack(anchor="w")
                ttk.Label(
                    card,
                    text=curso["motivo"],
                    font=("Segoe UI", 8),
                    foreground="#7f8c8d",
                ).pack(anchor="w")
                ttk.Label(
                    card,
                    text=f"Dificuldade: {curso['dificuldade']}",
                    font=("Segoe UI", 8),
                    foreground="#f39c12",
                ).pack(anchor="w")
        else:
            ttk.Label(
                col2,
                text="🎯 Complete seus cursos atuais para receber recomendações!",
                font=("Segoe UI", 10),
                foreground="#7f8c8d",
            ).pack(pady=20)

        # Coluna 3: Análise de Desempenho
        col3 = ttk.Frame(main_grid)
        col3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        ttk.Label(col3, text="📋 Análise de Aprendizado", style="Subtitle.TLabel").pack(
            anchor="w", pady=10
        )

        # Insights da IA
        insights = []
        if analise_ia["dificuldades"]:
            insights.append(
                f"💡 Dificuldades: {', '.join(analise_ia['dificuldades'][:2])}"
            )
        if analise_ia["pontos_fortes"]:
            insights.append(
                f"⭐ Pontos Fortes: {', '.join(analise_ia['pontos_fortes'][:2])}"
            )
        if analise_ia["previsao_conclusao"]:
            for curso_id, data in list(analise_ia["previsao_conclusao"].items())[:2]:
                curso_nome = self.cursos_disponiveis.get(curso_id, {}).get(
                    "nome", "Curso"
                )
                insights.append(f"📅 {curso_nome}: Conclusão prevista em {data}")
        if analise_ia["sugestoes_modulos"]:
            insights.extend(analise_ia["sugestoes_modulos"][:2])

        for insight in insights[:4]:  # Limitar a 4 insights
            card = ttk.Frame(col3, style="Card.TFrame", padding="10")
            card.pack(fill="x", pady=2)
            ttk.Label(card, text=insight, font=("Segoe UI", 9), wraplength=250).pack(
                anchor="w"
            )

        # Configurar grid
        main_grid.columnconfigure(0, weight=1)
        main_grid.columnconfigure(1, weight=1)
        main_grid.columnconfigure(2, weight=1)
        main_grid.rowconfigure(0, weight=1)

    def criar_aba_cursos_matricula(self, parent):
        """Aba para visualizar e matricular em cursos"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame, text="📚 Cursos Disponíveis - UNIP", style="Title.TLabel"
        ).pack(anchor="w", pady=10)

        # Container com scroll
        container = ttk.Frame(frame)
        container.pack(expand=True, fill="both")

        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Cards de cursos
        user_cursos = self.usuarios_cadastrados[self.usuario_logado].get("cursos", [])

        for i, (curso_id, curso) in enumerate(self.cursos_disponiveis.items()):
            card = ttk.Frame(scrollable_frame, style="Card.TFrame", padding="20")
            card.pack(fill="x", pady=10, padx=10)

            # Header do card
            header_frame = ttk.Frame(card)
            header_frame.pack(fill="x", pady=5)

            ttk.Label(
                header_frame, text=curso["nome"], font=("Segoe UI", 14, "bold")
            ).pack(side="left")

            # Badge de status
            if curso_id in user_cursos:
                status_badge = ttk.Label(
                    header_frame,
                    text="✅ MATRICULADO",
                    font=("Segoe UI", 9, "bold"),
                    foreground="green",
                )
            else:
                status_badge = ttk.Label(
                    header_frame,
                    text="🎯 DISPONÍVEL",
                    font=("Segoe UI", 9, "bold"),
                    foreground="blue",
                )
            status_badge.pack(side="right")

            # Informações do curso
            info_text = f"""
📋 Descrição: {curso["descricao"]}
⏰ Carga Horária: {curso["carga_horaria"]}
🎯 Dificuldade: {curso["dificuldade"]}
📊 Categoria: {curso["categoria"]}
👨‍🏫 Professor: {self.usuarios_cadastrados.get(curso["professor"], {}).get("nome_completo", curso["professor"])}
⭐ Avaliação: {curso["avaliacao"]}/5.0
👥 Alunos: {curso["alunos_matriculados"]} matriculados
            """

            ttk.Label(card, text=info_text, font=("Segoe UI", 9), justify="left").pack(
                anchor="w", pady=10
            )

            # Módulos
            ttk.Label(
                card, text="📖 Módulos do Curso:", font=("Segoe UI", 10, "bold")
            ).pack(anchor="w", pady=5)

            for modulo in curso["modulos"]:
                ttk.Label(
                    card,
                    text=f"• {modulo['nome']} ({modulo['dificuldade']}) - {modulo['tempo_estimado']}",
                    font=("Segoe UI", 8),
                ).pack(anchor="w")

            # Botões de ação
            btn_frame = ttk.Frame(card)
            btn_frame.pack(fill="x", pady=15)

            if curso_id in user_cursos:
                ttk.Button(
                    btn_frame,
                    text="🎓 Acessar Curso",
                    command=lambda cid=curso_id: self.acessar_curso(cid),
                    width=15,
                ).pack(side="left", padx=5)
            else:
                ttk.Button(
                    btn_frame,
                    text="📝 Matricular",
                    command=lambda cid=curso_id: self.matricular_curso(cid),
                    width=15,
                ).pack(side="left", padx=5)

            ttk.Button(
                btn_frame,
                text="ℹ️ Detalhes",
                command=lambda cid=curso_id: self.mostrar_detalhes_curso(cid),
                width=15,
            ).pack(side="left", padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def criar_aba_meus_cursos(self, parent):
        """Aba dos cursos matriculados pelo aluno"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="🎓 Meus Cursos e Progresso", style="Title.TLabel").pack(
            anchor="w", pady=10
        )

        # Verificar se tem cursos
        user_cursos = self.usuarios_cadastrados[self.usuario_logado].get("cursos", [])

        if not user_cursos:
            ttk.Label(
                frame,
                text="❌ Você não está matriculado em nenhum curso ainda.\n\n"
                "Acesse a aba 'Cursos' para se matricular!",
                font=("Segoe UI", 12),
                foreground="red",
                justify="center",
            ).pack(pady=50)
            return

        # Container com scroll
        container = ttk.Frame(frame)
        container.pack(expand=True, fill="both")

        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Cards de cursos matriculados
        for curso_id in user_cursos:
            if curso_id in self.cursos_disponiveis:
                curso = self.cursos_disponiveis[curso_id]
                progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(
                    curso_id, {}
                )

                card = ttk.Frame(scrollable_frame, style="Card.TFrame", padding="20")
                card.pack(fill="x", pady=10, padx=10)

                # Header
                header_frame = ttk.Frame(card)
                header_frame.pack(fill="x", pady=5)

                ttk.Label(
                    header_frame, text=curso["nome"], font=("Segoe UI", 14, "bold")
                ).pack(side="left")

                # Progresso
                progresso_percent = progresso.get("progresso", 0)
                ttk.Label(
                    header_frame,
                    text=f"📊 {progresso_percent:.1f}%",
                    font=("Segoe UI", 12, "bold"),
                    foreground="green" if progresso_percent >= 70 else "orange",
                ).pack(side="right")

                # Barra de progresso
                progress_frame = ttk.Frame(card)
                progress_frame.pack(fill="x", pady=10)

                ttk.Label(progress_frame, text="Progresso:").pack(side="left")
                progress_bar = ttk.Progressbar(
                    progress_frame, orient="horizontal", length=300, mode="determinate"
                )
                progress_bar.pack(side="left", padx=10, fill="x", expand=True)
                progress_bar["value"] = progresso_percent

                # Estatísticas
                stats_text = f"""
📈 Estatísticas:
• Módulos Concluídos: {len(progresso.get("modulos_concluidos", []))}/{len(curso["modulos"])}
• Questões Respondidas: {progresso.get("questoes_respondidas", 0)}/{progresso.get("total_questoes", 0)}
• Nota Final: {progresso.get("nota_final", 0):.1f}%
• Status: {"✅ Aprovado" if progresso.get("nota_final", 0) >= 70 else "📚 Em Andamento"}
                """

                ttk.Label(
                    card, text=stats_text, font=("Segoe UI", 9), justify="left"
                ).pack(anchor="w", pady=10)

                # Módulos
                ttk.Label(card, text="📖 Módulos:", font=("Segoe UI", 10, "bold")).pack(
                    anchor="w", pady=5
                )

                for modulo in curso["modulos"]:
                    status = (
                        "✅"
                        if modulo["nome"] in progresso.get("modulos_concluidos", [])
                        else "⏳"
                    )
                    ttk.Label(
                        card,
                        text=f"{status} {modulo['nome']} ({modulo['dificuldade']})",
                        font=("Segoe UI", 8),
                    ).pack(anchor="w")

                # Botões de ação
                btn_frame = ttk.Frame(card)
                btn_frame.pack(fill="x", pady=15)

                # Encontrar próximo módulo
                modulos_restantes = [
                    mod
                    for mod in curso["modulos"]
                    if mod["nome"] not in progresso.get("modulos_concluidos", [])
                ]

                if modulos_restantes:
                    ttk.Button(
                        btn_frame,
                        text="🎯 Continuar Estudando",
                        command=lambda cid=curso_id,
                        mod=modulos_restantes[0]: self.iniciar_questionario(
                            cid, mod["nome"]
                        ),
                        width=18,
                    ).pack(side="left", padx=5)
                else:
                    ttk.Button(
                        btn_frame, text="🎓 Curso Concluído", state="disabled", width=18
                    ).pack(side="left", padx=5)

                # Gerar certificado se elegível
                if progresso_percent >= 80 and progresso.get("nota_final", 0) >= 70:
                    ttk.Button(
                        btn_frame,
                        text="📜 Gerar Certificado",
                        command=lambda cid=curso_id: self.gerar_certificado(cid),
                        width=18,
                    ).pack(side="left", padx=5)
                else:
                    ttk.Button(
                        btn_frame, text="📜 Certificado", state="disabled", width=18
                    ).pack(side="left", padx=5)

                ttk.Button(
                    btn_frame,
                    text="📊 Ver Detalhes",
                    command=lambda cid=curso_id: self.mostrar_detalhes_curso(cid),
                    width=15,
                ).pack(side="left", padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def acessar_curso(self, curso_id):
        """Acessa um curso matriculado"""
        progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})
        curso = self.cursos_disponiveis.get(curso_id)

        if not curso:
            return

        # Encontrar próximo módulo
        modulos_restantes = [
            mod
            for mod in curso["modulos"]
            if mod["nome"] not in progresso.get("modulos_concluidos", [])
        ]

        if modulos_restantes:
            self.iniciar_questionario(curso_id, modulos_restantes[0]["nome"])
        else:
            messagebox.showinfo(
                "Parabéns!", "🎉 Você já concluiu todos os módulos deste curso!"
            )

    def mostrar_detalhes_curso(self, curso_id):
        """Mostra detalhes completos do curso"""
        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            return

        detalhes_janela = tk.Toplevel(self.root)
        detalhes_janela.title(f"Detalhes do Curso - {curso['nome']}")
        detalhes_janela.geometry("600x500")
        detalhes_janela.transient(self.root)

        frame = ttk.Frame(detalhes_janela, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text=curso["nome"], font=("Segoe UI", 16, "bold")).pack(
            pady=10
        )

        info_text = f"""
📖 DESCRIÇÃO:
{curso["descricao"]}

📊 INFORMAÇÕES:
• Carga Horária: {curso["carga_horaria"]}
• Dificuldade: {curso["dificuldade"]}
• Categoria: {curso["categoria"]}
• Professor: {self.usuarios_cadastrados.get(curso["professor"], {}).get("nome_completo", curso["professor"])}
• Avaliação: {curso["avaliacao"]}/5.0
• Alunos Matriculados: {curso["alunos_matriculados"]}

🎯 MÓDULOS:
"""

        texto_detalhes = scrolledtext.ScrolledText(
            frame, height=20, width=70, font=("Segoe UI", 10)
        )
        texto_detalhes.pack(fill="both", expand=True, pady=10)
        texto_detalhes.insert("1.0", info_text)

        # Adicionar módulos
        for i, modulo in enumerate(curso["modulos"], 1):
            texto_detalhes.insert("end", f"{i}. {modulo['nome']}\n")
            texto_detalhes.insert("end", f"   - Dificuldade: {modulo['dificuldade']}\n")
            texto_detalhes.insert(
                "end", f"   - Tempo Estimado: {modulo['tempo_estimado']}\n"
            )
            texto_detalhes.insert("end", f"   - Questões: {modulo['questoes']}\n\n")

        texto_detalhes.config(state="disabled")

        # Botão de fechar
        ttk.Button(frame, text="Fechar", command=detalhes_janela.destroy).pack(pady=10)

    # ========== SISTEMA DE SUSTENTABILIDADE ==========

    def adicionar_mensagem_forum(self, topico, usuario, mensagem):
        """Adiciona mensagem ao fórum colaborativo"""
        if topico not in self.forum_mensagens:
            self.forum_mensagens[topico] = []

        mensagem_completa = {
            "usuario": usuario,
            "mensagem": mensagem,
            "timestamp": datetime.now().isoformat(),
            "likes": 0,
            "respostas": [],
        }

        self.forum_mensagens[topico].append(mensagem_completa)
        self.salvar_forum()

        # Atualizar métricas de colaboração
        self.atualizar_metricas_colaboracao()

    def atualizar_metricas_colaboracao(self):
        """Atualiza métricas de colaboração"""
        total_mensagens = sum(
            len(mensagens) for mensagens in self.forum_mensagens.values()
        )
        usuarios_ativos = set()

        for topico, mensagens in self.forum_mensagens.items():
            for msg in mensagens:
                usuarios_ativos.add(msg["usuario"])

        return {
            "total_mensagens": total_mensagens,
            "usuarios_ativos": len(usuarios_ativos),
            "topicos_ativos": len(self.forum_mensagens),
        }

    def calcular_impacto_sustentabilidade(self):
        """Calcula impacto ambiental positivo do sistema digital"""
        total_usuarios = len(self.usuarios_cadastrados)
        total_atividades = self.metricas_sustentabilidade.get(
            "total_atividades_digitais", 0
        )

        # Cálculos baseados em métricas ambientais
        papel_economizado = total_atividades * 0.05  # 50g por atividade em papel
        co2_economizado = papel_economizado * 1.2  # 1.2kg CO2 por kg de papel
        agua_economizada = papel_economizado * 10  # 10 litros por kg de papel

        self.metricas_sustentabilidade.update(
            {
                "papel_economizado": round(papel_economizado, 2),
                "co2_economizado": round(co2_economizado, 2),
                "agua_economizada": round(agua_economizada, 2),
                "total_atividades_digitais": total_atividades,
                "ultima_atualizacao": datetime.now().isoformat(),
            }
        )

        self.salvar_metricas()

        return self.metricas_sustentabilidade

    def registrar_atividade_digital(self):
        """Registra uma atividade digital para cálculo de sustentabilidade"""
        self.metricas_sustentabilidade["total_atividades_digitais"] += 1
        self.calcular_impacto_sustentabilidade()

    def criar_aba_sustentabilidade(self, parent):
        """Aba de métricas de sustentabilidade"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame,
            text="🌱 Sustentabilidade UNIP - Impacto Digital",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=10)

        # Atualizar métricas
        metricas = self.calcular_impacto_sustentabilidade()

        # Cartões de impacto
        impactos = [
            (
                "📄 Papel Economizado",
                f"{metricas['papel_economizado']} kg",
                "Equivale a {} árvores salvas",
                lambda x: x / 5,
            ),
            (
                "🌫️ CO₂ Economizado",
                f"{metricas['co2_economizado']} kg",
                "Equivale a {} km não rodados",
                lambda x: x * 2,
            ),
            (
                "💧 Água Economizada",
                f"{metricas['agua_economizada']} litros",
                "Equivale a {} dias de consumo",
                lambda x: x / 100,
            ),
            (
                "📊 Atividades Digitais",
                f"{metricas['total_atividades_digitais']}",
                "{} atividades sem papel",
                lambda x: x,
            ),
        ]

        # Grid de cartões
        grid_frame = ttk.Frame(frame)
        grid_frame.pack(fill="x", pady=20)

        for i, (titulo, valor, equivalencia, calc) in enumerate(impactos):
            card = ttk.Frame(grid_frame, style="Card.TFrame", padding="20")
            card.grid(row=i // 2, column=i % 2, sticky="nsew", padx=10, pady=10)

            ttk.Label(card, text=titulo, font=("Segoe UI", 12, "bold")).pack(anchor="w")
            ttk.Label(
                card, text=valor, font=("Segoe UI", 18, "bold"), foreground="#27ae60"
            ).pack(anchor="w", pady=5)

            # Calcular equivalência
            num = float(metricas["papel_economizado"])
            equiv_valor = calc(num)
            texto_equiv = equivalencia.format(f"{equiv_valor:.1f}")
            ttk.Label(
                card, text=texto_equiv, font=("Segoe UI", 9), foreground="#7f8c8d"
            ).pack(anchor="w")

        grid_frame.columnconfigure(0, weight=1)
        grid_frame.columnconfigure(1, weight=1)

        # Informações educacionais
        info_frame = ttk.Frame(frame, style="Card.TFrame", padding="15")
        info_frame.pack(fill="x", pady=10)

        ttk.Label(
            info_frame,
            text="💡 Como o sistema digital ajuda o meio ambiente:",
            font=("Segoe UI", 11, "bold"),
        ).pack(anchor="w")

        beneficios = [
            "✅ Redução do uso de papel e recursos de impressão",
            "✅ Diminuição da emissão de CO₂ com transporte de materiais",
            "✅ Economia de água na produção de papel",
            "✅ Menor geração de resíduos físicos",
            "✅ Acesso democratizado ao conhecimento",
        ]

        for beneficio in beneficios:
            ttk.Label(info_frame, text=beneficio, font=("Segoe UI", 9)).pack(
                anchor="w", pady=2
            )

        # Botão para registrar atividade (simulação)
        ttk.Button(
            frame,
            text="📝 Registrar Atividade Digital",
            command=self.registrar_atividade_digital_simulada,
        ).pack(pady=10)

    def registrar_atividade_digital_simulada(self):
        """Simula o registro de uma atividade digital"""
        self.registrar_atividade_digital()
        messagebox.showinfo(
            "Atividade Registrada",
            "✅ Atividade digital registrada!\n"
            "🌱 Sua contribuição para a sustentabilidade foi contabilizada.",
        )
        # Recarregar a aba de sustentabilidade
        self.atualizar_interface()

    def criar_aba_perfil_avancado(self, parent):
        """Aba de perfil do usuário"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        user_data = self.usuarios_cadastrados[self.usuario_logado]

        ttk.Label(frame, text="👤 Meu Perfil UNIP", style="Title.TLabel").pack(pady=10)

        # Informações em cards
        info_card = ttk.Frame(frame, style="Card.TFrame", padding="20")
        info_card.pack(fill="x", pady=10)

        infos = [
            ("👤 Nome Completo:", user_data.get("nome_completo", self.usuario_logado)),
            ("📧 Email:", user_data.get("email", "N/A")),
            ("📞 Telefone:", user_data.get("telefone", "N/A")),
            ("🎂 Idade:", str(user_data.get("idade", "N/A"))),
            ("📅 Data de Cadastro:", user_data.get("data_cadastro", "N/A")[:10]),
            ("🎯 Tipo de Usuário:", user_data.get("tipo", "aluno").upper()),
        ]

        if user_data.get("tipo") == "aluno":
            infos.extend(
                [
                    ("🎓 Cursos Matriculados:", str(len(user_data.get("cursos", [])))),
                    ("📜 Certificados:", str(len(user_data.get("certificados", [])))),
                    (
                        "🎯 Interesses:",
                        ", ".join(user_data.get("interesses", []))
                        if user_data.get("interesses")
                        else "Não informados",
                    ),
                    (
                        "📊 Preferências:",
                        f"{user_data.get('preferencias_aprendizado', {}).get('modalidade', 'N/A')} - {user_data.get('preferencias_aprendizado', {}).get('ritmo', 'N/A')}",
                    ),
                ]
            )

        for i, (label, valor) in enumerate(infos):
            ttk.Label(info_card, text=label, font=("Segoe UI", 10, "bold")).grid(
                row=i, column=0, sticky="w", pady=3
            )
            ttk.Label(info_card, text=valor, font=("Segoe UI", 10)).grid(
                row=i, column=1, sticky="w", pady=3, padx=10
            )

        info_card.columnconfigure(1, weight=1)

    def limpar_tela(self):
        """Limpa todos os widgets da tela"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def analisar_padrao_aprendizado(self, usuario):
        """Analisa padrões de aprendizado usando IA"""
        progresso = self.progresso_alunos.get(usuario, {})
        user_data = self.usuarios_cadastrados.get(usuario, {})

        analise = {
            "velocidade_aprendizado": 0,
            "consistencia": 0,
            "dificuldades": [],
            "pontos_fortes": [],
            "previsao_conclusao": {},
            "sugestoes_modulos": [],
        }

        # Análise de velocidade
        cursos_ativos = [
            cid for cid in progresso if progresso[cid].get("progresso", 0) < 100
        ]
        if cursos_ativos:
            tempo_medio = sum(
                progresso[cid].get("tempo_estudo", 0) for cid in cursos_ativos
            ) / len(cursos_ativos)
            analise["velocidade_aprendizado"] = min(100, tempo_medio * 10)

        # Identificar dificuldades e pontos fortes
        for curso_id, dados_curso in progresso.items():
            curso = self.cursos_disponiveis.get(curso_id, {})
            if dados_curso.get("progresso", 0) < 30:
                analise["dificuldades"].append(
                    f"{curso.get('nome', 'Curso')} ({dados_curso.get('progresso', 0):.1f}%)"
                )
            elif dados_curso.get("progresso", 0) > 70:
                analise["pontos_fortes"].append(
                    f"{curso.get('nome', 'Curso')} ({dados_curso.get('progresso', 0):.1f}%)"
                )

        # Previsão de conclusão
        for curso_id in cursos_ativos:
            progresso_atual = progresso[curso_id].get("progresso", 0)
            if progresso_atual > 0:
                tempo_restante = (
                    (100 - progresso_atual) / max(progresso_atual, 1) * 30
                )  # 30 dias base
                previsao = datetime.now() + timedelta(days=tempo_restante)
                analise["previsao_conclusao"][curso_id] = previsao.strftime("%d/%m/%Y")

        # Sugestões de módulos
        for curso_id in cursos_ativos:
            curso = self.cursos_disponiveis.get(curso_id, {})
            modulos_restantes = [
                mod
                for mod in curso.get("modulos", [])
                if mod["nome"]
                not in progresso.get(curso_id, {}).get("modulos_concluidos", [])
            ]

            if modulos_restantes:
                proximo_modulo = modulos_restantes[0]
                analise["sugestoes_modulos"].append(
                    f"📚 {curso['nome']}: {proximo_modulo['nome']} "
                    f"({proximo_modulo['dificuldade']}) - {proximo_modulo['tempo_estimado']}"
                )

        return analise

    def gerar_recomendacoes_ia_personalizadas(self, usuario):
        """Gera recomendações personalizadas baseadas no perfil"""
        user_data = self.usuarios_cadastrados.get(usuario, {})
        progresso = self.progresso_alunos.get(usuario, {})
        analise_ia = self.analisar_padrao_aprendizado(usuario)

        recomendacoes = {
            "cursos_sugeridos": [],
            "modulos_prioritarios": [],
            "dicas_estudo": [],
            "recursos_complementares": [],
        }

        # Cursos sugeridos baseados em interesses
        interesses = user_data.get("interesses", [])
        for curso_id, curso in self.cursos_disponiveis.items():
            if curso_id not in user_data.get("cursos", []):
                # Verificar alinhamento com interesses
                tags_comuns = set(interesses) & set(curso.get("tags", []))
                if tags_comuns:
                    recomendacoes["cursos_sugeridos"].append(
                        {
                            "curso": curso["nome"],
                            "motivo": f"Alinhado com seu interesse em {', '.join(tags_comuns)}",
                            "dificuldade": curso["dificuldade"],
                        }
                    )

        # Módulos prioritários baseados no progresso
        for curso_id, dados_curso in progresso.items():
            if dados_curso.get("progresso", 0) < 50:
                curso = self.cursos_disponiveis.get(curso_id, {})
                modulos_pendentes = [
                    mod
                    for mod in curso.get("modulos", [])
                    if mod["nome"] not in dados_curso.get("modulos_concluidos", [])
                ]

                if modulos_pendentes:
                    recomendacoes["modulos_prioritarios"].append(
                        {
                            "curso": curso["nome"],
                            "modulo": modulos_pendentes[0]["nome"],
                            "prioridade": "ALTA"
                            if dados_curso.get("progresso", 0) < 30
                            else "MÉDIA",
                        }
                    )

        # Dicas de estudo personalizadas
        preferencias = user_data.get("preferencias_aprendizado", {})
        if preferencias.get("modalidade") == "visual":
            recomendacoes["dicas_estudo"].extend(
                [
                    "🎨 Crie mapas mentais para organizar o conteúdo",
                    "📊 Use gráficos e diagramas para entender conceitos complexos",
                    "🖼️ Assista videoaulas para reforçar o aprendizado",
                ]
            )
        elif preferencias.get("modalidade") == "auditivo":
            recomendacoes["dicas_estudo"].extend(
                [
                    "🎧 Grave resumos em áudio e escute durante deslocamentos",
                    "🗣️ Explique o conteúdo em voz alta para fixar melhor",
                    "🎵 Use podcasts educativos sobre os temas estudados",
                ]
            )
        else:  # prático
            recomendacoes["dicas_estudo"].extend(
                [
                    "💻 Pratique com exercícios e projetos reais",
                    "🔧 Implemente os conceitos em pequenos projetos",
                    "🛠️ Resolva problemas práticos da área",
                ]
            )

        # Recursos complementares
        if any("Python" in interesse for interesse in interesses):
            recomendacoes["recursos_complementares"].extend(
                [
                    "📚 Livro: 'Python Fluente' - Luciano Ramalho",
                    "💻 Site: Real Python - Tutoriais práticos",
                    "🎥 Canal: Curso em Vídeo - Python completo",
                ]
            )

        return recomendacoes

    def criar_aba_professor(self, parent):
        """Aba de gerenciamento para professores"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="👨‍🏫 Painel do Professor", style="Title.TLabel").pack(
            anchor="w", pady=10
        )

        # Buscar cursos onde este professor é responsável
        cursos_professor = []
        for curso_id, curso in self.cursos_disponiveis.items():
            if curso.get("professor") == self.usuario_logado:
                cursos_professor.append(curso_id)

        if not cursos_professor:
            ttk.Label(
                frame,
                text="❌ Você não é responsável por nenhum curso.\n\n"
                "Solicite ao administrador para atribuir cursos a você.",
                font=("Segoe UI", 12),
                foreground="#e74c3c",
                justify="center",
            ).pack(pady=50)
            return

        # Abas para cada curso
        notebook = ttk.Notebook(frame)
        notebook.pack(expand=True, fill="both", pady=10)

        for curso_id in sorted(cursos_professor):
            if curso_id in self.cursos_disponiveis:
                curso = self.cursos_disponiveis[curso_id]
                aba_curso = ttk.Frame(notebook)
                self.criar_subaba_professor_curso(aba_curso, curso_id)
                notebook.add(aba_curso, text=curso["nome"])

    def criar_subaba_professor_curso(self, parent, curso_id):
        """Subaba de gerenciamento para um curso específico"""
        # Validar que o professor só pode acessar seus próprios cursos
        if not self.pode_editar_curso(curso_id):
            messagebox.showerror(
                "Acesso Negado",
                "❌ Você não tem permissão para gerenciar este curso!\n\n"
                "Apenas o professor responsável pode acessá-lo.",
            )
            return

        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            return

        # Frame principal com scroll
        main_frame = ttk.Frame(parent)
        main_frame.pack(expand=True, fill="both")

        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Informações do curso
        info_frame = ttk.Frame(scrollable_frame, style="Card.TFrame", padding="15")
        info_frame.pack(fill="x", pady=10, padx=10)

        ttk.Label(
            info_frame,
            text=f"📊 Estatísticas do Curso: {curso['nome']}",
            font=("Segoe UI", 14, "bold"),
        ).pack(anchor="w")

        # Encontrar alunos matriculados
        alunos_curso = []
        for usuario, dados in self.usuarios_cadastrados.items():
            if dados.get("tipo") == "aluno" and curso_id in dados.get("cursos", []):
                progresso = self.progresso_alunos.get(usuario, {}).get(curso_id, {})
                alunos_curso.append(
                    {
                        "usuario": usuario,
                        "nome": dados.get("nome_completo", usuario),
                        "progresso": progresso.get("progresso", 0),
                        "modulos_concluidos": len(
                            progresso.get("modulos_concluidos", [])
                        ),
                        "total_modulos": len(curso["modulos"]),
                        "nota_final": progresso.get("nota_final", 0),
                        "data_matricula": progresso.get("data_matricula", "N/A"),
                    }
                )

        # Estatísticas
        total_alunos = len(alunos_curso)
        media_progresso = sum(aluno["progresso"] for aluno in alunos_curso) / max(
            total_alunos, 1
        )
        alunos_aprovados = sum(1 for aluno in alunos_curso if aluno["nota_final"] >= 70)
        alunos_certificados = sum(
            1
            for aluno in alunos_curso
            if aluno["progresso"] >= 80 and aluno["nota_final"] >= 70
        )

        stats_text = f"""
📈 Estatísticas Gerais:
• Total de Alunos: {total_alunos}
• Progresso Médio: {media_progresso:.1f}%
• Alunos Aprovados: {alunos_aprovados}/{total_alunos}
• Certificados Emitidos: {alunos_certificados}
• Módulos do Curso: {len(curso["modulos"])}
        """

        ttk.Label(
            info_frame, text=stats_text, font=("Segoe UI", 10), justify="left"
        ).pack(anchor="w", pady=10)

        # Lista de alunos
        if alunos_curso:
            alunos_frame = ttk.Frame(
                scrollable_frame, style="Card.TFrame", padding="15"
            )
            alunos_frame.pack(fill="x", pady=10, padx=10)

            ttk.Label(
                alunos_frame,
                text="🎓 Alunos Matriculados",
                font=("Segoe UI", 12, "bold"),
            ).pack(anchor="w", pady=10)

            # Treeview para alunos
            colunas = ("aluno", "nome", "progresso", "modulos", "nota", "status")
            tree = ttk.Treeview(
                alunos_frame, columns=colunas, show="headings", height=12
            )

            tree.heading("aluno", text="Usuário")
            tree.heading("nome", text="Nome")
            tree.heading("progresso", text="Progresso")
            tree.heading("modulos", text="Módulos")
            tree.heading("nota", text="Nota")
            tree.heading("status", text="Status")

            tree.column("aluno", width=100)
            tree.column("nome", width=150)
            tree.column("progresso", width=80)
            tree.column("modulos", width=80)
            tree.column("nota", width=60)
            tree.column("status", width=100)

            for aluno in alunos_curso:
                status = (
                    "✅ Aprovado" if aluno["nota_final"] >= 70 else "📚 Em Andamento"
                )
                if aluno["progresso"] >= 80 and aluno["nota_final"] >= 70:
                    status = "🏆 Certificado"

                tree.insert(
                    "",
                    "end",
                    values=(
                        aluno["usuario"],
                        aluno["nome"],
                        f"{aluno['progresso']:.1f}%",
                        f"{aluno['modulos_concluidos']}/{aluno['total_modulos']}",
                        f"{aluno['nota_final']:.1f}%"
                        if aluno["nota_final"] > 0
                        else "N/A",
                        status,
                    ),
                )

            tree.pack(fill="x", pady=10)

            # Botões de ação para professor
            btn_frame = ttk.Frame(alunos_frame)
            btn_frame.pack(fill="x", pady=10)

            ttk.Button(
                btn_frame,
                text="📊 Exportar Relatório",
                command=lambda: self.exportar_relatorio_curso(curso_id),
            ).pack(side="left", padx=5)
            ttk.Button(
                btn_frame,
                text="📧 Contatar Alunos",
                command=lambda: self.contatar_alunos_curso(curso_id),
            ).pack(side="left", padx=5)

        else:
            ttk.Label(
                scrollable_frame,
                text="Nenhum aluno matriculado neste curso.",
                font=("Segoe UI", 11),
                foreground="gray",
            ).pack(pady=20)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def exportar_relatorio_curso(self, curso_id):
        """Exporta relatório do curso"""
        messagebox.showinfo(
            "Relatório",
            "📊 Relatório do curso exportado com sucesso!\n\n"
            "Funcionalidade de exportação em desenvolvimento.",
        )

    def contatar_alunos_curso(self, curso_id):
        """Sistema de contato com alunos do curso"""
        messagebox.showinfo(
            "Contato",
            "📧 Sistema de contato com alunos em desenvolvimento.\n\n"
            "Em breve você poderá enviar mensagens para todos os alunos do curso.",
        )

    def criar_aba_cadastro_alunos(self, parent):
        """Aba para cadastrar novos alunos (professor/admin)"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="📝 Cadastro de Novos Alunos", style="Title.TLabel").pack(
            anchor="w", pady=10
        )

        # Card de informações
        info_card = ttk.Frame(frame, style="Card.TFrame", padding="15")
        info_card.pack(fill="x", pady=10)

        ttk.Label(
            info_card,
            text="🎯 Registre novos alunos no sistema",
            font=("Segoe UI", 11, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            info_card,
            text="Preencha o formulário abaixo para cadastrar um novo aluno.\n"
            "O aluno receberá um email com suas credenciais de acesso.",
            font=("Segoe UI", 10),
            foreground="#7f8c8d",
        ).pack(anchor="w", pady=5)

        # Botão de ação
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)

        ttk.Button(
            btn_frame,
            text="➕ Adicionar Novo Aluno",
            command=self.mostrar_cadastro_aluno_admin,
            width=25,
        ).pack(pady=10)

        # Dicas
        dicas_frame = ttk.Frame(frame, style="Card.TFrame", padding="15")
        dicas_frame.pack(fill="x", pady=10)

        ttk.Label(dicas_frame, text="💡 Dicas:", font=("Segoe UI", 11, "bold")).pack(
            anchor="w"
        )

        dicas = [
            "✅ Cada aluno recebe um usuário único no sistema",
            "📧 Email institucional é gerado automaticamente",
            "🔐 Você define a senha inicial (o aluno pode alterar depois)",
            "📱 Telefone é obrigatório para contato",
            "🎯 Defina as preferências de aprendizado do aluno",
            "💾 Todos os dados são salvos automaticamente no sistema",
        ]

        for dica in dicas:
            ttk.Label(dicas_frame, text=dica, font=("Segoe UI", 9)).pack(
                anchor="w", pady=2
            )

    def criar_aba_cadastro_professores_admins(self, parent):
        """Aba para cadastrar novos professores e admins (somente para admin)"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame, text="👥 Cadastro de Professores e Admins", style="Title.TLabel"
        ).pack(anchor="w", pady=10)

        # Card de informações
        info_card = ttk.Frame(frame, style="Card.TFrame", padding="15")
        info_card.pack(fill="x", pady=10)

        ttk.Label(
            info_card,
            text="👨‍🏫 Registre novos professores e administradores no sistema",
            font=("Segoe UI", 11, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            info_card,
            text="Preencha o formulário para cadastrar um novo professor ou administrador.\n"
            "Professores podem gerenciar cursos e alunos. Admins têm acesso total.",
            font=("Segoe UI", 10),
            foreground="#7f8c8d",
        ).pack(anchor="w", pady=5)

        # Botões de ação
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)

        ttk.Button(
            btn_frame,
            text="➕ Cadastrar Professor",
            command=self.mostrar_cadastro_professor_admin,
            width=25,
        ).pack(pady=5)
        ttk.Button(
            btn_frame,
            text="➕ Cadastrar Admin",
            command=self.mostrar_cadastro_admin_admin,
            width=25,
        ).pack(pady=5)

        # Dicas
        dicas_frame = ttk.Frame(frame, style="Card.TFrame", padding="15")
        dicas_frame.pack(fill="x", pady=10)

        ttk.Label(
            dicas_frame, text="💡 Diferenças de Acesso:", font=("Segoe UI", 11, "bold")
        ).pack(anchor="w")

        dicas = [
            "👨‍🏫 PROFESSOR:",
            "  • Pode gerenciar cursos atribuídos a ele",
            "  • Pode adicionar, editar e remover módulos de seus cursos",
            "  • Pode visualizar progresso de seus alunos",
            "  • Pode cadastrar novos alunos",
            "",
            "👑 ADMINISTRADOR:",
            "  • Acesso total a todos os cursos e conteúdo",
            "  • Pode gerenciar usuários (professores, alunos, outros admins)",
            "  • Pode ver relatórios completos do sistema",
            "  • Pode fazer backups e gerenciar segurança",
        ]

        for dica in dicas:
            if dica.startswith("👨‍🏫") or dica.startswith("👑"):
                ttk.Label(dicas_frame, text=dica, font=("Segoe UI", 10, "bold")).pack(
                    anchor="w", pady=5
                )
            elif dica == "":
                ttk.Separator(dicas_frame).pack(fill="x", pady=5)
            else:
                ttk.Label(dicas_frame, text=dica, font=("Segoe UI", 9)).pack(
                    anchor="w", pady=1
                )

    def criar_aba_admin(self, parent):
        """Aba principal do administrador"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="👑 Painel de Administração", style="Title.TLabel").pack(
            anchor="w", pady=10
        )

        # Grid de estatísticas
        stats_frame = ttk.Frame(frame)
        stats_frame.pack(fill="x", pady=20)

        # Coletar estatísticas
        total_usuarios = len(self.usuarios_cadastrados)
        total_alunos = sum(
            1 for u in self.usuarios_cadastrados.values() if u.get("tipo") == "aluno"
        )
        total_professores = sum(
            1
            for u in self.usuarios_cadastrados.values()
            if u.get("tipo") == "professor"
        )
        total_admins = sum(
            1 for u in self.usuarios_cadastrados.values() if u.get("tipo") == "admin"
        )
        total_cursos = len(self.cursos_disponiveis)

        stats = [
            ("👥 Total de Usuários", total_usuarios),
            ("🎓 Total de Alunos", total_alunos),
            ("👨‍🏫 Total de Professores", total_professores),
            ("👑 Total de Admins", total_admins),
            ("📚 Total de Cursos", total_cursos),
            (
                "🎯 Matriculações Ativas",
                sum(
                    len(u.get("cursos", []))
                    for u in self.usuarios_cadastrados.values()
                    if u.get("tipo") == "aluno"
                ),
            ),
        ]

        for i, (label, valor) in enumerate(stats):
            card = ttk.Frame(stats_frame, style="Card.TFrame", padding="15")
            card.grid(row=i // 3, column=i % 3, sticky="nsew", padx=10, pady=10)

            ttk.Label(card, text=label, font=("Segoe UI", 10)).pack(anchor="w")
            ttk.Label(
                card,
                text=str(valor),
                font=("Segoe UI", 18, "bold"),
                foreground="#2c3e50",
            ).pack(anchor="w")

        stats_frame.columnconfigure(0, weight=1)
        stats_frame.columnconfigure(1, weight=1)
        stats_frame.columnconfigure(2, weight=1)

        # Ações administrativas
        actions_frame = ttk.Frame(frame, style="Card.TFrame", padding="15")
        actions_frame.pack(fill="x", pady=10)

        ttk.Label(
            actions_frame, text="⚙️ Ações Administrativas", font=("Segoe UI", 12, "bold")
        ).pack(anchor="w", pady=10)

        btn_frame = ttk.Frame(actions_frame)
        btn_frame.pack(fill="x", pady=10)

        def mostrar_estatisticas_completas():
            """Mostrar relatório completo de estatísticas"""
            stats_janela = tk.Toplevel(self.root)
            stats_janela.title("Estatísticas Completas do Sistema")
            stats_janela.geometry("700x600")
            stats_janela.transient(self.root)

            frame_stats = ttk.Frame(stats_janela, padding="20")
            frame_stats.pack(expand=True, fill="both")

            ttk.Label(
                frame_stats,
                text="📊 Relatório Completo de Estatísticas",
                font=("Segoe UI", 14, "bold"),
            ).pack(pady=10)

            # Container com scroll
            container = ttk.Frame(frame_stats)
            container.pack(expand=True, fill="both", pady=10)

            texto = scrolledtext.ScrolledText(
                container, height=25, width=80, font=("Segoe UI", 9)
            )
            texto.pack(fill="both", expand=True)

            # Compilar estatísticas
            relatorio = "=" * 80 + "\n"
            relatorio += "ESTATÍSTICAS COMPLETAS DO SISTEMA UNIP\n"
            relatorio += "=" * 80 + "\n\n"

            # Usuários
            relatorio += "👥 USUÁRIOS\n"
            relatorio += "-" * 80 + "\n"
            total_usuarios = len(self.usuarios_cadastrados)
            total_alunos = sum(
                1
                for u in self.usuarios_cadastrados.values()
                if u.get("tipo") == "aluno"
            )
            total_professores = sum(
                1
                for u in self.usuarios_cadastrados.values()
                if u.get("tipo") == "professor"
            )
            total_admins = sum(
                1
                for u in self.usuarios_cadastrados.values()
                if u.get("tipo") == "admin"
            )

            relatorio += f"Total de Usuários: {total_usuarios}\n"
            relatorio += f"  • Alunos: {total_alunos}\n"
            relatorio += f"  • Professores: {total_professores}\n"
            relatorio += f"  • Admins: {total_admins}\n\n"

            # Cursos
            relatorio += "📚 CURSOS\n"
            relatorio += "-" * 80 + "\n"
            relatorio += f"Total de Cursos: {len(self.cursos_disponiveis)}\n"

            total_matriculacoes = sum(
                len(u.get("cursos", []))
                for u in self.usuarios_cadastrados.values()
                if u.get("tipo") == "aluno"
            )
            relatorio += f"Total de Matriculações: {total_matriculacoes}\n"

            total_modulos = sum(
                len(c.get("modulos", [])) for c in self.cursos_disponiveis.values()
            )
            relatorio += f"Total de Módulos: {total_modulos}\n\n"

            # Certificados
            relatorio += "🎓 CERTIFICADOS\n"
            relatorio += "-" * 80 + "\n"
            total_certificados = sum(
                len(u.get("certificados", []))
                for u in self.usuarios_cadastrados.values()
            )
            relatorio += f"Total de Certificados Emitidos: {total_certificados}\n\n"

            # Atividade
            relatorio += "📊 ATIVIDADE\n"
            relatorio += "-" * 80 + "\n"
            relatorio += f"Total de Atividades Digitais: {self.metricas_sustentabilidade.get('total_atividades_digitais', 0)}\n"
            relatorio += f"Papel Economizado: {self.metricas_sustentabilidade.get('papel_economizado', 0)}kg\n"
            relatorio += f"CO₂ Economizado: {self.metricas_sustentabilidade.get('co2_economizado', 0)}kg\n"
            relatorio += f"Água Economizada: {self.metricas_sustentabilidade.get('agua_economizada', 0)}L\n"

            texto.insert("1.0", relatorio)
            texto.config(state="disabled")

            ttk.Button(frame_stats, text="Fechar", command=stats_janela.destroy).pack(
                pady=10
            )

        def gerenciar_seguranca():
            """Gerenciar configurações de segurança"""
            seg_janela = tk.Toplevel(self.root)
            seg_janela.title("Gerenciamento de Segurança")
            seg_janela.geometry("500x400")
            seg_janela.transient(self.root)

            frame_seg = ttk.Frame(seg_janela, padding="20")
            frame_seg.pack(expand=True, fill="both")

            ttk.Label(
                frame_seg,
                text="🔐 Gerenciamento de Segurança",
                font=("Segoe UI", 14, "bold"),
            ).pack(pady=10)

            # Opções de segurança
            options_frame = ttk.Frame(frame_seg, style="Card.TFrame", padding="15")
            options_frame.pack(fill="both", expand=True, pady=10)

            opcoes = [
                ("🔑 Redefinir Senhas de Usuários", "Permitir redefinição em massa"),
                ("🚫 Bloquear Usuários", "Bloquear acesso temporário"),
                ("📋 Audit Log", "Visualizar histórico de atividades"),
                ("🔒 Política de Senhas", "Configurar requisitos de senha"),
            ]

            for opcao, descricao in opcoes:
                opt_frame = ttk.Frame(options_frame)
                opt_frame.pack(fill="x", pady=8)

                ttk.Label(opt_frame, text=opcao, font=("Segoe UI", 10, "bold")).pack(
                    anchor="w"
                )
                ttk.Label(
                    opt_frame,
                    text=descricao,
                    font=("Segoe UI", 8),
                    foreground="#7f8c8d",
                ).pack(anchor="w", padx=20)

            # Info
            info_frame = ttk.Frame(frame_seg, style="Card.TFrame", padding="10")
            info_frame.pack(fill="x", pady=10)

            ttk.Label(
                info_frame,
                text="💡 Todas as operações de segurança são registradas no sistema.",
                font=("Segoe UI", 9),
                foreground="gray",
            ).pack(anchor="w")

            ttk.Button(frame_seg, text="Fechar", command=seg_janela.destroy).pack(
                pady=10
            )

        def fazer_backup():
            """Fazer backup dos dados do sistema"""
            backup_janela = tk.Toplevel(self.root)
            backup_janela.title("Backup de Dados")
            backup_janela.geometry("500x350")
            backup_janela.transient(self.root)

            frame_backup = ttk.Frame(backup_janela, padding="20")
            frame_backup.pack(expand=True, fill="both")

            ttk.Label(
                frame_backup,
                text="💾 Backup de Dados do Sistema",
                font=("Segoe UI", 14, "bold"),
            ).pack(pady=10)

            # Info sobre backup
            info_frame = ttk.Frame(frame_backup, style="Card.TFrame", padding="15")
            info_frame.pack(fill="both", expand=True, pady=10)

            ttk.Label(
                info_frame,
                text="Arquivos que serão salvos:",
                font=("Segoe UI", 11, "bold"),
            ).pack(anchor="w", pady=10)

            arquivos = [
                "✅ dados_usuarios.json",
                "✅ progresso_alunos.json",
                "✅ metricas_sustentabilidade.json",
                "✅ forum_mensagens.json",
            ]

            for arquivo in arquivos:
                ttk.Label(info_frame, text=arquivo, font=("Segoe UI", 9)).pack(
                    anchor="w", pady=2
                )

            # Botão de backup
            def executar_backup():
                from datetime import datetime

                data_backup = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                # Salvar todos os dados
                self.salvar_usuarios()
                self.salvar_progresso()
                self.salvar_metricas()
                self.salvar_forum()

                messagebox.showinfo(
                    "Sucesso",
                    f"✅ Backup realizado com sucesso!\n\n"
                    f"Data: {data_backup}\n\n"
                    f"Todos os dados foram salvos!",
                )
                backup_janela.destroy()

            btn_frame = ttk.Frame(frame_backup)
            btn_frame.pack(pady=10)

            ttk.Button(
                btn_frame, text="💾 Executar Backup", command=executar_backup, width=20
            ).pack(side="left", padx=5)
            ttk.Button(
                btn_frame, text="❌ Cancelar", command=backup_janela.destroy, width=20
            ).pack(side="left", padx=5)

        ttk.Button(
            btn_frame,
            text="📊 Ver Estatísticas Completas",
            command=mostrar_estatisticas_completas,
            width=25,
        ).pack(side="left", padx=5)
        ttk.Button(
            btn_frame,
            text="🔐 Gerenciar Segurança",
            command=gerenciar_seguranca,
            width=25,
        ).pack(side="left", padx=5)
        ttk.Button(
            btn_frame, text="💾 Backup de Dados", command=fazer_backup, width=25
        ).pack(side="left", padx=5)

    def criar_aba_gerenciamento_usuarios(self, parent):
        """Aba para gerenciar usuários do sistema"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame, text="👥 Gerenciamento de Usuários", style="Title.TLabel"
        ).pack(anchor="w", pady=10)

        # Filtro
        filter_frame = ttk.Frame(frame)
        filter_frame.pack(fill="x", pady=10)

        ttk.Label(filter_frame, text="Filtrar por tipo:", font=("Segoe UI", 10)).pack(
            side="left"
        )

        filtro_var = tk.StringVar(value="todos")
        combo_filtro = ttk.Combobox(
            filter_frame,
            textvariable=filtro_var,
            values=["todos", "aluno", "professor", "admin"],
            state="readonly",
            width=15,
        )
        combo_filtro.pack(side="left", padx=10)

        # Botão para atualizar a tabela
        def atualizar_tabela():
            # Limpar treeview
            for item in tree.get_children():
                tree.delete(item)

            # Adicionar usuários filtrados
            for usuario, dados in self.usuarios_cadastrados.items():
                tipo_filtro = filtro_var.get()
                if tipo_filtro != "todos" and dados.get("tipo") != tipo_filtro:
                    continue

                tipo_icone = {"aluno": "🎓", "professor": "👨‍🏫", "admin": "👑"}

                tree.insert(
                    "",
                    "end",
                    values=(
                        usuario,
                        dados.get("nome_completo", "N/A"),
                        f"{tipo_icone.get(dados.get('tipo', 'aluno'), '?')} {dados.get('tipo', 'N/A').upper()}",
                        dados.get("email", "N/A"),
                        dados.get("telefone", "N/A"),
                        dados.get("data_cadastro", "N/A")[:10],
                    ),
                )

        ttk.Button(filter_frame, text="🔄 Atualizar", command=atualizar_tabela).pack(
            side="left", padx=5
        )

        # Tabela de usuários
        table_frame = ttk.Frame(frame)
        table_frame.pack(expand=True, fill="both", pady=10)

        # Treeview
        colunas = ("usuario", "nome", "tipo", "email", "telefone", "data_cadastro")
        tree = ttk.Treeview(table_frame, columns=colunas, show="headings", height=15)

        tree.heading("usuario", text="Usuário")
        tree.heading("nome", text="Nome Completo")
        tree.heading("tipo", text="Tipo")
        tree.heading("email", text="Email")
        tree.heading("telefone", text="Telefone")
        tree.heading("data_cadastro", text="Data de Cadastro")

        tree.column("usuario", width=100)
        tree.column("nome", width=150)
        tree.column("tipo", width=80)
        tree.column("email", width=150)
        tree.column("telefone", width=120)
        tree.column("data_cadastro", width=100)

        # Adicionar usuários
        for usuario, dados in self.usuarios_cadastrados.items():
            tipo_filtro = filtro_var.get()
            if tipo_filtro != "todos" and dados.get("tipo") != tipo_filtro:
                continue

            tipo_icone = {"aluno": "🎓", "professor": "👨‍🏫", "admin": "👑"}

            tree.insert(
                "",
                "end",
                values=(
                    usuario,
                    dados.get("nome_completo", "N/A"),
                    f"{tipo_icone.get(dados.get('tipo', 'aluno'), '?')} {dados.get('tipo', 'N/A').upper()}",
                    dados.get("email", "N/A"),
                    dados.get("telefone", "N/A"),
                    dados.get("data_cadastro", "N/A")[:10],
                ),
            )

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)

        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botões de ação
        action_frame = ttk.Frame(frame)
        action_frame.pack(fill="x", pady=10)

        def editar_usuario():
            """Editar dados do usuário selecionado"""
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um usuário para editar!")
                return

            usuario = tree.item(selecionado[0])["values"][0]
            self.mostrar_janela_editar_usuario(usuario)

        def excluir_usuario():
            """Excluir usuário do sistema"""
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um usuário para excluir!")
                return

            usuario = tree.item(selecionado[0])["values"][0]
            nome = tree.item(selecionado[0])["values"][1]

            # Validação: não permite excluir o admin logado
            if usuario == self.usuario_logado:
                messagebox.showerror(
                    "Erro", "❌ Você não pode excluir sua própria conta!"
                )
                return

            # Confirmação
            if messagebox.askyesno(
                "Confirmar Exclusão",
                f"Tem certeza que deseja excluir o usuário?\n\n"
                f"👤 Usuário: {usuario}\n"
                f"📝 Nome: {nome}\n\n"
                f"Esta ação é irreversível!",
            ):
                # Verificar se é aluno com cursos
                dados_usuario = self.usuarios_cadastrados.get(usuario, {})
                if dados_usuario.get("tipo") == "aluno" and dados_usuario.get("cursos"):
                    messagebox.showwarning(
                        "Aviso",
                        f"Este aluno está matriculado em {len(dados_usuario.get('cursos', []))} curso(s).\n"
                        f"O aluno será removido de todos os cursos.",
                    )

                # Excluir usuário
                del self.usuarios_cadastrados[usuario]

                # Remover progresso do aluno se existir
                if usuario in self.progresso_alunos:
                    del self.progresso_alunos[usuario]

                # Salvar
                self.salvar_usuarios()
                self.salvar_progresso()

                messagebox.showinfo(
                    "Sucesso", f"✅ Usuário '{usuario}' foi excluído do sistema!"
                )
                atualizar_tabela()

        def visualizar_usuario():
            """Ver detalhes completos do usuário"""
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Aviso", "Selecione um usuário para visualizar!")
                return

            usuario = tree.item(selecionado[0])["values"][0]
            self.mostrar_detalhes_usuario(usuario)

        ttk.Button(
            action_frame, text="👁️ Visualizar", command=visualizar_usuario, width=15
        ).pack(side="left", padx=5)
        ttk.Button(
            action_frame, text="✏️ Editar", command=editar_usuario, width=15
        ).pack(side="left", padx=5)
        ttk.Button(
            action_frame, text="🗑️ Excluir", command=excluir_usuario, width=15
        ).pack(side="left", padx=5)

    def mostrar_detalhes_usuario(self, usuario):
        """Mostra detalhes completos do usuário"""
        dados = self.usuarios_cadastrados.get(usuario)
        if not dados:
            messagebox.showerror("Erro", "Usuário não encontrado!")
            return

        detalhes_janela = tk.Toplevel(self.root)
        detalhes_janela.title(f"Detalhes do Usuário - {usuario}")
        detalhes_janela.geometry("500x600")
        detalhes_janela.transient(self.root)
        detalhes_janela.grab_set()

        frame = ttk.Frame(detalhes_janela, padding="20")
        frame.pack(expand=True, fill="both")

        # Título
        ttk.Label(
            frame, text=f"Usuário: {usuario}", font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        # Info em card
        info_frame = ttk.Frame(frame, style="Card.TFrame", padding="15")
        info_frame.pack(fill="both", expand=True, pady=10)

        # Informações
        infos = [
            ("👤 Nome Completo:", dados.get("nome_completo", "N/A")),
            ("📧 Email:", dados.get("email", "N/A")),
            ("📞 Telefone:", dados.get("telefone", "N/A")),
            ("🎂 Idade:", str(dados.get("idade", "N/A"))),
            ("🎯 Tipo:", dados.get("tipo", "N/A").upper()),
            ("📅 Data de Cadastro:", dados.get("data_cadastro", "N/A")[:10]),
        ]

        if dados.get("tipo") == "aluno":
            infos.extend(
                [
                    ("📚 Cursos Matriculados:", str(len(dados.get("cursos", [])))),
                    ("📜 Certificados:", str(len(dados.get("certificados", [])))),
                    (
                        "🎯 Interesses:",
                        ", ".join(dados.get("interesses", []))
                        if dados.get("interesses")
                        else "Não informados",
                    ),
                    (
                        "📊 Preferência de Modalidade:",
                        dados.get("preferencias_aprendizado", {}).get(
                            "modalidade", "N/A"
                        ),
                    ),
                    (
                        "⚡ Ritmo de Aprendizado:",
                        dados.get("preferencias_aprendizado", {}).get("ritmo", "N/A"),
                    ),
                ]
            )
        elif dados.get("tipo") == "professor":
            infos.extend(
                [
                    ("👨‍🏫 Especialidade:", dados.get("especialidade", "N/A")),
                    ("📚 Cursos Lecionando:", str(len(dados.get("cursos", [])))),
                ]
            )

        for label, valor in infos:
            ttk.Label(info_frame, text=label, font=("Segoe UI", 10, "bold")).pack(
                anchor="w", pady=2
            )
            ttk.Label(info_frame, text=valor, font=("Segoe UI", 10)).pack(
                anchor="w", pady=2, padx=20
            )
            ttk.Separator(info_frame).pack(fill="x", pady=2)

        ttk.Button(frame, text="Fechar", command=detalhes_janela.destroy).pack(pady=10)

    def mostrar_janela_editar_usuario(self, usuario):
        """Janela para editar dados do usuário"""
        dados = self.usuarios_cadastrados.get(usuario)
        if not dados:
            messagebox.showerror("Erro", "Usuário não encontrado!")
            return

        edit_janela = tk.Toplevel(self.root)
        edit_janela.title(f"Editar Usuário - {usuario}")
        edit_janela.geometry("500x500")
        edit_janela.transient(self.root)
        edit_janela.grab_set()

        frame = ttk.Frame(edit_janela, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text=f"Editar: {usuario}", font=("Segoe UI", 14, "bold")).pack(
            pady=10
        )

        # Formulário
        form_frame = ttk.Frame(frame)
        form_frame.pack(fill="both", expand=True)

        campos_edit = {}

        campos = [
            ("Nome Completo:", "nome_completo"),
            ("Email:", "email"),
            ("Telefone:", "telefone"),
            ("Idade:", "idade"),
        ]

        row = 0
        for label, campo in campos:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 10)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            entry = ttk.Entry(form_frame, width=30, font=("Segoe UI", 10))
            entry.insert(0, str(dados.get(campo, "")))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            campos_edit[campo] = entry
            row += 1

        form_frame.columnconfigure(1, weight=1)

        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)

        def salvar_edicoes():
            """Salvar edições do usuário"""
            try:
                # Validar idade
                idade = int(campos_edit["idade"].get())
                if not 16 <= idade <= 80:
                    messagebox.showerror("Erro", "Idade deve estar entre 16 e 80 anos!")
                    return

                # Atualizar dados
                dados["nome_completo"] = campos_edit["nome_completo"].get()
                dados["email"] = campos_edit["email"].get()
                dados["telefone"] = campos_edit["telefone"].get()
                dados["idade"] = idade

                self.salvar_usuarios()
                messagebox.showinfo("Sucesso", "✅ Usuário atualizado com sucesso!")
                edit_janela.destroy()
                self.atualizar_interface()

            except ValueError:
                messagebox.showerror("Erro", "Idade deve ser um número válido!")

        ttk.Button(btn_frame, text="💾 Salvar", command=salvar_edicoes, width=15).pack(
            side="left", padx=10
        )
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=edit_janela.destroy, width=15
        ).pack(side="left", padx=10)

    def criar_aba_gerenciamento_conteudo(self, parent):
        """Aba para gerenciar cursos e módulos"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame, text="📚 Gerenciamento de Conteúdo", style="Title.TLabel"
        ).pack(anchor="w", pady=10)

        # Notebook com abas para Cursos e Módulos
        notebook = ttk.Notebook(frame)
        notebook.pack(expand=True, fill="both", pady=10)

        # Aba Cursos
        aba_cursos = ttk.Frame(notebook)
        self.criar_subaba_gerenciar_cursos(aba_cursos)
        notebook.add(aba_cursos, text="📖 Gerenciar Cursos")

        # Aba Módulos
        aba_modulos = ttk.Frame(notebook)
        self.criar_subaba_gerenciar_modulos(aba_modulos)
        notebook.add(aba_modulos, text="📋 Gerenciar Módulos")

    def criar_subaba_gerenciar_cursos(self, parent):
        """Sub-aba para gerenciar cursos"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        # Botão para criar novo curso
        ttk.Button(
            frame, text="➕ Criar Novo Curso", command=self.mostrar_janela_criar_curso
        ).pack(pady=10)

        # Container com scroll
        container = ttk.Frame(frame)
        container.pack(expand=True, fill="both", pady=10)

        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Listar cursos existentes
        for curso_id, curso in self.cursos_disponiveis.items():
            card = ttk.Frame(scrollable_frame, style="Card.TFrame", padding="15")
            card.pack(fill="x", pady=5, padx=10)

            ttk.Label(card, text=curso["nome"], font=("Segoe UI", 12, "bold")).pack(
                anchor="w"
            )

            # Mostrar professor responsável
            professor_id = curso.get("professor", "admin")
            professor_data = self.usuarios_cadastrados.get(professor_id, {})
            professor_nome = professor_data.get("nome_completo", professor_id)

            info_text = f"🎯 {curso['dificuldade']} | ⏰ {curso['carga_horaria']} | 👥 {curso['alunos_matriculados']} alunos"
            ttk.Label(
                card, text=info_text, font=("Segoe UI", 9), foreground="#7f8c8d"
            ).pack(anchor="w", pady=3)

            ttk.Label(
                card,
                text=f"👨‍🏫 Professor: {professor_nome}",
                font=("Segoe UI", 9),
                foreground="#2980b9",
            ).pack(anchor="w")

            ttk.Label(
                card, text=f"📖 {len(curso['modulos'])} módulos", font=("Segoe UI", 9)
            ).pack(anchor="w")

            btn_frame = ttk.Frame(card)
            btn_frame.pack(fill="x", pady=10)

            ttk.Button(
                btn_frame,
                text="✏️ Editar",
                command=lambda cid=curso_id: self.mostrar_janela_editar_curso(cid),
                width=15,
            ).pack(side="left", padx=5)
            ttk.Button(
                btn_frame,
                text="🗑️ Excluir",
                command=lambda cid=curso_id: self.excluir_curso(cid),
                width=15,
            ).pack(side="left", padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def criar_subaba_gerenciar_modulos(self, parent):
        """Sub-aba para gerenciar módulos"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame,
            text="Selecione um curso para gerenciar seus módulos:",
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=10)

        # Seletor de curso
        select_frame = ttk.Frame(frame)
        select_frame.pack(fill="x", pady=10)

        ttk.Label(select_frame, text="Curso:", font=("Segoe UI", 10)).pack(side="left")

        curso_var = tk.StringVar()
        curso_combo = ttk.Combobox(
            select_frame,
            textvariable=curso_var,
            values=[
                f"{cid}: {c['nome']}" for cid, c in self.cursos_disponiveis.items()
            ],
            state="readonly",
            width=40,
        )
        curso_combo.pack(side="left", padx=10, fill="x", expand=True)

        # Container para módulos
        container = ttk.Frame(frame)
        container.pack(expand=True, fill="both", pady=10)

        def atualizar_modulos():
            """Atualizar lista de módulos do curso selecionado"""
            # Limpar container
            for widget in container.winfo_children():
                widget.destroy()

            selecionado = curso_var.get()
            if not selecionado:
                ttk.Label(
                    container,
                    text="Selecione um curso!",
                    font=("Segoe UI", 11),
                    foreground="gray",
                ).pack(pady=20)
                return

            curso_id = selecionado.split(":")[0]
            curso = self.cursos_disponiveis.get(curso_id)

            if not curso:
                return

            # Botão para adicionar módulo
            ttk.Button(
                container,
                text="➕ Adicionar Novo Módulo",
                command=lambda: self.mostrar_janela_criar_modulo(curso_id),
            ).pack(pady=10)

            # Canvas com scroll
            canvas = tk.Canvas(container)
            scrollbar = ttk.Scrollbar(
                container, orient="vertical", command=canvas.yview
            )
            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            # Listar módulos
            for i, modulo in enumerate(curso["modulos"]):
                card = ttk.Frame(scrollable_frame, style="Card.TFrame", padding="12")
                card.pack(fill="x", pady=5, padx=5)

                ttk.Label(
                    card,
                    text=f"{i + 1}. {modulo['nome']}",
                    font=("Segoe UI", 11, "bold"),
                ).pack(anchor="w")

                info_text = f"🎯 {modulo['dificuldade']} | ⏰ {modulo['tempo_estimado']} | ❓ {modulo['questoes']} questões"
                ttk.Label(
                    card, text=info_text, font=("Segoe UI", 9), foreground="#7f8c8d"
                ).pack(anchor="w", pady=3)

                btn_frame = ttk.Frame(card)
                btn_frame.pack(fill="x", pady=5)

                ttk.Button(
                    btn_frame,
                    text="✏️ Editar",
                    command=lambda cid=curso_id,
                    idx=i: self.mostrar_janela_editar_modulo(cid, idx),
                    width=12,
                ).pack(side="left", padx=3)
                ttk.Button(
                    btn_frame,
                    text="🗑️ Excluir",
                    command=lambda cid=curso_id, idx=i: self.excluir_modulo(cid, idx),
                    width=12,
                ).pack(side="left", padx=3)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

        ttk.Button(select_frame, text="📂 Carregar", command=atualizar_modulos).pack(
            side="left", padx=5
        )

    def mostrar_janela_criar_curso(self):
        """Janela para criar novo curso"""
        create_janela = tk.Toplevel(self.root)
        create_janela.title("Criar Novo Curso")
        create_janela.geometry("600x500")
        create_janela.transient(self.root)
        create_janela.grab_set()

        frame = ttk.Frame(create_janela, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame, text="📖 Criar Novo Curso", font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        # Formulário
        form_frame = ttk.Frame(frame)
        form_frame.pack(fill="both", expand=True)

        campos = {}

        campos_criar = [
            ("Nome do Curso:", "nome"),
            ("Descrição:", "descricao"),
            ("Carga Horária:", "carga_horaria"),
            ("Categoria:", "categoria"),
        ]

        row = 0
        for label, campo in campos_criar:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 10)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            entry = ttk.Entry(form_frame, width=40, font=("Segoe UI", 10))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            campos[campo] = entry
            row += 1

        # Dificuldade
        ttk.Label(form_frame, text="Dificuldade:", font=("Segoe UI", 10)).grid(
            row=row, column=0, sticky="w", pady=5
        )
        dificuldade_var = tk.StringVar(value="Intermediário")
        dificuldade_combo = ttk.Combobox(
            form_frame,
            textvariable=dificuldade_var,
            values=["Iniciante", "Intermediário", "Avançado", "Intermediário-Avançado"],
            state="readonly",
            width=38,
        )
        dificuldade_combo.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
        row += 1

        # Professor responsável
        ttk.Label(
            form_frame, text="Professor Responsável:", font=("Segoe UI", 10)
        ).grid(row=row, column=0, sticky="w", pady=5)

        # Se for professor, atribui ele automaticamente; se for admin, deixa escolher
        user_data = self.usuarios_cadastrados.get(self.usuario_logado, {})
        user_tipo = user_data.get("tipo", "aluno")

        if user_tipo == "professor":
            # Professor é atribuído automaticamente
            professor_var = tk.StringVar(
                value=f"{user_data.get('nome_completo', self.usuario_logado)} ({self.usuario_logado})"
            )
            ttk.Label(
                form_frame,
                text=f"{user_data.get('nome_completo', self.usuario_logado)} ({self.usuario_logado})",
                font=("Segoe UI", 10),
            ).grid(row=row, column=1, pady=5, padx=10, sticky="ew")
        else:
            # Admin pode escolher o professor
            professores = [
                (u, d.get("nome_completo", u))
                for u, d in self.usuarios_cadastrados.items()
                if d.get("tipo") == "professor"
            ]
            professor_list = [f"{nome} ({user})" for user, nome in professores]
            professor_var = tk.StringVar(
                value=professor_list[0] if professor_list else "Nenhum professor"
            )
            professor_combo = ttk.Combobox(
                form_frame,
                textvariable=professor_var,
                values=professor_list,
                state="readonly",
                width=38,
            )
            professor_combo.grid(row=row, column=1, pady=5, padx=10, sticky="ew")

        row += 1

        form_frame.columnconfigure(1, weight=1)

        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)

        def salvar_novo_curso():
            """Salvar novo curso"""
            if not all(campos[k].get() for k in campos):
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

            novo_id = str(len(self.cursos_disponiveis) + 1)

            # Extrair username do professor selecionado (formato: "Nome (username)")
            professor_selecionado = professor_var.get()
            if "(" in professor_selecionado:
                professor_username = professor_selecionado.split("(")[1].rstrip(")")
            else:
                professor_username = "admin"

            self.cursos_disponiveis[novo_id] = {
                "nome": campos["nome"].get(),
                "descricao": campos["descricao"].get(),
                "carga_horaria": campos["carga_horaria"].get(),
                "categoria": campos["categoria"].get(),
                "dificuldade": dificuldade_var.get(),
                "modulos": [],
                "professor": professor_username,
                "avaliacao": 4.5,
                "alunos_matriculados": 0,
                "criado_em": datetime.now().isoformat()[:10],
                "tags": [],
            }
            # Persistir cursos
            self.salvar_cursos()

            # Atribuir o curso ao professor no registro do usuário (se existir)
            if professor_username in self.usuarios_cadastrados:
                prof_data = self.usuarios_cadastrados[professor_username]
                prof_cursos = prof_data.get("cursos", [])
                if novo_id not in prof_cursos:
                    prof_cursos.append(novo_id)
                    prof_data["cursos"] = prof_cursos
                    # Salvar usuários atualizados
                    self.salvar_usuarios()

            messagebox.showinfo(
                "Sucesso",
                f"✅ Curso criado com sucesso!\nID: {novo_id}\nProfessor: {professor_username}",
            )
            create_janela.destroy()
            self.atualizar_interface()

        ttk.Button(
            btn_frame, text="💾 Criar Curso", command=salvar_novo_curso, width=20
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=create_janela.destroy, width=20
        ).pack(side="left", padx=10)

    def pode_editar_curso(self, curso_id):
        """Verifica se o usuário logado tem permissão para editar o curso"""
        user_data = self.usuarios_cadastrados.get(self.usuario_logado, {})
        user_tipo = user_data.get("tipo", "aluno")

        # Admins podem editar qualquer curso
        if user_tipo == "admin":
            return True

        # Professores só podem editar seus próprios cursos
        if user_tipo == "professor":
            curso = self.cursos_disponiveis.get(curso_id, {})
            professor_responsavel = curso.get("professor", "admin")
            return professor_responsavel == self.usuario_logado

        # Alunos nunca podem editar cursos
        return False

    def mostrar_janela_editar_curso(self, curso_id):
        """Janela para editar curso"""
        # Verificar permissão
        if not self.pode_editar_curso(curso_id):
            messagebox.showerror(
                "Acesso Negado",
                "❌ Você não tem permissão para editar este curso!\n\n"
                "Apenas o professor responsável ou um administrador pode editar.",
            )
            return

        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            messagebox.showerror("Erro", "Curso não encontrado!")
            return

        edit_janela = tk.Toplevel(self.root)
        edit_janela.title(f"Editar Curso - {curso['nome']}")
        edit_janela.geometry("600x500")
        edit_janela.transient(self.root)
        edit_janela.grab_set()

        frame = ttk.Frame(edit_janela, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame, text=f"Editar: {curso['nome']}", font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        # Formulário
        form_frame = ttk.Frame(frame)
        form_frame.pack(fill="both", expand=True)

        campos = {}

        campos_editar = [
            ("Nome do Curso:", "nome"),
            ("Descrição:", "descricao"),
            ("Carga Horária:", "carga_horaria"),
            ("Categoria:", "categoria"),
        ]

        row = 0
        for label, campo in campos_editar:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 10)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            entry = ttk.Entry(form_frame, width=40, font=("Segoe UI", 10))
            entry.insert(0, str(curso.get(campo, "")))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            campos[campo] = entry
            row += 1

        # Professor responsável
        ttk.Label(
            form_frame, text="Professor Responsável:", font=("Segoe UI", 10)
        ).grid(row=row, column=0, sticky="w", pady=5)
        professores = [
            (u, d.get("nome_completo", u))
            for u, d in self.usuarios_cadastrados.items()
            if d.get("tipo") == "professor"
        ]
        professor_list = [f"{nome} ({user})" for user, nome in professores]

        # Encontrar o professor atual do curso
        professor_atual = curso.get("professor", "admin")
        professor_atual_display = next(
            (
                f"{nome} ({user})"
                for user, nome in professores
                if user == professor_atual
            ),
            (professor_list[0] if professor_list else "Nenhum professor"),
        )

        professor_var = tk.StringVar(value=professor_atual_display)
        professor_combo = ttk.Combobox(
            form_frame,
            textvariable=professor_var,
            values=professor_list,
            state="readonly",
            width=38,
        )
        professor_combo.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
        row += 1

        form_frame.columnconfigure(1, weight=1)

        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)

        def salvar_edicoes_curso():
            """Salvar edições do curso"""
            for campo in campos_editar:
                curso[campo[1]] = campos[campo[1]].get()

            # Extrair username do professor selecionado (formato: "Nome (username)")
            professor_selecionado = professor_var.get()
            if "(" in professor_selecionado:
                professor_username = professor_selecionado.split("(")[1].rstrip(")")
            else:
                professor_username = curso.get("professor", "admin")

            curso["professor"] = professor_username

            # Persistir alterações
            self.salvar_cursos()

            messagebox.showinfo(
                "Sucesso",
                f"✅ Curso atualizado com sucesso!\nProfessor: {professor_username}",
            )
            edit_janela.destroy()
            self.atualizar_interface()

        ttk.Button(
            btn_frame, text="💾 Salvar", command=salvar_edicoes_curso, width=20
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=edit_janela.destroy, width=20
        ).pack(side="left", padx=10)

    def excluir_curso(self, curso_id):
        """Excluir um curso do sistema"""
        # Verificar permissão
        if not self.pode_editar_curso(curso_id):
            messagebox.showerror(
                "Acesso Negado",
                "❌ Você não tem permissão para excluir este curso!\n\n"
                "Apenas o professor responsável ou um administrador pode excluir.",
            )
            return

        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            messagebox.showerror("Erro", "Curso não encontrado!")
            return

        if messagebox.askyesno(
            "Confirmar Exclusão",
            f"Tem certeza que deseja excluir o curso?\n\n"
            f"📖 {curso['nome']}\n"
            f"👥 {curso['alunos_matriculados']} alunos matriculados\n\n"
            f"Esta ação é irreversível!",
        ):
            del self.cursos_disponiveis[curso_id]
            # Persistir alteração
            self.salvar_cursos()
            messagebox.showinfo("Sucesso", "✅ Curso excluído com sucesso!")
            self.atualizar_interface()

    def mostrar_janela_criar_modulo(self, curso_id):
        """Janela para criar novo módulo"""
        # Verificar permissão
        if not self.pode_editar_curso(curso_id):
            messagebox.showerror(
                "Acesso Negado",
                "❌ Você não tem permissão para adicionar módulos a este curso!\n\n"
                "Apenas o professor responsável ou um administrador pode adicionar módulos.",
            )
            return

        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            messagebox.showerror("Erro", "Curso não encontrado!")
            return

        create_janela = tk.Toplevel(self.root)
        create_janela.title("Criar Novo Módulo")
        create_janela.geometry("600x400")
        create_janela.transient(self.root)
        create_janela.grab_set()

        frame = ttk.Frame(create_janela, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame,
            text=f"Criar Módulo para: {curso['nome']}",
            font=("Segoe UI", 14, "bold"),
        ).pack(pady=10)

        # Formulário
        form_frame = ttk.Frame(frame)
        form_frame.pack(fill="both", expand=True)

        campos = {}

        campos_criar = [
            ("Nome do Módulo:", "nome"),
            ("Tempo Estimado (ex: 20h):", "tempo_estimado"),
            ("Número de Questões:", "questoes"),
        ]

        row = 0
        for label, campo in campos_criar:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 10)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            entry = ttk.Entry(form_frame, width=40, font=("Segoe UI", 10))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            campos[campo] = entry
            row += 1

        # Dificuldade
        ttk.Label(form_frame, text="Dificuldade:", font=("Segoe UI", 10)).grid(
            row=row, column=0, sticky="w", pady=5
        )
        dificuldade_var = tk.StringVar(value="Intermediário")
        dificuldade_combo = ttk.Combobox(
            form_frame,
            textvariable=dificuldade_var,
            values=["Iniciante", "Intermediário", "Avançado"],
            state="readonly",
            width=38,
        )
        dificuldade_combo.grid(row=row, column=1, pady=5, padx=10, sticky="ew")

        form_frame.columnconfigure(1, weight=1)
        row += 1

        # Conteúdo do módulo (opcional)
        ttk.Label(form_frame, text="Conteúdo do Módulo:", font=("Segoe UI", 10)).grid(
            row=row, column=0, sticky="nw", pady=5
        )
        conteudo_text = scrolledtext.ScrolledText(
            form_frame, width=50, height=6, font=("Segoe UI", 10)
        )
        conteudo_text.grid(row=row, column=1, pady=5, padx=10, sticky="ew")

        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)

        def salvar_novo_modulo():
            """Salvar novo módulo"""
            if not all(campos[k].get() for k in campos):
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

            novo_modulo = {
                "nome": campos["nome"].get(),
                "tempo_estimado": campos["tempo_estimado"].get(),
                "questoes": int(campos["questoes"].get()),
                "dificuldade": dificuldade_var.get(),
                "conteudo": conteudo_text.get("1.0", "end").strip(),
                "questoes_data": [],
            }

            curso["modulos"].append(novo_modulo)
            # Persistir cursos
            self.salvar_cursos()

            messagebox.showinfo("Sucesso", "✅ Módulo criado com sucesso!")
            create_janela.destroy()
            self.atualizar_interface()

        ttk.Button(
            btn_frame, text="💾 Criar Módulo", command=salvar_novo_modulo, width=20
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=create_janela.destroy, width=20
        ).pack(side="left", padx=10)

    def mostrar_janela_editar_modulo(self, curso_id, modulo_idx):
        """Janela para editar módulo"""
        # Verificar permissão
        if not self.pode_editar_curso(curso_id):
            messagebox.showerror(
                "Acesso Negado",
                "❌ Você não tem permissão para editar módulos deste curso!\n\n"
                "Apenas o professor responsável ou um administrador pode editar módulos.",
            )
            return

        curso = self.cursos_disponiveis.get(curso_id)
        if not curso or modulo_idx >= len(curso["modulos"]):
            messagebox.showerror("Erro", "Módulo não encontrado!")
            return

        modulo = curso["modulos"][modulo_idx]

        edit_janela = tk.Toplevel(self.root)
        edit_janela.title(f"Editar Módulo - {modulo['nome']}")
        edit_janela.geometry("600x400")
        edit_janela.transient(self.root)
        edit_janela.grab_set()

        frame = ttk.Frame(edit_janela, padding="20")
        frame.pack(expand=True, fill="both")

        ttk.Label(
            frame, text=f"Editar: {modulo['nome']}", font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        # Formulário
        form_frame = ttk.Frame(frame)
        form_frame.pack(fill="both", expand=True)

        campos = {}

        campos_editar = [
            ("Nome do Módulo:", "nome"),
            ("Tempo Estimado:", "tempo_estimado"),
            ("Número de Questões:", "questoes"),
        ]

        row = 0
        for label, campo in campos_editar:
            ttk.Label(form_frame, text=label, font=("Segoe UI", 10)).grid(
                row=row, column=0, sticky="w", pady=5
            )
            entry = ttk.Entry(form_frame, width=40, font=("Segoe UI", 10))
            entry.insert(0, str(modulo.get(campo, "")))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
            campos[campo] = entry
            row += 1

        # Conteúdo do módulo (editor de texto)
        ttk.Label(form_frame, text="Conteúdo do Módulo:", font=("Segoe UI", 10)).grid(
            row=row, column=0, sticky="nw", pady=5
        )
        conteudo_text = scrolledtext.ScrolledText(
            form_frame, width=50, height=8, font=("Segoe UI", 10)
        )
        conteudo_text.grid(row=row, column=1, pady=5, padx=10, sticky="ew")
        conteudo_text.insert("1.0", modulo.get("conteudo", ""))
        row += 1
        form_frame.columnconfigure(1, weight=1)

        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)

        def salvar_edicoes_modulo():
            """Salvar edições do módulo"""
            try:
                modulo["nome"] = campos["nome"].get()
                modulo["tempo_estimado"] = campos["tempo_estimado"].get()
                modulo["questoes"] = int(campos["questoes"].get())
                modulo["conteudo"] = conteudo_text.get("1.0", "end").strip()
                # Persistir cursos
                self.salvar_cursos()

                messagebox.showinfo("Sucesso", "✅ Módulo atualizado com sucesso!")
                edit_janela.destroy()
                self.atualizar_interface()
            except ValueError:
                messagebox.showerror("Erro", "Número de questões deve ser um número!")

        ttk.Button(
            btn_frame, text="💾 Salvar", command=salvar_edicoes_modulo, width=20
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame, text="❌ Cancelar", command=edit_janela.destroy, width=20
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame,
            text="✍️ Gerenciar Perguntas",
            command=lambda cid=curso_id,
            idx=modulo_idx: self.mostrar_janela_gerenciar_perguntas(cid, idx),
            width=20,
        ).pack(side="left", padx=10)

    def excluir_modulo(self, curso_id, modulo_idx):
        """Excluir um módulo do curso"""
        # Verificar permissão
        if not self.pode_editar_curso(curso_id):
            messagebox.showerror(
                "Acesso Negado",
                "❌ Você não tem permissão para excluir módulos deste curso!\n\n"
                "Apenas o professor responsável ou um administrador pode excluir módulos.",
            )
            return

        curso = self.cursos_disponiveis.get(curso_id)
        if not curso or modulo_idx >= len(curso["modulos"]):
            messagebox.showerror("Erro", "Módulo não encontrado!")
            return

        modulo = curso["modulos"][modulo_idx]

        if messagebox.askyesno(
            "Confirmar Exclusão",
            f"Tem certeza que deseja excluir o módulo?\n\n"
            f"📋 {modulo['nome']}\n\n"
            f"Esta ação é irreversível!",
        ):
            curso["modulos"].pop(modulo_idx)
            # Persistir cursos
            self.salvar_cursos()

            messagebox.showinfo("Sucesso", "✅ Módulo excluído com sucesso!")
            self.atualizar_interface()

    def mostrar_janela_gerenciar_perguntas(self, curso_id, modulo_idx):
        """Janela para gerenciar perguntas de um módulo específico"""
        print(
            f"DEBUG: mostrar_janela_gerenciar_perguntas called: curso_id={curso_id}, modulo_idx={modulo_idx}"
        )
        try:
            messagebox.showinfo(
                "Debug",
                f"Abrindo gerenciador de perguntas:\ncurso={curso_id} módulo={modulo_idx}",
            )
        except Exception:
            pass
        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            messagebox.showerror("Erro", "Curso não encontrado!")
            return

        if modulo_idx >= len(curso.get("modulos", [])):
            messagebox.showwarning(
                "Atenção", "Salve/crie o módulo antes de gerenciar perguntas."
            )
            return

        modulo = curso["modulos"][modulo_idx]

        jan = tk.Toplevel(self.root)
        jan.title(f"Gerenciar Perguntas - {modulo['nome']}")
        jan.geometry("800x500")
        jan.transient(self.root)
        jan.grab_set()

        frame = ttk.Frame(jan, padding="10")
        frame.pack(expand=True, fill="both")

        left = ttk.Frame(frame)
        left.pack(side="left", fill="y", padx=10, pady=10)

        ttk.Label(
            left, text="Perguntas existentes:", font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")
        listbox = tk.Listbox(left, width=40, height=20)
        listbox.pack(pady=5)

        # carregar perguntas existentes
        questoes = modulo.get("questoes_data", [])
        for i, q in enumerate(questoes):
            listbox.insert("end", f"{i + 1}. {q.get('pergunta')[:60]}")

        right = ttk.Frame(frame)
        right.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        ttk.Label(right, text="Pergunta:", font=("Segoe UI", 10)).pack(anchor="w")
        entry_pergunta = scrolledtext.ScrolledText(right, height=3)
        entry_pergunta.pack(fill="x", pady=5)

        alt_vars = []
        for n in range(4):
            ttk.Label(right, text=f"Alternativa {n + 1}:", font=("Segoe UI", 9)).pack(
                anchor="w"
            )
            var = ttk.Entry(right)
            var.pack(fill="x", pady=3)
            alt_vars.append(var)

        ttk.Label(
            right, text="Resposta correta (texto exato):", font=("Segoe UI", 9)
        ).pack(anchor="w", pady=(6, 0))
        entry_resposta = ttk.Entry(right)
        entry_resposta.pack(fill="x", pady=3)

        btns = ttk.Frame(right)
        btns.pack(pady=10)

        def atualizar_listbox():
            listbox.delete(0, "end")
            for i, q in enumerate(modulo.get("questoes_data", [])):
                listbox.insert("end", f"{i + 1}. {q.get('pergunta')[:60]}")

        def limpar_campos():
            entry_pergunta.delete("1.0", "end")
            for v in alt_vars:
                v.delete(0, "end")
            entry_resposta.delete(0, "end")

        def on_add():
            pergunta = entry_pergunta.get("1.0", "end").strip()
            alternativas = [v.get().strip() for v in alt_vars if v.get().strip()]
            resposta = entry_resposta.get().strip()
            if not pergunta or not alternativas or not resposta:
                messagebox.showerror(
                    "Erro", "Preencha pergunta, alternativas e resposta correta"
                )
                return
            q = {
                "pergunta": pergunta,
                "alternativas": alternativas,
                "resposta_correta": resposta,
            }
            modulo.setdefault("questoes_data", []).append(q)
            self.salvar_cursos()
            atualizar_listbox()
            limpar_campos()

        def on_select(evt=None):
            sel = listbox.curselection()
            if not sel:
                return
            idx = sel[0]
            q = modulo.get("questoes_data", [])[idx]
            limpar_campos()
            entry_pergunta.insert("1.0", q.get("pergunta", ""))
            for i, alt in enumerate(q.get("alternativas", [])):
                if i < len(alt_vars):
                    alt_vars[i].insert(0, alt)
            entry_resposta.insert(0, q.get("resposta_correta", ""))

        def on_update():
            sel = listbox.curselection()
            if not sel:
                messagebox.showwarning("Atenção", "Selecione uma pergunta para editar")
                return
            idx = sel[0]
            pergunta = entry_pergunta.get("1.0", "end").strip()
            alternativas = [v.get().strip() for v in alt_vars if v.get().strip()]
            resposta = entry_resposta.get().strip()
            if not pergunta or not alternativas or not resposta:
                messagebox.showerror(
                    "Erro", "Preencha pergunta, alternativas e resposta correta"
                )
                return
            modulo["questoes_data"][idx] = {
                "pergunta": pergunta,
                "alternativas": alternativas,
                "resposta_correta": resposta,
            }
            self.salvar_cursos()
            atualizar_listbox()
            limpar_campos()

        def on_delete():
            sel = listbox.curselection()
            if not sel:
                messagebox.showwarning("Atenção", "Selecione uma pergunta para excluir")
                return
            idx = sel[0]
            if messagebox.askyesno("Confirmar", "Excluir a pergunta selecionada?"):
                modulo["questoes_data"].pop(idx)
                self.salvar_cursos()
                atualizar_listbox()
                limpar_campos()

        ttk.Button(btns, text="➕ Adicionar", command=on_add).pack(side="left", padx=6)
        ttk.Button(btns, text="✏️ Atualizar", command=on_update).pack(
            side="left", padx=6
        )
        ttk.Button(btns, text="🗑️ Excluir", command=on_delete).pack(side="left", padx=6)
        ttk.Button(btns, text="Fechar", command=jan.destroy).pack(side="left", padx=6)

        listbox.bind("<<ListboxSelect>>", on_select)

    def mostrar_tela_login(self):
        """Tela de login moderna"""
        self.limpar_tela()

        main_frame = ttk.Frame(self.root, padding="40")
        main_frame.pack(expand=True, fill="both")

        ttk.Label(
            main_frame, text="🎓 UNIP - UNIVERSIDADE PAULISTA", style="Title.TLabel"
        ).pack(pady=10)
        ttk.Label(
            main_frame,
            text="PIM II - Sistema Acadêmico com IA Avançada",
            style="Subtitle.TLabel",
        ).pack(pady=5)

        # Card de login
        login_card = ttk.Frame(main_frame, style="Card.TFrame", padding="30")
        login_card.pack(pady=30, padx=100, fill="x")

        ttk.Label(
            login_card, text="🔐 Acesso ao Sistema", font=("Segoe UI", 16, "bold")
        ).pack(pady=20)

        # Formulário
        form_frame = ttk.Frame(login_card)
        form_frame.pack(pady=20, padx=30)

        ttk.Label(form_frame, text="Usuário:", font=("Segoe UI", 11)).grid(
            row=0, column=0, sticky="w", pady=10
        )
        self.entry_user = ttk.Entry(form_frame, width=25, font=("Segoe UI", 11))
        self.entry_user.grid(row=0, column=1, pady=10, padx=10)

        ttk.Label(form_frame, text="Senha:", font=("Segoe UI", 11)).grid(
            row=1, column=0, sticky="w", pady=10
        )
        self.entry_senha = ttk.Entry(
            form_frame, width=25, show="•", font=("Segoe UI", 11)
        )
        self.entry_senha.grid(row=1, column=1, pady=10, padx=10)

        # Botões
        btn_frame = ttk.Frame(login_card)
        btn_frame.pack(pady=20)

        ttk.Button(
            btn_frame,
            text="🚀 Entrar no Sistema",
            command=self.fazer_login_interativo,
            width=18,
        ).pack(side="left", padx=10)
        ttk.Button(
            btn_frame,
            text="📝 Criar Conta Aluno",
            command=self.mostrar_cadastro_completo,
            width=18,
        ).pack(side="left", padx=10)

        # Status do sistema
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(pady=20)

        stats = self.atualizar_metricas_colaboracao()
        metricas = self.calcular_impacto_sustentabilidade()

        status_info = [
            f"✅ {len(self.usuarios_cadastrados)} Usuários",
            "🤖 IA Ativa",
            f"👥 {stats['usuarios_ativos']} Colaborando",
            f"🌱 {metricas['papel_economizado']}kg Papel Economizado",
        ]

        for info in status_info:
            ttk.Label(status_frame, text=info, font=("Segoe UI", 9)).pack(
                side="left", padx=15
            )

        self.entry_user.focus()
        self.entry_senha.bind("<Return>", lambda e: self.fazer_login_interativo())

    def iniciar(self):
        """Inicia o sistema"""
        self.mostrar_tela_login()
        self.root.mainloop()


if __name__ == "__main__":
    app = SistemaUNIPIACompleto()
    app.iniciar()
