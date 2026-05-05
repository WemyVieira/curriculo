# pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import cm
from reportlab.lib import colors

# Caminho de saída do PDF
output_path = "Wemy_Felipe_Curriculo_1_Coluna.pdf"

# Criação do documento
doc = SimpleDocTemplate(output_path, pagesize=A4,
                        rightMargin=2 * cm, leftMargin=2 * cm,
                        topMargin=2 * cm, bottomMargin=2 * cm)

# Estilos personalizados
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="MyTitle", fontSize=20, textColor=colors.HexColor("#0A3D62"), spaceAfter=14, leading=22))
styles.add(
    ParagraphStyle(name="MySubtitle", fontSize=14, textColor=colors.HexColor("#0A3D62"), spaceBefore=10, spaceAfter=6,
                   leading=18))
styles.add(ParagraphStyle(name="MyBody", fontSize=11, leading=16, spaceAfter=6))
styles.add(ParagraphStyle(name="MyHeader", fontSize=18, textColor=colors.white, alignment=1, leading=22, spaceAfter=14,
                          backColor=colors.HexColor("#0A3D62")))

# Conteúdo do PDF
content = []

# Cabeçalho
content.append(Paragraph("Wemy Felipe", styles["MyHeader"]))
content.append(Spacer(1, 8))
content.append(Paragraph("Engenheiro de Software", styles["MyTitle"]))

# SOBRE MIM
content.append(Paragraph("Sobre mim", styles["MySubtitle"]))
content.append(Paragraph(
    "Engenheiro de Software com 10+ anos de experiência especializado em desenvolvimento backend escalável. "
    "Expert em Java com sólida atuação em Python e TypeScript. Histórico comprovado de entrega de soluções de alto impacto em ambientes corporativos de larga escala, "
    "com foco em arquitetura de microsserviços, APIs RESTful e otimização de performance. "
    "Praticante de Jiu-Jitsu Brasileiro, aplico princípios de disciplina e melhoria contínua no desenvolvimento de software. "
    "Apaixonado por explorar novas tecnologias e resolver problemas complexos através de arquiteturas bem projetadas.",
    styles["MyBody"]
))

# EXPERIÊNCIAS PROFISSIONAIS
content.append(Paragraph("Experiências Profissionais", styles["MySubtitle"]))

experiencias = [
    ("Software Engineer | Claro", "São Paulo, SP | Mai/2024 – Presente",
     "Desenvolvendo plataforma de streaming para Claro TV com foco em escalabilidade e performance. "
     "Principais contribuições: Arquitetei e implementei BFF usando Node.js/TypeScript/Express, integração de APIs e microserviços Python/Django, estratégias de cache e otimização, pipeline de testes automatizados e arquitetura distribuída."),

    ("Arquiteto de Software / Líder Técnico | Lello Condomínios", "São Paulo, SP | Nov/2018 – Mai/2024",
     "Liderei transformação tecnológica de sistemas legados para arquitetura moderna de microsserviços, comandando squad de inovação, definindo padrões arquiteturais, mentorando equipe e implementando arquitetura escalável com JWT, JPA/Hibernate e bancos Oracle/MariaDB."),

    # ("Software Engineer | Loggi", "São Paulo, SP | Mai/2021 – Ago/2022",
    #  "Desenvolvi soluções de alto impacto para otimizar operações logísticas, incluindo APIs Python/Django, otimização de gRPC, monorepo Python, bibliotecas internas e modelagem de dados complexos."),

    ("Desenvolvedor Full Stack | CCEE", "São Paulo, SP | Set/2019 – Mai/2021",
     "Desenvolvi soluções críticas para setor de energia elétrica, aumentando capacidade de geração de relatórios em 500%, arquitetura paralela com mensageria, reprocessamento automático e entrega de features críticas com metodologia ágil."),

    ("Desenvolvedor Full Stack | UNIFOR/NATI", "Fortaleza, CE | Fev/2016 – Nov/2018",
     "Criei aplicações web e mobile end-to-end, projetando modelos de dados robustos, interfaces user-friendly e implementando soluções escaláveis com foco em usabilidade e manutenibilidade.")
]

for cargo, periodo, descricao in experiencias:
    content.append(Paragraph(f"<b>{cargo}</b> — {periodo}", styles["MyBody"]))
    content.append(Paragraph(descricao, styles["MyBody"]))

# FORMAÇÃO ACADÊMICA
content.append(Paragraph("Formação Acadêmica", styles["MySubtitle"]))
formacoes = [
    "Especialização em Inteligência Artificial — USP | 2020 - 2022",
    "Bacharelado em Ciência da Computação — UNIFOR | 2012 - 2017",
    "Licenciatura Plena em Informática — UECE | 2012 - 2016"
]
for f in formacoes:
    content.append(Paragraph(f, styles["MyBody"]))

# CERTIFICAÇÕES
content.append(Paragraph("Certificações", styles["MySubtitle"]))
certificacoes = [
    "JavaScript Avançado I: ES6, Orientação a Objetos e Padrões de Projetos",
    "Lean Startup: Primeiros Passos da sua Startup Enxuta",
    "Expressões Regulares: Capturando Textos de Forma Mágica"
]
for c in certificacoes:
    content.append(Paragraph(f"• {c}", styles["MyBody"]))

# COMPETÊNCIAS TÉCNICAS
content.append(Paragraph("Competências Técnicas", styles["MySubtitle"]))
competencias = [
    "Linguagens: Java, Python, JavaScript, TypeScript",
    "Frameworks: Spring, Django, Node.js, Express",
    "Arquitetura: Microsserviços, APIs RESTful, Design Patterns, SOLID, Clean Architecture, DDD, BFF",
    "Bancos de Dados: Oracle, MariaDB, MySQL, PostgreSQL, JPA/Hibernate",
    "DevOps & Ferramentas: Docker, Kubernetes, Rancher, OpenShift, Git, CI/CD (Bamboo), Mensageria (Artemis, RabbitMQ)",
    "Tecnologias Adicionais: gRPC, Protocol Buffers, JWT, OAuth, WebSockets, Monorepo"
]
for comp in competencias:
    content.append(Paragraph(f"• {comp}", styles["MyBody"]))

# HABILIDADES INTERPESSOAIS
content.append(Paragraph("Habilidades Interpessoais", styles["MySubtitle"]))
soft_skills = [
    "Liderança Técnica",
    "Comunicação Eficaz",
    "Resolução de Problemas",
    "Trabalho em Equipe",
    "Adaptabilidade",
    "Senso de Dono"
]
for skill in soft_skills:
    content.append(Paragraph(f"• {skill}", styles["MyBody"]))

# Construção do PDF
doc.build(content)

print(f"PDF gerado com sucesso: {output_path}")