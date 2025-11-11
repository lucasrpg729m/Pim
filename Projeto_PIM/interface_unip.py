# interface_unip_final_completo.py - SISTEMA ACADÊMICO UNIP COM IA AVANÇADA
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import threading
from datetime import datetime, timedelta
import re
import random

class SistemaUNIPIACompleto:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UNIP PIM II - Sistema Acadêmico")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
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
        style.theme_use('clam')
        
        # Cores UNIP com tema moderno
        style.configure('TFrame', background='#f8f9fa')
        style.configure('TLabel', background='#f8f9fa', font=('Segoe UI', 10))
        style.configure('TButton', font=('Segoe UI', 10), padding=8)
        style.configure('Title.TLabel', font=('Segoe UI', 18, 'bold'), foreground='#2c3e50')
        style.configure('Subtitle.TLabel', font=('Segoe UI', 14, 'bold'), foreground='#34495e')
        style.configure('Card.TFrame', relief='raised', borderwidth=2)
        
        # ✅ NOVO ESTILO PARA RADIOBUTTON (ADICIONE ESTA LINHA)
        style.configure('Custom.TRadiobutton', font=('Segoe UI', 10))
        
    def carregar_contexto_ia(self):
        """Carrega contexto para IA"""
        return {
            "padroes_aprendizado": {},
            "recomendacoes_personalizadas": {},
            "alertas_desempenho": {},
            "previsoes_conclusao": {},
            "analise_sentimento": {}
        }
    
    def carregar_usuarios(self):
        """Carrega usuários do arquivo JSON"""
        try:
            with open('dados_usuarios.json', 'r', encoding='utf-8') as f:
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
                    "preferencias_aprendizado": {"modalidade": "visual", "ritmo": "moderado"}
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
                    "bio": "Professor com 15 anos de experiência em Python e Machine Learning"
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
                    "bio": "Especialista em tecnologias web modernas"
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
                    "preferencias_aprendizado": {"modalidade": "pratica", "ritmo": "acelerado"},
                    "interesses": ["Python", "Web Development", "IA"]
                }
            }
            self.salvar_usuarios(usuarios_base)
            return usuarios_base

    def salvar_usuarios(self, dados=None):
        """Salva usuários no arquivo JSON"""
        try:
            with open('dados_usuarios.json', 'w', encoding='utf-8') as f:
                json.dump(dados or self.usuarios_cadastrados, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar usuários: {e}")
            return False
    
    def carregar_cursos(self):
        """Carrega cursos disponíveis com conteúdo enriquecido"""
        cursos = {
            "1": {
                "nome": "Python para Ciência de Dados e IA",
                "carga_horaria": "80 horas",
                "modulos": [
                    {"nome": "Fundamentos do Python", "questoes": 3, "dificuldade": "Iniciante", "tempo_estimado": "10h"},
                    {"nome": "Estruturas de Dados Avançadas", "questoes": 3, "dificuldade": "Intermediário", "tempo_estimado": "15h"},
                    {"nome": "Análise de Dados com Pandas e NumPy", "questoes": 3, "dificuldade": "Intermediário", "tempo_estimado": "20h"}
                ],
                "categoria": "Tecnologia & IA",
                "dificuldade": "Intermediário-Avançado",
                "professor": "prof.python",
                "descricao": "Curso completo de Python para análise de dados, visualização e machine learning. Prepare-se para o mercado de ciência de dados!",
                "tags": ["Python", "Pandas", "Machine Learning", "Data Science"],
                "avaliacao": 4.8,
                "alunos_matriculados": 45,
                "criado_em": "2024-01-15"
            },
            "2": {
                "nome": "Desenvolvimento Web Full Stack Moderno", 
                "carga_horaria": "120 horas",
                "modulos": [
                    {"nome": "HTML5, CSS3 e JavaScript ES6+", "questoes": 3, "dificuldade": "Iniciante", "tempo_estimado": "25h"},
                    {"nome": "React.js e Hooks Avançados", "questoes": 3, "dificuldade": "Intermediário", "tempo_estimado": "30h"},
                    {"nome": "Node.js, Express e APIs REST", "questoes": 3, "dificuldade": "Intermediário", "tempo_estimado": "25h"}
                ],
                "categoria": "Desenvolvimento Web",
                "dificuldade": "Intermediário",
                "professor": "prof.web",
                "descricao": "Torne-se um desenvolvedor full stack aprendendo as tecnologias mais demandadas do mercado atual.",
                "tags": ["React", "Node.js", "JavaScript", "MongoDB"],
                "avaliacao": 4.7,
                "alunos_matriculados": 38,
                "criado_em": "2024-02-10"
            },
            "3": {
                "nome": "Inteligência Artificial Aplicada",
                "carga_horaria": "100 horas",
                "modulos": [
                    {"nome": "Fundamentos Matemáticos de IA", "questoes": 3, "dificuldade": "Intermediário", "tempo_estimado": "20h"},
                    {"nome": "Redes Neurais e Deep Learning", "questoes": 3, "dificuldade": "Avançado", "tempo_estimado": "30h"},
                    {"nome": "Processamento de Linguagem Natural (NLP)", "questoes": 3, "dificuldade": "Avançado", "tempo_estimado": "25h"}
                ],
                "categoria": "Inteligência Artificial",
                "dificuldade": "Avançado", 
                "professor": "admin",
                "descricao": "Aprofunde-se nos conceitos e aplicações práticas de Inteligência Artificial e Machine Learning.",
                "tags": ["Deep Learning", "NLP", "Computer Vision", "TensorFlow"],
                "avaliacao": 4.9,
                "alunos_matriculados": 28,
                "criado_em": "2024-01-20"
            }
        }
        return cursos
    
    def carregar_progresso(self):
        """Carrega progresso dos alunos"""
        try:
            with open('progresso_alunos.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    
    def carregar_forum(self):
        """Carrega mensagens do fórum colaborativo"""
        try:
            with open('forum_mensagens.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {
                "geral": [],
                "duvidas": [],
                "projetos": []
            }
    
    def carregar_metricas(self):
        """Carrega métricas de sustentabilidade"""
        try:
            with open('metricas_sustentabilidade.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {
                "papel_economizado": 0,  # em kg
                "co2_economizado": 0,    # em kg
                "agua_economizada": 0,   # em litros
                "total_atividades_digitais": 0
            }
    
    def salvar_progresso(self):
        """Salva progresso dos alunos"""
        try:
            with open('progresso_alunos.json', 'w', encoding='utf-8') as f:
                json.dump(self.progresso_alunos, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar progresso: {e}")
            return False

    def salvar_forum(self):
        """Salva mensagens do fórum"""
        try:
            with open('forum_mensagens.json', 'w', encoding='utf-8') as f:
                json.dump(self.forum_mensagens, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar fórum: {e}")
            return False

    def salvar_metricas(self):
        """Salva métricas de sustentabilidade"""
        try:
            with open('metricas_sustentabilidade.json', 'w', encoding='utf-8') as f:
                json.dump(self.metricas_sustentabilidade, f, indent=4, ensure_ascii=False)
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
        if curso_id in self.usuarios_cadastrados[self.usuario_logado]['cursos']:
            messagebox.showinfo("Info", "Você já está matriculado neste curso!")
            return False
        
        # Matricular
        self.usuarios_cadastrados[self.usuario_logado]['cursos'].append(curso_id)
        
        # Inicializar progresso
        if self.usuario_logado not in self.progresso_alunos:
            self.progresso_alunos[self.usuario_logado] = {}
        
        self.progresso_alunos[self.usuario_logado][curso_id] = {
            'modulos_concluidos': [],
            'questoes_respondidas': 0,
            'total_questoes': sum(modulo['questoes'] for modulo in self.cursos_disponiveis[curso_id]['modulos']),
            'progresso': 0,
            'nota_final': 0,
            'data_matricula': datetime.now().isoformat()
        }
        
        # Salvar alterações
        self.salvar_usuarios()
        self.salvar_progresso()
        
        # Registrar atividade para sustentabilidade
        self.registrar_atividade_digital()
        
        messagebox.showinfo("Sucesso!", 
            f"✅ Matriculado no curso: {self.cursos_disponiveis[curso_id]['nome']}\n\n"
            f"Acesse 'Meus Cursos' para começar seus estudos!")
        
        # ATUALIZAR INTERFACE IMEDIATAMENTE
        self.atualizar_interface()
        return True
    
    def iniciar_questionario(self, curso_id, modulo_nome):
        """Inicia questionário para o módulo"""
        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            return
        
        # Encontrar módulo
        modulo = next((m for m in curso['modulos'] if m['nome'] == modulo_nome), None)
        if not modulo:
            return
        
        # Verificar se já foi concluído
        if modulo_nome in self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {}).get('modulos_concluidos', []):
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
        frame.pack(expand=True, fill='both')
        
        ttk.Label(frame, text=f"📝 Questionário: {modulo['nome']}", 
                 font=('Segoe UI', 16, 'bold')).pack(pady=10)
        
        ttk.Label(frame, text=f"Responda as {modulo['questoes']} questões abaixo:",
                 font=('Segoe UI', 12)).pack(pady=5)
        
        # Container com scroll
        container = ttk.Frame(frame)
        container.pack(expand=True, fill='both', pady=10)
        
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Gerar questões dinâmicas baseadas no módulo
        respostas_usuario = {}
        questoes = self.gerar_questoes_modulo(modulo['nome'], modulo['questoes'])
        
        for i, questao in enumerate(questoes):
            quest_frame = ttk.Frame(scrollable_frame, relief='groove', borderwidth=1, padding="15")
            quest_frame.pack(fill='x', pady=8, padx=10)
            
            ttk.Label(quest_frame, text=f"Questão {i+1}: {questao['pergunta']}", 
                     font=('Segoe UI', 11, 'bold'), wraplength=600).pack(anchor='w')
            
            var = tk.StringVar()
            respostas_usuario[i] = var
            
            for j, alternativa in enumerate(questao['alternativas']):
                rb = ttk.Radiobutton(quest_frame, text=alternativa, variable=var, value=alternativa)
                rb.pack(anchor='w', pady=2)
                rb.configure(style='Custom.TRadiobutton')
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        def finalizar_questionario():
            # Calcular pontuação
            acertos = 0
            for i, questao in enumerate(questoes):
                if respostas_usuario[i].get() == questao['resposta_correta']:
                    acertos += 1
            
            percentual_acerto = (acertos / len(questoes)) * 100
            
            if percentual_acerto >= 70:  # 70% para aprovação
                # Atualizar progresso
                if self.usuario_logado not in self.progresso_alunos:
                    self.progresso_alunos[self.usuario_logado] = {}
                if curso_id not in self.progresso_alunos[self.usuario_logado]:
                    self.progresso_alunos[self.usuario_logado][curso_id] = {
                        'modulos_concluidos': [],
                        'questoes_respondidas': 0,
                        'total_questoes': 0,
                        'progresso': 0,
                        'nota_final': 0
                    }
                
                # Adicionar módulo concluído
                if modulo['nome'] not in self.progresso_alunos[self.usuario_logado][curso_id]['modulos_concluidos']:
                    self.progresso_alunos[self.usuario_logado][curso_id]['modulos_concluidos'].append(modulo['nome'])
                
                # Calcular novo progresso
                total_modulos = len(self.cursos_disponiveis[curso_id]['modulos'])
                modulos_concluidos = len(self.progresso_alunos[self.usuario_logado][curso_id]['modulos_concluidos'])
                novo_progresso = (modulos_concluidos / total_modulos) * 100
                
                self.progresso_alunos[self.usuario_logado][curso_id]['progresso'] = novo_progresso
                self.progresso_alunos[self.usuario_logado][curso_id]['questoes_respondidas'] += len(questoes)
                self.progresso_alunos[self.usuario_logado][curso_id]['nota_final'] = percentual_acerto
                
                self.salvar_progresso()
                
                # Verificar se curso foi 100% concluído
                if novo_progresso >= 100:
                    self.gerar_certificado_automatico(curso_id)
                # Verificar se pode gerar certificado
                elif novo_progresso >= 80:
                    self.mostrar_opcao_certificado(curso_id)
                
                messagebox.showinfo("Parabéns!", 
                    f"✅ Módulo concluído com sucesso!\n\n"
                    f"📊 Acertos: {acertos}/{len(questoes)} ({percentual_acerto:.1f}%)\n"
                    f"🎯 Progresso total: {novo_progresso:.1f}%\n"
                    f"🏆 Nota final: {percentual_acerto:.1f}")
            else:
                messagebox.showwarning("Tente Novamente", 
                    f"❌ Você precisa de pelo menos 70% de acertos.\n\n"
                    f"📊 Seus acertos: {acertos}/{len(questoes)} ({percentual_acerto:.1f}%)\n"
                    f"💡 Dica: Revise o conteúdo do módulo e tente novamente!")
            
            quest_janela.destroy()
            # ATUALIZAR INTERFACE APÓS QUESTIONÁRIO
            self.atualizar_interface()
        
        ttk.Button(frame, text="✅ Finalizar Questionário", 
                  command=finalizar_questionario, style='TButton').pack(pady=20)
    
    def gerar_questoes_modulo(self, modulo_nome, quantidade):
        """Gera questões dinâmicas baseadas no módulo"""
        # Banco de questões por módulo
        banco_questoes = {
            "Fundamentos do Python": [
                {
                    "pergunta": "Qual é a função usada para exibir texto no Python?",
                    "alternativas": ["print()", "echo()", "display()", "show()"],
                    "resposta_correta": "print()"
                },
                {
                    "pergunta": "Como se declara uma variável em Python?",
                    "alternativas": ["var x = 5", "x = 5", "let x = 5", "variable x = 5"],
                    "resposta_correta": "x = 5"
                },
                {
                    "pergunta": "Qual símbolo é usado para comentários em Python?",
                    "alternativas": ["//", "#", "/*", "--"],
                    "resposta_correta": "#"
                }
            ],
            "Estruturas de Dados Avançadas": [
                {
                    "pergunta": "Qual estrutura de dados é mutável em Python?",
                    "alternativas": ["Lista", "Tupla", "String", "Número"],
                    "resposta_correta": "Lista"
                },
                {
                    "pergunta": "Como criar um dicionário vazio?",
                    "alternativas": ["{}", "dict()", "[]", "Ambas A e B"],
                    "resposta_correta": "Ambas A e B"
                },
                {
                    "pergunta": "Qual método adiciona elemento ao final da lista?",
                    "alternativas": ["append()", "add()", "insert()", "push()"],
                    "resposta_correta": "append()"
                }
            ],
            "Análise de Dados com Pandas e NumPy": [
                {
                    "pergunta": "Qual biblioteca é usada para análise de dados?",
                    "alternativas": ["Pandas", "TensorFlow", "Django", "Flask"],
                    "resposta_correta": "Pandas"
                },
                {
                    "pergunta": "Como importar o pandas normalmente?",
                    "alternativas": ["import pandas", "import pandas as pd", "from pandas import *", "Todas as anteriores"],
                    "resposta_correta": "import pandas as pd"
                },
                {
                    "pergunta": "Qual função do NumPy cria array de zeros?",
                    "alternativas": ["zeros()", "empty()", "ones()", "array()"],
                    "resposta_correta": "zeros()"
                }
            ],
            "HTML5, CSS3 e JavaScript ES6+": [
                {
                    "pergunta": "Qual tag HTML5 é usada para conteúdo semântico principal?",
                    "alternativas": ["<main>", "<content>", "<body>", "<section>"],
                    "resposta_correta": "<main>"
                },
                {
                    "pergunta": "Como declarar uma variável com escopo de bloco em JavaScript?",
                    "alternativas": ["var", "let", "const", "variable"],
                    "resposta_correta": "let"
                },
                {
                    "pergunta": "Qual propriedade CSS muda a cor do texto?",
                    "alternativas": ["color", "text-color", "font-color", "text-style"],
                    "resposta_correta": "color"
                }
            ],
            "React.js e Hooks Avançados": [
                {
                    "pergunta": "Qual hook é usado para estado em componentes funcionais?",
                    "alternativas": ["useState", "useEffect", "useContext", "useReducer"],
                    "resposta_correta": "useState"
                },
                {
                    "pergunta": "React é uma biblioteca para:",
                    "alternativas": ["Interface de usuário", "Backend", "Banco de dados", "Mobile"],
                    "resposta_correta": "Interface de usuário"
                },
                {
                    "pergunta": "Como criar componente em React?",
                    "alternativas": ["function Component() {}", "class Component {}", "Ambas", "Nenhuma"],
                    "resposta_correta": "Ambas"
                }
            ],
            "Node.js, Express e APIs REST": [
                {
                    "pergunta": "Node.js é um ambiente de execução:",
                    "alternativas": ["JavaScript no servidor", "Python no servidor", "Java no cliente", "C++ no navegador"],
                    "resposta_correta": "JavaScript no servidor"
                },
                {
                    "pergunta": "Qual método HTTP para criar recurso?",
                    "alternativas": ["POST", "GET", "PUT", "DELETE"],
                    "resposta_correta": "POST"
                },
                {
                    "pergunta": "Express.js é um:",
                    "alternativas": ["Framework web", "Banco de dados", "Linguagem", "Editor de código"],
                    "resposta_correta": "Framework web"
                }
            ],
            "Fundamentos Matemáticos de IA": [
                {
                    "pergunta": "Qual área matemática é fundamental para IA?",
                    "alternativas": ["Álgebra Linear", "Geometria", "Trigonometria", "Aritmética"],
                    "resposta_correta": "Álgebra Linear"
                },
                {
                    "pergunta": "O que é um vetor em machine learning?",
                    "alternativas": ["Array unidimensional", "Matriz 2x2", "Número complexo", "Função"],
                    "resposta_correta": "Array unidimensional"
                },
                {
                    "pergunta": "Para que serve cálculo em IA?",
                    "alternativas": ["Otimização", "Visualização", "Interface", "Armazenamento"],
                    "resposta_correta": "Otimização"
                }
            ],
            "Redes Neurais e Deep Learning": [
                {
                    "pergunta": "O que é uma rede neural?",
                    "alternativas": ["Modelo inspirado no cérebro", "Banco de dados", "Protocolo de rede", "Linguagem"],
                    "resposta_correta": "Modelo inspirado no cérebro"
                },
                {
                    "pergunta": "Qual função de ativação é comum?",
                    "alternativas": ["ReLU", "Sigmoid", "Tanh", "Todas"],
                    "resposta_correta": "Todas"
                },
                {
                    "pergunta": "Deep Learning usa:",
                    "alternativas": ["Múltiplas camadas", "Uma camada", "Sem camadas", "Camadas físicas"],
                    "resposta_correta": "Múltiplas camadas"
                }
            ],
            "Processamento de Linguagem Natural (NLP)": [
                {
                    "pergunta": "NLP significa:",
                    "alternativas": ["Natural Language Processing", "Neural Language Program", "Network Layer Protocol", "New Learning Process"],
                    "resposta_correta": "Natural Language Processing"
                },
                {
                    "pergunta": "Qual técnica converte texto em números?",
                    "alternativas": ["Tokenização", "Vectorization", "Parsing", "Compilation"],
                    "resposta_correta": "Vectorization"
                },
                {
                    "pergunta": "BERT é um modelo de:",
                    "alternativas": ["Linguagem", "Visão", "Áudio", "Dados"],
                    "resposta_correta": "Linguagem"
                }
            ]
        }
        
        # Retornar questões do módulo ou gerar padrão
        if modulo_nome in banco_questoes:
            return banco_questoes[modulo_nome][:quantidade]
        else:
            # Questões genéricas
            return [
                {
                    "pergunta": f"Qual é o conceito principal do módulo {modulo_nome}?",
                    "alternativas": ["Conceito A", "Conceito B", "Conceito C", "Conceito D"],
                    "resposta_correta": "Conceito A"
                }
                for _ in range(quantidade)
            ]
    
    def mostrar_opcao_certificado(self, curso_id):
        """Mostra opção para gerar certificado se atingiu 80%"""
        progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})
        
        if progresso.get('progresso', 0) >= 80 and progresso.get('nota_final', 0) >= 70:
            if messagebox.askyesno("Certificado Disponível!", 
                                 f"🎓 Parabéns! Você atingiu {progresso['progresso']:.1f}% do curso!\n\n"
                                 f"Deseja gerar seu certificado agora?"):
                self.gerar_certificado(curso_id)
    
    def gerar_certificado_automatico(self, curso_id):
        """Gera certificado automaticamente quando curso é 100% concluído"""
        progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})
        curso = self.cursos_disponiveis.get(curso_id)
        user_data = self.usuarios_cadastrados[self.usuario_logado]
        
        if not curso:
            return
        
        # Verificar se pode gerar certificado
        if progresso.get('progresso', 0) < 100:
            return
        
        if progresso.get('nota_final', 0) < 70:
            return
        
        # Adicionar aos certificados do usuário
        if 'certificados' not in user_data:
            user_data['certificados'] = []
        
        certificado_info = {
            'curso': curso['nome'],
            'curso_id': curso_id,
            'data': datetime.now().strftime('%d/%m/%Y'),
            'carga_horaria': curso['carga_horaria'],
            'aluno_nome': user_data['nome_completo'],
            'aluno_usuario': self.usuario_logado,
            'nota_final': progresso.get('nota_final', 0),
            'progresso': progresso.get('progresso', 0),
            'tipo': 'Conclusão Total'
        }
        
        user_data['certificados'].append(certificado_info)
        self.salvar_usuarios()
        
        # Registrar atividade sustentável
        self.registrar_atividade_digital()
        
        messagebox.showinfo("🎓 Certificado Gerado Automaticamente!", 
            f"📄 PARABÉNS! Você concluiu 100% do curso!\n\n"
            f"👤 Para: {user_data['nome_completo']}\n"
            f"📚 Curso: {curso['nome']}\n"
            f"📅 Data: {certificado_info['data']}\n"
            f"⏰ Carga Horária: {curso['carga_horaria']}\n"
            f"🏆 Nota Final: {progresso.get('nota_final', 0):.1f}%\n\n"
            f"🎓 UNIP - Universidade Paulista\n"
            f"✅ Certificado gerado automaticamente!")
    
    def gerar_certificado(self, curso_id):
        """Gera certificado para o curso"""
        progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})
        curso = self.cursos_disponiveis.get(curso_id)
        user_data = self.usuarios_cadastrados[self.usuario_logado]
        
        if not curso:
            messagebox.showerror("Erro", "Curso não encontrado!")
            return
        
        # Verificar se pode gerar certificado
        if progresso.get('progresso', 0) < 80:
            messagebox.showwarning("Atenção", 
                "❌ Você precisa concluir pelo menos 80% do curso para gerar o certificado!")
            return
        
        if progresso.get('nota_final', 0) < 70:
            messagebox.showwarning("Atenção", 
                "❌ Você precisa ter nota mínima de 70% para gerar o certificado!")
            return
        
        # Adicionar aos certificados do usuário
        if 'certificados' not in user_data:
            user_data['certificados'] = []
        
        certificado_info = {
            'curso': curso['nome'],
            'curso_id': curso_id,
            'data': datetime.now().strftime('%d/%m/%Y'),
            'carga_horaria': curso['carga_horaria'],
            'aluno_nome': user_data['nome_completo'],
            'aluno_usuario': self.usuario_logado,
            'nota_final': progresso.get('nota_final', 0),
            'progresso': progresso.get('progresso', 0),
            'tipo': 'Parcial (80%+)'
        }
        
        user_data['certificados'].append(certificado_info)
        self.salvar_usuarios()
        
        # Registrar atividade sustentável
        self.registrar_atividade_digital()
        
        messagebox.showinfo("✅ Certificado Gerado!", 
            f"📄 Certificado criado com sucesso!\n\n"
            f"👤 Para: {user_data['nome_completo']}\n"
            f"📚 Curso: {curso['nome']}\n"
            f"📅 Data: {certificado_info['data']}\n"
            f"⏰ Carga Horária: {curso['carga_horaria']}\n"
            f"🏆 Nota Final: {progresso.get('nota_final', 0):.1f}%\n"
            f"📊 Progresso: {progresso.get('progresso', 0):.1f}%\n\n"
            f"🎓 UNIP - Universidade Paulista")

    # ========== SISTEMA DE ATUALIZAÇÃO DE INTERFACE ==========
    
    def atualizar_interface(self):
        """Atualiza toda a interface após mudanças nos dados"""
        if self.usuario_logado:
            self.mostrar_dashboard_ia()

    # ========== SISTEMA DE CADASTRO COM TELEFONE FORMATADO ==========
    
    def formatar_telefone(self, event=None):
        """Formata o telefone automaticamente enquanto digita"""
        entry = self.entries_cadastro['entry_telefone']
        texto = entry.get().replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        
        if len(texto) >= 11:
            # Formato: (11) 99999-9999
            texto_formatado = f"({texto[:2]}) {texto[2:7]}-{texto[7:11]}"
            entry.delete(0, tk.END)
            entry.insert(0, texto_formatado)
        elif len(texto) >= 7:
            # Formato: (11) 9999-9999
            texto_formatado = f"({texto[:2]}) {texto[2:6]}-{texto[6:10]}"
            entry.delete(0, tk.END)
            entry.insert(0, texto_formatado)
        elif len(texto) >= 2:
            # Formato: (11
            texto_formatado = f"({texto[:2]})"
            entry.delete(0, tk.END)
            entry.insert(0, texto_formatado)

    def validar_telefone(self, telefone):
        """Valida telefone no formato brasileiro"""
        # Remover formatação para validar
        telefone_limpo = telefone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        
        if len(telefone_limpo) not in [10, 11]:
            return "Telefone deve ter 10 ou 11 dígitos"
        
        if not telefone_limpo.isdigit():
            return "Telefone deve conter apenas números"
        
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
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="📝 Cadastro de Novo Aluno", 
                 font=('Segoe UI', 14, 'bold')).pack(pady=10)
        
        # Frame do formulário
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill='both', expand=True)
        
        campos = [
            ("👤 Nome Completo:", "entry_nome", False),
            ("🔐 Nome de Usuário:", "entry_user", False),
            ("📞 Telefone (apenas números):", "entry_telefone", False),
            ("🎂 Idade:", "entry_idade", False),
            ("🎯 Interesses (separados por vírgula):", "entry_interesses", False),
            ("🔒 Senha:", "entry_senha", True),
            ("🔒 Confirmar Senha:", "entry_confirmar_senha", True)
        ]
        
        self.entries_cadastro = {}
        row = 0
        
        for label, nome, is_senha in campos:
            ttk.Label(form_frame, text=label, font=('Segoe UI', 9)).grid(row=row, column=0, sticky='w', pady=5)
            if is_senha:
                entry = ttk.Entry(form_frame, width=30, show="•", font=('Segoe UI', 10))
            else:
                entry = ttk.Entry(form_frame, width=30, font=('Segoe UI', 10))
            entry.grid(row=row, column=1, pady=5, padx=10, sticky='ew')
            self.entries_cadastro[nome] = entry
            row += 1
        
        # Configurar formatação automática do telefone
        self.entries_cadastro['entry_telefone'].bind('<KeyRelease>', self.formatar_telefone)
        
        # Preferências de aprendizado
        ttk.Label(form_frame, text="🎯 Preferências de Aprendizado:", 
                 font=('Segoe UI', 9, 'bold')).grid(row=row, column=0, sticky='w', pady=10)
        row += 1
        
        # Modalidade
        ttk.Label(form_frame, text="Modalidade:", font=('Segoe UI', 9)).grid(row=row, column=0, sticky='w', pady=5)
        self.modalidade_var = tk.StringVar(value="pratica")
        modalidade_frame = ttk.Frame(form_frame)
        modalidade_frame.grid(row=row, column=1, sticky='w', pady=5)
        ttk.Radiobutton(modalidade_frame, text="Prática", variable=self.modalidade_var, value="pratica").pack(side='left')
        ttk.Radiobutton(modalidade_frame, text="Visual", variable=self.modalidade_var, value="visual").pack(side='left')
        ttk.Radiobutton(modalidade_frame, text="Auditivo", variable=self.modalidade_var, value="auditivo").pack(side='left')
        row += 1
        
        # Ritmo
        ttk.Label(form_frame, text="Ritmo:", font=('Segoe UI', 9)).grid(row=row, column=0, sticky='w', pady=5)
        self.ritmo_var = tk.StringVar(value="moderado")
        ritmo_frame = ttk.Frame(form_frame)
        ritmo_frame.grid(row=row, column=1, sticky='w', pady=5)
        ttk.Radiobutton(ritmo_frame, text="Acelerado", variable=self.ritmo_var, value="acelerado").pack(side='left')
        ttk.Radiobutton(ritmo_frame, text="Moderado", variable=self.ritmo_var, value="moderado").pack(side='left')
        ttk.Radiobutton(ritmo_frame, text="Calmo", variable=self.ritmo_var, value="calmo").pack(side='left')
        row += 1
        
        form_frame.columnconfigure(1, weight=1)
        
        # Frame de botões
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="✅ Cadastrar", command=self.executar_cadastro, 
                  width=15).pack(side='left', padx=10)
        ttk.Button(btn_frame, text="🔄 Limpar", command=self.limpar_formulario_cadastro, 
                  width=15).pack(side='left', padx=10)
        ttk.Button(btn_frame, text="❌ Cancelar", command=cadastro_janela.destroy, 
                  width=15).pack(side='left', padx=10)
        
        # Dicas de validação
        dicas_frame = ttk.Frame(main_frame)
        dicas_frame.pack(fill='x', pady=10)
        
        dicas_text = """💡 Dicas de Cadastro:
• Usuário: 4-20 caracteres (letras, números, _)
• Senha: Mínimo 8 caracteres, 1 maiúscula, 1 número, 1 símbolo
• Telefone: Digite apenas números (11 dígitos com DDD)
• Email será gerado automaticamente: usuario@aluno.unip.br"""
        
        ttk.Label(dicas_frame, text=dicas_text, font=('Segoe UI', 8), 
                 foreground='gray', justify='left').pack(anchor='w')

    # ========== MÉTODOS RESTANTES (mantidos da versão anterior) ==========
    
    def limpar_formulario_cadastro(self):
        """Limpa todos os campos do formulário"""
        for entry in self.entries_cadastro.values():
            entry.delete(0, 'end')
    
    def validar_nome_usuario(self, nome):
        if not re.match(r'^[a-zA-Z0-9_]{4,20}$', nome):
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
            campo = nome.replace('entry_', '')
            dados[campo] = entry.get().strip()
        
        # Validar campos obrigatórios
        campos_obrigatorios = ['nome', 'user', 'telefone', 'idade', 'senha', 'confirmar_senha']
        for campo in campos_obrigatorios:
            if not dados[campo]:
                messagebox.showerror("Erro", f"Campo '{campo}' é obrigatório!")
                return
        
        # Validações específicas
        erros = []
        
        # Verificar se usuário já existe
        if dados['user'] in self.usuarios_cadastrados:
            erros.append("Usuário já existe!")
        
        # Validar nome de usuário
        if erro := self.validar_nome_usuario(dados['user']):
            erros.append(erro)
        
        # Validar telefone
        if erro := self.validar_telefone(dados['telefone']):
            erros.append(erro)
        
        # Validar idade
        if erro := self.validar_idade(dados['idade']):
            erros.append(erro)
        
        # Validar senha
        if erro := self.validar_senha(dados['senha']):
            erros.append(erro)
        
        # Verificar se senhas coincidem
        if dados['senha'] != dados['confirmar_senha']:
            erros.append("Senhas não coincidem!")
        
        # Se há erros, mostrar todos
        if erros:
            messagebox.showerror("Erros de Validação", "\n".join(f"• {erro}" for erro in erros))
            return
        
        # Processar interesses
        interesses = [interesse.strip() for interesse in dados.get('interesses', '').split(',') if interesse.strip()]
        
        # Gerar email automático
        email = self.gerar_email_unip(dados['user'])
        
        # Criar usuário
        self.usuarios_cadastrados[dados['user']] = {
            "senha": dados['senha'],
            "email": email,
            "idade": int(dados['idade']),
            "is_admin": False,
            "tipo": "aluno",
            "data_cadastro": datetime.now().isoformat(),
            "cursos": [],
            "nome_completo": dados['nome'],
            "telefone": dados['telefone'],
            "certificados": [],
            "modulos_concluidos": {},
            "ultimo_acesso": None,
            "preferencias_aprendizado": {
                "modalidade": self.modalidade_var.get(),
                "ritmo": self.ritmo_var.get()
            },
            "interesses": interesses
        }
        
        # Salvar no JSON
        if self.salvar_usuarios():
            messagebox.showinfo("Sucesso!", 
                f"✅ Aluno cadastrado com sucesso!\n\n"
                f"👤 Nome: {dados['nome']}\n"
                f"📧 Email: {email}\n"
                f"🔐 Usuário: {dados['user']}\n"
                f"📞 Telefone: {dados['telefone']}\n"
                f"🎯 Interesses: {', '.join(interesses) if interesses else 'Não informados'}\n\n"
                f"Bem-vindo à UNIP!")
            
            # Fechar janela de cadastro
            self.entries_cadastro['entry_user'].master.master.master.destroy()
        else:
            messagebox.showerror("Erro", "Falha ao salvar dados do usuário!")
    
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
        tipo_usuario = user_data.get('tipo', 'aluno')
        
        # Header moderno
        header_frame = ttk.Frame(self.root, style='Card.TFrame', padding="15")
        header_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(header_frame, 
                 text=f"🚀 Bem-vindo, {user_data.get('nome_completo', self.usuario_logado)}!",
                 style='Title.TLabel').pack(side='left')
        
        tipo_text = {
            'admin': '👑 Administrador do Sistema',
            'professor': '👨‍🏫 Professor', 
            'aluno': '🎓 Aluno UNIP'
        }
        
        ttk.Label(header_frame, 
                 text=tipo_text.get(tipo_usuario, '🎓 Aluno'),
                 font=('Segoe UI', 12, 'bold'),
                 foreground='#7f8c8d').pack(side='left', padx=20)
        
        ttk.Button(header_frame, text="🚪 Sair", 
                  command=self.mostrar_tela_login,
                  style='TButton').pack(side='right')
        
        # Abas principais com IA
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        if tipo_usuario == 'aluno':
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
            
        elif tipo_usuario == 'professor':
            # Aba Professor
            aba_professor = ttk.Frame(notebook)
            self.criar_aba_professor(aba_professor)
            notebook.add(aba_professor, text="👨‍🏫 Painel Professor")
        
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
        frame.pack(expand=True, fill='both')
        
        # Análise IA do aluno
        analise_ia = self.analisar_padrao_aprendizado(self.usuario_logado)
        recomendacoes_ia = self.gerar_recomendacoes_ia_personalizadas(self.usuario_logado)
        
        # Grid principal
        main_grid = ttk.Frame(frame)
        main_grid.pack(expand=True, fill='both')
        
        # Coluna 1: Métricas de Progresso
        col1 = ttk.Frame(main_grid)
        col1.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(col1, text="📈 Meu Progresso", 
                 style='Subtitle.TLabel').pack(anchor='w', pady=10)
        
        # Cartões de métricas
        progresso_data = self.progresso_alunos.get(self.usuario_logado, {})
        total_cursos = len(progresso_data)
        cursos_concluidos = sum(1 for dados in progresso_data.values() if dados.get('progresso', 0) >= 100)
        progresso_medio = sum(dados.get('progresso', 0) for dados in progresso_data.values()) / max(total_cursos, 1)
        
        metricas = [
            ("🎓 Cursos Ativos", total_cursos),
            ("✅ Concluídos", cursos_concluidos),
            ("📊 Progresso Médio", f"{progresso_medio:.1f}%"),
            ("🚀 Velocidade", f"{analise_ia['velocidade_aprendizado']:.1f}%")
        ]
        
        for texto, valor in metricas:
            card = ttk.Frame(col1, style='Card.TFrame', padding="15")
            card.pack(fill='x', pady=5)
            ttk.Label(card, text=texto, font=('Segoe UI', 10)).pack(anchor='w')
            ttk.Label(card, text=str(valor), font=('Segoe UI', 16, 'bold'), 
                     foreground='#2c3e50').pack(anchor='w')
        
        # Coluna 2: Recomendações IA
        col2 = ttk.Frame(main_grid)
        col2.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(col2, text="🤖 Recomendações IA", 
                 style='Subtitle.TLabel').pack(anchor='w', pady=10)
        
        # Recomendações em cards
        if recomendacoes_ia['cursos_sugeridos']:
            for curso in recomendacoes_ia['cursos_sugeridos'][:3]:
                card = ttk.Frame(col2, style='Card.TFrame', padding="12")
                card.pack(fill='x', pady=3)
                
                ttk.Label(card, text=curso['curso'], 
                         font=('Segoe UI', 10, 'bold')).pack(anchor='w')
                ttk.Label(card, text=curso['motivo'], 
                         font=('Segoe UI', 8),
                         foreground='#7f8c8d').pack(anchor='w')
                ttk.Label(card, text=f"Dificuldade: {curso['dificuldade']}", 
                         font=('Segoe UI', 8),
                         foreground='#f39c12').pack(anchor='w')
        else:
            ttk.Label(col2, text="🎯 Complete seus cursos atuais para receber recomendações!",
                     font=('Segoe UI', 10), foreground='#7f8c8d').pack(pady=20)
        
        # Coluna 3: Análise de Desempenho
        col3 = ttk.Frame(main_grid)
        col3.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)
        
        ttk.Label(col3, text="📋 Análise de Aprendizado", 
                 style='Subtitle.TLabel').pack(anchor='w', pady=10)
        
        # Insights da IA
        insights = []
        if analise_ia['dificuldades']:
            insights.append(f"💡 Dificuldades: {', '.join(analise_ia['dificuldades'][:2])}")
        if analise_ia['pontos_fortes']:
            insights.append(f"⭐ Pontos Fortes: {', '.join(analise_ia['pontos_fortes'][:2])}")
        if analise_ia['previsao_conclusao']:
            for curso_id, data in list(analise_ia['previsao_conclusao'].items())[:2]:
                curso_nome = self.cursos_disponiveis.get(curso_id, {}).get('nome', 'Curso')
                insights.append(f"📅 {curso_nome}: Conclusão prevista em {data}")
        if analise_ia['sugestoes_modulos']:
            insights.extend(analise_ia['sugestoes_modulos'][:2])
        
        for insight in insights[:4]:  # Limitar a 4 insights
            card = ttk.Frame(col3, style='Card.TFrame', padding="10")
            card.pack(fill='x', pady=2)
            ttk.Label(card, text=insight, font=('Segoe UI', 9), 
                     wraplength=250).pack(anchor='w')
        
        # Configurar grid
        main_grid.columnconfigure(0, weight=1)
        main_grid.columnconfigure(1, weight=1)
        main_grid.columnconfigure(2, weight=1)
        main_grid.rowconfigure(0, weight=1)
    
    def criar_aba_cursos_matricula(self, parent):
        """Aba para visualizar e matricular em cursos"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill='both')
        
        ttk.Label(frame, text="📚 Cursos Disponíveis - UNIP", 
                 style='Title.TLabel').pack(anchor='w', pady=10)
        
        # Container com scroll
        container = ttk.Frame(frame)
        container.pack(expand=True, fill='both')
        
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Cards de cursos
        user_cursos = self.usuarios_cadastrados[self.usuario_logado].get('cursos', [])
        
        for i, (curso_id, curso) in enumerate(self.cursos_disponiveis.items()):
            card = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="20")
            card.pack(fill='x', pady=10, padx=10)
            
            # Header do card
            header_frame = ttk.Frame(card)
            header_frame.pack(fill='x', pady=5)
            
            ttk.Label(header_frame, text=curso['nome'], 
                     font=('Segoe UI', 14, 'bold')).pack(side='left')
            
            # Badge de status
            if curso_id in user_cursos:
                status_badge = ttk.Label(header_frame, text="✅ MATRICULADO", 
                                       font=('Segoe UI', 9, 'bold'), foreground='green')
            else:
                status_badge = ttk.Label(header_frame, text="🎯 DISPONÍVEL", 
                                       font=('Segoe UI', 9, 'bold'), foreground='blue')
            status_badge.pack(side='right')
            
            # Informações do curso
            info_text = f"""
📋 Descrição: {curso['descricao']}
⏰ Carga Horária: {curso['carga_horaria']}
🎯 Dificuldade: {curso['dificuldade']}
📊 Categoria: {curso['categoria']}
👨‍🏫 Professor: {self.usuarios_cadastrados.get(curso['professor'], {}).get('nome_completo', curso['professor'])}
⭐ Avaliação: {curso['avaliacao']}/5.0
👥 Alunos: {curso['alunos_matriculados']} matriculados
            """
            
            ttk.Label(card, text=info_text, font=('Segoe UI', 9), 
                     justify='left').pack(anchor='w', pady=10)
            
            # Módulos
            ttk.Label(card, text="📖 Módulos do Curso:", 
                     font=('Segoe UI', 10, 'bold')).pack(anchor='w', pady=5)
            
            for modulo in curso['modulos']:
                ttk.Label(card, text=f"• {modulo['nome']} ({modulo['dificuldade']}) - {modulo['tempo_estimado']}",
                         font=('Segoe UI', 8)).pack(anchor='w')
            
            # Botões de ação
            btn_frame = ttk.Frame(card)
            btn_frame.pack(fill='x', pady=15)
            
            if curso_id in user_cursos:
                ttk.Button(btn_frame, text="🎓 Acessar Curso", 
                          command=lambda cid=curso_id: self.acessar_curso(cid),
                          width=15).pack(side='left', padx=5)
            else:
                ttk.Button(btn_frame, text="📝 Matricular", 
                          command=lambda cid=curso_id: self.matricular_curso(cid),
                          width=15).pack(side='left', padx=5)
            
            ttk.Button(btn_frame, text="ℹ️ Detalhes", 
                      command=lambda cid=curso_id: self.mostrar_detalhes_curso(cid),
                      width=15).pack(side='left', padx=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def criar_aba_meus_cursos(self, parent):
        """Aba dos cursos matriculados pelo aluno"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill='both')
        
        ttk.Label(frame, text="🎓 Meus Cursos e Progresso", 
                 style='Title.TLabel').pack(anchor='w', pady=10)
        
        # Verificar se tem cursos
        user_cursos = self.usuarios_cadastrados[self.usuario_logado].get('cursos', [])
        
        if not user_cursos:
            ttk.Label(frame, text="❌ Você não está matriculado em nenhum curso ainda.\n\n"
                     "Acesse a aba 'Cursos' para se matricular!",
                     font=('Segoe UI', 12), foreground='red', justify='center').pack(pady=50)
            return
        
        # Container com scroll
        container = ttk.Frame(frame)
        container.pack(expand=True, fill='both')
        
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Cards de cursos matriculados
        for curso_id in user_cursos:
            if curso_id in self.cursos_disponiveis:
                curso = self.cursos_disponiveis[curso_id]
                progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})
                
                card = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="20")
                card.pack(fill='x', pady=10, padx=10)
                
                # Header
                header_frame = ttk.Frame(card)
                header_frame.pack(fill='x', pady=5)
                
                ttk.Label(header_frame, text=curso['nome'], 
                         font=('Segoe UI', 14, 'bold')).pack(side='left')
                
                # Progresso
                progresso_percent = progresso.get('progresso', 0)
                ttk.Label(header_frame, text=f"📊 {progresso_percent:.1f}%", 
                         font=('Segoe UI', 12, 'bold'),
                         foreground='green' if progresso_percent >= 70 else 'orange').pack(side='right')
                
                # Barra de progresso
                progress_frame = ttk.Frame(card)
                progress_frame.pack(fill='x', pady=10)
                
                ttk.Label(progress_frame, text="Progresso:").pack(side='left')
                progress_bar = ttk.Progressbar(progress_frame, orient='horizontal', 
                                             length=300, mode='determinate')
                progress_bar.pack(side='left', padx=10, fill='x', expand=True)
                progress_bar['value'] = progresso_percent
                
                # Estatísticas
                stats_text = f"""
📈 Estatísticas:
• Módulos Concluídos: {len(progresso.get('modulos_concluidos', []))}/{len(curso['modulos'])}
• Questões Respondidas: {progresso.get('questoes_respondidas', 0)}/{progresso.get('total_questoes', 0)}
• Nota Final: {progresso.get('nota_final', 0):.1f}%
• Status: {"✅ Aprovado" if progresso.get('nota_final', 0) >= 70 else "📚 Em Andamento"}
                """
                
                ttk.Label(card, text=stats_text, font=('Segoe UI', 9), 
                         justify='left').pack(anchor='w', pady=10)
                
                # Módulos
                ttk.Label(card, text="📖 Módulos:", 
                         font=('Segoe UI', 10, 'bold')).pack(anchor='w', pady=5)
                
                for modulo in curso['modulos']:
                    status = "✅" if modulo['nome'] in progresso.get('modulos_concluidos', []) else "⏳"
                    ttk.Label(card, text=f"{status} {modulo['nome']} ({modulo['dificuldade']})",
                             font=('Segoe UI', 8)).pack(anchor='w')
                
                # Botões de ação
                btn_frame = ttk.Frame(card)
                btn_frame.pack(fill='x', pady=15)
                
                # Encontrar próximo módulo
                modulos_restantes = [mod for mod in curso['modulos'] 
                                   if mod['nome'] not in progresso.get('modulos_concluidos', [])]
                
                if modulos_restantes:
                    ttk.Button(btn_frame, text="🎯 Continuar Estudando", 
                              command=lambda cid=curso_id, mod=modulos_restantes[0]: 
                              self.iniciar_questionario(cid, mod['nome']),
                              width=18).pack(side='left', padx=5)
                else:
                    ttk.Button(btn_frame, text="🎓 Curso Concluído", 
                              state='disabled',
                              width=18).pack(side='left', padx=5)
                
                # Gerar certificado se elegível
                if progresso_percent >= 80 and progresso.get('nota_final', 0) >= 70:
                    ttk.Button(btn_frame, text="📜 Gerar Certificado", 
                              command=lambda cid=curso_id: self.gerar_certificado(cid),
                              width=18).pack(side='left', padx=5)
                else:
                    ttk.Button(btn_frame, text="📜 Certificado", 
                              state='disabled',
                              width=18).pack(side='left', padx=5)
                
                ttk.Button(btn_frame, text="📊 Ver Detalhes", 
                          command=lambda cid=curso_id: self.mostrar_detalhes_curso(cid),
                          width=15).pack(side='left', padx=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def acessar_curso(self, curso_id):
        """Acessa um curso matriculado"""
        progresso = self.progresso_alunos.get(self.usuario_logado, {}).get(curso_id, {})
        curso = self.cursos_disponiveis.get(curso_id)
        
        if not curso:
            return
        
        # Encontrar próximo módulo
        modulos_restantes = [mod for mod in curso['modulos'] 
                           if mod['nome'] not in progresso.get('modulos_concluidos', [])]
        
        if modulos_restantes:
            self.iniciar_questionario(curso_id, modulos_restantes[0]['nome'])
        else:
            messagebox.showinfo("Parabéns!", "🎉 Você já concluiu todos os módulos deste curso!")
    
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
        frame.pack(expand=True, fill='both')
        
        ttk.Label(frame, text=curso['nome'], 
                 font=('Segoe UI', 16, 'bold')).pack(pady=10)
        
        info_text = f"""
📖 DESCRIÇÃO:
{curso['descricao']}

📊 INFORMAÇÕES:
• Carga Horária: {curso['carga_horaria']}
• Dificuldade: {curso['dificuldade']}
• Categoria: {curso['categoria']}
• Professor: {self.usuarios_cadastrados.get(curso['professor'], {}).get('nome_completo', curso['professor'])}
• Avaliação: {curso['avaliacao']}/5.0
• Alunos Matriculados: {curso['alunos_matriculados']}

🎯 MÓDULOS:
"""
        
        texto_detalhes = scrolledtext.ScrolledText(frame, height=20, width=70, font=('Segoe UI', 10))
        texto_detalhes.pack(fill='both', expand=True, pady=10)
        texto_detalhes.insert('1.0', info_text)
        
        # Adicionar módulos
        for i, modulo in enumerate(curso['modulos'], 1):
            texto_detalhes.insert('end', f"{i}. {modulo['nome']}\n")
            texto_detalhes.insert('end', f"   - Dificuldade: {modulo['dificuldade']}\n")
            texto_detalhes.insert('end', f"   - Tempo Estimado: {modulo['tempo_estimado']}\n")
            texto_detalhes.insert('end', f"   - Questões: {modulo['questoes']}\n\n")
        
        texto_detalhes.config(state='disabled')
        
        # Botão de fechar
        ttk.Button(frame, text="Fechar", 
                  command=detalhes_janela.destroy).pack(pady=10)

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
            "respostas": []
        }
        
        self.forum_mensagens[topico].append(mensagem_completa)
        self.salvar_forum()
        
        # Atualizar métricas de colaboração
        self.atualizar_metricas_colaboracao()
    
    def atualizar_metricas_colaboracao(self):
        """Atualiza métricas de colaboração"""
        total_mensagens = sum(len(mensagens) for mensagens in self.forum_mensagens.values())
        usuarios_ativos = set()
        
        for topico, mensagens in self.forum_mensagens.items():
            for msg in mensagens:
                usuarios_ativos.add(msg['usuario'])
        
        return {
            "total_mensagens": total_mensagens,
            "usuarios_ativos": len(usuarios_ativos),
            "topicos_ativos": len(self.forum_mensagens)
        }
    
    def calcular_impacto_sustentabilidade(self):
        """Calcula impacto ambiental positivo do sistema digital"""
        total_usuarios = len(self.usuarios_cadastrados)
        total_atividades = self.metricas_sustentabilidade.get('total_atividades_digitais', 0)
        
        # Cálculos baseados em métricas ambientais
        papel_economizado = total_atividades * 0.05  # 50g por atividade em papel
        co2_economizado = papel_economizado * 1.2    # 1.2kg CO2 por kg de papel
        agua_economizada = papel_economizado * 10    # 10 litros por kg de papel
        
        self.metricas_sustentabilidade.update({
            "papel_economizado": round(papel_economizado, 2),
            "co2_economizado": round(co2_economizado, 2),
            "agua_economizada": round(agua_economizada, 2),
            "total_atividades_digitais": total_atividades,
            "ultima_atualizacao": datetime.now().isoformat()
        })
        
        self.salvar_metricas()
        
        return self.metricas_sustentabilidade
    
    def registrar_atividade_digital(self):
        """Registra uma atividade digital para cálculo de sustentabilidade"""
        self.metricas_sustentabilidade['total_atividades_digitais'] += 1
        self.calcular_impacto_sustentabilidade()
    
    def criar_aba_sustentabilidade(self, parent):
        """Aba de métricas de sustentabilidade"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill='both')
        
        ttk.Label(frame, text="🌱 Sustentabilidade UNIP - Impacto Digital", 
                 style='Subtitle.TLabel').pack(anchor='w', pady=10)
        
        # Atualizar métricas
        metricas = self.calcular_impacto_sustentabilidade()
        
        # Cartões de impacto
        impactos = [
            ("📄 Papel Economizado", f"{metricas['papel_economizado']} kg", "Equivale a {} árvores salvas", lambda x: x/5),
            ("🌫️ CO₂ Economizado", f"{metricas['co2_economizado']} kg", "Equivale a {} km não rodados", lambda x: x*2),
            ("💧 Água Economizada", f"{metricas['agua_economizada']} litros", "Equivale a {} dias de consumo", lambda x: x/100),
            ("📊 Atividades Digitais", f"{metricas['total_atividades_digitais']}", "{} atividades sem papel", lambda x: x)
        ]
        
        # Grid de cartões
        grid_frame = ttk.Frame(frame)
        grid_frame.pack(fill='x', pady=20)
        
        for i, (titulo, valor, equivalencia, calc) in enumerate(impactos):
            card = ttk.Frame(grid_frame, style='Card.TFrame', padding="20")
            card.grid(row=i//2, column=i%2, sticky='nsew', padx=10, pady=10)
            
            ttk.Label(card, text=titulo, font=('Segoe UI', 12, 'bold')).pack(anchor='w')
            ttk.Label(card, text=valor, font=('Segoe UI', 18, 'bold'), 
                     foreground='#27ae60').pack(anchor='w', pady=5)
            
            # Calcular equivalência
            num = float(metricas['papel_economizado'])
            equiv_valor = calc(num)
            texto_equiv = equivalencia.format(f"{equiv_valor:.1f}")
            ttk.Label(card, text=texto_equiv, font=('Segoe UI', 9),
                     foreground='#7f8c8d').pack(anchor='w')
        
        grid_frame.columnconfigure(0, weight=1)
        grid_frame.columnconfigure(1, weight=1)
        
        # Informações educacionais
        info_frame = ttk.Frame(frame, style='Card.TFrame', padding="15")
        info_frame.pack(fill='x', pady=10)
        
        ttk.Label(info_frame, text="💡 Como o sistema digital ajuda o meio ambiente:",
                 font=('Segoe UI', 11, 'bold')).pack(anchor='w')
        
        beneficios = [
            "✅ Redução do uso de papel e recursos de impressão",
            "✅ Diminuição da emissão de CO₂ com transporte de materiais",
            "✅ Economia de água na produção de papel",
            "✅ Menor geração de resíduos físicos",
            "✅ Acesso democratizado ao conhecimento"
        ]
        
        for beneficio in beneficios:
            ttk.Label(info_frame, text=beneficio, font=('Segoe UI', 9)).pack(anchor='w', pady=2)
        
        # Botão para registrar atividade (simulação)
        ttk.Button(frame, text="📝 Registrar Atividade Digital", 
                  command=self.registrar_atividade_digital_simulada).pack(pady=10)
    
    def registrar_atividade_digital_simulada(self):
        """Simula o registro de uma atividade digital"""
        self.registrar_atividade_digital()
        messagebox.showinfo("Atividade Registrada", 
                           "✅ Atividade digital registrada!\n"
                           "🌱 Sua contribuição para a sustentabilidade foi contabilizada.")
        # Recarregar a aba de sustentabilidade
        self.atualizar_interface()
    
    def criar_aba_perfil_avancado(self, parent):
        """Aba de perfil do usuário"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill='both')
        
        user_data = self.usuarios_cadastrados[self.usuario_logado]
        
        ttk.Label(frame, text="👤 Meu Perfil UNIP", 
                 style='Title.TLabel').pack(pady=10)
        
        # Informações em cards
        info_card = ttk.Frame(frame, style='Card.TFrame', padding="20")
        info_card.pack(fill='x', pady=10)
        
        infos = [
            ("👤 Nome Completo:", user_data.get('nome_completo', self.usuario_logado)),
            ("📧 Email:", user_data.get('email', 'N/A')),
            ("📞 Telefone:", user_data.get('telefone', 'N/A')),
            ("🎂 Idade:", str(user_data.get('idade', 'N/A'))),
            ("📅 Data de Cadastro:", user_data.get('data_cadastro', 'N/A')[:10]),
            ("🎯 Tipo de Usuário:", user_data.get('tipo', 'aluno').upper())
        ]
        
        if user_data.get('tipo') == 'aluno':
            infos.extend([
                ("🎓 Cursos Matriculados:", str(len(user_data.get('cursos', [])))),
                ("📜 Certificados:", str(len(user_data.get('certificados', [])))),
                ("🎯 Interesses:", ', '.join(user_data.get('interesses', [])) if user_data.get('interesses') else 'Não informados'),
                ("📊 Preferências:", f"{user_data.get('preferencias_aprendizado', {}).get('modalidade', 'N/A')} - {user_data.get('preferencias_aprendizado', {}).get('ritmo', 'N/A')}")
            ])
        
        for i, (label, valor) in enumerate(infos):
            ttk.Label(info_card, text=label, font=('Segoe UI', 10, 'bold')).grid(row=i, column=0, sticky='w', pady=3)
            ttk.Label(info_card, text=valor, font=('Segoe UI', 10)).grid(row=i, column=1, sticky='w', pady=3, padx=10)
        
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
            "sugestoes_modulos": []
        }
        
        # Análise de velocidade
        cursos_ativos = [cid for cid in progresso if progresso[cid].get('progresso', 0) < 100]
        if cursos_ativos:
            tempo_medio = sum(progresso[cid].get('tempo_estudo', 0) for cid in cursos_ativos) / len(cursos_ativos)
            analise["velocidade_aprendizado"] = min(100, tempo_medio * 10)
        
        # Identificar dificuldades e pontos fortes
        for curso_id, dados_curso in progresso.items():
            curso = self.cursos_disponiveis.get(curso_id, {})
            if dados_curso.get('progresso', 0) < 30:
                analise["dificuldades"].append(f"{curso.get('nome', 'Curso')} ({dados_curso.get('progresso', 0):.1f}%)")
            elif dados_curso.get('progresso', 0) > 70:
                analise["pontos_fortes"].append(f"{curso.get('nome', 'Curso')} ({dados_curso.get('progresso', 0):.1f}%)")
        
        # Previsão de conclusão
        for curso_id in cursos_ativos:
            progresso_atual = progresso[curso_id].get('progresso', 0)
            if progresso_atual > 0:
                tempo_restante = (100 - progresso_atual) / max(progresso_atual, 1) * 30  # 30 dias base
                previsao = datetime.now() + timedelta(days=tempo_restante)
                analise["previsao_conclusao"][curso_id] = previsao.strftime("%d/%m/%Y")
        
        # Sugestões de módulos
        for curso_id in cursos_ativos:
            curso = self.cursos_disponiveis.get(curso_id, {})
            modulos_restantes = [mod for mod in curso.get('modulos', []) 
                               if mod['nome'] not in progresso.get(curso_id, {}).get('modulos_concluidos', [])]
            
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
            "recursos_complementares": []
        }
        
        # Cursos sugeridos baseados em interesses
        interesses = user_data.get('interesses', [])
        for curso_id, curso in self.cursos_disponiveis.items():
            if curso_id not in user_data.get('cursos', []):
                # Verificar alinhamento com interesses
                tags_comuns = set(interesses) & set(curso.get('tags', []))
                if tags_comuns:
                    recomendacoes["cursos_sugeridos"].append({
                        'curso': curso['nome'],
                        'motivo': f"Alinhado com seu interesse em {', '.join(tags_comuns)}",
                        'dificuldade': curso['dificuldade']
                    })
        
        # Módulos prioritários baseados no progresso
        for curso_id, dados_curso in progresso.items():
            if dados_curso.get('progresso', 0) < 50:
                curso = self.cursos_disponiveis.get(curso_id, {})
                modulos_pendentes = [mod for mod in curso.get('modulos', []) 
                                   if mod['nome'] not in dados_curso.get('modulos_concluidos', [])]
                
                if modulos_pendentes:
                    recomendacoes["modulos_prioritarios"].append({
                        'curso': curso['nome'],
                        'modulo': modulos_pendentes[0]['nome'],
                        'prioridade': 'ALTA' if dados_curso.get('progresso', 0) < 30 else 'MÉDIA'
                    })
        
        # Dicas de estudo personalizadas
        preferencias = user_data.get('preferencias_aprendizado', {})
        if preferencias.get('modalidade') == 'visual':
            recomendacoes["dicas_estudo"].extend([
                "🎨 Crie mapas mentais para organizar o conteúdo",
                "📊 Use gráficos e diagramas para entender conceitos complexos",
                "🖼️ Assista videoaulas para reforçar o aprendizado"
            ])
        elif preferencias.get('modalidade') == 'auditivo':
            recomendacoes["dicas_estudo"].extend([
                "🎧 Grave resumos em áudio e escute durante deslocamentos",
                "🗣️ Explique o conteúdo em voz alta para fixar melhor",
                "🎵 Use podcasts educativos sobre os temas estudados"
            ])
        else:  # prático
            recomendacoes["dicas_estudo"].extend([
                "💻 Pratique com exercícios e projetos reais",
                "🔧 Implemente os conceitos em pequenos projetos",
                "🛠️ Resolva problemas práticos da área"
            ])
        
        # Recursos complementares
        if any('Python' in interesse for interesse in interesses):
            recomendacoes["recursos_complementares"].extend([
                "📚 Livro: 'Python Fluente' - Luciano Ramalho",
                "💻 Site: Real Python - Tutoriais práticos",
                "🎥 Canal: Curso em Vídeo - Python completo"
            ])
        
        return recomendacoes

    def criar_aba_professor(self, parent):
        """Aba de gerenciamento para professores"""
        frame = ttk.Frame(parent, padding="20")
        frame.pack(expand=True, fill='both')
        
        user_data = self.usuarios_cadastrados[self.usuario_logado]
        cursos_professor = user_data.get('cursos', [])
        
        ttk.Label(frame, text="👨‍🏫 Painel do Professor", 
                 style='Title.TLabel').pack(anchor='w', pady=10)
        
        if not cursos_professor:
            ttk.Label(frame, text="❌ Você não é responsável por nenhum curso.",
                     font=('Segoe UI', 12), foreground='red').pack(pady=50)
            return
        
        # Abas para cada curso
        notebook = ttk.Notebook(frame)
        notebook.pack(expand=True, fill='both', pady=10)
        
        for curso_id in cursos_professor:
            if curso_id in self.cursos_disponiveis:
                curso = self.cursos_disponiveis[curso_id]
                aba_curso = ttk.Frame(notebook)
                self.criar_subaba_professor_curso(aba_curso, curso_id)
                notebook.add(aba_curso, text=curso['nome'])
    
    def criar_subaba_professor_curso(self, parent, curso_id):
        """Subaba de gerenciamento para um curso específico"""
        curso = self.cursos_disponiveis.get(curso_id)
        if not curso:
            return
        
        # Frame principal com scroll
        main_frame = ttk.Frame(parent)
        main_frame.pack(expand=True, fill='both')
        
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Informações do curso
        info_frame = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="15")
        info_frame.pack(fill='x', pady=10, padx=10)
        
        ttk.Label(info_frame, text=f"📊 Estatísticas do Curso: {curso['nome']}", 
                 font=('Segoe UI', 14, 'bold')).pack(anchor='w')
        
        # Encontrar alunos matriculados
        alunos_curso = []
        for usuario, dados in self.usuarios_cadastrados.items():
            if dados.get('tipo') == 'aluno' and curso_id in dados.get('cursos', []):
                progresso = self.progresso_alunos.get(usuario, {}).get(curso_id, {})
                alunos_curso.append({
                    'usuario': usuario,
                    'nome': dados.get('nome_completo', usuario),
                    'progresso': progresso.get('progresso', 0),
                    'modulos_concluidos': len(progresso.get('modulos_concluidos', [])),
                    'total_modulos': len(curso['modulos']),
                    'nota_final': progresso.get('nota_final', 0),
                    'data_matricula': progresso.get('data_matricula', 'N/A')
                })
        
        # Estatísticas
        total_alunos = len(alunos_curso)
        media_progresso = sum(aluno['progresso'] for aluno in alunos_curso) / max(total_alunos, 1)
        alunos_aprovados = sum(1 for aluno in alunos_curso if aluno['nota_final'] >= 70)
        alunos_certificados = sum(1 for aluno in alunos_curso if aluno['progresso'] >= 80 and aluno['nota_final'] >= 70)
        
        stats_text = f"""
📈 Estatísticas Gerais:
• Total de Alunos: {total_alunos}
• Progresso Médio: {media_progresso:.1f}%
• Alunos Aprovados: {alunos_aprovados}/{total_alunos}
• Certificados Emitidos: {alunos_certificados}
• Módulos do Curso: {len(curso['modulos'])}
        """
        
        ttk.Label(info_frame, text=stats_text, font=('Segoe UI', 10), 
                 justify='left').pack(anchor='w', pady=10)
        
        # Lista de alunos
        if alunos_curso:
            alunos_frame = ttk.Frame(scrollable_frame, style='Card.TFrame', padding="15")
            alunos_frame.pack(fill='x', pady=10, padx=10)
            
            ttk.Label(alunos_frame, text="🎓 Alunos Matriculados", 
                     font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=10)
            
            # Treeview para alunos
            colunas = ('aluno', 'nome', 'progresso', 'modulos', 'nota', 'status')
            tree = ttk.Treeview(alunos_frame, columns=colunas, show='headings', height=12)
            
            tree.heading('aluno', text='Usuário')
            tree.heading('nome', text='Nome')
            tree.heading('progresso', text='Progresso')
            tree.heading('modulos', text='Módulos')
            tree.heading('nota', text='Nota')
            tree.heading('status', text='Status')
            
            tree.column('aluno', width=100)
            tree.column('nome', width=150)
            tree.column('progresso', width=80)
            tree.column('modulos', width=80)
            tree.column('nota', width=60)
            tree.column('status', width=100)
            
            for aluno in alunos_curso:
                status = "✅ Aprovado" if aluno['nota_final'] >= 70 else "📚 Em Andamento"
                if aluno['progresso'] >= 80 and aluno['nota_final'] >= 70:
                    status = "🏆 Certificado"
                
                tree.insert('', 'end', values=(
                    aluno['usuario'],
                    aluno['nome'],
                    f"{aluno['progresso']:.1f}%",
                    f"{aluno['modulos_concluidos']}/{aluno['total_modulos']}",
                    f"{aluno['nota_final']:.1f}%" if aluno['nota_final'] > 0 else "N/A",
                    status
                ))
            
            tree.pack(fill='x', pady=10)
            
            # Botões de ação para professor
            btn_frame = ttk.Frame(alunos_frame)
            btn_frame.pack(fill='x', pady=10)
            
            ttk.Button(btn_frame, text="📊 Exportar Relatório", 
                      command=lambda: self.exportar_relatorio_curso(curso_id)).pack(side='left', padx=5)
            ttk.Button(btn_frame, text="📧 Contatar Alunos", 
                      command=lambda: self.contatar_alunos_curso(curso_id)).pack(side='left', padx=5)
        
        else:
            ttk.Label(scrollable_frame, text="Nenhum aluno matriculado neste curso.",
                     font=('Segoe UI', 11), foreground='gray').pack(pady=20)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def exportar_relatorio_curso(self, curso_id):
        """Exporta relatório do curso"""
        messagebox.showinfo("Relatório", 
                           f"📊 Relatório do curso exportado com sucesso!\n\n"
                           f"Funcionalidade de exportação em desenvolvimento.")
    
    def contatar_alunos_curso(self, curso_id):
        """Sistema de contato com alunos do curso"""
        messagebox.showinfo("Contato", 
                           f"📧 Sistema de contato com alunos em desenvolvimento.\n\n"
                           f"Em breve você poderá enviar mensagens para todos os alunos do curso.")

    def mostrar_tela_login(self):
        """Tela de login moderna"""
        self.limpar_tela()
        
        main_frame = ttk.Frame(self.root, padding="40")
        main_frame.pack(expand=True, fill='both')
        
        ttk.Label(main_frame, text="🎓 UNIP - UNIVERSIDADE PAULISTA", 
                 style='Title.TLabel').pack(pady=10)
        ttk.Label(main_frame, text="PIM II - Sistema Acadêmico com IA Avançada",
                 style='Subtitle.TLabel').pack(pady=5)
        
        # Card de login
        login_card = ttk.Frame(main_frame, style='Card.TFrame', padding="30")
        login_card.pack(pady=30, padx=100, fill='x')
        
        ttk.Label(login_card, text="🔐 Acesso ao Sistema", 
                 font=('Segoe UI', 16, 'bold')).pack(pady=20)
        
        # Formulário
        form_frame = ttk.Frame(login_card)
        form_frame.pack(pady=20, padx=30)
        
        ttk.Label(form_frame, text="Usuário:", font=('Segoe UI', 11)).grid(row=0, column=0, sticky='w', pady=10)
        self.entry_user = ttk.Entry(form_frame, width=25, font=('Segoe UI', 11))
        self.entry_user.grid(row=0, column=1, pady=10, padx=10)
        
        ttk.Label(form_frame, text="Senha:", font=('Segoe UI', 11)).grid(row=1, column=0, sticky='w', pady=10)
        self.entry_senha = ttk.Entry(form_frame, width=25, show="•", font=('Segoe UI', 11))
        self.entry_senha.grid(row=1, column=1, pady=10, padx=10)
        
        # Botões
        btn_frame = ttk.Frame(login_card)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="🚀 Entrar no Sistema", 
                  command=self.fazer_login_interativo, 
                  width=18).pack(side='left', padx=10)
        ttk.Button(btn_frame, text="📝 Criar Conta Aluno", 
                  command=self.mostrar_cadastro_completo, 
                  width=18).pack(side='left', padx=10)
        
        # Status do sistema
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(pady=20)
        
        stats = self.atualizar_metricas_colaboracao()
        metricas = self.calcular_impacto_sustentabilidade()
        
        status_info = [
            f"✅ {len(self.usuarios_cadastrados)} Usuários",
            f"🤖 IA Ativa",
            f"👥 {stats['usuarios_ativos']} Colaborando",
            f"🌱 {metricas['papel_economizado']}kg Papel Economizado"
        ]
        
        for info in status_info:
            ttk.Label(status_frame, text=info, font=('Segoe UI', 9)).pack(side='left', padx=15)
        
        self.entry_user.focus()
        self.entry_senha.bind('<Return>', lambda e: self.fazer_login_interativo())

    def iniciar(self):
        """Inicia o sistema"""
        self.mostrar_tela_login()
        self.root.mainloop()

if __name__ == "__main__":
    app = SistemaUNIPIACompleto()
    app.iniciar()