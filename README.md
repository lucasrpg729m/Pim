📚 UNIP PIM II - Sistema Acadêmico
🚀 Início Rápido - Primeiros Passos
Sistema acadêmico com interface gráfica para gerenciamento de cursos, questionários, fórum e certificados.

⚠️INSTALAÇÃO ESSENCIAL
Antes de executar o programa, instale uma dependência para gerar certificados:

pip install reportlab
IMPORTANTE : Sem reportlab, o sistema não conseguirá gerar os certificados em PDF!

Executar a Plataforma
python interface_unip.py
Uma janela do sistema acadêmico será aberta automaticamente.

👤 Login - Usuários de Teste
Contas Disponíveis para Testar
Administrador:

Matrícula:admin
Senha:Admin@123
Professor Python:

Matrícula:prof.python
Senha:Professor@123
Professor Web:

Matrícula:prof.web
Senha:Professor@123
Criar novo usuário
Clique em "Criar Conta" na tela inicial
📊 Funcionalidades Principais
1. Gerenciamento de Cursos
Visualizar cursos disponíveis
Matrícula-se em cursos
Acompanhar módulos e conteúdos
Ver carga
2. Questionários e Avaliações
Responder questionários dos módulos
r ✓
Acompanhar o progresso por disciplina
Feedback de desempenho
3. Certificados em PDF ✅
Gerados automaticamente ao completar cursos
Salvos na pastacertificados/
Solicite reportlabinstalação (veja início do README)
4. Painel de Progresso
Estatísticas de desempenho
Taxas de ceri
Histórico de acessos
📁 Estrutura de Arquivos
c:\Users\nelia\Desktop\Pin\
├── interface_unip.py              # Sistema principal (Tkinter)
├── cursos_disponiveis.json        # Catálogo de cursos
├── dados_usuarios.json            # Dados dos usuários
├── progresso_alunos.json          # Progresso acadêmico
├── metricas_sustentabilidade.json # Estatísticas gerais
├── certificados/                  # Pasta com certificados PDF
├── README.md                       # Este arquivo
└── __pycache__/                   # Cache Python (auto-gerado)
🔧 Dependências e Configuração
Obrigatória para Certificados
pip install reportlab
Verificar Instalação
pip show reportlab
Se a saída aparecer, está instalado corretamente.

📝 Dados salvos (Arquivos JSON)
O sistema armazena automaticamente:

dados_usuarios.json : Perfis de usuários, senhas, preferências
cursos_disponiveis.json : Catálogo de cursos e módulos
progresso_alunos.json : Notas, conexões, histórico
métricas_sustentabilidade.json : KPIs e estatísticas globais
Todos os dados são salvos em tempo real.

🐛 Solução de Problemas
Certificados não geram
Verifique se reportlabestá instalado
Confirme que a pasta certificados/existe e tem permissão de escrita
Confira espaço em disco disponível
Interface não abre
Confirme se o Python 3.8+ está instalado
Verifique se tkinterestá disponível
Teste com:python -m tkinter
Dados não são salvos
Verifique as verificações de escrita no diretório
Confirme que os arquivos .json existem
Tente executar como administrador se necessário
✅ Lista de verificação
Python 3.8 ou superior instalado
 pip install reportlabexecutado
Todos os arquivos .json presentes
A massa certificados/existe
 python interface_unip.pyroda sem erros
Consegue fazer login com credenciais de teste
📞 Dicas Financeiras
Sempre instale reportlabantes de usar o sistema
-se de fazer backup dos arquivos JSON periodicamente
Use as contas de teste para familiarizar-se com o sistema
Leia os conteúdos dos cursos antes de fazer os questionários
Sistema Acadêmico UNIP PIM II – Novembro de 2025

📝 Notas Importantes
⚠️ Backup regular : Os dados são salvos automaticamente em JSON
⚠️ Segurança : Não compartilhe sua senha com ninguém
⚠️ Tempo limite : Os questionários têm tempo limite (confira antes de iniciar)
⚠️ Compatibilidade : Testado em Windows 10/11 com Python 3.8+
🎉 Bem-vindo à UNIP!
Desejamos muito sucesso em sua jornada acadêmica. Aproveite todos os recursos disponíveis e boa sorte nos seus estudos!

Última atualização : Novembro de 2025

Sistema Acadêmico UNIP PIM II - Todos os direitos reservados
