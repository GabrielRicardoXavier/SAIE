### importar itens ###
import tkinter
import pyodbc
import time
import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

Dados_conexao = ("Driver={SQL Server};"
                 "Server=DESKTOP-MFB01UH;"
                 "Database=Alunos")
conexao = pyodbc.connect(Dados_conexao)
cursor = conexao.cursor()

### criando a área de trabalho ###
trabalho = Tk()
#trabalho.geometry('10000x1000+0+0')
width = trabalho.winfo_screenwidth()
height = trabalho.winfo_screenheight()
trabalho.geometry("%dx%d" % (width, height))
trabalho.title('SAIE - Sistema de Atendimento de Inclusão Educacional')
trabalho.configure(bg='light gray')

### funções ###
def semComando():
    print("")

def abrirAditamento():
    novoTrabalhoAditamento = Toplevel()
    novoTrabalhoAditamento.geometry('1090x620+260+70')
    novoTrabalhoAditamento.resizable(False,False)
    novoTrabalhoAditamento.title('Aditamento')
    novoTrabalhoAditamento.configure(bg='light gray')
    novoTrabalhoAditamento.transient(trabalho)
    novoTrabalhoAditamento.focus_force()
    novoTrabalhoAditamento.grab_set()

    Ea_imgAditamento = Label(novoTrabalhoAditamento, image=imgEA)
    Ea_imgAditamento.place(x=1020, y=30, width=60, height=45)

    ### Label ###
    CadastroAlunoAditamentoLabel = Label(novoTrabalhoAditamento, text="Cadastro de Aluno", font="Arial 8 bold", bg='light grey', foreground='blue')
    CadastroAlunoAditamentoLabel.place(x=7, y=4)

    CodigoAditamentoLabel = Label(novoTrabalhoAditamento, text="Código", font="Arial 9 bold", bg='light grey')
    CodigoAditamentoLabel.place(x=10, y=40)

    AlunoAditamentoLabel = Label(novoTrabalhoAditamento, text="Aluno", bg='light grey')
    AlunoAditamentoLabel.place(x=100, y=40)

    MatriculaAditamentoLabel = Label(novoTrabalhoAditamento, text="Matrícula", bg='light grey')
    MatriculaAditamentoLabel.place(x=368, y=40)

    SerieAditamentoLabel = Label(novoTrabalhoAditamento, text="Série", bg='light grey')
    SerieAditamentoLabel.place(x=497, y=40)

    TurmaAditamentoLabel = Label(novoTrabalhoAditamento, text="Turma", bg='light grey')
    TurmaAditamentoLabel.place(x=747, y=40)

    NascimentoAditamentoLabel = Label(novoTrabalhoAditamento, text="Nascimento", bg='light grey')
    NascimentoAditamentoLabel.place(x=837, y=40)

    AnoAditamentoLabel = Label(novoTrabalhoAditamento, text="Ano", font="Arial 9 bold", bg='light grey')
    AnoAditamentoLabel.place(x=927, y=40)

    NomeMaeAditamentoLabel = Label(novoTrabalhoAditamento, text="Nome da Mãe", bg='light grey')
    NomeMaeAditamentoLabel.place(x=10, y=80)

    EnderecoAditamentoLabel = Label(novoTrabalhoAditamento, text="Endereço", bg='light grey')
    EnderecoAditamentoLabel.place(x=340, y=80)

    UnidadeEscolarAditamentoLabel = Label(novoTrabalhoAditamento, text="Unidade Escolar", bg='light grey')
    UnidadeEscolarAditamentoLabel.place(x=670, y=80)

    DiagnosticoAditamentoLabel = Label(novoTrabalhoAditamento, text="Diagnóstico", bg='light grey')
    DiagnosticoAditamentoLabel.place(x=10, y=120)

    DiaLaudoAditamentoLabel = Label(novoTrabalhoAditamento, text="Dia Laudo", bg='light grey')
    DiaLaudoAditamentoLabel.place(x=378, y=120)

    MesLaudoAditamentoLabel = Label(novoTrabalhoAditamento, text="Mês Laudo", bg='light grey')
    MesLaudoAditamentoLabel.place(x=442, y=120)

    AnoLaudoAditamentoLabel = Label(novoTrabalhoAditamento, text="Ano Laudo", bg='light grey')
    AnoLaudoAditamentoLabel.place(x=510, y=120)

    MedicoAditamentoLabel = Label(novoTrabalhoAditamento, text="Nome do Médico", bg='light grey')
    MedicoAditamentoLabel.place(x=580, y=120)

    CRMAditamentoLabel = Label(novoTrabalhoAditamento, text="CRM", bg='light grey')
    CRMAditamentoLabel.place(x=820, y=120)

    ResponsavelAditamentoLabel = Label(novoTrabalhoAditamento, text="Nome do Responsável", bg='light grey')
    ResponsavelAditamentoLabel.place(x=10, y=160)

    RegistroAditamentoLabel = Label(novoTrabalhoAditamento, text="n° Registro", bg='light grey')
    RegistroAditamentoLabel.place(x=340, y=160)

    OrgaoAditamentoLabel = Label(novoTrabalhoAditamento, text="Orgão", bg='light grey')
    OrgaoAditamentoLabel.place(x=486, y=160)

    UFAditamentoLabel = Label(novoTrabalhoAditamento, text="UF", bg='light grey')
    UFAditamentoLabel.place(x=576, y=160)

    CPFAditamentoLabel = Label(novoTrabalhoAditamento, text="CPF", bg='light grey')
    CPFAditamentoLabel.place(x=665, y=160)

    ProtocoloAditamentoLabel = Label(novoTrabalhoAditamento, text="Protocolo", bg='light grey')
    ProtocoloAditamentoLabel.place(x=834, y=160)

    ArquivoAnexoAditamentoLabel = Label(novoTrabalhoAditamento, text="Arquivo Anexo do Laudo/Relatório Médico", bg='light grey', font="Arial 9 bold")
    ArquivoAnexoAditamentoLabel.place(x=10, y=200)

    DataAditamentoLabel = Label(novoTrabalhoAditamento, text="Data", bg='light grey')
    DataAditamentoLabel.place(x=780, y=200)

    DataAditamentoLabel = Label(novoTrabalhoAditamento, text="** de   ***   de ***", bg='light grey', font="Arial 11 bold", foreground='blue')
    DataAditamentoLabel.place(x=740, y=220)

    EspacoAditamentoLabel = Label(novoTrabalhoAditamento, text='__________________________________________________________________________________________________________________________________________________________________________________________________________________', bg='light grey')
    EspacoAditamentoLabel.place(x=10, y=240)

    FamiliaAditamentoLabel = Label(novoTrabalhoAditamento, text='Família', font="Arial 11", bg='light grey', foreground='blue')
    FamiliaAditamentoLabel.place(x=20, y=260)

    EscolaAditamentoLabel = Label(novoTrabalhoAditamento, text='Escola', font="Arial 11", bg='light grey', foreground='blue')
    EscolaAditamentoLabel.place(x=500, y=260)

    ### Text ###
    CodigoAditamento = Text(novoTrabalhoAditamento, width=10, height=1)
    CodigoAditamento.place(x=10, y=60)

    AlunoAditamento = tkinter.StringVar()
    AlunoAditamentocbbx = ttk.Combobox(novoTrabalhoAditamento, width=40, height=1, textvariable=AlunoAditamento)
    AlunoAditamentocbbx.place(x=100, y=60)

    comandoAlunoAditamento = "SELECT TOP (1000) * from AlunosTabela"
    cursor.execute(comandoAlunoAditamento)

    for row in cursor.fetchall():
        textoAlunoAditamento = f'{row.Aluno}'
        AlunoAditamentocbbx['value'] = textoAlunoAditamento

    MatriculaAditamento = Text(novoTrabalhoAditamento, bg='light yellow', width=15, height=1)
    MatriculaAditamento.place(x=368, y=60)

    SerieAditamento = Text(novoTrabalhoAditamento, width=30, height=1)
    SerieAditamento.place(x=497, y=60)

    TurmaAditamento = Text(novoTrabalhoAditamento, width=10, height=1)
    TurmaAditamento.place(x=747, y=60)

    NascimentoAditamento = Text(novoTrabalhoAditamento, width=10, height=1)
    NascimentoAditamento.place(x=837, y=60)

    AnoAditamento = Text(novoTrabalhoAditamento, width=6, height=1)
    AnoAditamento.place(x=927, y=60)

    NomeMaeAditamento = Text(novoTrabalhoAditamento, width=40, height=1)
    NomeMaeAditamento.place(x=10, y=100)

    EnderecoAditamento = Text(novoTrabalhoAditamento, width=40, height=1)
    EnderecoAditamento.place(x=340, y=100)

    UnidadeEscolarAditamento = Text(novoTrabalhoAditamento, width=38, height=1)
    UnidadeEscolarAditamento.place(x=670, y=100)

    DiagnosticoAditamento = Text(novoTrabalhoAditamento, bg='light yellow', width=45, height=1)
    DiagnosticoAditamento.place(x=10, y=140)

    DiaLaudoAditamento = Text(novoTrabalhoAditamento, width=7, height=1)
    DiaLaudoAditamento.place(x=378, y=140)

    MesLaudoAditamento = Text(novoTrabalhoAditamento, width=9, height=1)
    MesLaudoAditamento.place(x=442, y=140)

    AnoLaudoAditamento = Text(novoTrabalhoAditamento, width=5, height=1)
    AnoLaudoAditamento.place(x=522, y=140)

    MedicoAditamento = Text(novoTrabalhoAditamento, width=30, height=1)
    MedicoAditamento.place(x=570, y=140)

    CRMAditamento = Text(novoTrabalhoAditamento, width=19, height=1)
    CRMAditamento.place(x=820, y=140)

    NomeResponsavelAditamento = Text(novoTrabalhoAditamento, width=40, height=1)
    NomeResponsavelAditamento.place(x=10, y=180)

    NumeroRegistroAditamento = Text(novoTrabalhoAditamento, width=17, height=1)
    NumeroRegistroAditamento.place(x=340, y=180)

    OrgaoAditamento = Text(novoTrabalhoAditamento, width=10, height=1)
    OrgaoAditamento.place(x=486, y=180)

    UFAditamento = Text(novoTrabalhoAditamento, width=10, height=1)
    UFAditamento.place(x=576, y=180)

    CPFAditamento = Text(novoTrabalhoAditamento, width=20, height=1)
    CPFAditamento.place(x=665, y=180)

    ProtocoloAditamento = Text(novoTrabalhoAditamento, width=17, height=1)
    ProtocoloAditamento.place(x=834, y=180)

    ArquivoAnexoDoLaudoAditamento = Text(novoTrabalhoAditamento, width=80, height=1)
    ArquivoAnexoDoLaudoAditamento.place(x=10, y=220)

    ArquivoAnexoDoLaudoAditamentoButton = Button(novoTrabalhoAditamento, text='ABRE ANEXO', font='negrito 8 bold', bg="Lime")
    ArquivoAnexoDoLaudoAditamentoButton.place(x=655, y=220, width=80, height=21)

    Familia1Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Familia1Aditamento.place(x=15, y=285)

    Familia2Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Familia2Aditamento.place(x=15, y=310)

    Familia3Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Familia3Aditamento.place(x=15, y=335)

    Familia4Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Familia4Aditamento.place(x=15, y=360)

    Familia5Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Familia5Aditamento.place(x=15, y=385)

    Familia6Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Familia6Aditamento.place(x=15, y=410)

    Escola1Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Escola1Aditamento.place(x=495, y=285)

    Escola2Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Escola2Aditamento.place(x=495, y=310)

    Escola3Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Escola3Aditamento.place(x=495, y=335)

    Escola4Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Escola4Aditamento.place(x=495, y=360)

    Escola5Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Escola5Aditamento.place(x=495, y=385)

    Escola6Aditamento = Text(novoTrabalhoAditamento, width=55, height=1)
    Escola6Aditamento.place(x=495, y=410)

    Foto_Aluno_Adit = Label(novoTrabalhoAditamento, image=imgFoto_Aluno)
    Foto_Aluno_Adit.place(x=990, y=80)


######################################

def abrirTurma():
    novoTurma1 = Toplevel()
    novoTurma1.geometry('1090x620+260+70')
    novoTurma1.resizable(False,False)
    novoTurma1.title('Inventário de Turma')
    novoTurma1.configure(bg='light gray')
    novoTurma1.transient(trabalho)
    novoTurma1.focus_force()
    novoTurma1.grab_set()

    Ea_imgTurma = Label(novoTurma1, image=imgEA)
    Ea_imgTurma.place(x=1020, y=3, width=60, height=45)
### itens novo trabalho 1 ###
### criando frame ###
    fr_rolagem3 = Frame(novoTurma1, borderwidth=1, relief="solid")
    fr_rolagem3.place(x=7, y=50, width=1080, height=75)

    ### criando o canvas ###
    canvas3 = Canvas(novoTurma1)
    canvas3.place(x=8, y=51, width=1050, height=73)

    for row in cursor.fetchall():
        textoTurma = f'{row.Turma}'
        cb101 = Checkbutton(fr_rolagem3, text=textoTurma, width=200, anchor=W)
        cb101.grid(row=1, column=1)


        #fr_rolagem3['value'] = textoTurma



    ### criando a barra de rolagem ###
    barra_de_rolagem = ttk.Scrollbar(fr_rolagem3, orient=VERTICAL, command=canvas3.yview)
    barra_de_rolagem.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvas3.configure(yscrollcommand=barra_de_rolagem.set)
    canvas3.bind('<Configure>', lambda e: canvas3.configure(scrollregion=canvas3.bbox("all")))

    fr_rolagem3 = Frame(canvas3)

    canvas3.create_window((0, 0), window=fr_rolagem3, anchor="nw")

    ### multipage ###
    rows = 0
    while rows < 50:
        novoTurma1.rowconfigure(rows, weight=1)
        novoTurma1.columnconfigure(rows, weight=1)
        rows += 1
    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nb2 = ttk.Notebook(novoTurma1)
    nb2.grid(row=12, column=1, columnspan=48, rowspan=35, sticky="NESW")

    ### page1 ###
    pageTurma1 = ttk.Frame(nb2)
    nb2.add(pageTurma1, text="Avaliação de turma")
    #############
    ### criando frame page 1 ###
    fr_rolagemTurma = Frame(pageTurma1, borderwidth=1, relief="solid")
    fr_rolagemTurma.place(x=7, y=30, width=1035, height=355)

    ### criando o canvas ###
    canvasTurma = Canvas(pageTurma1)
    canvasTurma.place(x=8, y=31, width=1000, height=333)

    ### criando a barra de rolagem ###
    barra_de_rolagem2Turma = ttk.Scrollbar(fr_rolagemTurma, orient=VERTICAL, command=canvasTurma.yview)
    barra_de_rolagem2Turma.pack(side=RIGHT, fill=Y)

    barra_de_rolagem3Turma = ttk.Scrollbar(fr_rolagemTurma, orient=HORIZONTAL, command=canvasTurma.xview)
    barra_de_rolagem3Turma.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasTurma.configure(yscrollcommand=barra_de_rolagem2Turma.set)
    canvasTurma.bind('<Configure>', lambda e: canvasTurma.configure(scrollregion=canvasTurma.bbox("all")))

    canvasTurma.configure(xscrollcommand=barra_de_rolagem3Turma.set)
    canvasTurma.bind('<Configure>', lambda e: canvasTurma.configure(scrollregion=canvasTurma.bbox("all")))

    fr_rolagemTurma = Frame(canvasTurma)

    canvasTurma.create_window((0, 0), window=fr_rolagemTurma, anchor="nw")

### coisas ###
    chkb101 = Checkbutton(fr_rolagemTurma, text="1.01 - A Turma é muito entrosada", width=400, anchor=W)
    chkb101.grid(row=1, column=1)

    chkb102 = Checkbutton(fr_rolagemTurma, text="1.02 - Tem um bom relacionamento uns com os outros", width=400, anchor=W)
    chkb102.grid(row=2, column=1)

    chkb103 = Checkbutton(fr_rolagemTurma, text="1.03 - As crianças dessa turma são um pouco agitadas", width=400, anchor=W)
    chkb103.grid(row=3, column=1)

    chkb104 = Checkbutton(fr_rolagemTurma, text="1.04 - Tem facilidade de organizar a sala de aula", width=400, anchor=W)
    chkb104.grid(row=4, column=1)

    chkb105 = Checkbutton(fr_rolagemTurma, text="1.05 - As vezes alguns brigam", width=400, anchor=W)
    chkb105.grid(row=5, column=1)

    chkb106 = Checkbutton(fr_rolagemTurma, text="1.06 - São fáceis de perdoar", width=400, anchor=W)
    chkb106.grid(row=6, column=1)

    chkb107 = Checkbutton(fr_rolagemTurma, text="1.07 - Ocorrem alguns casos de agressividade verbal", width=400, anchor=W)
    chkb107.grid(row=7, column=1)

    chkb108 = Checkbutton(fr_rolagemTurma, text="1.08 - A adaptação da turma foi boa", width=400, anchor=W)
    chkb108.grid(row=8, column=1)

    chkb109 = Checkbutton(fr_rolagemTurma, text="1.09 - Não aceitam ser repreendidas", width=400, anchor=W)
    chkb109.grid(row=9, column=1)

    chkb110 = Checkbutton(fr_rolagemTurma, text="1.10 - Desobedeçem as normas para uma boa convivência em grupo, princpalmente nos momentos de desenvolverem trabalhos em grupos", width=400, anchor=W)
    chkb110.grid(row=10, column=1)

    chkb111 = Checkbutton(fr_rolagemTurma, text="1.11 - Falam alto de mais", width=400, anchor=W)
    chkb111.grid(row=11, column=1)

    chkb112 = Checkbutton(fr_rolagemTurma, text="1.12 - Não esperam sua vez de falar", width=400, anchor=W)
    chkb112.grid(row=12, column=1)

    chkb113 = Checkbutton(fr_rolagemTurma, text="1.13 - A maioria das crianças preferem brincar em grupo", width=400, anchor=W)
    chkb113.grid(row=13, column=1)

    chkb114 = Checkbutton(fr_rolagemTurma, text="1.14 - Alguns alunos apresentam dificuldades em desenvolver atividades sozinhos", width=400, anchor=W)
    chkb114.grid(row=14, column=1)

    chkb115 = Checkbutton(fr_rolagemTurma, text="1.15 - São bastante participativos nas atividades propostas em sala de aula", width=400, anchor=W)
    chkb115.grid(row=15, column=1)

    chkb116 = Checkbutton(fr_rolagemTurma, text="1.16 - Realizam o que é proposto com atenção e capricho", width=400, anchor=W)
    chkb116.grid(row=16, column=1)

    chkb117 = Checkbutton(fr_rolagemTurma, text="1.17 - Exceto aluno(s) aqui citado(s), que demonstra(m) desinteresse, desânimo em desenvolver as atividades rotineiras e aparenta não ter acompanhamento familiar, apresentando assim um grau na dificuldade de execução", width=400, anchor=W)
    chkb117.grid(row=17, column=1)

    chkb118 = Checkbutton(fr_rolagemTurma, text="1.18 - A turma gosta de participar das atividades pedagógicas e recreativas como, recontar histórias, roda de conversas ou até mesmo discutir um assunto, dramatização, dançar, cantar", width=400, anchor=W)
    chkb118.grid(row=18, column=1)

    chkb119 = Checkbutton(fr_rolagemTurma, text="1.19 - Turma bastante ativa e enérgica. Com exceção do(a) aluno(a) aqui citado(a), que tem sido incentivada a interagir com o grupo", width=400, anchor=W)
    chkb119.grid(row=19, column=1)

    chkb120 = Checkbutton(fr_rolagemTurma, text="1.20 - A classe tem interesse por jogos como jogo de damas, dominós, bingos de sons e letras, caça rimas e caça palavras, dado sonoro enfim jogos variados", width=400, anchor=W)
    chkb120.grid(row=20, column=1)

    chkb121 = Checkbutton(fr_rolagemTurma, text="1.21 - A maioria compreende e obedece as normas estabelecidas, exigindo dos seus colegas o cumprimento das mesmas", width=400, anchor=W)
    chkb121.grid(row=21, column=1)

    chkb122 = Checkbutton(fr_rolagemTurma, text="1.22 - Há aqueles que por momentos desrespeitam normas", width=400, anchor=W)
    chkb122.grid(row=22, column=1)

    chkb123 = Checkbutton(fr_rolagemTurma, text="1.23 - A turma conversa muito, umas com tons altos e outros baixos, expressando seus sentimentos, desejos e insatisfações. Mas quando me ponho em silêncio e de pé olhando bem para eles, logos eles observam e moderam sua voz", width=400, anchor=W)
    chkb123.grid(row=23, column=1)

    chkb124 = Checkbutton(fr_rolagemTurma, text="1.24 - A maioria das famílias dos alunos participam ativamente", width=400, anchor=W)
    chkb124.grid(row=24, column=1)

    chkb125 = Checkbutton(fr_rolagemTurma, text="1.25 - As famílias deixam a desejar nas reuniões realizadas pela escola no decorrer do ano", width=400, anchor=W)
    chkb125.grid(row=25, column=1)

    chkb126 = Checkbutton(fr_rolagemTurma, text="1.26 - Alguns familiares não costumam buscar informações e esclarecer dúvidas com a professora sempre que necessário", width=400, anchor=W)
    chkb126.grid(row=26, column=1)

    chkb127 = Checkbutton(fr_rolagemTurma, text="1.27 - No decorrer do ano os laços afetivos foram fortalecidos entre alguns alunos", width=400, anchor=W)
    chkb127.grid(row=27, column=1)

    chkb128 = Checkbutton(fr_rolagemTurma, text="1.28 - A relação entre professor e aluno é muito boa", width=400, anchor=W)
    chkb128.grid(row=28, column=1)

    chkb129 = Checkbutton(fr_rolagemTurma, text="1.29 - Em questão da aprendizagem, os alunos apresentam um bom rendimento no decorrer do ano, com exceções de (aluno(s) aqui citado(s)), que mostram alguma dificuldade cognitiva, seja na leitura e ou escrita, cálculos ou interpretação textual, que sugere-se uma avaliação", width=400, anchor=W)
    chkb129.grid(row=28, column=1)

    chkb130 = Checkbutton(fr_rolagemTurma, text="1.30 - É visível o interesse da turma, que demonstra CRIATIVIDADE EMPENHO", width=400, anchor=W)
    chkb130.grid(row=30, column=1)

    ### page2 ###
    pageTurma2 = ttk.Frame(nb2)
    nb2.add(pageTurma2, text="Aluno(s) Citado(s) no Item: 1.17:")

    perguntaTurma2 = Label(pageTurma2, text="Aluno(s) Citado(s) no Item 1.17:", font="Arial 11 bold", foreground='blue')
    perguntaTurma2.place(x=7, y=8)

    ### criando frame page 2 ###
    fr_rolagem5Turma = Frame(pageTurma2, borderwidth=1, relief="solid")
    fr_rolagem5Turma.place(x=7, y=30, width=1035, height=355)

    ### criando o canvas ###
    canvasTurma5 = Canvas(pageTurma2)
    canvasTurma5.place(x=8, y=31, width=1000, height=333)

    ### criando a barra de rolagem ###
    barra_de_rolagem4 = ttk.Scrollbar(fr_rolagem5Turma, orient=VERTICAL, command=canvasTurma5.yview)
    barra_de_rolagem4.pack(side=RIGHT, fill=Y)

    barra_de_rolagem5 = ttk.Scrollbar(fr_rolagem5Turma, orient=HORIZONTAL, command=canvasTurma5.xview)
    barra_de_rolagem5.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasTurma5.configure(yscrollcommand=barra_de_rolagem4.set)
    canvasTurma5.bind('<Configure>', lambda e: canvasTurma5.configure(scrollregion=canvasTurma5.bbox("all")))

    canvasTurma5.configure(xscrollcommand=barra_de_rolagem5.set)
    canvasTurma5.bind('<Configure>', lambda e: canvasTurma5.configure(scrollregion=canvasTurma5.bbox("all")))

    fr_rolagemTurma5 = Frame(canvasTurma5)

    canvasTurma5.create_window((0, 0), window=fr_rolagemTurma5, anchor="nw")
    #############

    ### page3 ###
    pageTurma3 = ttk.Frame(nb2)
    nb2.add(pageTurma3, text="Aluno(s) Citado(s) no Item: 1.19:")

    perguntaTurma3 = Label(pageTurma3, text="Aluno(s) Citado(s) no Item 1.19:", font="Arial 11 bold", foreground='red')
    perguntaTurma3.place(x=7, y=8)

    ### criando frame page 3 ###
    fr_rolagem6Turma = Frame(pageTurma3, borderwidth=1, relief="solid")
    fr_rolagem6Turma.place(x=7, y=30, width=1035, height=355)

    ### criando o canvas ###
    canvas6Turma = Canvas(pageTurma3)
    canvas6Turma.place(x=8, y=31, width=1000, height=333)

    ### criando a barra de rolagem ###
    barra_de_rolagem6 = ttk.Scrollbar(fr_rolagem6Turma, orient=VERTICAL, command=canvas6Turma.yview)
    barra_de_rolagem6.pack(side=RIGHT, fill=Y)

    barra_de_rolagem7 = ttk.Scrollbar(fr_rolagem6Turma, orient=HORIZONTAL, command=canvas6Turma.xview)
    barra_de_rolagem7.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvas6Turma.configure(yscrollcommand=barra_de_rolagem6.set)
    canvas6Turma.bind('<Configure>', lambda e: canvas6Turma.configure(scrollregion=canvas6Turma.bbox("all")))

    canvas6Turma.configure(xscrollcommand=barra_de_rolagem7.set)
    canvas6Turma.bind('<Configure>', lambda e: canvas6Turma.configure(scrollregion=canvas6Turma.bbox("all")))

    fr_rolagem6 = Frame(canvas6Turma)

    canvas6Turma.create_window((0, 0), window=fr_rolagem6, anchor="nw")
    #############

    ### page4 ###
    pageTurma4 = ttk.Frame(nb2)
    nb2.add(pageTurma4, text="Aluno(s) Citado(s) no item 1.29")

    perguntaTurma4 = Label(pageTurma4, text="Aluno(s) Citado(s) no Item 1.29:", font="Arial 11 bold", foreground='green')
    perguntaTurma4.place(x=7, y=8)

    ### criando frame page 3 ###
    fr_rolagem7 = Frame(pageTurma4, borderwidth=1, relief="solid")
    fr_rolagem7.place(x=7, y=30, width=1035, height=355)

    ### criando o canvas ###
    canvas7 = Canvas(pageTurma4)
    canvas7.place(x=8, y=31, width=1000, height=333)

    ### criando a barra de rolagem ###
    barra_de_rolagem8 = ttk.Scrollbar(fr_rolagem7, orient=VERTICAL, command=canvas7.yview)
    barra_de_rolagem8.pack(side=RIGHT, fill=Y)

    barra_de_rolagem9 = ttk.Scrollbar(fr_rolagem7, orient=HORIZONTAL, command=canvas7.xview)
    barra_de_rolagem9.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvas7.configure(yscrollcommand=barra_de_rolagem8.set)
    canvas7.bind('<Configure>', lambda e: canvas7.configure(scrollregion=canvas7.bbox("all")))

    canvas7.configure(xscrollcommand=barra_de_rolagem9.set)
    canvas7.bind('<Configure>', lambda e: canvas7.configure(scrollregion=canvas7.bbox("all")))

    fr_rolagem7 = Frame(canvas7)

    canvas7.create_window((0, 0), window=fr_rolagem7, anchor="nw")
    #############

    ### page5 ###
    page5 = ttk.Frame(nb2)
    nb2.add(page5, text="Observações Adicionais")

    perguntapg5 = Label(page5, text= "Observações Adicionais:", font="Arial 11 bold")
    perguntapg5.place(x=20, y=10)

    respostaText1pg4 = Text(page5, width=129, height=22)
    respostaText1pg4.place(x=20, y=40)
    #############



def abrirIndividual():
    novoTrabalho2 = Toplevel()
    novoTrabalho2.geometry('1090x620+260+70')
    novoTrabalho2.resizable(False,False)
    novoTrabalho2.title('Inventário Individual de Aluno')
    novoTrabalho2.configure(bg='light gray')
    novoTrabalho2.transient(trabalho)
    novoTrabalho2.focus_force()
    novoTrabalho2.grab_set()

    ### itens novo trabalho 9 ###
    CodigoLbl = Label(novoTrabalho2, text='Código', font="Arial 9 bold", bg='light grey', )
    CodigoLbl.place(x=10, y=30)

    AlunoLbl = Label(novoTrabalho2, text='Aluno', bg='light grey')
    AlunoLbl.place(x=70, y=30)

    SerieLbl = Label(novoTrabalho2, text='Série', bg='light grey')
    SerieLbl.place(x=410, y=30)

    TurmaLbl = Label(novoTrabalho2, text='Turma', bg='light grey')
    TurmaLbl.place(x=590, y=30)

    ProfessorLbl = Label(novoTrabalho2, text='Professor(a)', bg='light grey')
    ProfessorLbl.place(x=655, y=30)

    CodigoIndividual = Text(novoTrabalho2, width=6, height=1)
    CodigoIndividual.place(x=10, y=50)

    AlunoIndividualAuxiliar = tkinter.StringVar()
    AlunoIndividual = ttk.Combobox(novoTrabalho2, width=52, height=1, textvariable=AlunoIndividualAuxiliar)
    AlunoIndividual.place(x=70, y=50)

    SerieIndividualAuxiliar = tkinter.StringVar()
    SerieIndividual = ttk.Combobox(novoTrabalho2, width=25, height=1, textvariable=SerieIndividualAuxiliar)
    SerieIndividual.place(x=410, y=50)

    TurmaIndividualAuxiliar = tkinter.StringVar()
    TurmaIndividual = ttk.Combobox(novoTrabalho2, width=6, height=1, textvariable=TurmaIndividualAuxiliar)
    TurmaIndividual.place(x=590, y=50)

    ProfessorIndividualAuxiliar = tkinter.StringVar()
    ProfessorIndividual = ttk.Combobox(novoTrabalho2, width=43, height=1, textvariable=ProfessorIndividualAuxiliar)
    ProfessorIndividual.place(x=655, y=50)

    AlunoIndividual = Label(novoTrabalho2, image=imgFoto_Aluno)
    AlunoIndividual.place(x=950, y=30)

    ### itens novo trabalho 1 ###
    ### criando frame ###
    fr_rolagemINDIVIDUAL = Frame(novoTrabalho2, borderwidth=1, relief="solid")
    fr_rolagemINDIVIDUAL.place(x=7, y=80, width=930, height=75)

    ### criando o canvas ###
    canvasINDIVIDUAL = Canvas(novoTrabalho2)
    canvasINDIVIDUAL.place(x=8, y=81, width=910, height=73)

    ### criando a barra de rolagem ###
    barra_de_rolagemINDIVIDUAL = ttk.Scrollbar(fr_rolagemINDIVIDUAL, orient=VERTICAL, command=canvasINDIVIDUAL.yview)
    barra_de_rolagemINDIVIDUAL.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasINDIVIDUAL.configure(yscrollcommand=barra_de_rolagemINDIVIDUAL.set)
    canvasINDIVIDUAL.bind('<Configure>', lambda e: canvasINDIVIDUAL.configure(scrollregion=canvasINDIVIDUAL.bbox("all")))

    fr_rolagemINDIVIDUAL = Frame(canvasINDIVIDUAL)

    canvasINDIVIDUAL.create_window((0, 0), window=fr_rolagemINDIVIDUAL, anchor="nw")


    ### multipage ###
    rows = 0
    while rows < 50:
        novoTrabalho2.rowconfigure(rows, weight=1)
        novoTrabalho2.columnconfigure(rows, weight=1)
        rows += 1
    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nb1 = ttk.Notebook(novoTrabalho2)
    nb1.grid(row=15, column=1, columnspan=48, rowspan=40, sticky="NESW")

    page1 = ttk.Frame(nb1)
    nb1.add(page1, text="1.1 - Habilidades e Competências Possuídas pelo(a) Aluno")

    page2 = ttk.Frame(nb1)
    nb1.add(page2, text="1.2 - Queixa Escolar")

    page3 = ttk.Frame(nb1)
    nb1.add(page3, text="1.3 - Registro de Encaminhamento Multidiciplinares")

    page4 = ttk.Frame(nb1)
    nb1.add(page4, text="1.4 - Estratégias Utilizadas até o Momento")

    ### criando frame ###
    fr_rolagem2 = Frame(page1, borderwidth=1, relief="solid")
    fr_rolagem2.place(x=7, y=50, width=480, height=275)

    ### criando o canvas ###
    canvas2 = Canvas(page1)
    canvas2.place(x=8, y=51, width=450, height=273)

    ### criando a barra de rolagem ###
    barra_de_rolagem = ttk.Scrollbar(fr_rolagem2, orient=VERTICAL, command=canvas2.yview)
    barra_de_rolagem.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvas2.configure(yscrollcommand=barra_de_rolagem.set)
    canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))

    fr_rolagem2 = Frame(canvas2)

    canvas2.create_window((0, 0), window=fr_rolagem2, anchor="nw")

    ### criando a pergunta ###
    pergunda1 = Label(page1, text="1.1 - Habilidades e Competências Possuídas pelo(a) Aluno(a):", font="Arial 10 bold", width=50, anchor=W)
    pergunda1.place(x=5, y=15)

    ### criando os checkButtons ###
    cb101 = Checkbutton(fr_rolagem2, text="Aprender a Aprender", width=200, anchor=W)
    cb101.grid(row=1, column=1)

    cb102 = Checkbutton(fr_rolagem2, text="Argumentações", width=200, anchor=W)
    cb102.grid(row=2, column=1)

    cb103 = Checkbutton(fr_rolagem2, text="Autoconhecimento", width=200, anchor=W)
    cb103.grid(row=3, column=1)

    cb104 = Checkbutton(fr_rolagem2, text="Autocuidado", width=200, anchor=W)
    cb104.grid(row=4, column=1)

    cb105 = Checkbutton(fr_rolagem2, text="Autogestão", width=200, anchor=W)
    cb105.grid(row=5, column=1)

    cb106 = Checkbutton(fr_rolagem2, text="Autonomia", width=200, anchor=W)
    cb106.grid(row=6, column=1)

    cb107 = Checkbutton(fr_rolagem2, text="Busca de Precisão", width=200, anchor=W)
    cb107.grid(row=7, column=1)

    cb108 = Checkbutton(fr_rolagem2, text="Cidadania Global", width=200, anchor=W)
    cb108.grid(row=8, column=1)

    cb109 = Checkbutton(fr_rolagem2, text="Comunicação", width=200, anchor=W)
    cb109.grid(row=9, column=1)

    cb110 = Checkbutton(fr_rolagem2, text="Conhecimento", width=200, anchor=W)
    cb110.grid(row=10, column=1)

    cb111 = Checkbutton(fr_rolagem2, text="Cooperação", width=200, anchor=W)
    cb111.grid(row=11, column=1)

    cb112 = Checkbutton(fr_rolagem2, text="Cultura Digital", width=200, anchor=W)
    cb112.grid(row=12, column=1)

    cb113 = Checkbutton(fr_rolagem2, text="Empatia", width=200, anchor=W)
    cb113.grid(row=13, column=1)

    cb114 = Checkbutton(fr_rolagem2, text="Empreendimento", width=200, anchor=W)
    cb114.grid(row=14, column=1)

    cb115 = Checkbutton(fr_rolagem2, text="Escuta Empática", width=200, anchor=W)
    cb115.grid(row=15, column=1)

    ############################################

    cb116 = Checkbutton(fr_rolagem2, text="Flexibilidade de Pensamento", width=200, anchor=W)
    cb116.grid(row=16, column=1)

    cb117 = Checkbutton(fr_rolagem2, text="Gerenciamento das Impusividades", width=200, anchor=W)
    cb117.grid(row=17, column=1)

    cb118 = Checkbutton(fr_rolagem2, text="Inteeligência Emocional", width=200, anchor=W)
    cb118.grid(row=18, column=1)

    cb119 = Checkbutton(fr_rolagem2, text="Liderança", width=200, anchor=W)
    cb119.grid(row=19, column=1)

    cb120 = Checkbutton(fr_rolagem2, text="Pensamento Científico", width=200, anchor=W)
    cb120.grid(row=20, column=1)

    cb121 = Checkbutton(fr_rolagem2, text="Pensamento Criativo", width=200, anchor=W)
    cb121.grid(row=21, column=1)

    cb122 = Checkbutton(fr_rolagem2, text="Pensamento Crítico", width=200, anchor=W)
    cb122.grid(row=22, column=1)

    ### 1.2 ###
    pergunta2 = Label(page2, text="1.2 - Queixa Escolar:",
                      font="Arial 10 bold", width=50, anchor=W)
    pergunta2.place(x=5, y=15)

    resposta2 = Text(page2, width=132, height=20)
    resposta2.place(x=7, y=50)

    ### 1.3 ###
    pergunta3 = Label(page3, text="1.3 - Registro de Encaminhamento Multidiciplinares:", font="Arial 10 bold", width=50, anchor=W)
    pergunta3.place(x=5, y=15)

    resposta3 = Text(page3, width=132, height=20)
    resposta3.place(x=7, y=50)

    ### 1.4 ###
    pergunta4 = Label(page4, text="1.4 - Estratégias Utilizadas até o Momento:", font="Arial 10 bold", width=50, anchor=W)
    pergunta4.place(x=5, y=15)

    resposta4 = Text(page4, width=132, height=20)
    resposta4.place(x=7, y=50)


def abrirPEI():
    novoTrabalhoPEI = Toplevel()
    novoTrabalhoPEI.geometry('1090x620+260+70')
    novoTrabalhoPEI.resizable(False,False)
    novoTrabalhoPEI.title('PEI - Programa Educacional Individualizado')
    novoTrabalhoPEI.configure(bg='light gray')
    novoTrabalhoPEI.transient(trabalho)
    novoTrabalhoPEI.focus_force()
    novoTrabalhoPEI.grab_set()

    FiltroPEI = Button(novoTrabalhoPEI, bg="grey")
    FiltroPEI.place(x=20, y=10, width=20, height=20)

    NovoPEI = Button(novoTrabalhoPEI, bg="grey")
    NovoPEI.place(x=50, y=10, width=20, height=20)

    LimparPEI = Button(novoTrabalhoPEI, bg="grey")
    LimparPEI.place(x=80, y=10, width=20, height=20)

    ExcluirPEI = Button(novoTrabalhoPEI, bg="grey")
    ExcluirPEI.place(x=110, y=10, width=20, height=20)

    ResultadosPEI = Button(novoTrabalhoPEI, bg="grey")
    ResultadosPEI.place(x=140, y=10, width=20, height=20)

    AvancarPEI = Button(novoTrabalhoPEI, bg="grey")
    AvancarPEI.place(x=170, y=10, width=20, height=20)

    TodosPEI = Button(novoTrabalhoPEI, bg="grey")
    TodosPEI.place(x=200, y=10, width=20, height=20)

    IndividualPEI = Button(novoTrabalhoPEI, bg="grey")
    IndividualPEI.place(x=230, y=10, width=20, height=20)

    HomePEI = Button(novoTrabalhoPEI, bg="grey")
    HomePEI.place(x=260, y=10, width=20, height=20)

    InclusaoPEI = Button(novoTrabalhoPEI, bg="grey")
    InclusaoPEI.place(x=290, y=10, width=20, height=20)

    CodigoPEI1 = Text(novoTrabalhoPEI, width=5, height=1)
    CodigoPEI1.place(x=20, y=72)

    AlunoPEI1 = tkinter.StringVar()
    AlunoPEI1cbbx = ttk.Combobox(novoTrabalhoPEI, width=40, height=1, textvariable=AlunoPEI1)
    AlunoPEI1cbbx.place(x=70, y=72)

    Ativo_PEI = Checkbutton(novoTrabalhoPEI, bg="light grey")
    Ativo_PEI.place(x=335, y=72)

    VerificaPEI = Button(novoTrabalhoPEI, text='Verifica', font='negrito 8', bg="Red")
    VerificaPEI.place(x=360, y=72, width=50, height=20)

    MatriculaPEI1 = Text(novoTrabalhoPEI, bg='light yellow', width=7, height=1)
    MatriculaPEI1.place(x=415, y=72)

    seriePEI1 = Text(novoTrabalhoPEI, width=26, height=1)
    seriePEI1.place(x=480, y=72)

    TurmaPEI1 = Text(novoTrabalhoPEI, width=5, height=1)
    TurmaPEI1.place(x=695, y=72)

    NascimentoPEI1 = Text(novoTrabalhoPEI, width=10, height=1)
    NascimentoPEI1.place(x=742, y=72)

    BimestrePEI1 = tkinter.StringVar()
    BimestrePEI1cbbx = ttk.Combobox(novoTrabalhoPEI, width=15, height=1, textvariable=BimestrePEI1)
    BimestrePEI1cbbx.place(x=830, y=72)

    Ano_LetivoPEI1 = Text(novoTrabalhoPEI, width=4, height=1)
    Ano_LetivoPEI1.place(x=945, y=72)

    Foto_Aluno_PEI = Label(novoTrabalhoPEI, image=imgFoto_Aluno)
    Foto_Aluno_PEI.place(x=987, y=80)

    Nome_MaePEI1 = Text(novoTrabalhoPEI, width=45, height=1)
    Nome_MaePEI1.place(x=20, y=118)

    EnderecoPEI1 = Text(novoTrabalhoPEI, width=40, height=1)
    EnderecoPEI1.place(x=390, y=118)

    Unidade_EscolarPEI1 = Text(novoTrabalhoPEI, width=31, height=1)
    Unidade_EscolarPEI1.place(x=720, y=118)

    CID_PEI = Checkbutton(novoTrabalhoPEI, bg="light grey", text='CID 11', font="Negrito 10 bold", foreground='blue')
    CID_PEI.place(x=20, y=165)

    Codigo_CID_PEI1 = tkinter.StringVar()
    Codigo_CID_PEI1cbbx = ttk.Combobox(novoTrabalhoPEI, width=15, height=1, textvariable=Codigo_CID_PEI1)
    Codigo_CID_PEI1cbbx.place(x=90, y=165)

    DiagnosticoPEI1 = Text(novoTrabalhoPEI, bg='light yellow', width=40, height=1)
    DiagnosticoPEI1.place(x=210, y=165)

    DiagnosticoButaoPEI1 = Button(novoTrabalhoPEI, bg="light grey", image=imgPlusPEI)
    DiagnosticoButaoPEI1.place(x=530, y=165, width=20, height=20)

    Data_LaudoPEI1 = Text(novoTrabalhoPEI, width=10, height=1)
    Data_LaudoPEI1.place(x=555, y=165)

    MedicoPEI1 = Text(novoTrabalhoPEI, width=19, height=1)
    MedicoPEI1.place(x=645, y=165)

    CRMPEI1 = Text(novoTrabalhoPEI, width=9, height=1)
    CRMPEI1.place(x=805, y=165)

    Data_ProtocoloPEI1 = Text(novoTrabalhoPEI, width=10, height=1)
    Data_ProtocoloPEI1.place(x=885, y=165)

    ### PEI LABELS ###
    codigoPEI_LBL = Label(novoTrabalhoPEI, text="Código", font="Negrito 7 bold", bg='light gray')
    codigoPEI_LBL.place(x=20, y=51)

    AlunoPEI_LBL = Label(novoTrabalhoPEI, text="Aluno", bg='light gray')
    AlunoPEI_LBL.place(x=70, y=51)

    AtivoPEI_LBL = Label(novoTrabalhoPEI, text="Ativo", font="Negrito 8 bold", bg='light gray')
    AtivoPEI_LBL.place(x=329, y=51)

    MatriculaPEI_LBL = Label(novoTrabalhoPEI, text="Matricula", bg='light gray')
    MatriculaPEI_LBL.place(x=415, y=51)

    SeriePEI_LBL = Label(novoTrabalhoPEI, text="Série", bg='light gray')
    SeriePEI_LBL.place(x=480, y=51)

    TurmaPEI_LBL = Label(novoTrabalhoPEI, text="Turma", bg='light gray')
    TurmaPEI_LBL.place(x=695, y=51)

    NascimentoPEI_LBL = Label(novoTrabalhoPEI, text="Nascimento", bg='light gray')
    NascimentoPEI_LBL.place(x=742, y=51)

    BimestrePEI_LBL = Label(novoTrabalhoPEI, text="Bimestre", bg='light gray')
    BimestrePEI_LBL.place(x=830, y=51)

    BimestrePEI_LBL = Label(novoTrabalhoPEI, text="Ano", bg='light gray')
    BimestrePEI_LBL.place(x=945, y=51)

    Nome_MaePEI_LBL = Label(novoTrabalhoPEI, text="Nome da Mãe", bg='light gray')
    Nome_MaePEI_LBL.place(x=20, y=97)

    EnderecoPEI_LBL = Label(novoTrabalhoPEI, text="Endereço", bg='light gray')
    EnderecoPEI_LBL.place(x=385, y=97)

    Unidade_EscolarPEI_LBL = Label(novoTrabalhoPEI, text="Unidade Escolar", bg='light gray')
    Unidade_EscolarPEI_LBL.place(x=717, y=97)

    CIDPEI_LBL = Label(novoTrabalhoPEI, text="Seleção de CID", font="Negrito 7 bold", bg='light gray', foreground='red')
    CIDPEI_LBL.place(x=15, y=144)

    Codigo_CIDPEI_LBL = Label(novoTrabalhoPEI, text="Código do CID", font="Negrito 8 bold", bg='light gray')
    Codigo_CIDPEI_LBL.place(x=90, y=144)

    DiagnosticoPEI_LBL = Label(novoTrabalhoPEI, text="Diagnóstico", bg='light gray')
    DiagnosticoPEI_LBL.place(x=210, y=144)

    DataLaudoPEI_LBL = Label(novoTrabalhoPEI, text="Data do Laudo", bg='light gray')
    DataLaudoPEI_LBL.place(x=555, y=144)

    MedicoPEI_LBL = Label(novoTrabalhoPEI, text="Médico", bg='light gray')
    MedicoPEI_LBL.place(x=645, y=144)

    CrmPEI_LBL = Label(novoTrabalhoPEI, text="CRM", bg='light gray')
    CrmPEI_LBL.place(x=805, y=144)

    DataProtocoloPEI_LBL = Label(novoTrabalhoPEI, text="Data do Protocolo", bg='light gray')
    DataProtocoloPEI_LBL.place(x=875, y=144)

    ### Barra de Progresso ###
    BarraDeProgressoPEI = ttk.Progressbar(novoTrabalhoPEI, orient=HORIZONTAL, length=1070, mode='determinate')
    BarraDeProgressoPEI.place(x=10, y=210)

    def step():
        BarraDeProgressoPEI['value'] += 1

    def reset():
        BarraDeProgressoPEI['value'] = 0

    ### multipage ###
    rows = 0
    while rows < 50:
        novoTrabalhoPEI.rowconfigure(rows, weight=1)
        novoTrabalhoPEI.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPEI = ttk.Notebook(novoTrabalhoPEI)
    nbPEI.grid(row=23, column=1, columnspan=48, rowspan=29, sticky="NESW")

    ### page1 ###
    page1PEI = ttk.Frame(nbPEI)
    nbPEI.add(page1PEI, text="Visualização")

    ### criando frame ###
    fr_rolagemPEI = Frame(page1PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI.place(x=2, y=10, width=1045, height=278)

    ### criando o canvas ###
    canvasPEI = Canvas(page1PEI)
    canvasPEI.place(x=3, y=20, width=1025, height=265)

    ### criando a barra de rolagem ###
    barra_de_rolagemPEI = ttk.Scrollbar(fr_rolagemPEI, orient=VERTICAL, command=canvasPEI.yview)
    barra_de_rolagemPEI.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI.configure(yscrollcommand=barra_de_rolagemPEI.set)
    canvasPEI.bind('<Configure>', lambda e: canvasPEI.configure(scrollregion=canvasPEI.bbox("all")))

    fr_rolagemPEI = Frame(canvasPEI)

    canvasPEI.create_window((0, 0), window=fr_rolagemPEI, anchor="nw")

    BotaoProgressoPEI1 = Button(page1PEI, text="Próximo", command=step)
    BotaoProgressoPEI1.place(x=1000, y=300)
    ###########

    ### page2 ###
    page2PEI = ttk.Frame(nbPEI)
    nbPEI.add(page2PEI, text="3 - Resumo de Escolaridade")

    identificacao = Label(page2PEI, text="BREVE DESCRIÇÃO DE ESCOLARIDADE DO ALUNO", font="Negrito 10 bold", foreground='blue')
    identificacao.place(x=10, y=10)

    anexoLbl = Label(page2PEI, text="Anexo de Laudo/Relatório Médico:", font="Arial 8")
    anexoLbl.place(x=410, y=10)

    anexoTXT = Text(page2PEI, width=40, height=1)
    anexoTXT.place(x=580, y=10)

    AnexarPEI_LBL = Button(page2PEI, text="ANEXAR", font="Negrito 8 bold", bg='cyan')
    AnexarPEI_LBL.place(x=905, y=8)

    AbrePEI_LBL = Button(page2PEI, text="ABRE", font="Negrito 8 bold", bg='chartreuse')
    AbrePEI_LBL.place(x=960, y=8)

    ResumoTXT = Text(page2PEI, width=129, height=18)
    ResumoTXT.place(x=10, y=40)

    ### page3 ###
    page3PEI = ttk.Frame(nbPEI)
    nbPEI.add(page3PEI, text="4 - Funcionalidades")

    identificacao = Label(page3PEI, text="DESTRUIÇÃO DAS FUNCIONALIDADES DO ALUNO", font="Negrito 10 bold", foreground='blue')
    identificacao.place(x=10, y=10)

    DestruicaoTXT = Text(page3PEI, width=129, height=18)
    DestruicaoTXT.place(x=10, y=40)

    ### page4 ###
    page4PEI = ttk.Frame(nbPEI)
    nbPEI.add(page4PEI, text="5 - Habilidades Escolares")

    ### multipage ###
    rows = 0
    while rows < 50:
        page4PEI.rowconfigure(rows, weight=1)
        page4PEI.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPEIpg4 = ttk.Notebook(page4PEI)
    nbPEIpg4.grid(row=1, column=1, columnspan=48, rowspan=48, sticky="NESW")

    ### page5.01 ###
    page501PEI = ttk.Frame(nbPEIpg4)
    nbPEIpg4.add(page501PEI, text="5.1 - Comunicação Oral")

    Inventario = Label(page501PEI, text="5 - INVENTÁRIO DAS HABILIDADES ESCOLARES", font="Negrito 10 bold", foreground='blue')
    Inventario.place(x=10, y=5)

    Comunicacao = Label(page501PEI, text="5.1 - Comunicação Oral", font="Negrito 10 bold")
    Comunicacao.place(x=20, y=25)

    cbComunicacao51 = Checkbutton(page501PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao51.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI51 = Frame(page501PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI51.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI51 = Canvas(page501PEI)
    canvasPEI51.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem51 = ttk.Scrollbar(fr_rolagemPEI51, orient=VERTICAL, command=canvasPEI51.yview)
    barra_de_rolagem51.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI51.configure(yscrollcommand=barra_de_rolagem51.set)
    canvasPEI51.bind('<Configure>', lambda e: canvasPEI51.configure(scrollregion=canvasPEI51.bbox("all")))

    fr_rolagemPEI51 = Frame(canvasPEI51)

    canvasPEI51.create_window((0, 0), window=fr_rolagemPEI51, anchor="nw")

    ### coisas ###
    chkbPEI510 = Checkbutton(fr_rolagemPEI51, text="5.1.0 - Sem Habilidades de Comunicação Oral", width=400, anchor=W)
    chkbPEI510.grid(row=1, column=1)

    chkbPEI511 = Checkbutton(fr_rolagemPEI51, text="5.1.1 - Relata acontecimentos simples de modo compreensível",
                             width=400, anchor=W)
    chkbPEI511.grid(row=2, column=1)

    chkbPEI512 = Checkbutton(fr_rolagemPEI51, text="5.1.2 - Lembra-se de dar recados após, aproximadamente,10 minutos",
                             width=400, anchor=W)
    chkbPEI512.grid(row=3, column=1)

    chkbPEI513 = Checkbutton(fr_rolagemPEI51,
                             text="5.1.3 - Comunica-se com outras pessoas usando outro tipo de linguagem (gestos, comunicação alternativa) que não a oral",
                             width=400, anchor=W)
    chkbPEI513.grid(row=4, column=1)

    chkbPEI514 = Checkbutton(fr_rolagemPEI51, text="5.1.4 - Utiliza a linguagem oral para se comunicar", width=400,
                             anchor=W)
    chkbPEI514.grid(row=5, column=1)
    ##########################################################################################

    ### page5.02 ###
    page502PEI = ttk.Frame(nbPEIpg4)
    nbPEIpg4.add(page502PEI, text="5.2 - Comunicação Oral")

    Inventario = Label(page502PEI, text="5 - INVENTÁRIO DAS HABILIDADES ESCOLARES", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    Leitura = Label(page502PEI, text="5.2 - Leitura e Escrita", font="Negrito 10 bold")
    Leitura.place(x=20, y=25)

    cbLeitura52 = Checkbutton(page502PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbLeitura52.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI52 = Frame(page502PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI52.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    page502PEI = Canvas(page502PEI)
    page502PEI.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem52 = ttk.Scrollbar(fr_rolagemPEI52, orient=VERTICAL, command=page502PEI.yview)
    barra_de_rolagem52.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    page502PEI.configure(yscrollcommand=barra_de_rolagem52.set)
    page502PEI.bind('<Configure>', lambda e: page502PEI.configure(scrollregion=page502PEI.bbox("all")))

    fr_rolagemPEI52 = Frame(page502PEI)

    page502PEI.create_window((0, 0), window=fr_rolagemPEI52, anchor="nw")

    ### coisas ###
    chkbPEI520 = Checkbutton(fr_rolagemPEI52, text="5.2.0 - Sem Habilidades de Leitura e Escrita", width=400, anchor=W)
    chkbPEI520.grid(row=1, column=1)

    chkbPEI521 = Checkbutton(fr_rolagemPEI52, text="5.2.1 - Conhece as letras do alfabeto", width=400, anchor=W)
    chkbPEI521.grid(row=2, column=1)

    chkbPEI522 = Checkbutton(fr_rolagemPEI52, text="5.2.2 - Reconhece a diferença entre letras e números", width=400,
                             anchor=W)
    chkbPEI522.grid(row=3, column=1)

    chkbPEI523 = Checkbutton(fr_rolagemPEI52, text="5.2.3 - Domina sílabas simples", width=400, anchor=W)
    chkbPEI523.grid(row=4, column=1)

    chkbPEI524 = Checkbutton(fr_rolagemPEI52, text="5.2.4 - Ouve histórias com atenção", width=400, anchor=W)
    chkbPEI524.grid(row=5, column=1)

    chkbPEI525 = Checkbutton(fr_rolagemPEI52, text="5.2.5 - Consegue compreender histórias e reproduzilas", width=400, anchor=W)
    chkbPEI525.grid(row=6, column=1)

    chkbPEI526 = Checkbutton(fr_rolagemPEI52, text="5.2.6 - Participa de jogos, atendendo às regras", width=400, anchor=W)
    chkbPEI526.grid(row=7, column=1)

    chkbPEI527 = Checkbutton(fr_rolagemPEI52, text="5.2.7 - Utiliza vocabulário adequado para faixa etária", width=400, anchor=W)
    chkbPEI527.grid(row=8, column=1)

    chkbPEI528 = Checkbutton(fr_rolagemPEI52, text="5.2.8 - Sabe soletrar", width=400, anchor=W)
    chkbPEI528.grid(row=9, column=1)

    chkbPEI529 = Checkbutton(fr_rolagemPEI52, text="5.2.9 - Consegue escrever palavras simples", width=400, anchor=W)
    chkbPEI529.grid(row=10, column=1)

    chkbPEI5210 = Checkbutton(fr_rolagemPEI52, text="5.2.10 - É capaz de assinar seu nome", width=400, anchor=W)
    chkbPEI5210.grid(row=11, column=1)

    chkbPEI5211 = Checkbutton(fr_rolagemPEI52, text="5.2.11 - Escrve endereços (com o objetivo de saber aonde chegar)", width=400, anchor=W)
    chkbPEI5211.grid(row=12, column=1)

    chkbPEI5212 = Checkbutton(fr_rolagemPEI52, text="5.2.12 - Escreve pequenos textos e/ou bilhetes", width=400, anchor=W)
    chkbPEI5212.grid(row=13, column=1)

    chkbPEI5213 = Checkbutton(fr_rolagemPEI52, text="5.2.13 - Escreve sob ditado", width=400, anchor=W)
    chkbPEI5213.grid(row=14, column=1)

    chkbPEI5214 = Checkbutton(fr_rolagemPEI52, text="5.2.14 - Lê com compreensão pequenos textos", width=400, anchor=W)
    chkbPEI5214.grid(row=15, column=1)

    chkbPEI5215 = Checkbutton(fr_rolagemPEI52, text="5.2.15 - Lê e segue instituições impressas, por ex. em transportes públicos", width=400, anchor=W)
    chkbPEI5215.grid(row=16, column=1)

    ### page5.03 ###
    page503PEI = ttk.Frame(nbPEIpg4)
    nbPEIpg4.add(page503PEI, text="5.3 - Raciocínio Lógico")

    Inventario = Label(page503PEI, text="5 - INVENTÁRIO DAS HABILIDADES ESCOLARES", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    Raciocinio = Label(page503PEI, text="5.3 - Raciocínio Lógico", font="Negrito 10 bold")
    Raciocinio.place(x=20, y=25)

    cbRaciocinio53 = Checkbutton(page503PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbRaciocinio53.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI53 = Frame(page503PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI53.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    page503PEI = Canvas(page503PEI)
    page503PEI.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem53 = ttk.Scrollbar(fr_rolagemPEI53, orient=VERTICAL, command=page503PEI.yview)
    barra_de_rolagem53.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    page503PEI.configure(yscrollcommand=barra_de_rolagem53.set)
    page503PEI.bind('<Configure>', lambda e: page503PEI.configure(scrollregion=page503PEI.bbox("all")))

    fr_rolagemPEI53 = Frame(page503PEI)

    page503PEI.create_window((0, 0), window=fr_rolagemPEI53, anchor="nw")

    ### coisas ###
    chkbPEI530 = Checkbutton(fr_rolagemPEI53, text="5.3.0 - Sem habílidades de raciocínio lógico", width=400, anchor=W)
    chkbPEI530.grid(row=1, column=1)

    chkbPEI531 = Checkbutton(fr_rolagemPEI53, text="5.3.1 - Relaciona quantidade ao número", width=400, anchor=W)
    chkbPEI531.grid(row=2, column=1)

    chkbPEI532 = Checkbutton(fr_rolagemPEI53, text="5.3.2 - Soluciona problemas", width=400,
                             anchor=W)
    chkbPEI532.grid(row=3, column=1)

    chkbPEI533 = Checkbutton(fr_rolagemPEI53, text="5.3.3 - Reconhece os valores dos preços dos produtos", width=400, anchor=W)
    chkbPEI533.grid(row=4, column=1)

    chkbPEI534 = Checkbutton(fr_rolagemPEI53, text="5.3.4 - Identifica o valor do dinheiro", width=400, anchor=W)
    chkbPEI534.grid(row=5, column=1)

    chkbPEI535 = Checkbutton(fr_rolagemPEI53, text="5.3.5 - Diferencia notas e moedas", width=400, anchor=W)
    chkbPEI535.grid(row=6, column=1)

    chkbPEI536 = Checkbutton(fr_rolagemPEI53, text="5.3.6 - Sabe agrupar dinheiro para formar valores", width=400, anchor=W)
    chkbPEI536.grid(row=7, column=1)

    chkbPEI537 = Checkbutton(fr_rolagemPEI53, text="5.3.7 - Dá troco, quando necessário nas atividades realizadas em sala de aula", width=400, anchor=W)
    chkbPEI537.grid(row=8, column=1)

    chkbPEI538 = Checkbutton(fr_rolagemPEI53, text="5.3.8 - Possui conceitos como: cor, tamanho, dormas geométricas, posição direta e esquerda, antecessor e sucessor", width=400, anchor=W)
    chkbPEI538.grid(row=9, column=1)

    chkbPEI539 = Checkbutton(fr_rolagemPEI53, text="5.3.9 - Reconhece a relação entre número e dias do mês (localização temporal)", width=400, anchor=W)
    chkbPEI539.grid(row=10, column=1)

    chkbPEI5310 = Checkbutton(fr_rolagemPEI53, text="5.3.10 - Identifica dias da semana", width=400, anchor=W)
    chkbPEI5310.grid(row=11, column=1)

    chkbPEI5311 = Checkbutton(fr_rolagemPEI53, text="5.3.11 - Reconhece horas em relógio digital", width=400, anchor=W)
    chkbPEI5311.grid(row=12, column=1)

    chkbPEI5312 = Checkbutton(fr_rolagemPEI53, text="5.3.12 - Reconhece horas exatas (em relógio com ponteiro)", width=400, anchor=W)
    chkbPEI5312.grid(row=13, column=1)

    chkbPEI5313 = Checkbutton(fr_rolagemPEI53, text="5.3.13 - Reconhece horas não exatas (meia hora ou 7 minutos, por exemplo), em relógio digital", width=400, anchor=W)
    chkbPEI5313.grid(row=14, column=1)

    chkbPEI5314 = Checkbutton(fr_rolagemPEI53, text="5.3.14 - Reconhece horas não exatas (em relógio com ponteiros)", width=400, anchor=W)
    chkbPEI5314.grid(row=15, column=1)

    chkbPEI5315 = Checkbutton(fr_rolagemPEI53, text="5.3.15 - Associa horários aos acontecimentos", width=400, anchor=W)
    chkbPEI5315.grid(row=16, column=1)

    ### page5.04 ###
    page504PEI = ttk.Frame(nbPEIpg4)
    nbPEIpg4.add(page504PEI, text="5.4 - Informática na Escola")

    Inventario = Label(page504PEI, text="5 - INVENTÁRIO DAS HABILIDADES ESCOLARES", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    Informatica = Label(page504PEI, text="5.4 - Informática na Escola", font="Negrito 10 bold")
    Informatica.place(x=20, y=25)

    cbInformatica54 = Checkbutton(page504PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbInformatica54.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI54 = Frame(page504PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI54.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    page504PEI = Canvas(page504PEI)
    page504PEI.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem54 = ttk.Scrollbar(fr_rolagemPEI54, orient=VERTICAL, command=page504PEI.yview)
    barra_de_rolagem54.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    page504PEI.configure(yscrollcommand=barra_de_rolagem54.set)
    page504PEI.bind('<Configure>', lambda e: page504PEI.configure(scrollregion=page504PEI.bbox("all")))

    fr_rolagemPEI54 = Frame(page504PEI)

    page504PEI.create_window((0, 0), window=fr_rolagemPEI54, anchor="nw")

    ### coisas ###
    chkbPEI540 = Checkbutton(fr_rolagemPEI54, text="5.4.0 - Sem habilidades de informática na escola", width=400, anchor=W)
    chkbPEI540.grid(row=1, column=1)

    chkbPEI541 = Checkbutton(fr_rolagemPEI54, text="5.4.1 - Usa o computador comm relativa autonomia (liga, desliga, acessa arquivos e programas)", width=400, anchor=W)
    chkbPEI541.grid(row=2, column=1)

    chkbPEI542 = Checkbutton(fr_rolagemPEI54, text="5.4.2 - Sabe usar o computador e Internet quando disponibilizado na escola", width=400, anchor=W)
    chkbPEI542.grid(row=3, column=1)

    ### page5 ###
    page5PEI = ttk.Frame(nbPEI)
    nbPEI.add(page5PEI, text="6 - Habilidades Sociais")

    Inventario = Label(page5PEI, text="5 - INVENTÁRIO DAS HABILIDADES ESCOLARES", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    Raciocinio = Label(page5PEI, text="6.1 - Habilidades sociais possuídas", font="Negrito 10 bold")
    Raciocinio.place(x=20, y=25)

    cbHabilidades61 = Checkbutton(page5PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbHabilidades61.place(x=10, y=45)

    ### criando frame ###
    fr_rolagem6PEI = Frame(page5PEI, borderwidth=1, relief="solid")
    fr_rolagem6PEI.place(x=2, y=80, width=1045, height=228)

    ### criando o canvas ###
    canvas6PEI = Canvas(page5PEI)
    canvas6PEI.place(x=3, y=83, width=1025, height=223)

    ### criando a barra de rolagem ###
    barra_de_rolagem6PEI = ttk.Scrollbar(fr_rolagem6PEI, orient=VERTICAL, command=canvas6PEI.yview)
    barra_de_rolagem6PEI.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvas6PEI.configure(yscrollcommand=barra_de_rolagem6PEI.set)
    canvas6PEI.bind('<Configure>', lambda e: canvas6PEI.configure(scrollregion=canvas6PEI.bbox("all")))

    fr_rolagem6PEI = Frame(canvas6PEI)

    canvas6PEI.create_window((0, 0), window=fr_rolagem6PEI, anchor="nw")

    chkbPEI610 = Checkbutton(fr_rolagem6PEI, text="6.1.0 - Sem habilidades sociais", width=400, anchor=W)
    chkbPEI610.grid(row=1, column=1)

    chkbPEI611 = Checkbutton(fr_rolagem6PEI, text="6.1.1 - Junta-se a um grupo em brincadeiras", width=400, anchor=W)
    chkbPEI611.grid(row=2, column=1)

    chkbPEI612 = Checkbutton(fr_rolagem6PEI, text="6.1.2 - Recusa pedido de colega", width=400, anchor=W)
    chkbPEI612.grid(row=3, column=1)

    chkbPEI613 = Checkbutton(fr_rolagem6PEI, text="6.1.3 - Expressa desagrado", width=400, anchor=W)
    chkbPEI613.grid(row=4, column=1)

    chkbPEI614 = Checkbutton(fr_rolagem6PEI, text="6.1.4 - Pede ajuda ao colega em classe", width=400, anchor=W)
    chkbPEI614.grid(row=5, column=1)

    chkbPEI615 = Checkbutton(fr_rolagem6PEI, text="6.1.5 - Solicita mudança de comportamento do outro", width=400, anchor=W)
    chkbPEI615.grid(row=6, column=1)

    chkbPEI616 = Checkbutton(fr_rolagem6PEI, text="6.1.6 - Pede desculpas", width=400, anchor=W)
    chkbPEI616.grid(row=7, column=1)

    chkbPEI617 = Checkbutton(fr_rolagem6PEI, text="6.1.7 - Demonstra espírito esportivo", width=400, anchor=W)
    chkbPEI617.grid(row=8, column=1)

    chkbPEI618 = Checkbutton(fr_rolagem6PEI, text="6.1.8 - Media conflitos entre colegas", width=400, anchor=W)
    chkbPEI618.grid(row=9, column=1)

    chkbPEI619 = Checkbutton(fr_rolagem6PEI, text="6.1.9 - Negocia ou converce", width=400, anchor=W)
    chkbPEI619.grid(row=10, column=1)

    chkbPEI6110 = Checkbutton(fr_rolagem6PEI, text="6.1.10 - Ofereçe ajuda", width=400, anchor=W)
    chkbPEI6110.grid(row=11, column=1)

    chkbPEI6111 = Checkbutton(fr_rolagem6PEI, text="6.1.11 - Propõe nova brincadeira", width=400, anchor=W)
    chkbPEI6111.grid(row=12, column=1)

    chkbPEI6112 = Checkbutton(fr_rolagem6PEI, text="6.1.12 - Propõe porquê (questiona)", width=400, anchor=W)
    chkbPEI6112.grid(row=13, column=1)

    chkbPEI6113 = Checkbutton(fr_rolagem6PEI, text="6.1.13 - Responde pergunta da professora", width=400, anchor=W)
    chkbPEI6113.grid(row=14, column=1)

    chkbPEI6114 = Checkbutton(fr_rolagem6PEI, text="6.1.14 - aceita gozações", width=400, anchor=W)
    chkbPEI6114.grid(row=15, column=1)

    chkbPEI6115 = Checkbutton(fr_rolagem6PEI, text="6.1.15 - Agradece um eloguio", width=400, anchor=W)
    chkbPEI6115.grid(row=16, column=1)

    chkbPEI6116 = Checkbutton(fr_rolagem6PEI, text="6.1.16 - Resiste à pressão do grupo", width=400, anchor=W)
    chkbPEI6116.grid(row=17, column=1)

    chkbPEI6117 = Checkbutton(fr_rolagem6PEI, text="6.1.17 - Consola o colega", width=400, anchor=W)
    chkbPEI6117.grid(row=18, column=1)
    ###########

    ### page 6 ###
    page6PEI = ttk.Frame(nbPEI)
    nbPEI.add(page6PEI, text="7 - CEI (Currículo Específico Individual)")

    ### multipage ###
    rows = 0
    while rows < 50:
        page6PEI.rowconfigure(rows, weight=1)
        page6PEI.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPEIpg6 = ttk.Notebook(page6PEI)
    nbPEIpg6.grid(row=1, column=1, columnspan=48, rowspan=48, sticky="NESW")

    ### page7.01 ###
    page701PEI = ttk.Frame(nbPEIpg6)
    nbPEIpg6.add(page701PEI, text="7.1 - Instrumentos e Metodologias Necessárias ao Desenvolvimento do Aluno")

    Inventario = Label(page701PEI, text="7 - CEI (Currículo Específico Individual)", font="Negrito 10 bold", foreground='blue')
    Inventario.place(x=10, y=5)

    IMNDA = Label(page701PEI, text="7.1 - Instrumentos e Metodologias Necessárias ao Desenvolvimento do Aluno", font="Negrito 10 bold")
    IMNDA.place(x=20, y=25)

    cbComunicacao71 = Checkbutton(page701PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao71.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI71 = Frame(page701PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI71.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI71 = Canvas(page701PEI)
    canvasPEI71.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem71 = ttk.Scrollbar(fr_rolagemPEI71, orient=VERTICAL, command=canvasPEI71.yview)
    barra_de_rolagem71.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI71.configure(yscrollcommand=barra_de_rolagem71.set)
    canvasPEI71.bind('<Configure>', lambda e: canvasPEI71.configure(scrollregion=canvasPEI71.bbox("all")))

    fr_rolagemPEI71 = Frame(canvasPEI71)

    canvasPEI71.create_window((0, 0), window=fr_rolagemPEI71, anchor="nw")

    ### coisas ###
    chkbPEI710 = Checkbutton(fr_rolagemPEI71, text="7.1.0 - Nenhum instrumento pedagógico necessário ao desenvolvimento", width=400, anchor=W)
    chkbPEI710.grid(row=1, column=1)

    chkbPEI711 = Checkbutton(fr_rolagemPEI71, text="7.1.1 - Apoio pedagógco personalizado. (Art.17°)", width=400, anchor=W)
    chkbPEI711.grid(row=2, column=1)

    chkbPEI712 = Checkbutton(fr_rolagemPEI71, text="7.1.2 - Apoio individual", width=400, anchor=W)
    chkbPEI712.grid(row=3, column=1)

    chkbPEI713 = Checkbutton(fr_rolagemPEI71, text="7.1.3 - Estimulação sensorial", width=400, anchor=W)
    chkbPEI713.grid(row=4, column=1)

    chkbPEI714 = Checkbutton(fr_rolagemPEI71, text="7.1.4 - Utilização de materiais adequados", width=400, anchor=W)
    chkbPEI714.grid(row=5, column=1)

    chkbPEI715 = Checkbutton(fr_rolagemPEI71, text="7.1.5 - Compreenção, identificação e reconhecimento de vocais e consoantes e seus valores fonêmicos", width=400, anchor=W)
    chkbPEI715.grid(row=6, column=1)

    chkbPEI716 = Checkbutton(fr_rolagemPEI71, text="7.1.6 - Associação de fonemas e grafemas", width=400, anchor=W)
    chkbPEI716.grid(row=7, column=1)

    chkbPEI717 = Checkbutton(fr_rolagemPEI71, text="7.1.7 - Segmentação e reconstrução de palavras", width=400, anchor=W)
    chkbPEI717.grid(row=8, column=1)

    chkbPEI718 = Checkbutton(fr_rolagemPEI71, text="7.1.8 - Construção de acrônimos", width=400, anchor=W)
    chkbPEI718.grid(row=9, column=1)

    chkbPEI719 = Checkbutton(fr_rolagemPEI71, text="7.1.9 - Treino de rimas (aliteração e assonância)", width=400, anchor=W)
    chkbPEI719.grid(row=10, column=1)

    chkbPEI7110 = Checkbutton(fr_rolagemPEI71, text="7.1.10 - Repetição sistemática de determinados conteúdos", width=400, anchor=W)
    chkbPEI7110.grid(row=11, column=1)

    chkbPEI7111 = Checkbutton(fr_rolagemPEI71, text="7.1.11 - Treino do uso de dicionários e prontuuários", width=400, anchor=W)
    chkbPEI7111.grid(row=12, column=1)

    chkbPEI7112 = Checkbutton(fr_rolagemPEI71, text="7.1.12 - Apresentação cuidadosa do material escrito (Cabeçalhos destacados, letras claras, uso de esquemas, poucas palavras escritas)", width=400, anchor=W)
    chkbPEI7112.grid(row=13, column=1)

    chkbPEI7113 = Checkbutton(fr_rolagemPEI71, text="7.1.13 - Desenvolvimento da auto estima e da auto confiança, através de constante reforço positivo", width=400, anchor=W)
    chkbPEI7113.grid(row=14, column=1)

    chkbPEI7114 = Checkbutton(fr_rolagemPEI71, text="7.1.14 - Aprendizagem multissensorial", width=400, anchor=W)
    chkbPEI7114.grid(row=15, column=1)

    chkbPEI7115 = Checkbutton(fr_rolagemPEI71, text="7.1.15 - Altomatização de competências adiquiridas", width=400, anchor=W)
    chkbPEI7115.grid(row=16, column=1)

    ### page7.02 ###
    page702PEI = ttk.Frame(nbPEIpg6)
    nbPEIpg6.add(page702PEI, text="7.2 - Tecnologia de apoio (Art. 22°)")

    Inventario = Label(page702PEI, text="7 - CEI (Currículo Específico Individual)", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    TAart22 = Label(page702PEI, text="7.2 - Tecnologia de apoio (Art. 22°)", font="Negrito 10 bold")
    TAart22.place(x=20, y=25)

    cbComunicacao72 = Checkbutton(page702PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao72.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI72 = Frame(page702PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI72.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI72 = Canvas(page702PEI)
    canvasPEI72.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem71 = ttk.Scrollbar(fr_rolagemPEI72, orient=VERTICAL, command=canvasPEI72.yview)
    barra_de_rolagem71.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI72.configure(yscrollcommand=barra_de_rolagem71.set)
    canvasPEI72.bind('<Configure>', lambda e: canvasPEI72.configure(scrollregion=canvasPEI72.bbox("all")))

    fr_rolagemPEI72 = Frame(canvasPEI72)

    canvasPEI72.create_window((0, 0), window=fr_rolagemPEI72, anchor="nw")

    ### coisas ###
    chkbPEI720 = Checkbutton(fr_rolagemPEI72, text="7.2.0 - Nenhum instrumento tecnologico necessário ao desenvolvimento", width=400, anchor=W)
    chkbPEI720.grid(row=1, column=1)

    chkbPEI721 = Checkbutton(fr_rolagemPEI72, text="7.2.1 - Manuais/Livros/Materiais impressos específicos para leitura, escrita e cálculos", width=400, anchor=W)
    chkbPEI721.grid(row=2, column=1)

    chkbPEI722 = Checkbutton(fr_rolagemPEI72, text="7.2.2 - Equipamentos informático adaptado", width=400, anchor=W)
    chkbPEI722.grid(row=3, column=1)

    chkbPEI723 = Checkbutton(fr_rolagemPEI72, text="7.2.3 - Software didático", width=400, anchor=W)
    chkbPEI723.grid(row=4, column=1)

    chkbPEI724 = Checkbutton(fr_rolagemPEI72, text="7.2.4 - Aparelho auditivo/óculos/lupa", width=400, anchor=W)
    chkbPEI724.grid(row=5, column=1)

    chkbPEI725 = Checkbutton(fr_rolagemPEI72, text="7.2.5 - Cadeira de rodas", width=400, anchor=W)
    chkbPEI725.grid(row=6, column=1)

    chkbPEI726 = Checkbutton(fr_rolagemPEI72, text="7.2.6 - Sistema Alternativo e Aumentativo de Comunicação (SAAC)", width=400, anchor=W)
    chkbPEI726.grid(row=7, column=1)

    ### page 8 ###
    page8PEI = ttk.Frame(nbPEI)
    nbPEI.add(page8PEI, text="8 - Interveções Necessárias")

    ### multipage ###
    rows = 0
    while rows < 50:
        page8PEI.rowconfigure(rows, weight=1)
        page8PEI.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPEIpg8 = ttk.Notebook(page8PEI)
    nbPEIpg8.grid(row=1, column=1, columnspan=48, rowspan=48, sticky="NESW")

    ### page8.01 ###
    page801PEI = ttk.Frame(nbPEIpg8)
    nbPEIpg8.add(page801PEI, text="8.1 - Exercício da memória de curto prazo")

    Inventario = Label(page801PEI, text="8 - Intervenções necessárias", font="Negrito 10 bold", foreground='blue')
    Inventario.place(x=10, y=5)

    Exerciciomemoria = Label(page801PEI, text="8.1 - Exercício da memória de curto prazo",
                  font="Negrito 10 bold")
    Exerciciomemoria.place(x=20, y=25)

    cbComunicacao81 = Checkbutton(page801PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao81.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI81 = Frame(page801PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI81.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI81 = Canvas(page801PEI)
    canvasPEI81.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem81 = ttk.Scrollbar(fr_rolagemPEI81, orient=VERTICAL, command=canvasPEI81.yview)
    barra_de_rolagem81.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI81.configure(yscrollcommand=barra_de_rolagem81.set)
    canvasPEI81.bind('<Configure>', lambda e: canvasPEI81.configure(scrollregion=canvasPEI81.bbox("all")))

    fr_rolagemPEI81 = Frame(canvasPEI81)

    canvasPEI81.create_window((0, 0), window=fr_rolagemPEI81, anchor="nw")

    ### coisas ###
    chkbPEI810 = Checkbutton(fr_rolagemPEI81, text="8.1.0 - Nenhuma intervenção necessária", width=400, anchor=W)
    chkbPEI810.grid(row=1, column=1)

    chkbPEI811 = Checkbutton(fr_rolagemPEI81, text="8.1.1 - Fazer desenvolvida e os reproduzir posteriormente", width=400, anchor=W)
    chkbPEI811.grid(row=2, column=1)

    chkbPEI812 = Checkbutton(fr_rolagemPEI81, text="8.1.2 - Visualizar imagens e as reproduzir graficamente", width=400, anchor=W)
    chkbPEI812.grid(row=3, column=1)

    chkbPEI813 = Checkbutton(fr_rolagemPEI81, text="8.1.3 - Memorizar pronomes de um desenho", width=400, anchor=W)
    chkbPEI813.grid(row=4, column=1)

    chkbPEI814 = Checkbutton(fr_rolagemPEI81, text="8.1.4 - Reproduzir sequências de números", width=400, anchor=W)
    chkbPEI814.grid(row=5, column=1)

    chkbPEI815 = Checkbutton(fr_rolagemPEI81, text="8.1.5 - Reproduzir histórias, provérbios e legendas", width=400, anchor=W)
    chkbPEI815.grid(row=6, column=1)

    ### page8.02 ###
    page802PEI = ttk.Frame(nbPEIpg8)
    nbPEIpg8.add(page802PEI, text="8.2 - Treino de percepção e a memória visual")

    Inventario = Label(page802PEI, text="8 - Intervenções necessárias", font="Negrito 10 bold", foreground='blue')
    Inventario.place(x=10, y=5)

    Treinomemoria = Label(page802PEI, text="8.2 - Treino de percepção e a memória visual", font="Negrito 10 bold")
    Treinomemoria.place(x=20, y=25)

    cbComunicacao82 = Checkbutton(page802PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao82.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI82 = Frame(page802PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI82.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI82 = Canvas(page802PEI)
    canvasPEI82.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem82 = ttk.Scrollbar(fr_rolagemPEI82, orient=VERTICAL, command=canvasPEI82.yview)
    barra_de_rolagem82.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI82.configure(yscrollcommand=barra_de_rolagem82.set)
    canvasPEI82.bind('<Configure>', lambda e: canvasPEI82.configure(scrollregion=canvasPEI82.bbox("all")))

    fr_rolagemPEI82 = Frame(canvasPEI82)

    canvasPEI82.create_window((0, 0), window=fr_rolagemPEI82, anchor="nw")

    ### coisas ###
    chkbPEI820 = Checkbutton(fr_rolagemPEI82, text="8.2.0 - Nenhuma Intervenção necessária", width=400, anchor=W)
    chkbPEI820.grid(row=1, column=1)

    chkbPEI821 = Checkbutton(fr_rolagemPEI82, text="8.2.1 - Distinguir letras com formas idênticas", width=400, anchor=W)
    chkbPEI821.grid(row=2, column=1)

    chkbPEI822 = Checkbutton(fr_rolagemPEI82, text="8.2.2 - Fazer a correspondência entre figuras iguais", width=400, anchor=W)
    chkbPEI822.grid(row=3, column=1)

    chkbPEI823 = Checkbutton(fr_rolagemPEI82, text="8.2.3 - Fazer a correspondência entre letras ou conjuntos iguais", width=400, anchor=W)
    chkbPEI823.grid(row=4, column=1)

    chkbPEI824 = Checkbutton(fr_rolagemPEI82, text="8.2.4 - Identificar uma determinada letra num texto", width=400, anchor=W)
    chkbPEI824.grid(row=5, column=1)

    chkbPEI825 = Checkbutton(fr_rolagemPEI82, text="8.2.5 - Identificar o número de vezes que uma letra ou um algarismo se repetem", width=400, anchor=W)
    chkbPEI825.grid(row=6, column=1)

    chkbPEI826 = Checkbutton(fr_rolagemPEI82, text="8.2.6 - Identificar semelhanças ou diferenças entre desenhos", width=400, anchor=W)
    chkbPEI826.grid(row=7, column=1)

    chkbPEI827 = Checkbutton(fr_rolagemPEI82, text="8.2.7 - Identificar elementos em falta", width=400, anchor=W)
    chkbPEI827.grid(row=8, column=1)

    chkbPEI828 = Checkbutton(fr_rolagemPEI82, text="8.2.8 - Perceber figuras em fundos diferentes", width=400, anchor=W)
    chkbPEI828.grid(row=9, column=1)

    chkbPEI829 = Checkbutton(fr_rolagemPEI82, text="8.2.9 - Discriminar formas geométricas", width=400, anchor=W)
    chkbPEI829.grid(row=10, column=1)

    chkbPEI8210 = Checkbutton(fr_rolagemPEI82, text="8.2.10 - Descobrir num texto palavras iguais ao modelo", width=400, anchor=W)
    chkbPEI8210.grid(row=11, column=1)

    chkbPEI8211 = Checkbutton(fr_rolagemPEI82, text="8.2.11 - Procurar objetos específicos numa imagem ou num desenho", width=400, anchor=W)
    chkbPEI8211.grid(row=12, column=1)

    chkbPEI8212 = Checkbutton(fr_rolagemPEI82, text="8.2.12 - Selecionar conjuntos a partir de um dado critério", width=400, anchor=W)
    chkbPEI8212.grid(row=13, column=1)

    ### page8.03 ###
    page803PEI = ttk.Frame(nbPEIpg8)
    nbPEIpg8.add(page803PEI, text="8.3 - Desenvolvimento da linguagem")

    Inventario = Label(page803PEI, text="8 - Intervenções necessárias", font="Negrito 10 bold", foreground='blue')
    Inventario.place(x=10, y=5)

    Desenvolvimentolinguagem = Label(page803PEI, text="8.3 - Desenvolvimento da linguagem", font="Negrito 10 bold")
    Desenvolvimentolinguagem.place(x=20, y=25)

    cbComunicacao83 = Checkbutton(page803PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao83.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI83 = Frame(page803PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI83.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI83 = Canvas(page803PEI)
    canvasPEI83.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem83 = ttk.Scrollbar(fr_rolagemPEI83, orient=VERTICAL, command=canvasPEI83.yview)
    barra_de_rolagem83.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI83.configure(yscrollcommand=barra_de_rolagem83.set)
    canvasPEI83.bind('<Configure>', lambda e: canvasPEI83.configure(scrollregion=canvasPEI83.bbox("all")))

    fr_rolagemPEI83 = Frame(canvasPEI83)

    canvasPEI83.create_window((0, 0), window=fr_rolagemPEI83, anchor="nw")

    ### coisas ###
    chkbPEI830 = Checkbutton(fr_rolagemPEI83, text="8.3.0 - Nenhuma intervenção necessária", width=400, anchor=W)
    chkbPEI830.grid(row=1, column=1)

    chkbPEI831 = Checkbutton(fr_rolagemPEI83, text="8.3.1 - Reconhecer/ler os signos linguisticos", width=400, anchor=W)
    chkbPEI831.grid(row=2, column=1)

    chkbPEI832 = Checkbutton(fr_rolagemPEI83, text="8.3.2 - Reconhecer, através da leitura e da escrita, sílabas diretas e inversas, por ordem crescente de dificuldade", width=400, anchor=W)
    chkbPEI832.grid(row=3, column=1)

    chkbPEI833 = Checkbutton(fr_rolagemPEI83, text="8.3.3 - Diferenciar fonêmas similares no ponto ou modo de atrticulação", width=400, anchor=W)
    chkbPEI833.grid(row=4, column=1)

    chkbPEI834 = Checkbutton(fr_rolagemPEI83, text="8.3.4 - Formar palavra a partir de sílabas dadas", width=400, anchor=W)
    chkbPEI834.grid(row=5, column=1)

    chkbPEI835 = Checkbutton(fr_rolagemPEI83, text="8.3.5 - Preencher lacunas em frases com palavras dadas", width=400, anchor=W)
    chkbPEI835.grid(row=6, column=1)

    chkbPEI836 = Checkbutton(fr_rolagemPEI83, text="8.3.6 - Construir palavras a partir dos erros cometidos", width=400, anchor=W)
    chkbPEI836.grid(row=7, column=1)

    chkbPEI837 = Checkbutton(fr_rolagemPEI83, text="8.3.7 - Descrever uma situação, um desenho, uma imagem", width=400, anchor=W)
    chkbPEI837.grid(row=8, column=1)

    chkbPEI838 = Checkbutton(fr_rolagemPEI83, text="8.3.8 - Descrever as características de um objeto (cor, tamanho, forma, textura, utilidade)", width=400, anchor=W)
    chkbPEI838.grid(row=9, column=1)

    ### page 8.04 ###
    page804PEI = ttk.Frame(nbPEIpg8)
    nbPEIpg8.add(page804PEI, text="8.4 - Desenvolvimento da consequência fonológica")

    Inventario = Label(page804PEI, text="8 - Intervenções necessárias", font="Negrito 10 bold", foreground='blue')
    Inventario.place(x=10, y=5)

    DesenvolvimentoConsequenciaFonologica = Label(page804PEI, text="8.4 - Desenvolvimento da consequência fonológica", font="Negrito 10 bold")
    DesenvolvimentoConsequenciaFonologica.place(x=20, y=25)

    cbComunicacao84 = Checkbutton(page804PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao84.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI84 = Frame(page804PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI84.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI84 = Canvas(page804PEI)
    canvasPEI84.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem84 = ttk.Scrollbar(fr_rolagemPEI84, orient=VERTICAL, command=canvasPEI84.yview)
    barra_de_rolagem84.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI84.configure(yscrollcommand=barra_de_rolagem84.set)
    canvasPEI84.bind('<Configure>', lambda e: canvasPEI84.configure(scrollregion=canvasPEI84.bbox("all")))

    fr_rolagemPEI84 = Frame(canvasPEI84)

    canvasPEI84.create_window((0, 0), window=fr_rolagemPEI84, anchor="nw")

    ### coisas ###
    chkbPEI840 = Checkbutton(fr_rolagemPEI84, text="8.4.0 - Nenhuma intervenção necessária", width=400, anchor=W)
    chkbPEI840.grid(row=1, column=1)

    chkbPEI841 = Checkbutton(fr_rolagemPEI84, text="8.4.1 - Ler uma palavra, apesar de faltarem letras", width=400, anchor=W)
    chkbPEI841.grid(row=2, column=1)

    chkbPEI842 = Checkbutton(fr_rolagemPEI84, text="8.4.2 - Ler uma palavra, apesar de faltar uma sílaba", width=400, anchor=W)
    chkbPEI842.grid(row=3, column=1)

    chkbPEI843 = Checkbutton(fr_rolagemPEI84, text="8.4.3 - Dizer oralmente o som das letras", width=400, anchor=W)
    chkbPEI843.grid(row=4, column=1)

    chkbPEI844 = Checkbutton(fr_rolagemPEI84, text="8.4.4 - Dividir silabicamente palavras", width=400, anchor=W)
    chkbPEI844.grid(row=5, column=1)

    chkbPEI845 = Checkbutton(fr_rolagemPEI84, text="8.4.5 - Reconhecer o som das letras com grafia e som semelhantes", width=400, anchor=W)
    chkbPEI845.grid(row=6, column=1)

    chkbPEI846 = Checkbutton(fr_rolagemPEI84, text="8.4.6 - Fazer palavras cruzadas", width=400, anchor=W)
    chkbPEI846.grid(row=7, column=1)

    ### page 8.05 ###
    page805PEI = ttk.Frame(nbPEIpg8)
    nbPEIpg8.add(page805PEI, text="8.5 - Treino da percepção e a memória auditivas")

    Inventario = Label(page805PEI, text="8 - Intervenções necessárias", font="Negrito 10 bold", foreground='blue')
    Inventario.place(x=10, y=5)

    TreinoMemoriaAuditivas = Label(page805PEI, text="8.5 - Treino da percepção e a memória auditivas", font="Negrito 10 bold")
    TreinoMemoriaAuditivas.place(x=20, y=25)

    cbComunicacao85 = Checkbutton(page805PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao85.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI85 = Frame(page805PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI85.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI85 = Canvas(page805PEI)
    canvasPEI85.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem85 = ttk.Scrollbar(fr_rolagemPEI85, orient=VERTICAL, command=canvasPEI85.yview)
    barra_de_rolagem85.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI85.configure(yscrollcommand=barra_de_rolagem85.set)
    canvasPEI85.bind('<Configure>', lambda e: canvasPEI85.configure(scrollregion=canvasPEI85.bbox("all")))

    fr_rolagemPEI85 = Frame(canvasPEI85)

    canvasPEI85.create_window((0, 0), window=fr_rolagemPEI85, anchor="nw")

    ### coisas ###
    chkbPEI850 = Checkbutton(fr_rolagemPEI85, text="8.5.0 - Nenhuma intervenção necessária", width=400, anchor=W)
    chkbPEI850.grid(row=1, column=1)

    chkbPEI851 = Checkbutton(fr_rolagemPEI85, text="8.5.1 - Selecionar desenhos a partir do som inicial da palavra que o nomeia", width=400, anchor=W)
    chkbPEI851.grid(row=2, column=1)

    chkbPEI852 = Checkbutton(fr_rolagemPEI85, text="8.5.2 - Seleciona a palavra que indica o plural", width=400, anchor=W)
    chkbPEI852.grid(row=3, column=1)

    chkbPEI853 = Checkbutton(fr_rolagemPEI85, text="8.5.3 - Descobrir palavra a partir da primeira letra", width=400, anchor=W)
    chkbPEI853.grid(row=4, column=1)

    chkbPEI854 = Checkbutton(fr_rolagemPEI85, text="8.5.4 - Completar palavras ou frases", width=400, anchor=W)
    chkbPEI854.grid(row=5, column=1)

    chkbPEI855 = Checkbutton(fr_rolagemPEI85, text="8.5.5 - Selecionar a palavra correta", width=400, anchor=W)
    chkbPEI855.grid(row=6, column=1)

    chkbPEI856 = Checkbutton(fr_rolagemPEI85, text="8.5.6 - Fazer, oralmente, a divisão silábica das palavras", width=400, anchor=W)
    chkbPEI856.grid(row=7, column=1)

    chkbPEI857 = Checkbutton(fr_rolagemPEI85, text="8.5.7 - Recordar provérbios, canções, lengalengas", width=400, anchor=W)
    chkbPEI857.grid(row=8, column=1)

    chkbPEI858 = Checkbutton(fr_rolagemPEI85, text="8.5.8 - Recordar antônimos e sinônimos", width=400, anchor=W)
    chkbPEI858.grid(row=9, column=1)

    chkbPEI859 = Checkbutton(fr_rolagemPEI85, text="8.5.9 - Construir frases a partir de uma ou mais palavras dadas", width=400, anchor=W)
    chkbPEI859.grid(row=10, column=1)

    chkbPEI8510 = Checkbutton(fr_rolagemPEI85, text="8.5.10 - Reproduzir batimentos rítimicos", width=400, anchor=W)
    chkbPEI8510.grid(row=11, column=1)

    chkbPEI8511 = Checkbutton(fr_rolagemPEI85, text="8.5.11 - Reconhecer frases absurdas", width=400, anchor=W)
    chkbPEI8511.grid(row=12, column=1)

    chkbPEI8512 = Checkbutton(fr_rolagemPEI85, text="8.5.12 - Reconhecer afirmações verdadeiras ou falsas", width=400, anchor=W)
    chkbPEI8512.grid(row=13, column=1)

    chkbPEI8513 = Checkbutton(fr_rolagemPEI85, text="8.5.13 - Reconhecer sons do ambiente (gravados ou não)", width=400, anchor=W)
    chkbPEI8513.grid(row=14, column=1)

    chkbPEI8514 = Checkbutton(fr_rolagemPEI85, text="8.5.14 - Relacionar sons ouvidos com a respectiva fonte", width=400, anchor=W)
    chkbPEI8514.grid(row=15, column=1)

    chkbPEI8515 = Checkbutton(fr_rolagemPEI85, text="8.5.15 - Ouvir e reproduzir diferentes sílabas", width=400, anchor=W)
    chkbPEI8515.grid(row=16, column=1)

    ### page 9 ###
    page9PEI = ttk.Frame(nbPEI)
    nbPEI.add(page9PEI, text="9 - FAC (Ficha de Adequação Curricular)")

    ### multipage ###
    rows = 0
    while rows < 50:
        page9PEI.rowconfigure(rows, weight=1)
        page9PEI.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPEIpg9 = ttk.Notebook(page9PEI)
    nbPEIpg9.grid(row=1, column=1, columnspan=48, rowspan=48, sticky="NESW")

    ### page 9.01 ###
    page901PEI = ttk.Frame(nbPEIpg9)
    nbPEIpg9.add(page901PEI, text="9.1 - Questões Organizativas")

    Inventario = Label(page901PEI, text="9 - FAC (Ficha de Adequação Curricular)", font="Negrito 10 bold", foreground='blue')
    Inventario.place(x=10, y=5)

    QuestoesOrganizativas = Label(page901PEI, text="9.1 - Questões Organizativas", font="Negrito 10 bold")
    QuestoesOrganizativas.place(x=20, y=25)

    cbComunicacao91 = Checkbutton(page901PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao91.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI91 = Frame(page901PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI91.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI91 = Canvas(page901PEI)
    canvasPEI91.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem91 = ttk.Scrollbar(fr_rolagemPEI91, orient=VERTICAL, command=canvasPEI91.yview)
    barra_de_rolagem91.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI91.configure(yscrollcommand=barra_de_rolagem91.set)
    canvasPEI91.bind('<Configure>', lambda e: canvasPEI91.configure(scrollregion=canvasPEI91.bbox("all")))

    fr_rolagemPEI91 = Frame(canvasPEI91)

    canvasPEI91.create_window((0, 0), window=fr_rolagemPEI91, anchor="nw")

    ### coisas ###
    chkbPEI910 = Checkbutton(fr_rolagemPEI91, text="9.1.0 - Nenhuma adequação para as Questões Organizativas", width=400, anchor=W)
    chkbPEI910.grid(row=1, column=1)

    chkbPEI911 = Checkbutton(fr_rolagemPEI91, text="9.1.1 - Tipos de agrupamento: fileiras ou grupos de acordo com a necessidade", width=400, anchor=W)
    chkbPEI911.grid(row=2, column=1)

    chkbPEI912 = Checkbutton(fr_rolagemPEI91, text="9.1.2 - Posição na sala de aula: próximo a mesa da professora", width=400, anchor=W)
    chkbPEI912.grid(row=3, column=1)

    chkbPEI913 = Checkbutton(fr_rolagemPEI91, text="9.1.3 - Estabelecimento de rotina, com normas e limites a serem observados por toda a turma", width=400, anchor=W)
    chkbPEI913.grid(row=4, column=1)

    chkbPEI914 = Checkbutton(fr_rolagemPEI91, text="9.1.4 - Jogos interativos; recreação dirigida", width=400, anchor=W)
    chkbPEI914.grid(row=5, column=1)

    chkbPEI915 = Checkbutton(fr_rolagemPEI91, text="9.1.5 - Eventos escolares; festas, passeios, histórias contadas", width=400, anchor=W)
    chkbPEI915.grid(row=6, column=1)

    chkbPEI916 = Checkbutton(fr_rolagemPEI91, text="9.1.6 - Oficinas; atividades artísticas", width=400, anchor=W)
    chkbPEI916.grid(row=7, column=1)

    chkbPEI917 = Checkbutton(fr_rolagemPEI91, text="9.1.7 - Materiais utilizados: jogos pedagógicos, material para leitura, material concreto", width=400, anchor=W)
    chkbPEI917.grid(row=8, column=1)

    chkbPEI918 = Checkbutton(fr_rolagemPEI91, text="9.1.8 - Materiais utilizados: catão conflit, quebra-cabeças, alfabetos vários modelos, materiais concretos diversos", width=400, anchor=W)
    chkbPEI918.grid(row=9, column=1)

    ### page 9.02 ###
    page902PEI = ttk.Frame(nbPEIpg9)
    nbPEIpg9.add(page902PEI, text="9.2 - Questões Metedológicas e Didáticas")

    Inventario = Label(page902PEI, text="9 - FAC (Ficha de Adequação Curricular)", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    MetedologicasDidaticas = Label(page902PEI, text="9.2 - Questões Metedológicas e Didáticas", font="Negrito 10 bold")
    MetedologicasDidaticas.place(x=20, y=25)

    cbComunicacao92 = Checkbutton(page902PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao92.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI92 = Frame(page902PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI92.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI92 = Canvas(page902PEI)
    canvasPEI92.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem92 = ttk.Scrollbar(fr_rolagemPEI92, orient=VERTICAL, command=canvasPEI92.yview)
    barra_de_rolagem92.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI92.configure(yscrollcommand=barra_de_rolagem92.set)
    canvasPEI92.bind('<Configure>', lambda e: canvasPEI92.configure(scrollregion=canvasPEI92.bbox("all")))

    fr_rolagemPEI92 = Frame(canvasPEI92)

    canvasPEI92.create_window((0, 0), window=fr_rolagemPEI92, anchor="nw")

    ### coisas ###
    chkbPEI920 = Checkbutton(fr_rolagemPEI92, text="9.2.0 - Nenhuma adequação para as Questões Metedológicas e Didáticas ", width=400, anchor=W)
    chkbPEI920.grid(row=1, column=1)

    chkbPEI921 = Checkbutton(fr_rolagemPEI92, text="9.2.1 - Priorização de conteúdos e objetivos mais significativos", width=400, anchor=W)
    chkbPEI921.grid(row=2, column=1)

    chkbPEI922 = Checkbutton(fr_rolagemPEI92, text="9.2.2 - Valorizar conteúdos em detrimento da correção ortográfica; esplicitando o significado das palavras escritas que o aluno não compreende", width=400, anchor=W)
    chkbPEI922.grid(row=3, column=1)

    chkbPEI923 = Checkbutton(fr_rolagemPEI92, text="9.2.3 - Sequência gradativa dos conteúdos", width=400, anchor=W)
    chkbPEI923.grid(row=4, column=1)

    chkbPEI924 = Checkbutton(fr_rolagemPEI92, text="9.2.4 - Atividades diferenciadas, adequadas ao nível de aprendizagem", width=400, anchor=W)
    chkbPEI924.grid(row=5, column=1)

    chkbPEI925 = Checkbutton(fr_rolagemPEI92, text="9.2.5 - Redução de ativiidades", width=400, anchor=W)
    chkbPEI925.grid(row=6, column=1)

    chkbPEI926 = Checkbutton(fr_rolagemPEI92, text="9.2.6 - Avaliação diferenciada com perguntas simplificadas sem complexidade linguística (a nível morfo sintático semântico e lexical). (Art. 20°)", width=400, anchor=W)
    chkbPEI926.grid(row=7, column=1)

    chkbPEI927 = Checkbutton(fr_rolagemPEI92, text="9.2.7 - Privilegiar a avaliação oral em vez da escrita a qual será contínua (forma/meio de expreção). (Art. 20°)", width=400, anchor=W)
    chkbPEI927.grid(row=8, column=1)

    chkbPEI928 = Checkbutton(fr_rolagemPEI92, text="9.2.8 - Utilização de material concreto", width=400, anchor=W)
    chkbPEI928.grid(row=9, column=1)

    chkbPEI929 = Checkbutton(fr_rolagemPEI92, text="9.2.9 - Trabalho de identificação", width=400, anchor=W)
    chkbPEI929.grid(row=10, column=1)

    chkbPEI9210 = Checkbutton(fr_rolagemPEI92, text="9.2.10 - Reforço Escola", width=400, anchor=W)
    chkbPEI9210.grid(row=11, column=1)

    ### page 9.03 ###
    page903PEI = ttk.Frame(nbPEIpg9)
    nbPEIpg9.add(page903PEI, text="9.3 - Questões da Temporalidade")

    Inventario = Label(page903PEI, text="9 - FAC (Ficha de Adequação Curricular)", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    QuestoesTemporalidade = Label(page903PEI, text="9.3 - Questões da Temporalidade", font="Negrito 10 bold")
    QuestoesTemporalidade.place(x=20, y=25)

    cbComunicacao93 = Checkbutton(page903PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao93.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI93 = Frame(page903PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI93.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI93 = Canvas(page903PEI)
    canvasPEI93.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem93 = ttk.Scrollbar(fr_rolagemPEI93, orient=VERTICAL, command=canvasPEI93.yview)
    barra_de_rolagem93.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI93.configure(yscrollcommand=barra_de_rolagem93.set)
    canvasPEI93.bind('<Configure>', lambda e: canvasPEI93.configure(scrollregion=canvasPEI93.bbox("all")))

    fr_rolagemPEI93 = Frame(canvasPEI93)

    canvasPEI93.create_window((0, 0), window=fr_rolagemPEI93, anchor="nw")

    ### coisas ###
    chkbPEI930 = Checkbutton(fr_rolagemPEI93, text="9.3.0 - Nenhuma adequação para as Questões da Temporalidade", width=400, anchor=W)
    chkbPEI930.grid(row=1, column=1)

    chkbPEI931 = Checkbutton(fr_rolagemPEI93, text="9.3.1 - Tempo maior para a realização das atividades", width=400, anchor=W)
    chkbPEI931.grid(row=2, column=1)

    chkbPEI932 = Checkbutton(fr_rolagemPEI93, text="9.3.2 - Tempo maior para a realização das avaliações", width=400, anchor=W)
    chkbPEI932.grid(row=3, column=1)

    chkbPEI933 = Checkbutton(fr_rolagemPEI93, text="9.3.3 - Prolongamento do conteúdo com permanência de um ano ou mmais", width=400, anchor=W)
    chkbPEI933.grid(row=4, column=1)

    ### page 9.04 ###
    page904PEI = ttk.Frame(nbPEIpg9)
    nbPEIpg9.add(page904PEI, text="9.4 - Questões Práticas para o Aluno")

    Inventario = Label(page904PEI, text="9 - FAC (Ficha de Adequação Curricular)", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    QuestoesPraticasAluno = Label(page904PEI, text="9.4 - Questões Práticas para o Aluno", font="Negrito 10 bold")
    QuestoesPraticasAluno.place(x=20, y=25)

    cbComunicacao94 = Checkbutton(page904PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao94.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI94 = Frame(page904PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI94.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI94 = Canvas(page904PEI)
    canvasPEI94.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem94 = ttk.Scrollbar(fr_rolagemPEI94, orient=VERTICAL, command=canvasPEI94.yview)
    barra_de_rolagem94.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI94.configure(yscrollcommand=barra_de_rolagem94.set)
    canvasPEI94.bind('<Configure>', lambda e: canvasPEI94.configure(scrollregion=canvasPEI94.bbox("all")))

    fr_rolagemPEI94 = Frame(canvasPEI94)

    canvasPEI94.create_window((0, 0), window=fr_rolagemPEI94, anchor="nw")

    ### coisas ###
    chkbPEI940 = Checkbutton(fr_rolagemPEI94, text="9.4.0 - Nenhuma adequação para as Questões para as Práticas para o Aluno", width=400, anchor=W)
    chkbPEI940.grid(row=1, column=1)

    chkbPEI941 = Checkbutton(fr_rolagemPEI94, text="9.4.1 - Organizar as atividades e mochila", width=400, anchor=W)
    chkbPEI941.grid(row=2, column=1)

    chkbPEI942 = Checkbutton(fr_rolagemPEI94, text="9.4.2 - Fazer a tarefa de forma autônoma, desde que estejam de acordo com seu nível de aprendizagem", width=400, anchor=W)
    chkbPEI942.grid(row=3, column=1)

    chkbPEI943 = Checkbutton(fr_rolagemPEI94, text="9.4.3 - Adiquirir rotina de leitura", width=400, anchor=W)
    chkbPEI943.grid(row=4, column=1)

    ### page 9.05 ###
    page905PEI = ttk.Frame(nbPEIpg9)
    nbPEIpg9.add(page905PEI, text="9.5 - Questões do Contexto Escolar")

    Inventario = Label(page905PEI, text="9 - FAC (Ficha de Adequação Curricular)", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    QuestoesContextoEscolar = Label(page905PEI, text="9.5 - Questões do Contexto Escolar", font="Negrito 10 bold")
    QuestoesContextoEscolar.place(x=20, y=25)

    cbComunicacao95 = Checkbutton(page905PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao95.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI95 = Frame(page905PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI95.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI95 = Canvas(page905PEI)
    canvasPEI95.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem95 = ttk.Scrollbar(fr_rolagemPEI95, orient=VERTICAL, command=canvasPEI95.yview)
    barra_de_rolagem95.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI95.configure(yscrollcommand=barra_de_rolagem95.set)
    canvasPEI95.bind('<Configure>', lambda e: canvasPEI95.configure(scrollregion=canvasPEI95.bbox("all")))

    fr_rolagemPEI95 = Frame(canvasPEI95)

    canvasPEI95.create_window((0, 0), window=fr_rolagemPEI95, anchor="nw")

    ### coisas ###
    chkbPEI950 = Checkbutton(fr_rolagemPEI95, text="9.5.0 - Nenhuma Adequação para as Questões de Contexto Escolar", width=400, anchor=W)
    chkbPEI950.grid(row=1, column=1)

    chkbPEI951 = Checkbutton(fr_rolagemPEI95, text="9.5.1 - Envolvimento de toda a comunidade escolar para garantir a inclusão do aluno", width=400, anchor=W)
    chkbPEI951.grid(row=2, column=1)

    chkbPEI952 = Checkbutton(fr_rolagemPEI95, text="9.5.2 - Participação no projeto interventivo", width=400, anchor=W)
    chkbPEI952.grid(row=3, column=1)

    chkbPEI953 = Checkbutton(fr_rolagemPEI95, text="9.5.3 - Acompanhamento do SOE – Serviço de Orientação Educacional", width=400, anchor=W)
    chkbPEI953.grid(row=4, column=1)

    ### page 9.06 ###
    page906PEI = ttk.Frame(nbPEIpg9)
    nbPEIpg9.add(page906PEI, text="9.6 - Questões Conceituais")

    Inventario = Label(page906PEI, text="9 - FAC (Ficha de Adequação Curricular)", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    QuestoesConceituais = Label(page906PEI, text="9.6 - Questões Conceituais", font="Negrito 10 bold")
    QuestoesConceituais.place(x=20, y=25)

    cbComunicacao96 = Checkbutton(page906PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao96.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI96 = Frame(page906PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI96.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI96 = Canvas(page906PEI)
    canvasPEI96.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem96 = ttk.Scrollbar(fr_rolagemPEI96, orient=VERTICAL, command=canvasPEI96.yview)
    barra_de_rolagem96.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI96.configure(yscrollcommand=barra_de_rolagem96.set)
    canvasPEI96.bind('<Configure>', lambda e: canvasPEI96.configure(scrollregion=canvasPEI96.bbox("all")))

    fr_rolagemPEI96 = Frame(canvasPEI96)

    canvasPEI96.create_window((0, 0), window=fr_rolagemPEI96, anchor="nw")

    ### coisas ###
    chkbPEI960 = Checkbutton(fr_rolagemPEI96, text="9.6.0 - Nenhuma Adequação para as Questões Conceituais", width=400, anchor=W)
    chkbPEI960.grid(row=1, column=1)

    chkbPEI961 = Checkbutton(fr_rolagemPEI96, text="9.6.1 - Liguagem: Expressar de forma adequada seus sentidos, desejos e emoções", width=400, anchor=W)
    chkbPEI961.grid(row=2, column=1)

    chkbPEI962 = Checkbutton(fr_rolagemPEI96, text="9.6.2 - Leitura e escrita: Escrever palavras simples que lhe sejam significativas, grafar o nome completo sem auxílio ", width=400, anchor=W)
    chkbPEI962.grid(row=3, column=1)

    chkbPEI963 = Checkbutton(fr_rolagemPEI96, text="9.6.3 - Auto direcionamento: Locomove-se com independência nos espaços da escola e vizinhanças ", width=400, anchor=W)
    chkbPEI963.grid(row=4, column=1)

    chkbPEI964 = Checkbutton(fr_rolagemPEI96, text="9.6.4 - Hábitos de vida em grupo: Realizar atividades em grupo, solicitando ajuda dos colegas e expressando seus desejos e opiniões", width=400, anchor=W)
    chkbPEI964.grid(row=5, column=1)

    chkbPEI965 = Checkbutton(fr_rolagemPEI96, text="9.6.5 - Nomeação de objetos concretos", width=400, anchor=W)
    chkbPEI965.grid(row=6, column=1)

    chkbPEI966 = Checkbutton(fr_rolagemPEI96, text="9.6.6 - Fornecer dados pessoais tais como nome completo, idade, data do aniversário, endereço, etc.", width=400, anchor=W)
    chkbPEI966.grid(row=7, column=1)

    chkbPEI967 = Checkbutton(fr_rolagemPEI96, text="9.6.7 - Contar objetos, comparar quantidades", width=400, anchor=W)
    chkbPEI967.grid(row=8, column=1)

    chkbPEI968 = Checkbutton(fr_rolagemPEI96, text="9.6.8 - Memorizar sequências", width=400, anchor=W)
    chkbPEI968.grid(row=9, column=1)

    ### page 9.07 ###
    page907PEI = ttk.Frame(nbPEIpg9)
    nbPEIpg9.add(page907PEI, text="9.7 - Questões Sociais")

    Inventario = Label(page907PEI, text="9 - FAC (Ficha de Adequação Curricular)", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    MetedologicasDidaticas = Label(page907PEI, text="9.7 - Questões Sociais", font="Negrito 10 bold")
    MetedologicasDidaticas.place(x=20, y=25)

    cbComunicacao97 = Checkbutton(page907PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao97.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI97 = Frame(page907PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI97.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI97 = Canvas(page907PEI)
    canvasPEI97.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem97 = ttk.Scrollbar(fr_rolagemPEI97, orient=VERTICAL, command=canvasPEI97.yview)
    barra_de_rolagem97.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI97.configure(yscrollcommand=barra_de_rolagem97.set)
    canvasPEI97.bind('<Configure>', lambda e: canvasPEI97.configure(scrollregion=canvasPEI97.bbox("all")))

    fr_rolagemPEI97 = Frame(canvasPEI97)

    canvasPEI97.create_window((0, 0), window=fr_rolagemPEI97, anchor="nw")

    ### coisas ###
    chkbPEI970 = Checkbutton(fr_rolagemPEI97, text="9.7.0 - Nenhuma Adequação para as Questões Sociais", width=400, anchor=W)
    chkbPEI970.grid(row=1, column=1)

    chkbPEI971 = Checkbutton(fr_rolagemPEI97, text="9.7.1 - Maior interação com os outros", width=400, anchor=W)
    chkbPEI971.grid(row=2, column=1)

    chkbPEI972 = Checkbutton(fr_rolagemPEI97, text="9.7.2 - Melhore de autoestima", width=400, anchor=W)
    chkbPEI972.grid(row=3, column=1)

    ### page 9.08 ###
    page908PEI = ttk.Frame(nbPEIpg9)
    nbPEIpg9.add(page908PEI, text="9.8 - Questões de Família")

    Inventario = Label(page908PEI, text="9 - FAC (Ficha de Adequação Curricular)", font="Negrito 10 bold",
                       foreground='blue')
    Inventario.place(x=10, y=5)

    QuestoesFamilia = Label(page908PEI, text="9.8 - Questões de Família", font="Negrito 10 bold")
    QuestoesFamilia.place(x=20, y=25)

    cbComunicacao98 = Checkbutton(page908PEI, text="Seleciona Tudo", foreground='red', width=21, anchor=W)
    cbComunicacao98.place(x=10, y=45)

    ### CRIANDO FRAME ###
    fr_rolagemPEI98 = Frame(page908PEI, borderwidth=1, relief="solid")
    fr_rolagemPEI98.place(x=7, y=65, width=1010, height=205)

    ### criando o canvas ###
    canvasPEI98 = Canvas(page908PEI)
    canvasPEI98.place(x=8, y=66, width=990, height=203)

    ### criando a barra de rolagem ###
    barra_de_rolagem98 = ttk.Scrollbar(fr_rolagemPEI98, orient=VERTICAL, command=canvasPEI98.yview)
    barra_de_rolagem98.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPEI98.configure(yscrollcommand=barra_de_rolagem98.set)
    canvasPEI98.bind('<Configure>', lambda e: canvasPEI98.configure(scrollregion=canvasPEI98.bbox("all")))

    fr_rolagemPEI98 = Frame(canvasPEI98)

    canvasPEI98.create_window((0, 0), window=fr_rolagemPEI98, anchor="nw")

    ### coisas ###
    chkbPEI980 = Checkbutton(fr_rolagemPEI98, text="9.8.0 - Nenhuma adequação para as Questões de Família", width=400, anchor=W)
    chkbPEI980.grid(row=1, column=1)

    chkbPEI981 = Checkbutton(fr_rolagemPEI98, text="9.8.1 - Maior orientação quanto às atividades de casa", width=400, anchor=W)
    chkbPEI981.grid(row=2, column=1)

    chkbPEI982 = Checkbutton(fr_rolagemPEI98, text="9.8.2 - Buscar aividade física, de acordo com liberação médica", width=400, anchor=W)
    chkbPEI982.grid(row=3, column=1)

    chkbPEI983 = Checkbutton(fr_rolagemPEI98, text="9.8.3 - Reforço contínuo", width=400, anchor=W)
    chkbPEI983.grid(row=4, column=1)

    chkbPEI984 = Checkbutton(fr_rolagemPEI98, text="9.8.4 - Compromisso com providência de documentações e encaminhamentos a especialistas solicitados pela escola", width=400, anchor=W)
    chkbPEI984.grid(row=5, column=1)

    ### page 10 ###
    page10PEI = ttk.Frame(nbPEI)
    nbPEI.add(page10PEI, text="10 - Total em Hora/Aula | 11 - Metas priorizadas para o aluno | 13 - Implementação do PEI")

    ### multipage ###
    rows = 0
    while rows < 50:
        page10PEI.rowconfigure(rows, weight=1)
        page10PEI.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPEIpg10 = ttk.Notebook(page10PEI)
    nbPEIpg10.grid(row=1, column=1, columnspan=48, rowspan=48, sticky="NESW")

    ### page 10 ###
    page101PEI = ttk.Frame(nbPEIpg10)
    nbPEIpg10.add(page101PEI, text="10 - Questões Organizativas")

    HoraAula = Label(page101PEI, text="10 - Distribuição de Hora/Aula", font="Negrito 10 bold", foreground='blue')
    HoraAula.place(x=5, y=5)

    Pergunta101PEI = Label(page101PEI, text="""10.1 - Base Nacional Comum de Língua Portuguêsa,
Matemática, Geografia, História e Ciências""", font="Negrito 8 bold")
    Pergunta101PEI.place(x=10, y=40)

    Pergunta102PEI = Label(page101PEI, text="10.2 - Acompanhamento Pedagógico em Lígua Por-\ntuguesa e Matemática", font="Negrito 8 bold")
    Pergunta102PEI.place(x=10, y=145)

    Pergunta103PEI = Label(page101PEI, text="10.3 - Formação de hábitos Individual e Social", font="Negrito 8 bold")
    Pergunta103PEI.place(x=350, y=40)

    Pergunta104PEI = Label(page101PEI, text="10.4 - Base nacional comum de Educação Física e\nArtes", font="Negrito 8 bold")
    Pergunta104PEI.place(x=350, y=145)

    Pergunta105PEI = Label(page101PEI, text="10.5 - Atividades Artísticas, Culturais, Esporti-\nvas e Motoras", font="Negrito 8 bold")
    Pergunta105PEI.place(x=680, y=40)

    Pergunta101PEI = Label(page101PEI, text="10.6 - Total de Aulas de Acompanhamento no Período", font="Negrito 8 bold")
    Pergunta101PEI.place(x=680, y=145)

    ### radiobutton ###
    ## vars ##
    OptionintPEI101 = IntVar()
    OptionintPEI102 = IntVar()
    OptionintPEI103 = IntVar()
    OptionintPEI104 = IntVar()
    OptionintPEI105 = IntVar()
    OptionintPEI106 = IntVar()

    ## 10.1 ##
    CB101011_PEI = Radiobutton(page101PEI, text="10.1.1 - 220 h/Aulas", value=1, width=14, anchor=W, variable=OptionintPEI101)
    CB101011_PEI.place(x=30, y=75)

    CB101012_PEI = Radiobutton(page101PEI, text="10.1.2 - 440 h/Aulas", value=2, width=14, anchor=W, variable=OptionintPEI101)
    CB101012_PEI.place(x=30, y=95)

    CB101013_PEI = Radiobutton(page101PEI, text="10.1.3 - 880 h/Aulas", value=3, width=14, anchor=W, variable=OptionintPEI101)
    CB101013_PEI.place(x=30, y=115)

    ## 10.2 ##
    CB101021_PEI = Radiobutton(page101PEI, text="10.2.1 - 121 h/Aulas", value=1, width=14, anchor=W, variable=OptionintPEI102)
    CB101021_PEI.place(x=30, y=175)

    CB101022_PEI = Radiobutton(page101PEI, text="10.2.2 - 242 h/Aulas", value=2, width=14, anchor=W, variable=OptionintPEI102)
    CB101022_PEI.place(x=30, y=195)

    CB101023_PEI = Radiobutton(page101PEI, text="10.2.3 - 484 h/Aulas", value=3, width=14, anchor=W, variable=OptionintPEI102)
    CB101023_PEI.place(x=30, y=215)

    ## 10.3 ##
    CB101031_PEI = Radiobutton(page101PEI, text="10.3.1 - 22 h/Aulas", value=1, width=14, anchor=W, variable=OptionintPEI103)
    CB101031_PEI.place(x=370, y=65)

    CB101032_PEI = Radiobutton(page101PEI, text="10.3.2 - 44 h/Aulas", value=2, width=14, anchor=W, variable=OptionintPEI103)
    CB101032_PEI.place(x=370, y=85)

    CB101033_PEI = Radiobutton(page101PEI, text="10.3.3 - 88 h/Aulas", value=3, width=14, anchor=W, variable=OptionintPEI103)
    CB101033_PEI.place(x=370, y=105)

    ## 10.4 ##
    CB101041_PEI = Radiobutton(page101PEI, text="10.4.1 - 22 h/Aulas", value=1, width=14, anchor=W, variable=OptionintPEI104)
    CB101041_PEI.place(x=370, y=175)

    CB101042_PEI = Radiobutton(page101PEI, text="10.4.2 - 44 h/Aulas", value=2, width=14, anchor=W, variable=OptionintPEI104)
    CB101042_PEI.place(x=370, y=195)

    CB101043_PEI = Radiobutton(page101PEI, text="10.4.3 - 88 h/Aulas", value=3, width=14, anchor=W, variable=OptionintPEI104)
    CB101043_PEI.place(x=370, y=215)

    ## 10.5 ##
    CB101051_PEI = Radiobutton(page101PEI, text="10.5.1 - 22 h/Aulas", value=1, width=14, anchor=W, variable=OptionintPEI105)
    CB101051_PEI.place(x=700, y=75)

    CB101052_PEI = Radiobutton(page101PEI, text="10.5.2 - 44 h/Aulas", value=2, width=14, anchor=W, variable=OptionintPEI105)
    CB101052_PEI.place(x=700, y=95)

    CB101053_PEI = Radiobutton(page101PEI, text="10.5.3 - 88 h/Aulas", value=3, width=14, anchor=W, variable=OptionintPEI105)
    CB101053_PEI.place(x=700, y=115)

    ## 10.6 ##
    CB101061_PEI = Radiobutton(page101PEI, text="10.6.1 - 407 h/Aulas", value=1, width=14, anchor=W, variable=OptionintPEI106)
    CB101061_PEI.place(x=700, y=175)

    CB101062_PEI = Radiobutton(page101PEI, text="10.6.2 - 814 h/Aulas", value=2, width=14, anchor=W, variable=OptionintPEI106)
    CB101062_PEI.place(x=700, y=195)

    CB101063_PEI = Radiobutton(page101PEI, text="10.6.3 - 1624 h/Aulas", value=3, width=15, anchor=W, variable=OptionintPEI106)
    CB101063_PEI.place(x=700, y=215)

    ### page 11 ###
    page11PEI = ttk.Frame(nbPEIpg10)
    nbPEIpg10.add(page11PEI, text="11 - Metas Priorizadas para o Aluno")

    ### multipage ###
    rows = 0
    while rows < 50:
        page11PEI.rowconfigure(rows, weight=1)
        page11PEI.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPEIpg11 = ttk.Notebook(page11PEI)
    nbPEIpg11.grid(row=1, column=1, columnspan=48, rowspan=48, sticky="NESW")

    ### page 10 ###
    page111PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page111PEI, text="Mat")

    Metas11 = Label(page111PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    Matematica = Label(page111PEI, text="Matemática", font="Arial 10 bold")
    Matematica.place(x=5, y=20)

    Mat11PEIText = Text(page111PEI, width=123, height=13)
    Mat11PEIText.place(x=10, y=40)

    page112PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page112PEI, text="Por")

    Metas11 = Label(page112PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    Portugues = Label(page112PEI, text="Português", font="Arial 10 bold")
    Portugues.place(x=5, y=20)

    Por11PEIText = Text(page112PEI, width=123, height=13)
    Por11PEIText.place(x=10, y=40)

    page113PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page113PEI, text="Cie")

    Metas11 = Label(page113PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    Ciencias = Label(page113PEI, text="Ciências", font="Arial 10 bold")
    Ciencias.place(x=5, y=20)

    Cie11PEIText = Text(page113PEI, width=123, height=13)
    Cie11PEIText.place(x=10, y=40)

    page114PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page114PEI, text="His")

    Metas11 = Label(page114PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    Historia = Label(page114PEI, text="História", font="Arial 10 bold")
    Historia.place(x=5, y=20)

    His11PEIText = Text(page114PEI, width=123, height=13)
    His11PEIText.place(x=10, y=40)

    page115PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page115PEI, text="Geo")

    Metas11 = Label(page115PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    Geografia = Label(page115PEI, text="Geografia", font="Arial 10 bold")
    Geografia.place(x=5, y=20)

    Geo11PEIText = Text(page115PEI, width=123, height=13)
    Geo11PEIText.place(x=10, y=40)

    page116PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page116PEI, text="EF")

    Metas11 = Label(page116PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    EdFisica = Label(page116PEI, text="Educação Física", font="Arial 10 bold")
    EdFisica.place(x=5, y=20)

    EF11PEIText = Text(page116PEI, width=123, height=13)
    EF11PEIText.place(x=10, y=40)

    page117PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page117PEI, text="Rel")

    Metas11 = Label(page117PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    ReligiaoPEI = Label(page117PEI, text="Religião", font="Arial 10 bold")
    ReligiaoPEI.place(x=5, y=20)

    Rel11PEIText = Text(page117PEI, width=123, height=13)
    Rel11PEIText.place(x=10, y=40)

    page118PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page118PEI, text="Ing")

    Metas11 = Label(page118PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    InglesPEI = Label(page118PEI, text="Inglês", font="Arial 10 bold")
    InglesPEI.place(x=5, y=20)

    Ing11PEIText = Text(page118PEI, width=123, height=13)
    Ing11PEIText.place(x=10, y=40)

    page119PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page119PEI, text="Esp")

    Metas11 = Label(page119PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    EspanholPEI = Label(page119PEI, text="Espanhol", font="Arial 10 bold")
    EspanholPEI.place(x=5, y=20)

    Esp11PEIText = Text(page119PEI, width=123, height=13)
    Esp11PEIText.place(x=10, y=40)

    page120PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page120PEI, text="Fis")

    Metas11 = Label(page120PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    FisicaPEI = Label(page120PEI, text="Física", font="Arial 10 bold")
    FisicaPEI.place(x=5, y=20)

    Fis11PEIText = Text(page120PEI, width=123, height=13)
    Fis11PEIText.place(x=10, y=40)

    page121PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page121PEI, text="Qui")

    Metas11 = Label(page121PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    QuimicaPEI = Label(page121PEI, text="Quimica", font="Arial 10 bold")
    QuimicaPEI.place(x=5, y=20)

    Qui11PEIText = Text(page121PEI, width=123, height=13)
    Qui11PEIText.place(x=10, y=40)

    page122PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page122PEI, text="Red")

    Metas11 = Label(page122PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    RedacaoPEI = Label(page122PEI, text="Redação", font="Arial 10 bold")
    RedacaoPEI.place(x=5, y=20)

    Red11PEIText = Text(page122PEI, width=123, height=13)
    Red11PEIText.place(x=10, y=40)

    page123PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page123PEI, text="Escuta")

    Metas11 = Label(page123PEI, text="11 - Metas Priorizadas para o Aluno", font="Arial 7 bold", foreground='blue')
    Metas11.place(x=5, y=5)

    EscutaPEI = Label(page123PEI, text="Escuta", font="Arial 10 bold")
    EscutaPEI.place(x=5, y=20)

    Escuta11PEIText = Text(page123PEI, width=123, height=13)
    Escuta11PEIText.place(x=10, y=40)

    page124PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page124PEI, text="****")

    page125PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page125PEI, text="****")

    page126PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page126PEI, text="****")

    page127PEI = ttk.Frame(nbPEIpg11)
    nbPEIpg11.add(page127PEI, text="***")

    ### page 11 ###
    page13PEI = ttk.Frame(nbPEIpg10)
    nbPEIpg10.add(page13PEI, text="13 - Implantação do PEI")

    ImplantacaoPEI = Label(page13PEI, text="13 - Implantação do PEI", font="Negrito 10 bold", foreground='blue')
    ImplantacaoPEI.place(x=5, y=5)

    Pergunta131PEI = Label(page13PEI, text="13.1 - Critérios", font="Negrito 8 bold")
    Pergunta131PEI.place(x=10, y=25)

    Pergunta132PEI = Label(page13PEI, text="13.2 - Instrumentos", font="Negrito 8 bold")
    Pergunta132PEI.place(x=10, y=65)

    Pergunta133PEI = Label(page13PEI, text="13.3 - Intervenientes", font="Negrito 8 bold")
    Pergunta133PEI.place(x=10, y=105)

    Pergunta134PEI = Label(page13PEI, text="13.4 - Momentos de avaliação", font="Negrito 8 bold")
    Pergunta134PEI.place(x=10, y=145)

    Pergunta135PEI = Label(page13PEI, text="13.5 - Próxima revisão", font="Negrito 8 bold")
    Pergunta135PEI.place(x=10, y=185)

    ### TEXTS ###
    Resposta131PEI = Text(page13PEI, width=60, height=1)
    Resposta131PEI.place(x=10, y=45)

    Resposta132PEI = Text(page13PEI, width=60, height=1)
    Resposta132PEI.place(x=10, y=85)

    Resposta133PEI = Text(page13PEI, width=60, height=1)
    Resposta133PEI.place(x=10, y=125)

    Resposta134PEI = Text(page13PEI, width=60, height=1)
    Resposta134PEI.place(x=10, y=165)

    Resposta135PEI = Text(page13PEI, width=60, height=1)
    Resposta135PEI.place(x=10, y=205)

    ### page 12 ###
    page12PEI = ttk.Frame(nbPEI)
    nbPEI.add(page12PEI, text="12 - Participação do Aluno | 14 - Avaliação do PEI")

    ### multipage ###
    rows = 0
    while rows < 50:
        page12PEI.rowconfigure(rows, weight=1)
        page12PEI.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPEIpg12 = ttk.Notebook(page12PEI)
    nbPEIpg12.grid(row=1, column=1, columnspan=48, rowspan=48, sticky="NESW")

    ### page 12 ###
    page12PEI = ttk.Frame(nbPEIpg12)
    nbPEIpg12.add(page12PEI, text="12 - Nível de Participação nas Atividades da Turma")

    Participacao12 = Label(page12PEI, text="12 - Nível de Participação nas Atividades da Turma", font="Arial 10 bold", foreground='blue')
    Participacao12.place(x=5, y=10)

    Desc12 = Label(page12PEI, text="Descrição da Participação do Aluno nas Atividades da Turma")
    Desc12.place(x=10, y=40)

    page12PEIText = Text(page12PEI, width=129, height=14)
    page12PEIText.place(x=10, y=60)

    ### page 14 ###
    page14PEI = ttk.Frame(nbPEIpg12)
    nbPEIpg12.add(page14PEI, text="14 - Nível de Participação nas Atividades da Turma")

    Participacao12 = Label(page14PEI, text="14 - Avaliação do PEI", font="Arial 10 bold", foreground='blue')
    Participacao12.place(x=5, y=10)

    Desc14 = Label(page14PEI, text="Descrição Detalhada da Avaliação PEI no Período Aplicado")
    Desc14.place(x=10, y=40)

    MarqueParaExibir = Checkbutton(page14PEI, text="Marque para exibir INSTRUÇÕES", font="Arial 9 bold", foreground='red', width=28, anchor=W)
    MarqueParaExibir.place(x=740, y=40)

    page14PEIText = Text(page14PEI, width=129, height=14)
    page14PEIText.place(x=10, y=60)

    ### page 15 ###
    page15PEI = ttk.Frame(nbPEI)
    nbPEI.add(page15PEI, text="15 - Homologação do PEI")

    PeiElaborado15 = Label(page15PEI, text="15.1 - PEI Elaborado por:", font="Arial 10 bold", foreground='blue')
    PeiElaborado15.place(x=5, y=10)

    Professor15PEI = Label(page15PEI, text="Professor(a):", font="Arial 9 bold")
    Professor15PEI.place(x=15, y=40)

    Competente15PEI = Label(page15PEI, text="Competente", font="Arial 9 bold")
    Competente15PEI.place(x=365, y=40)

    Pergunta152PEI = Label(page15PEI, text="15.2 - Coordenação do PEI a cargo")
    Pergunta152PEI.place(x=655, y=40)

    Pergunta153PEI = Label(page15PEI, text="15.3 - Aprovado pelo conselho pedagógico em:")
    Pergunta153PEI.place(x=655, y=80)

    Pergunta154PEI = Label(page15PEI, text="15.4 - Homologia pelo conselho executivo em:")
    Pergunta154PEI.place(x=655, y=120)

    Pergunta155PEI = Label(page15PEI, text="15.5 - Concordo com as medidas educativas definidas, o Encarregado de Educação:")
    Pergunta155PEI.place(x=655, y=160)

    Pergunta156PEI = Label(page15PEI, text="15.6 - Ciência da família dos processos (Responsável legal):")
    Pergunta156PEI.place(x=655, y=200)

    Pergunta157PEI = Label(page15PEI, text="15.7 - Proficional de Educação Especial:")
    Pergunta157PEI.place(x=655, y=240)

    ### texts ###
    Pergunta152TextPei = Text(page15PEI, width=50, height=1)
    Pergunta152TextPei.place(x=655, y=60)

    Pergunta153TextPei = Text(page15PEI, width=50, height=1)
    Pergunta153TextPei.place(x=655, y=100)

    Pergunta154TextPei = Text(page15PEI, width=50, height=1)
    Pergunta154TextPei.place(x=655, y=140)

    Pergunta155TextPei = Text(page15PEI, width=50, height=1)
    Pergunta155TextPei.place(x=655, y=180)

    Pergunta156TextPei = Text(page15PEI, width=50, height=1)
    Pergunta156TextPei.place(x=655, y=220)

    Pergunta157TextPei = Text(page15PEI, width=50, height=1)
    Pergunta157TextPei.place(x=655, y=260)

    ### professor ###
    ProfessorVar1 = tkinter.StringVar()
    ProfessorCbbx1 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar1)
    ProfessorCbbx1.place(x=15, y=60)

    ProfessorVar2 = tkinter.StringVar()
    ProfessorCbbx2 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar2)
    ProfessorCbbx2.place(x=15, y=80)

    ProfessorVar3 = tkinter.StringVar()
    ProfessorCbbx3 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar3)
    ProfessorCbbx3.place(x=15, y=100)

    ProfessorVar4 = tkinter.StringVar()
    ProfessorCbbx4 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar4)
    ProfessorCbbx4.place(x=15, y=120)

    ProfessorVar5 = tkinter.StringVar()
    ProfessorCbbx5 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar5)
    ProfessorCbbx5.place(x=15, y=140)

    ProfessorVar6 = tkinter.StringVar()
    ProfessorCbbx6 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar6)
    ProfessorCbbx6.place(x=15, y=160)

    ProfessorVar7 = tkinter.StringVar()
    ProfessorCbbx7 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar7)
    ProfessorCbbx7.place(x=15, y=180)

    ProfessorVar8 = tkinter.StringVar()
    ProfessorCbbx8 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar8)
    ProfessorCbbx8.place(x=15, y=200)

    ProfessorVar9 = tkinter.StringVar()
    ProfessorCbbx9 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar9)
    ProfessorCbbx9.place(x=15, y=220)

    ProfessorVar10 = tkinter.StringVar()
    ProfessorCbbx10 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar10)
    ProfessorCbbx10.place(x=15, y=240)

    ProfessorVar11 = tkinter.StringVar()
    ProfessorCbbx11 = ttk.Combobox(page15PEI, width=50, height=1, textvariable=ProfessorVar11)
    ProfessorCbbx11.place(x=15, y=260)

    ### competente ###
    competenteVar1 = tkinter.StringVar()
    competenteCbbx1 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar1)
    competenteCbbx1.place(x=365, y=60)

    competenteVar2 = tkinter.StringVar()
    competenteCbbx2 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar2)
    competenteCbbx2.place(x=365, y=80)

    competenteVar3 = tkinter.StringVar()
    competenteCbbx3 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar3)
    competenteCbbx3.place(x=365, y=100)

    competenteVar4 = tkinter.StringVar()
    competenteCbbx4 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar4)
    competenteCbbx4.place(x=365, y=120)

    competenteVar5 = tkinter.StringVar()
    competenteCbbx5 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar5)
    competenteCbbx5.place(x=365, y=140)

    competenteVar6 = tkinter.StringVar()
    competenteCbbx6 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar6)
    competenteCbbx6.place(x=365, y=160)

    competenteVar7 = tkinter.StringVar()
    competenteCbbx7 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar7)
    competenteCbbx7.place(x=365, y=180)

    competenteVar8 = tkinter.StringVar()
    competenteCbbx8 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar8)
    competenteCbbx8.place(x=365, y=200)

    competenteVar9 = tkinter.StringVar()
    competenteCbbx9 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar9)
    competenteCbbx9.place(x=365, y=220)

    competenteVar10 = tkinter.StringVar()
    competenteCbbx10 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar10)
    competenteCbbx10.place(x=365, y=240)

    competenteVar11 = tkinter.StringVar()
    competenteCbbx11 = ttk.Combobox(page15PEI, width=40, height=1, textvariable=competenteVar11)
    competenteCbbx11.place(x=365, y=260)

    Ea_imgPEI = Label(novoTrabalhoPEI, image=imgEA)
    Ea_imgPEI.place(x=1020, y=30, width=60, height=45)

    BotaoResetarBarraPEI = Button(page15PEI, text="Resetar", command=reset)
    BotaoResetarBarraPEI.place(x=1000, y=300)

def abrirConselhoClasse():
    novoTrabalhoConselhoClasse = Toplevel()
    novoTrabalhoConselhoClasse.geometry('1090x620+260+70')
    novoTrabalhoConselhoClasse.resizable(False,False)
    novoTrabalhoConselhoClasse.title('Ata do Conselho de Classe')
    novoTrabalhoConselhoClasse.configure(bg='light gray')
    novoTrabalhoConselhoClasse.transient(trabalho)
    novoTrabalhoConselhoClasse.focus_force()
    novoTrabalhoConselhoClasse.grab_set()

    BimestreCC = tkinter.StringVar()
    BimestreCCcbbx = ttk.Combobox(novoTrabalhoConselhoClasse, width=20, height=1, textvariable=BimestreCC)
    BimestreCCcbbx.place(x=350, y=10)

    PeriodoCC1Text = Text(novoTrabalhoConselhoClasse, width=10, height=1)
    PeriodoCC1Text.place(x=570, y=10)

    PeriodoCC2Text = Text(novoTrabalhoConselhoClasse, width=10, height=1)
    PeriodoCC2Text.place(x=665, y=10)

    CodigoCCText = Text(novoTrabalhoConselhoClasse, width=7, height=1)
    CodigoCCText.place(x=10, y=126)

    CodigoCCLabel = Label(novoTrabalhoConselhoClasse, text='Código', bg='Light Grey', font="Arial 9 bold")
    CodigoCCLabel.place(x=10, y=105)

    TurmaCC = tkinter.StringVar()
    TurmaCCcbbx = ttk.Combobox(novoTrabalhoConselhoClasse, width=6, height=1, textvariable=TurmaCC)
    TurmaCCcbbx.place(x=80, y=126)

    TurmaCCLabel = Label(novoTrabalhoConselhoClasse, text='Turma', bg='Light Grey')
    TurmaCCLabel.place(x=80, y=105)

    SerieCCText = Text(novoTrabalhoConselhoClasse, width=24, height=1)
    SerieCCText.place(x=150, y=126)

    SerieCCLabel = Label(novoTrabalhoConselhoClasse, text='Série', bg='Light Grey')
    SerieCCLabel.place(x=150, y=105)

    OrdemCC = tkinter.StringVar()
    OrdemCCcbbx = ttk.Combobox(novoTrabalhoConselhoClasse, width=30, height=1, textvariable=OrdemCC)
    OrdemCCcbbx.place(x=360, y=126)

    OrdemCCLabel = Label(novoTrabalhoConselhoClasse, text='Ordem', bg='Light Grey')
    OrdemCCLabel.place(x=360, y=105)

    UnidadeCCText = Text(novoTrabalhoConselhoClasse, width=30, height=1)
    UnidadeCCText.place(x=10, y=168)

    UnidadeCCLabel = Label(novoTrabalhoConselhoClasse, text='Unidade', bg='Light Grey')
    UnidadeCCLabel.place(x=10, y=147)

    CidadeCC = tkinter.StringVar()
    CidadeCCcbbx = ttk.Combobox(novoTrabalhoConselhoClasse, width=10, height=1, textvariable=CidadeCC)
    CidadeCCcbbx.place(x=265, y=168)

    CidadeCCLabel = Label(novoTrabalhoConselhoClasse, text='Cidade', bg='Light Grey')
    CidadeCCLabel.place(x=265, y=147)

    EstadoCC = tkinter.StringVar()
    EstadoCCcbbx = ttk.Combobox(novoTrabalhoConselhoClasse, width=30, height=1, textvariable=EstadoCC)
    EstadoCCcbbx.place(x=360, y=168)

    EstadoCCLabel = Label(novoTrabalhoConselhoClasse, text='Estado', bg='Light Grey')
    EstadoCCLabel.place(x=360, y=147)

    BimestreCCLabel = Label(novoTrabalhoConselhoClasse, text="Bimestre:", bg='light grey')
    BimestreCCLabel.place(x=290, y=10)

    PeriodoCC1Label = Label(novoTrabalhoConselhoClasse, text="Período:", bg='light grey')
    PeriodoCC1Label.place(x=520, y=10)

    PeriodoCC2Label = Label(novoTrabalhoConselhoClasse, text="à", bg='light grey')
    PeriodoCC2Label.place(x=655, y=10)

    LocalDataFrameCCLabel = Label(novoTrabalhoConselhoClasse, width=40, height=2)
    LocalDataFrameCCLabel.place(x=785, y=10)

    LocalDataCCLabel = Label(novoTrabalhoConselhoClasse, text="Local e Data")
    LocalDataCCLabel.place(x=795, y=10)

    DiaMesAnoHoraCCLabel = Label(novoTrabalhoConselhoClasse, width=69, height=3)
    DiaMesAnoHoraCCLabel.place(x=585, y=135)

    DiaCPAlunoLabel = Label(novoTrabalhoConselhoClasse, text="Dia:")
    DiaCPAlunoLabel.place(x=600, y=150)

    MesCPAlunoLabel = Label(novoTrabalhoConselhoClasse, text="Mês:")
    MesCPAlunoLabel.place(x=660, y=150)

    AnoCPAlunoLabel = Label(novoTrabalhoConselhoClasse, text="Ano:")
    AnoCPAlunoLabel.place(x=815, y=150)

    HoraCPAlunoLabel = Label(novoTrabalhoConselhoClasse, text="Hora:")
    HoraCPAlunoLabel.place(x=950, y=150)

    DiaCCText = Text(novoTrabalhoConselhoClasse, width=3, height=1)
    DiaCCText.place(x=630, y=150)

    MesCCText = Text(novoTrabalhoConselhoClasse, width=15, height=1)
    MesCCText.place(x=690, y=150)

    AnoCCText = Text(novoTrabalhoConselhoClasse, width=5, height=1)
    AnoCCText.place(x=845, y=150)

    HoraCCText = Text(novoTrabalhoConselhoClasse, width=2, height=1)
    HoraCCText.place(x=985, y=150)

    MinutoCCText = Text(novoTrabalhoConselhoClasse, width=2, height=1)
    MinutoCCText.place(x=1005, y=150)

    ### multipage ###
    rows = 0
    while rows < 50:
        novoTrabalhoConselhoClasse.rowconfigure(rows, weight=1)
        novoTrabalhoConselhoClasse.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbCC = ttk.Notebook(novoTrabalhoConselhoClasse)
    nbCC.grid(row=17, column=0, columnspan=49, rowspan=39, sticky="NESW")

    ### page1 ###
    page1CC = ttk.Frame(nbCC)
    nbCC.add(page1CC, text="Equipe")

    ImageCC1Label = Label(page1CC, image=imgCCpage1)
    ImageCC1Label.place(x=10, y=10)

    DiretoriaText = Text(page1CC, width=37, height=1)
    DiretoriaText.place(x=10, y=100)

    DiretoriaLabel = Label(page1CC, text="Diretoria")
    DiretoriaLabel.place(x=10, y=75)

    SecretariaText = Text(page1CC, width=37, height=1)
    SecretariaText.place(x=10, y=145)

    SecretariaLabel = Label(page1CC, text="Secretaria")
    SecretariaLabel.place(x=10, y=120)

    CoordenacaoLabel = Label(page1CC, text="Coordenação")
    CoordenacaoLabel.place(x=10, y=165)

    CoordenacaoCC = tkinter.StringVar()
    CoordenacaoCCcbbx = ttk.Combobox(page1CC, width=46, height=1, textvariable=CoordenacaoCC)
    CoordenacaoCCcbbx.place(x=10, y=187)

    OrientacaoLabel = Label(page1CC, text="Orientação")
    OrientacaoLabel.place(x=10, y=210)

    OrientacaoCC = tkinter.StringVar()
    OrientacaoCCcbbx = ttk.Combobox(page1CC, width=46, height=1, textvariable=OrientacaoCC)
    OrientacaoCCcbbx.place(x=10, y=234)

    CapelaniaText = Text(page1CC, width=37, height=1)
    CapelaniaText.place(x=10, y=280)

    CapelaniaLabel = Label(page1CC, text="Capelania")
    CapelaniaLabel.place(x=10, y=257)

    ### itens novo trabalho 1 ###
    ### criando frame ###
    fr_rolagemCC = Frame(novoTrabalhoConselhoClasse, borderwidth=1, relief="solid")
    fr_rolagemCC.place(x=7, y=50, width=1070, height=55)

    ### criando o canvas ###
    canvasCC = Canvas(novoTrabalhoConselhoClasse)
    canvasCC.place(x=8, y=51, width=1050, height=53)

    ### criando a barra de rolagem ###
    barra_de_rolagemCC = ttk.Scrollbar(fr_rolagemCC, orient=VERTICAL, command=canvasCC.yview)
    barra_de_rolagemCC.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasCC.configure(yscrollcommand=barra_de_rolagemCC.set)
    canvasCC.bind('<Configure>',
                  lambda e: canvasCC.configure(scrollregion=canvasCC.bbox("all")))

    fr_rolagemCC = Frame(canvasCC)

    canvasCC.create_window((0, 0), window=fr_rolagemCC, anchor="nw")

    ### itens novo trabalho 1 ###
    ### criando frame ###
    fr_rolagemCC1 = Frame(page1CC, borderwidth=1, relief="solid")
    fr_rolagemCC1.place(x=332, y=30, width=345, height=348)

    ### criando o canvas ###
    canvasCC1 = Canvas(page1CC)
    canvasCC1.place(x=333, y=40, width=325, height=335)

    ### criando a barra de rolagem ###
    barra_de_rolagemCC1 = ttk.Scrollbar(fr_rolagemCC1, orient=VERTICAL, command=canvasCC1.yview)
    barra_de_rolagemCC1.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasCC1.configure(yscrollcommand=barra_de_rolagemCC1.set)
    canvasCC1.bind('<Configure>', lambda e: canvasCC1.configure(scrollregion=canvasCC1.bbox("all")))

    fr_rolagemCC1 = Frame(canvasCC1)

    canvasCC1.create_window((0, 0), window=fr_rolagemCC1, anchor="nw")

    ProfessoresPresentesCCLabel = Label(page1CC, text="Professores Presentes:", font='Arial 9 bold', foreground='darkblue')
    ProfessoresPresentesCCLabel.place(x=330, y=7)

    OradorCCLabel = Label(page1CC, text="Orador do Conselho de Classe:", font='Arial 9 bold', foreground='darkblue')
    OradorCCLabel.place(x=795, y=7)

    OradorCCText = Text(page1CC, width=43, height=1)
    OradorCCText.place(x=710, y=30)

    TemaExplanadoCCLabel = Label(page1CC, text="Tema Explanado no Conselho de Classe", font='Arial 9 bold', foreground='darkblue')
    TemaExplanadoCCLabel.place(x=767, y=50)

    TemaExplanadoCCText = Text(page1CC, width=43, height=19)
    TemaExplanadoCCText.place(x=710, y=70)

    ### page2 ###
    page2CC = ttk.Frame(nbCC)
    nbCC.add(page2CC, text="Estatísticas")

    ### Esquerda ###
    QuantidadeNomesAlunosCCLabel = Label(page2CC, text="Quantidade e Nomes de Alunos com Média Baixa por Diciplina", font='Arial 9 bold', foreground='blue')
    QuantidadeNomesAlunosCCLabel.place(x=10, y=7)

    TurmaSelecionadaCCLabel = Label(page2CC, text='Turma')
    TurmaSelecionadaCCLabel.place(x=376, y=27)

    TurmaSelecionadaCCText = Text(page2CC, width=6, height=1)
    TurmaSelecionadaCCText.place(x=418, y=27)

    ### criando frame page 1 ###
    fr_rolagem1CC = Frame(page2CC, borderwidth=1, relief="solid")
    fr_rolagem1CC.place(x=7, y=60, width=505, height=305)

    ### criando o canvas ###
    canvas1CC = Canvas(page2CC)
    canvas1CC.place(x=8, y=61, width=470, height=286)

    ### criando a barra de rolagem ###
    barra_de_rolagem1CC = ttk.Scrollbar(fr_rolagem1CC, orient=VERTICAL, command=canvas1CC.yview)
    barra_de_rolagem1CC.pack(side=RIGHT, fill=Y)

    barra_de_rolagem2CC = ttk.Scrollbar(fr_rolagem1CC, orient=HORIZONTAL, command=canvas1CC.xview)
    barra_de_rolagem2CC.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ##
    canvas1CC.configure(yscrollcommand=barra_de_rolagem1CC.set)
    canvas1CC.bind('<Configure>', lambda e: canvas1CC.configure(scrollregion=canvas1CC.bbox("all")))

    canvas1CC.configure(xscrollcommand=barra_de_rolagem2CC.set)
    canvas1CC.bind('<Configure>', lambda e: canvas1CC.configure(scrollregion=canvas1CC.bbox("all")))

    fr_rolagem1CC = Frame(canvas1CC)

    canvas1CC.create_window((0, 0), window=fr_rolagem1CC, anchor="nw")

    ### Direita ###
    QuantidadeNomesAlunosCCLabel = Label(page2CC, text="Quantidade e Nomes de Alunos Faltosos por Diciplina",
                                         font='Arial 9 bold', foreground='blue')
    QuantidadeNomesAlunosCCLabel.place(x=540, y=7)

    TurmaSelecionadaCCLabel = Label(page2CC, text='Turma')
    TurmaSelecionadaCCLabel.place(x=940, y=27)

    TurmaSelecionadaCCText = Text(page2CC, width=6, height=1)
    TurmaSelecionadaCCText.place(x=982, y=27)

    ### criando frame page 1 ###
    fr_rolagem2CC = Frame(page2CC, borderwidth=1, relief="solid")
    fr_rolagem2CC.place(x=540, y=60, width=495, height=305)

    ### criando o canvas ###
    canvas2CC = Canvas(page2CC)
    canvas2CC.place(x=541, y=61, width=460, height=286)

    ### criando a barra de rolagem ###
    barra_de_rolagem3CC = ttk.Scrollbar(fr_rolagem2CC, orient=VERTICAL, command=canvas2CC.yview)
    barra_de_rolagem3CC.pack(side=RIGHT, fill=Y)

    barra_de_rolagem4CC = ttk.Scrollbar(fr_rolagem2CC, orient=HORIZONTAL, command=canvas2CC.xview)
    barra_de_rolagem4CC.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ##
    canvas2CC.configure(yscrollcommand=barra_de_rolagem3CC.set)
    canvas2CC.bind('<Configure>', lambda e: canvas2CC.configure(scrollregion=canvas2CC.bbox("all")))

    canvas2CC.configure(xscrollcommand=barra_de_rolagem4CC.set)
    canvas2CC.bind('<Configure>', lambda e: canvas2CC.configure(scrollregion=canvas2CC.bbox("all")))

    fr_rolagem2CC = Frame(canvas2CC)

    canvas2CC.create_window((0, 0), window=fr_rolagem2CC, anchor="nw")

    ### page3 ###
    page3CC = ttk.Frame(nbCC)
    nbCC.add(page3CC, text="Avaliação de Turma")

    ### Pergunta1 ###
    FrameCCPergunta1 = Frame(page3CC, bg='Light Grey', width=475, height=70)
    FrameCCPergunta1.place(x=5, y=20)

    QuantoAproveitamentoCCLabel = Label(page3CC, text="1 - Quanto ao aproveitamento da turma:", bg='Light Grey', font="Arial 9 bold", foreground='blue')
    QuantoAproveitamentoCCLabel.place(x=10, y=30)

    OptionintCC1 = IntVar()

    ExcelenteCC1 = Radiobutton(page3CC, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W, variable=OptionintCC1)
    ExcelenteCC1.place(x=20, y=55)

    SuficienteCC1 = Radiobutton(page3CC, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W, variable=OptionintCC1)
    SuficienteCC1.place(x=100, y=55)

    SatisfatorioCC1 = Radiobutton(page3CC, text="Satisfatório", bg='Light Grey', value=3, width=14, anchor=W, variable=OptionintCC1)
    SatisfatorioCC1.place(x=180, y=55)

    InsuficienteCC1 = Radiobutton(page3CC, text="Insuficiente", bg='Light Grey', value=4, width=8, anchor=W, variable=OptionintCC1)
    InsuficienteCC1.place(x=265, y=55)

    ### Pergunta2 ###
    FrameCCPergunta2 = Frame(page3CC, bg='Light Grey', width=475, height=70)
    FrameCCPergunta2.place(x=5, y=130)

    QuantoDisciplinaTurmaCCLabel = Label(page3CC, text="2 - Quanto a disciplina da turma:", bg='Light Grey', font="Arial 9 bold", foreground='blue')
    QuantoDisciplinaTurmaCCLabel.place(x=10, y=140)

    OptionintCC2 = IntVar()

    ExcelenteCC2 = Radiobutton(page3CC, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W, variable=OptionintCC2)
    ExcelenteCC2.place(x=20, y=160)

    SuficienteCC2 = Radiobutton(page3CC, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W, variable=OptionintCC2)
    SuficienteCC2.place(x=100, y=160)

    SatisfatoriaCC2 = Radiobutton(page3CC, text="Satisfatória", bg='Light Grey', value=3, width=14, anchor=W, variable=OptionintCC2)
    SatisfatoriaCC2.place(x=180, y=160)

    BaixaCC2 = Radiobutton(page3CC, text="Baixa", bg='Light Grey', value=4, width=8, anchor=W, variable=OptionintCC2)
    BaixaCC2.place(x=265, y=160)

    ### Pergunta3 ###
    FrameCCPergunta3 = Frame(page3CC, bg='Light Grey', width=475, height=70)
    FrameCCPergunta3.place(x=5, y=230)

    QuantoParticipacaoTurmaClasseCCLabel = Label(page3CC, text="3 - Quanto a participação da turma em classe:", bg='Light Grey', font="Arial 9 bold", foreground='blue')
    QuantoParticipacaoTurmaClasseCCLabel.place(x=10, y=240)

    OptionintCC3 = IntVar()

    ExcelenteCC3 = Radiobutton(page3CC, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W, variable=OptionintCC3)
    ExcelenteCC3.place(x=20, y=260)

    SuficienteCC3 = Radiobutton(page3CC, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W, variable=OptionintCC3)
    SuficienteCC3.place(x=100, y=260)

    SatisfatorioCC3 = Radiobutton(page3CC, text="Satisfatório", bg='Light Grey', value=3, width=14, anchor=W, variable=OptionintCC3)
    SatisfatorioCC3.place(x=180, y=260)

    InsuficienteCC3 = Radiobutton(page3CC, text="Insuficiente", bg='Light Grey', value=4, width=8, anchor=W, variable=OptionintCC3)
    InsuficienteCC3.place(x=265, y=260)

    ### Pergunta4 ###
    FrameCCPergunta4 = Frame(page3CC, bg='Light Grey', width=580, height=70)
    FrameCCPergunta4.place(x=490, y=20)

    QuantoFrequenciaTurmaCCLabel = Label(page3CC, text="4 - Quanto a frequência da turma:", bg='Light Grey', font="Arial 9 bold", foreground='blue')
    QuantoFrequenciaTurmaCCLabel.place(x=500, y=30)

    OptionintCC4 = IntVar()

    ExcelenteCC4 = Radiobutton(page3CC, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W, variable=OptionintCC4)
    ExcelenteCC4.place(x=510, y=50)

    SuficienteCC4 = Radiobutton(page3CC, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W, variable=OptionintCC4)
    SuficienteCC4.place(x=590, y=50)

    SatisfatoriaCC4 = Radiobutton(page3CC, text="Satisfatória", bg='Light Grey', value=3, width=14, anchor=W, variable=OptionintCC4)
    SatisfatoriaCC4.place(x=670, y=50)

    BaixaCC4 = Radiobutton(page3CC, text="Baixa", bg='Light Grey', value=4, width=14, anchor=W, variable=OptionintCC4)
    BaixaCC4.place(x=755, y=50)

    ### Pergunta5 ###
    FrameCCPergunta5 = Frame(page3CC, bg='Light Grey', width=580, height=70)
    FrameCCPergunta5.place(x=490, y=130)

    QuantoComunicacaoTurmaCCLabel = Label(page3CC, text="5 - Quanto a Comunicação da turma com os professores:", bg='Light Grey', font="Arial 9 bold", foreground='blue')
    QuantoComunicacaoTurmaCCLabel.place(x=500, y=140)

    OptionintCC5 = IntVar()

    ExcelenteCC5 = Radiobutton(page3CC, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W, variable=OptionintCC5)
    ExcelenteCC5.place(x=510, y=160)

    SuficienteCC5 = Radiobutton(page3CC, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W, variable=OptionintCC5)
    SuficienteCC5.place(x=590, y=160)

    SatisfatorioCC5 = Radiobutton(page3CC, text="Satisfatório", bg='Light Grey', value=3, width=14, anchor=W, variable=OptionintCC5)
    SatisfatorioCC5.place(x=670, y=160)

    InsuficienteCC5 = Radiobutton(page3CC, text="Insuficiente", bg='Light Grey', value=4, width=14, anchor=W, variable=OptionintCC5)
    InsuficienteCC5.place(x=755, y=160)

    ### Pergunta6 ###
    FrameCCPergunta6 = Frame(page3CC, bg='Light Grey', width=580, height=70)
    FrameCCPergunta6.place(x=490, y=230)

    QuantoRelacaoTurmaCCLabel = Label(page3CC, text="6 - Quanto a Relação interpessoal da turma", bg='Light Grey', font="Arial 9 bold", foreground='blue')
    QuantoRelacaoTurmaCCLabel.place(x=500, y=240)

    OptionintCC6 = IntVar()

    ExcelenteCC6 = Radiobutton(page3CC, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W, variable=OptionintCC6)
    ExcelenteCC6.place(x=510, y=260)

    SuficienteCC6 = Radiobutton(page3CC, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W, variable=OptionintCC6)
    SuficienteCC6.place(x=590, y=260)

    SatisfatoriaCC6 = Radiobutton(page3CC, text="Satisfatória", bg='Light Grey', value=3, width=14, anchor=W, variable=OptionintCC6)
    SatisfatoriaCC6.place(x=670, y=260)

    InsuficientaCC6 = Radiobutton(page3CC, text="Baixa", bg='Light Grey', value=4, width=14, anchor=W, variable=OptionintCC6)
    InsuficientaCC6.place(x=755, y=260)

    ### page4 ###
    page4CC = ttk.Frame(nbCC)
    nbCC.add(page4CC, text="Apontamento dos Dicentes")

    AlunosDestacaramCCLabel = Label(page4CC, text="Alunos que se Destacaram Positivamente no Bimestre", font='Arial 9 bold', foreground='blue')
    AlunosDestacaramCCLabel.place(x=10, y=7)

    DestaquesCCLabel = Label(page4CC, text="Destaques")
    DestaquesCCLabel.place(x=15, y=40)

    VISUALIZAANTERIOR1 = Checkbutton(page4CC, text="VISUALIZA LISTA ANTERIOR", font='Arial 9 bold', foreground='red' , width=400, anchor=W)
    VISUALIZAANTERIOR1.place(x=150, y=40)

    ### criando frame page 4 ###
    fr_rolagem4CC = Frame(page4CC, borderwidth=1, relief="solid")
    fr_rolagem4CC.place(x=7, y=60, width=325, height=325)

    ### criando o canvas ###
    canvas4CC = Canvas(page4CC)
    canvas4CC.place(x=8, y=61, width=305, height=305)

    ### criando a barra de rolagem ###
    barra_de_rolagem5CC = ttk.Scrollbar(fr_rolagem4CC, orient=VERTICAL, command=canvas4CC.yview)
    barra_de_rolagem5CC.pack(side=RIGHT, fill=Y)

    barra_de_rolagem6CC = ttk.Scrollbar(fr_rolagem4CC, orient=HORIZONTAL, command=canvas4CC.xview)
    barra_de_rolagem6CC.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ##
    canvas4CC.configure(yscrollcommand=barra_de_rolagem5CC.set)
    canvas4CC.bind('<Configure>', lambda e: canvas4CC.configure(scrollregion=canvas4CC.bbox("all")))

    canvas4CC.configure(xscrollcommand=barra_de_rolagem6CC.set)
    canvas4CC.bind('<Configure>', lambda e: canvas4CC.configure(scrollregion=canvas4CC.bbox("all")))

    fr_rolagem4CC = Frame(canvas4CC)

    canvas4CC.create_window((0, 0), window=fr_rolagem4CC, anchor="nw")

    AlunosApontadosCCLabel = Label(page4CC, text="Alunos Apontados com algum Grau de Dificuldades", font='Arial 9 bold', foreground='blue')
    AlunosApontadosCCLabel.place(x=360, y=7)

    AcademicasCCLabel = Label(page4CC, text="Acadêmicas")
    AcademicasCCLabel.place(x=360, y=40)

    VISUALIZAANTERIOR2 = Checkbutton(page4CC, text="VISUALIZA LISTA ANTERIOR", font='Arial 9 bold', foreground='red', width=22, anchor=W)
    VISUALIZAANTERIOR2.place(x=504, y=40)


    ### criando frame page 401 ###
    fr_rolagem401CC = Frame(page4CC, borderwidth=1, relief="solid")
    fr_rolagem401CC.place(x=360, y=60, width=325, height=325)

    ### criando o canvas ###
    canvas401CC = Canvas(page4CC)
    canvas401CC.place(x=361, y=61, width=305, height=305)

    ### criando a barra de rolagem ###
    barra_de_rolagem7CC = ttk.Scrollbar(fr_rolagem401CC, orient=VERTICAL, command=canvas401CC.yview)
    barra_de_rolagem7CC.pack(side=RIGHT, fill=Y)

    barra_de_rolagem8CC = ttk.Scrollbar(fr_rolagem401CC, orient=HORIZONTAL, command=canvas401CC.xview)
    barra_de_rolagem8CC.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ##
    canvas401CC.configure(yscrollcommand=barra_de_rolagem7CC.set)
    canvas401CC.bind('<Configure>', lambda e: canvas401CC.configure(scrollregion=canvas401CC.bbox("all")))

    canvas401CC.configure(xscrollcommand=barra_de_rolagem8CC.set)
    canvas401CC.bind('<Configure>', lambda e: canvas401CC.configure(scrollregion=canvas401CC.bbox("all")))

    fr_rolagem401CC = Frame(canvas401CC)

    canvas401CC.create_window((0, 0), window=fr_rolagem401CC, anchor="nw")
    ##########################################################################

    VisualizacaoListaCCLabel = Label(page4CC, text="Visualização de Lista Anterior")
    VisualizacaoListaCCLabel.place(x=720, y=40)

    VisualizacaoCCText = Text(page4CC, width=43, height=20)
    VisualizacaoCCText.place(x=715, y=60)

    ### page5 ###
    page5CC = ttk.Frame(nbCC)
    nbCC.add(page5CC, text="Proposição do Conselho de Classe")

    TurmaCCLabel = Label(page5CC, text="Turma", font="Arial 8 bold")
    TurmaCCLabel.place(x=505, y=10)

    TurmaSelecionadaCC5 = tkinter.StringVar()
    TurmaSelecionadaCC5cbbx = ttk.Combobox(page5CC, width=6, height=1, textvariable=TurmaSelecionadaCC5)
    TurmaSelecionadaCC5cbbx.place(x=505, y=30)

    Salvar_Itens_SelectCCPg5Button = Button(page5CC, image=imgSalvar)
    Salvar_Itens_SelectCCPg5Button.place(x=514, y=60, width=40, height=40)

    Transf_Itens_SelectCCPg5Button = Button(page5CC, image=imgTransferir)
    Transf_Itens_SelectCCPg5Button.place(x=514, y=120, width=40, height=40)

    Limpar_Itens_SelectCCPg5Button = Button(page5CC, image=imgLimpar)
    Limpar_Itens_SelectCCPg5Button.place(x=514, y=170, width=40, height=40)



    Carregar_Itens_SelectCCPg5Button = Button(page5CC, image=imgCarregar)
    Carregar_Itens_SelectCCPg5Button.place(x=514, y=220, width=40, height=40)

    ### criando frame ###
    fr_rolagemCC5 = Frame(page5CC, borderwidth=1, relief="solid")
    fr_rolagemCC5.place(x=9, y=9, width=490, height=261)

    ### criando o canvas ###
    canvasCC5 = Canvas(page5CC)
    canvasCC5.place(x=10, y=10, width=472, height=244)

    ### criando a barra de rolagem ###
    barra_de_rolagem9CC = ttk.Scrollbar(fr_rolagemCC5, orient=VERTICAL, command=canvasCC5.yview)
    barra_de_rolagem9CC.pack(side=RIGHT, fill=Y)

    barra_de_rolagem10CC = ttk.Scrollbar(fr_rolagemCC5, orient=HORIZONTAL, command=canvasCC5.xview)
    barra_de_rolagem10CC.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasCC5.configure(yscrollcommand=barra_de_rolagem9CC.set)
    canvasCC5.bind('<Configure>', lambda e: canvasCC5.configure(scrollregion=canvasCC5.bbox("all")))

    canvasCC5.configure(xscrollcommand=barra_de_rolagem10CC.set)
    canvasCC5.bind('<Configure>', lambda e: canvasCC5.configure(scrollregion=canvasCC5.bbox("all")))

    fr_rolagemCC5 = Frame(canvasCC5)

    canvasCC5.create_window((0, 0), window=fr_rolagemCC5, anchor="nw")

    ### criando frame ###
    fr_rolagemCC501 = Frame(page5CC, borderwidth=1, relief="solid")
    fr_rolagemCC501.place(x=569, y=9, width=500, height=261)

    ### criando o canvas ###
    canvasCC501 = Canvas(page5CC)
    canvasCC501.place(x=570, y=10, width=482, height=244)

    ### criando a barra de rolagem ###
    barra_de_rolagem11CC = ttk.Scrollbar(fr_rolagemCC501, orient=VERTICAL, command=canvasCC501.yview)
    barra_de_rolagem11CC.pack(side=RIGHT, fill=Y)

    barra_de_rolagem12CC = ttk.Scrollbar(fr_rolagemCC501, orient=HORIZONTAL, command=canvasCC501.xview)
    barra_de_rolagem12CC.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasCC501.configure(yscrollcommand=barra_de_rolagem11CC.set)
    canvasCC501.bind('<Configure>', lambda e: canvasCC501.configure(scrollregion=canvasCC501.bbox("all")))

    canvasCC501.configure(xscrollcommand=barra_de_rolagem12CC.set)
    canvasCC501.bind('<Configure>', lambda e: canvasCC501.configure(scrollregion=canvasCC501.bbox("all")))

    fr_rolagemCC501 = Frame(canvasCC501)

    canvasCC501.create_window((0, 0), window=fr_rolagemCC501, anchor="nw")

    CosideracoesCCLbl = Label(page5CC, text="Considerações", font="Arial 9 bold", foreground='blue')
    CosideracoesCCLbl.place(x=10, y=270)

    CosideracoesCC = Text(page5CC, width=131, height=6)
    CosideracoesCC.place(x=10, y=290)

def abrirPlanejamento():
    novoTrabalhoPlanejamento = Toplevel()
    novoTrabalhoPlanejamento.geometry('1090x620+260+70')
    novoTrabalhoPlanejamento.resizable(False,False)
    novoTrabalhoPlanejamento.title('Planejamento Pedagógico Anual')
    novoTrabalhoPlanejamento.configure(bg='light gray')
    novoTrabalhoPlanejamento.transient(trabalho)
    novoTrabalhoPlanejamento.focus_force()
    novoTrabalhoPlanejamento.grab_set()

    ValidarPeriodoButtonPlanejamento = Button(novoTrabalhoPlanejamento, text='Validar Período', font='negrito 9 bold', bg="Lime")
    ValidarPeriodoButtonPlanejamento.place(x=975, y=35, width=100, height=31)

    PeriodoInicialPlanejamentoLabel = Label(novoTrabalhoPlanejamento, text="Período Inicial", font="Arial 8 bold", bg='light grey', foreground='blue')
    PeriodoInicialPlanejamentoLabel.place(x=725, y=20)

    PeriodoInicialPlanejamento = tkinter.StringVar()
    PeriodoInicialPlanejamentocbbx = ttk.Combobox(novoTrabalhoPlanejamento, width=16, height=1, textvariable=PeriodoInicialPlanejamento)
    PeriodoInicialPlanejamentocbbx.place(x=725, y=40)

    PeriodoFinalPlanejamentoLabel = Label(novoTrabalhoPlanejamento, text="Período Final", font="Arial 8 bold", bg='light grey', foreground='red')
    PeriodoFinalPlanejamentoLabel.place(x=850, y=20)

    PeriodoFinalPlanejamento = tkinter.StringVar()
    PeriodoFinalPlanejamentocbbx = ttk.Combobox(novoTrabalhoPlanejamento, width=16, height=1, textvariable=PeriodoFinalPlanejamento)
    PeriodoFinalPlanejamentocbbx.place(x=850, y=40)

    BimestrePlanejamentoLabel = Label(novoTrabalhoPlanejamento, text="Bimestre", bg='light grey')
    BimestrePlanejamentoLabel.place(x=630, y=19)

    BimestrePlanejamento = tkinter.StringVar()
    BimestrePlanejamentoPlanejamentocbbx = ttk.Combobox(novoTrabalhoPlanejamento, width=11, height=1, textvariable=BimestrePlanejamento)
    BimestrePlanejamentoPlanejamentocbbx.place(x=630, y=40)

    SeriePlanejamentoLabel = Label(novoTrabalhoPlanejamento, text="Série", bg='light grey')
    SeriePlanejamentoLabel.place(x=410, y=19)

    SeriePlanejamento = tkinter.StringVar()
    SeriePlanejamentoPlanejamentocbbx = ttk.Combobox(novoTrabalhoPlanejamento, width=31, height=1, textvariable=SeriePlanejamento)
    SeriePlanejamentoPlanejamentocbbx.place(x=410, y=40)

    TurmaPlanejamentoLabel = Label(novoTrabalhoPlanejamento, text="Turma", bg='light grey')
    TurmaPlanejamentoLabel.place(x=315, y=19)

    TurmaPlanejamento = tkinter.StringVar()
    TurmaPlanejamentoPlanejamentocbbx = ttk.Combobox(novoTrabalhoPlanejamento, width=11, height=1, textvariable=TurmaPlanejamento)
    TurmaPlanejamentoPlanejamentocbbx.place(x=315, y=40)

    ProfessorPlanejamentoLabel = Label(novoTrabalhoPlanejamento, text="Professor(a)", bg='light grey')
    ProfessorPlanejamentoLabel.place(x=100, y=19)

    ProfessorPlanejamento = tkinter.StringVar()
    ProfessorPlanejamentoPlanejamentocbbx = ttk.Combobox(novoTrabalhoPlanejamento, width=31, height=1, textvariable=ProfessorPlanejamento)
    ProfessorPlanejamentoPlanejamentocbbx.place(x=100, y=40)

    CodigoPlanejamentoLabel = Label(novoTrabalhoPlanejamento, text="Código", bg='light grey', font="Arial 8 bold")
    CodigoPlanejamentoLabel.place(x=10, y=20)

    CodigoPlanejamentoText = Text(novoTrabalhoPlanejamento, width=10, height=1)
    CodigoPlanejamentoText.place(x=10, y=40)

    ### criando frame page 3 ###
    fr_rolagemPlanejamnto = Frame(novoTrabalhoPlanejamento, borderwidth=1, relief="solid")
    fr_rolagemPlanejamnto.place(x=7, y=80, width=1070, height=75)

    ### criando o canvas ###
    canvasPlanejamnto = Canvas(novoTrabalhoPlanejamento)
    canvasPlanejamnto.place(x=8, y=81, width=1051, height=56)

    ### criando a barra de rolagem ###
    barra_de_rolagemPlanejamntoVert = ttk.Scrollbar(fr_rolagemPlanejamnto, orient=VERTICAL, command=canvasPlanejamnto.yview)
    barra_de_rolagemPlanejamntoVert.pack(side=RIGHT, fill=Y)

    barra_de_rolagemPlanejamntoHoriz = ttk.Scrollbar(fr_rolagemPlanejamnto, orient=HORIZONTAL, command=canvasPlanejamnto.xview)
    barra_de_rolagemPlanejamntoHoriz.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasPlanejamnto.configure(yscrollcommand=barra_de_rolagemPlanejamntoVert.set)
    canvasPlanejamnto.bind('<Configure>', lambda e: canvasPlanejamnto.configure(scrollregion=canvasPlanejamnto.bbox("all")))

    canvasPlanejamnto.configure(xscrollcommand=barra_de_rolagemPlanejamntoHoriz.set)
    canvasPlanejamnto.bind('<Configure>', lambda e: canvasPlanejamnto.configure(scrollregion=canvasPlanejamnto.bbox("all")))

    fr_rolagemPlanejamnto = Frame(canvasPlanejamnto)

    canvasPlanejamnto.create_window((0, 0), window=fr_rolagemPlanejamnto, anchor="nw")





### multipage ###
    rows = 0
    while rows < 50:
        novoTrabalhoPlanejamento.rowconfigure(rows, weight=1)
        novoTrabalhoPlanejamento.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentopg = ttk.Notebook(novoTrabalhoPlanejamento)
    nbPlanejamentopg.grid(row=14, column=0, columnspan=53, rowspan=48, sticky="NESW")

    pagePlanejamentoMat = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoMat, text="Matemática")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoMat.rowconfigure(rows, weight=1)
        pagePlanejamentoMat.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentopgsub = ttk.Notebook(pagePlanejamentoMat)
    nbPlanejamentopgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamento = ttk.Frame(nbPlanejamentopgsub)
    nbPlanejamentopgsub.add(pageConteudoPlanejamento, text="Conteúdo")

    ComponentePlanejamentoLabel = Label(pageConteudoPlanejamento, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabel.place(x=1, y=5)

    ComponentePlanejamentoText = Text(pageConteudoPlanejamento, width=40, height=1)
    ComponentePlanejamentoText.place(x=80, y=5)

    DetalhesPlanejamentoText = Text(pageConteudoPlanejamento, width=128, height=18)
    DetalhesPlanejamentoText.place(x=5, y=30)

    pageObjetivoPlanejamento = ttk.Frame(nbPlanejamentopgsub)
    nbPlanejamentopgsub.add(pageObjetivoPlanejamento, text="Objetivo")

    ObjetivoPlanejamentoText = Text(pageObjetivoPlanejamento, width=128, height=20)
    ObjetivoPlanejamentoText.place(x=5, y=5)

    pageEstatisticasPlanejamento = ttk.Frame(nbPlanejamentopgsub)
    nbPlanejamentopgsub.add(pageEstatisticasPlanejamento, text="Estatísticas")

    EstatisticasPlanejamentoText = Text(pageEstatisticasPlanejamento, width=128, height=20)
    EstatisticasPlanejamentoText.place(x=5, y=5)

    pageRecursosPlanejamento = ttk.Frame(nbPlanejamentopgsub)
    nbPlanejamentopgsub.add(pageRecursosPlanejamento, text="Recursos")

    RecursosPlanejamentoText = Text(pageRecursosPlanejamento, width=128, height=20)
    RecursosPlanejamentoText.place(x=5, y=5)

    pageMetasGeraisPlanejamento = ttk.Frame(nbPlanejamentopgsub)
    nbPlanejamentopgsub.add(pageMetasGeraisPlanejamento, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoText = Text(pageMetasGeraisPlanejamento, width=128, height=20)
    MetasGeraisPlanejamentoText.place(x=5, y=5)

    pagePlanejamentoPort = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoPort, text="Português")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoPort.rowconfigure(rows, weight=1)
        pagePlanejamentoPort.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoPortpgsub = ttk.Notebook(pagePlanejamentoPort)
    nbPlanejamentoPortpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoPort = ttk.Frame(nbPlanejamentoPortpgsub)
    nbPlanejamentoPortpgsub.add(pageConteudoPlanejamentoPort, text="Conteúdo")

    ComponentePlanejamentoLabelPort = Label(pageConteudoPlanejamentoPort, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelPort.place(x=1, y=5)

    ComponentePlanejamentoTextPort = Text(pageConteudoPlanejamentoPort, width=40, height=1)
    ComponentePlanejamentoTextPort.place(x=80, y=5)

    DetalhesPlanejamentoTextPort = Text(pageConteudoPlanejamentoPort, width=128, height=18)
    DetalhesPlanejamentoTextPort.place(x=5, y=30)

    pageObjetivoPlanejamentoPort = ttk.Frame(nbPlanejamentoPortpgsub)
    nbPlanejamentoPortpgsub.add(pageObjetivoPlanejamentoPort, text="Objetivo")

    ObjetivoPlanejamentoTextPort = Text(pageObjetivoPlanejamentoPort, width=128, height=20)
    ObjetivoPlanejamentoTextPort.place(x=5, y=5)

    pageEstatisticasPlanejamentoPort = ttk.Frame(nbPlanejamentoPortpgsub)
    nbPlanejamentoPortpgsub.add(pageEstatisticasPlanejamentoPort, text="Estatísticas")

    EstatisticasPlanejamentoTextPort = Text(pageEstatisticasPlanejamentoPort, width=128, height=20)
    EstatisticasPlanejamentoTextPort.place(x=5, y=5)

    pageRecursosPlanejamentoPort = ttk.Frame(nbPlanejamentoPortpgsub)
    nbPlanejamentoPortpgsub.add(pageRecursosPlanejamentoPort, text="Recursos")

    RecursosPlanejamentoTextPort = Text(pageRecursosPlanejamentoPort, width=128, height=20)
    RecursosPlanejamentoTextPort.place(x=5, y=5)

    pageMetasGeraisPlanejamentoPort = ttk.Frame(nbPlanejamentoPortpgsub)
    nbPlanejamentoPortpgsub.add(pageMetasGeraisPlanejamentoPort, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextPort = Text(pageMetasGeraisPlanejamentoPort, width=128, height=20)
    MetasGeraisPlanejamentoTextPort.place(x=5, y=5)

    pagePlanejamentoCie = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoCie, text="Ciêcias")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoCie.rowconfigure(rows, weight=1)
        pagePlanejamentoCie.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoCiepgsub = ttk.Notebook(pagePlanejamentoCie)
    nbPlanejamentoCiepgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoCie = ttk.Frame(nbPlanejamentoCiepgsub)
    nbPlanejamentoCiepgsub.add(pageConteudoPlanejamentoCie, text="Conteúdo")

    ComponentePlanejamentoLabelCie = Label(pageConteudoPlanejamentoCie, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelCie.place(x=1, y=5)

    ComponentePlanejamentoTextCie = Text(pageConteudoPlanejamentoCie, width=40, height=1)
    ComponentePlanejamentoTextCie.place(x=80, y=5)

    DetalhesPlanejamentoTextCie = Text(pageConteudoPlanejamentoCie, width=128, height=18)
    DetalhesPlanejamentoTextCie.place(x=5, y=30)

    pageObjetivoPlanejamentoCie = ttk.Frame(nbPlanejamentoCiepgsub)
    nbPlanejamentoCiepgsub.add(pageObjetivoPlanejamentoCie, text="Objetivo")

    ObjetivoPlanejamentoTextCie = Text(pageObjetivoPlanejamentoCie, width=128, height=20)
    ObjetivoPlanejamentoTextCie.place(x=5, y=5)

    pageEstatisticasPlanejamentoCie = ttk.Frame(nbPlanejamentoCiepgsub)
    nbPlanejamentoCiepgsub.add(pageEstatisticasPlanejamentoCie, text="Estatísticas")

    EstatisticasPlanejamentoTextCie = Text(pageEstatisticasPlanejamentoCie, width=128, height=20)
    EstatisticasPlanejamentoTextCie.place(x=5, y=5)

    pageRecursosPlanejamentoCie = ttk.Frame(nbPlanejamentoCiepgsub)
    nbPlanejamentoCiepgsub.add(pageRecursosPlanejamentoCie, text="Recursos")

    RecursosPlanejamentoTextCie = Text(pageRecursosPlanejamentoCie, width=128, height=20)
    RecursosPlanejamentoTextCie.place(x=5, y=5)

    pageMetasGeraisPlanejamentoCie = ttk.Frame(nbPlanejamentoCiepgsub)
    nbPlanejamentoCiepgsub.add(pageMetasGeraisPlanejamentoCie, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextCie = Text(pageMetasGeraisPlanejamentoCie, width=128, height=20)
    MetasGeraisPlanejamentoTextCie.place(x=5, y=5)

    pagePlanejamentoHist = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoHist, text="História")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoHist.rowconfigure(rows, weight=1)
        pagePlanejamentoHist.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoHistpgsub = ttk.Notebook(pagePlanejamentoHist)
    nbPlanejamentoHistpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoHist = ttk.Frame(nbPlanejamentoHistpgsub)
    nbPlanejamentoHistpgsub.add(pageConteudoPlanejamentoHist, text="Conteúdo")

    ComponentePlanejamentoLabelHist = Label(pageConteudoPlanejamentoHist, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelHist.place(x=1, y=5)

    ComponentePlanejamentoTextHist = Text(pageConteudoPlanejamentoHist, width=40, height=1)
    ComponentePlanejamentoTextHist.place(x=80, y=5)

    DetalhesPlanejamentoTextHist = Text(pageConteudoPlanejamentoHist, width=128, height=18)
    DetalhesPlanejamentoTextHist.place(x=5, y=30)

    pageObjetivoPlanejamentoHist = ttk.Frame(nbPlanejamentoHistpgsub)
    nbPlanejamentoHistpgsub.add(pageObjetivoPlanejamentoHist, text="Objetivo")

    ObjetivoPlanejamentoTextHist = Text(pageObjetivoPlanejamentoHist, width=128, height=20)
    ObjetivoPlanejamentoTextHist.place(x=5, y=5)

    pageEstatisticasPlanejamentoHist = ttk.Frame(nbPlanejamentoHistpgsub)
    nbPlanejamentoHistpgsub.add(pageEstatisticasPlanejamentoHist, text="Estatísticas")

    EstatisticasPlanejamentoTextHist = Text(pageEstatisticasPlanejamentoHist, width=128, height=20)
    EstatisticasPlanejamentoTextHist.place(x=5, y=5)

    pageRecursosPlanejamentoHist = ttk.Frame(nbPlanejamentoHistpgsub)
    nbPlanejamentoHistpgsub.add(pageRecursosPlanejamentoHist, text="Recursos")

    RecursosPlanejamentoTextHist = Text(pageRecursosPlanejamentoHist, width=128, height=20)
    RecursosPlanejamentoTextHist.place(x=5, y=5)

    pageMetasGeraisPlanejamentoHist = ttk.Frame(nbPlanejamentoHistpgsub)
    nbPlanejamentoHistpgsub.add(pageMetasGeraisPlanejamentoHist, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextHist = Text(pageMetasGeraisPlanejamentoHist, width=128, height=20)
    MetasGeraisPlanejamentoTextHist.place(x=5, y=5)

    pagePlanejamentoGeo = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoGeo, text="Geografia")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoGeo.rowconfigure(rows, weight=1)
        pagePlanejamentoGeo.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoGeopgsub = ttk.Notebook(pagePlanejamentoGeo)
    nbPlanejamentoGeopgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoGeo = ttk.Frame(nbPlanejamentoGeopgsub)
    nbPlanejamentoGeopgsub.add(pageConteudoPlanejamentoGeo, text="Conteúdo")

    ComponentePlanejamentoLabelGeo = Label(pageConteudoPlanejamentoGeo, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelGeo.place(x=1, y=5)

    ComponentePlanejamentoTextGeo = Text(pageConteudoPlanejamentoGeo, width=40, height=1)
    ComponentePlanejamentoTextGeo.place(x=80, y=5)

    DetalhesPlanejamentoTextGeo = Text(pageConteudoPlanejamentoGeo, width=128, height=18)
    DetalhesPlanejamentoTextGeo.place(x=5, y=30)

    pageObjetivoPlanejamentoGeo = ttk.Frame(nbPlanejamentoGeopgsub)
    nbPlanejamentoGeopgsub.add(pageObjetivoPlanejamentoGeo, text="Objetivo")

    ObjetivoPlanejamentoTextGeo = Text(pageObjetivoPlanejamentoGeo, width=128, height=20)
    ObjetivoPlanejamentoTextGeo.place(x=5, y=5)

    pageEstatisticasPlanejamentoGeo = ttk.Frame(nbPlanejamentoGeopgsub)
    nbPlanejamentoGeopgsub.add(pageEstatisticasPlanejamentoGeo, text="Estatísticas")

    EstatisticasPlanejamentoTextGeo = Text(pageEstatisticasPlanejamentoGeo, width=128, height=20)
    EstatisticasPlanejamentoTextGeo.place(x=5, y=5)

    pageRecursosPlanejamentoGeo = ttk.Frame(nbPlanejamentoGeopgsub)
    nbPlanejamentoGeopgsub.add(pageRecursosPlanejamentoGeo, text="Recursos")

    RecursosPlanejamentoTextGeo = Text(pageRecursosPlanejamentoGeo, width=128, height=20)
    RecursosPlanejamentoTextGeo.place(x=5, y=5)

    pageMetasGeraisPlanejamentoGeo = ttk.Frame(nbPlanejamentoGeopgsub)
    nbPlanejamentoGeopgsub.add(pageMetasGeraisPlanejamentoGeo, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextGeo = Text(pageMetasGeraisPlanejamentoGeo, width=128, height=20)
    MetasGeraisPlanejamentoTextGeo.place(x=5, y=5)

    pagePlanejamentoArte = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoArte, text="Arte")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoArte.rowconfigure(rows, weight=1)
        pagePlanejamentoArte.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoArtpgsub = ttk.Notebook(pagePlanejamentoArte)
    nbPlanejamentoArtpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoArt = ttk.Frame(nbPlanejamentoArtpgsub)
    nbPlanejamentoArtpgsub.add(pageConteudoPlanejamentoArt, text="Conteúdo")

    ComponentePlanejamentoLabelArt = Label(pageConteudoPlanejamentoArt, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelArt.place(x=1, y=5)

    ComponentePlanejamentoTextArt = Text(pageConteudoPlanejamentoArt, width=40, height=1)
    ComponentePlanejamentoTextArt.place(x=80, y=5)

    DetalhesPlanejamentoTextArt = Text(pageConteudoPlanejamentoArt, width=128, height=18)
    DetalhesPlanejamentoTextArt.place(x=5, y=30)

    pageObjetivoPlanejamentoArt = ttk.Frame(nbPlanejamentoArtpgsub)
    nbPlanejamentoArtpgsub.add(pageObjetivoPlanejamentoArt, text="Objetivo")

    ObjetivoPlanejamentoTextArt = Text(pageObjetivoPlanejamentoArt, width=128, height=20)
    ObjetivoPlanejamentoTextArt.place(x=5, y=5)

    pageEstatisticasPlanejamentoArt = ttk.Frame(nbPlanejamentoArtpgsub)
    nbPlanejamentoArtpgsub.add(pageEstatisticasPlanejamentoArt, text="Estatísticas")

    EstatisticasPlanejamentoTextArt = Text(pageEstatisticasPlanejamentoArt, width=128, height=20)
    EstatisticasPlanejamentoTextArt.place(x=5, y=5)

    pageRecursosPlanejamentoArt = ttk.Frame(nbPlanejamentoArtpgsub)
    nbPlanejamentoArtpgsub.add(pageRecursosPlanejamentoArt, text="Recursos")

    RecursosPlanejamentoTextGeo = Text(pageRecursosPlanejamentoArt, width=128, height=20)
    RecursosPlanejamentoTextGeo.place(x=5, y=5)

    pageMetasGeraisPlanejamentoArt = ttk.Frame(nbPlanejamentoArtpgsub)
    nbPlanejamentoArtpgsub.add(pageMetasGeraisPlanejamentoArt, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextArt = Text(pageMetasGeraisPlanejamentoArt, width=128, height=20)
    MetasGeraisPlanejamentoTextArt.place(x=5, y=5)

    pagePlanejamentoEdFis = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoEdFis, text="Ed.Física")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoEdFis.rowconfigure(rows, weight=1)
        pagePlanejamentoEdFis.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoEdFispgsub = ttk.Notebook(pagePlanejamentoEdFis)
    nbPlanejamentoEdFispgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoEdFis = ttk.Frame(nbPlanejamentoEdFispgsub)
    nbPlanejamentoEdFispgsub.add(pageConteudoPlanejamentoEdFis, text="Conteúdo")

    ComponentePlanejamentoLabelEdFis = Label(pageConteudoPlanejamentoEdFis, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelEdFis.place(x=1, y=5)

    ComponentePlanejamentoTextEdFis = Text(pageConteudoPlanejamentoEdFis, width=40, height=1)
    ComponentePlanejamentoTextEdFis.place(x=80, y=5)

    DetalhesPlanejamentoTextEdFis = Text(pageConteudoPlanejamentoEdFis, width=128, height=18)
    DetalhesPlanejamentoTextEdFis.place(x=5, y=30)

    pageObjetivoPlanejamentoEdFis = ttk.Frame(nbPlanejamentoEdFispgsub)
    nbPlanejamentoEdFispgsub.add(pageObjetivoPlanejamentoEdFis, text="Objetivo")

    ObjetivoPlanejamentoTextEdFis = Text(pageObjetivoPlanejamentoEdFis, width=128, height=20)
    ObjetivoPlanejamentoTextEdFis.place(x=5, y=5)

    pageEstatisticasPlanejamentoEdFis = ttk.Frame(nbPlanejamentoEdFispgsub)
    nbPlanejamentoEdFispgsub.add(pageEstatisticasPlanejamentoEdFis, text="Estatísticas")

    EstatisticasPlanejamentoTextEdFis = Text(pageEstatisticasPlanejamentoEdFis, width=128, height=20)
    EstatisticasPlanejamentoTextEdFis.place(x=5, y=5)

    pageRecursosPlanejamentoEdFis = ttk.Frame(nbPlanejamentoEdFispgsub)
    nbPlanejamentoEdFispgsub.add(pageRecursosPlanejamentoEdFis, text="Recursos")

    RecursosPlanejamentoTextEdFis = Text(pageRecursosPlanejamentoEdFis, width=128, height=20)
    RecursosPlanejamentoTextEdFis.place(x=5, y=5)

    pageMetasGeraisPlanejamentoEdFis = ttk.Frame(nbPlanejamentoEdFispgsub)
    nbPlanejamentoEdFispgsub.add(pageMetasGeraisPlanejamentoEdFis, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextEdFis = Text(pageMetasGeraisPlanejamentoEdFis, width=128, height=20)
    MetasGeraisPlanejamentoTextEdFis.place(x=5, y=5)

    pagePlanejamentoRel = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoRel, text="Religião")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoRel.rowconfigure(rows, weight=1)
        pagePlanejamentoRel.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoRelpgsub = ttk.Notebook(pagePlanejamentoRel)
    nbPlanejamentoRelpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoRel = ttk.Frame(nbPlanejamentoRelpgsub)
    nbPlanejamentoRelpgsub.add(pageConteudoPlanejamentoRel, text="Conteúdo")

    ComponentePlanejamentoLabelRel = Label(pageConteudoPlanejamentoRel, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelRel.place(x=1, y=5)

    ComponentePlanejamentoTextRel = Text(pageConteudoPlanejamentoRel, width=40, height=1)
    ComponentePlanejamentoTextRel.place(x=80, y=5)

    DetalhesPlanejamentoTextRel = Text(pageConteudoPlanejamentoRel, width=128, height=18)
    DetalhesPlanejamentoTextRel.place(x=5, y=30)

    pageObjetivoPlanejamentoRel = ttk.Frame(nbPlanejamentoRelpgsub)
    nbPlanejamentoRelpgsub.add(pageObjetivoPlanejamentoRel, text="Objetivo")

    ObjetivoPlanejamentoTextRel = Text(pageObjetivoPlanejamentoRel, width=128, height=20)
    ObjetivoPlanejamentoTextRel.place(x=5, y=5)

    pageEstatisticasPlanejamentoRel = ttk.Frame(nbPlanejamentoRelpgsub)
    nbPlanejamentoRelpgsub.add(pageEstatisticasPlanejamentoRel, text="Estatísticas")

    EstatisticasPlanejamentoTextRel = Text(pageEstatisticasPlanejamentoRel, width=128, height=20)
    EstatisticasPlanejamentoTextRel.place(x=5, y=5)

    pageRecursosPlanejamentoRel = ttk.Frame(nbPlanejamentoRelpgsub)
    nbPlanejamentoRelpgsub.add(pageRecursosPlanejamentoRel, text="Recursos")

    RecursosPlanejamentoTextRel = Text(pageRecursosPlanejamentoRel, width=128, height=20)
    RecursosPlanejamentoTextRel.place(x=5, y=5)

    pageMetasGeraisPlanejamentoRel = ttk.Frame(nbPlanejamentoRelpgsub)
    nbPlanejamentoRelpgsub.add(pageMetasGeraisPlanejamentoRel, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextRel = Text(pageMetasGeraisPlanejamentoRel, width=128, height=20)
    MetasGeraisPlanejamentoTextRel.place(x=5, y=5)

    pagePlanejamentoIng = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoIng, text="Inglês")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoIng.rowconfigure(rows, weight=1)
        pagePlanejamentoIng.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoIngpgsub = ttk.Notebook(pagePlanejamentoIng)
    nbPlanejamentoIngpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoIng = ttk.Frame(nbPlanejamentoIngpgsub)
    nbPlanejamentoIngpgsub.add(pageConteudoPlanejamentoIng, text="Conteúdo")

    ComponentePlanejamentoLabelIng = Label(pageConteudoPlanejamentoIng, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelIng.place(x=1, y=5)

    ComponentePlanejamentoTextIng = Text(pageConteudoPlanejamentoIng, width=40, height=1)
    ComponentePlanejamentoTextIng.place(x=80, y=5)

    DetalhesPlanejamentoTextIng = Text(pageConteudoPlanejamentoIng, width=128, height=18)
    DetalhesPlanejamentoTextIng.place(x=5, y=30)

    pageObjetivoPlanejamentoIng = ttk.Frame(nbPlanejamentoIngpgsub)
    nbPlanejamentoIngpgsub.add(pageObjetivoPlanejamentoIng, text="Objetivo")

    ObjetivoPlanejamentoTextIng = Text(pageObjetivoPlanejamentoIng, width=128, height=20)
    ObjetivoPlanejamentoTextIng.place(x=5, y=5)

    pageEstatisticasPlanejamentoIng = ttk.Frame(nbPlanejamentoIngpgsub)
    nbPlanejamentoIngpgsub.add(pageEstatisticasPlanejamentoIng, text="Estatísticas")

    EstatisticasPlanejamentoTextIng = Text(pageEstatisticasPlanejamentoIng, width=128, height=20)
    EstatisticasPlanejamentoTextIng.place(x=5, y=5)

    pageRecursosPlanejamentoIng = ttk.Frame(nbPlanejamentoIngpgsub)
    nbPlanejamentoIngpgsub.add(pageRecursosPlanejamentoIng, text="Recursos")

    RecursosPlanejamentoTextIng = Text(pageRecursosPlanejamentoIng, width=128, height=20)
    RecursosPlanejamentoTextIng.place(x=5, y=5)

    pageMetasGeraisPlanejamentoIng = ttk.Frame(nbPlanejamentoIngpgsub)
    nbPlanejamentoIngpgsub.add(pageMetasGeraisPlanejamentoIng, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextIng = Text(pageMetasGeraisPlanejamentoIng, width=128, height=20)
    MetasGeraisPlanejamentoTextIng.place(x=5, y=5)

    pagePlanejamentoEsp = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoEsp, text="Espanhol")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoEsp.rowconfigure(rows, weight=1)
        pagePlanejamentoEsp.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoEsppgsub = ttk.Notebook(pagePlanejamentoEsp)
    nbPlanejamentoEsppgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoEsp = ttk.Frame(nbPlanejamentoEsppgsub)
    nbPlanejamentoEsppgsub.add(pageConteudoPlanejamentoEsp, text="Conteúdo")

    ComponentePlanejamentoLabelEsp = Label(pageConteudoPlanejamentoEsp, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelEsp.place(x=1, y=5)

    ComponentePlanejamentoTextEsp = Text(pageConteudoPlanejamentoEsp, width=40, height=1)
    ComponentePlanejamentoTextEsp.place(x=80, y=5)

    DetalhesPlanejamentoTextEsp = Text(pageConteudoPlanejamentoEsp, width=128, height=18)
    DetalhesPlanejamentoTextEsp.place(x=5, y=30)

    pageObjetivoPlanejamentoEsp = ttk.Frame(nbPlanejamentoEsppgsub)
    nbPlanejamentoEsppgsub.add(pageObjetivoPlanejamentoEsp, text="Objetivo")

    ObjetivoPlanejamentoTextEsp = Text(pageObjetivoPlanejamentoEsp, width=128, height=20)
    ObjetivoPlanejamentoTextEsp.place(x=5, y=5)

    pageEstatisticasPlanejamentoEsp = ttk.Frame(nbPlanejamentoEsppgsub)
    nbPlanejamentoEsppgsub.add(pageEstatisticasPlanejamentoEsp, text="Estatísticas")

    EstatisticasPlanejamentoTextEsp = Text(pageEstatisticasPlanejamentoEsp, width=128, height=20)
    EstatisticasPlanejamentoTextEsp.place(x=5, y=5)

    pageRecursosPlanejamentoEsp = ttk.Frame(nbPlanejamentoEsppgsub)
    nbPlanejamentoEsppgsub.add(pageRecursosPlanejamentoEsp, text="Recursos")

    RecursosPlanejamentoTextEsp = Text(pageRecursosPlanejamentoEsp, width=128, height=20)
    RecursosPlanejamentoTextEsp.place(x=5, y=5)

    pageMetasGeraisPlanejamentoEsp = ttk.Frame(nbPlanejamentoEsppgsub)
    nbPlanejamentoEsppgsub.add(pageMetasGeraisPlanejamentoEsp, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextEsp = Text(pageMetasGeraisPlanejamentoEsp, width=128, height=20)
    MetasGeraisPlanejamentoTextEsp.place(x=5, y=5)

    pagePlanejamentoQui = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoQui, text="Química")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoQui.rowconfigure(rows, weight=1)
        pagePlanejamentoQui.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoQuipgsub = ttk.Notebook(pagePlanejamentoQui)
    nbPlanejamentoQuipgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoQui = ttk.Frame(nbPlanejamentoQuipgsub)
    nbPlanejamentoQuipgsub.add(pageConteudoPlanejamentoQui, text="Conteúdo")

    ComponentePlanejamentoLabelQui = Label(pageConteudoPlanejamentoQui, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelQui.place(x=1, y=5)

    ComponentePlanejamentoTextQui = Text(pageConteudoPlanejamentoQui, width=40, height=1)
    ComponentePlanejamentoTextQui.place(x=80, y=5)

    DetalhesPlanejamentoTextQui = Text(pageConteudoPlanejamentoQui, width=128, height=18)
    DetalhesPlanejamentoTextQui.place(x=5, y=30)

    pageObjetivoPlanejamentoQui = ttk.Frame(nbPlanejamentoQuipgsub)
    nbPlanejamentoQuipgsub.add(pageObjetivoPlanejamentoQui, text="Objetivo")

    ObjetivoPlanejamentoTextQui = Text(pageObjetivoPlanejamentoQui, width=128, height=20)
    ObjetivoPlanejamentoTextQui.place(x=5, y=5)

    pageEstatisticasPlanejamentoQui = ttk.Frame(nbPlanejamentoQuipgsub)
    nbPlanejamentoQuipgsub.add(pageEstatisticasPlanejamentoQui, text="Estatísticas")

    EstatisticasPlanejamentoTextQui = Text(pageEstatisticasPlanejamentoQui, width=128, height=20)
    EstatisticasPlanejamentoTextQui.place(x=5, y=5)

    pageRecursosPlanejamentoQui = ttk.Frame(nbPlanejamentoQuipgsub)
    nbPlanejamentoQuipgsub.add(pageRecursosPlanejamentoQui, text="Recursos")

    RecursosPlanejamentoTextQui = Text(pageRecursosPlanejamentoQui, width=128, height=20)
    RecursosPlanejamentoTextQui.place(x=5, y=5)

    pageMetasGeraisPlanejamentoQui = ttk.Frame(nbPlanejamentoQuipgsub)
    nbPlanejamentoQuipgsub.add(pageMetasGeraisPlanejamentoQui, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextQui = Text(pageMetasGeraisPlanejamentoQui, width=128, height=20)
    MetasGeraisPlanejamentoTextQui.place(x=5, y=5)

    pagePlanejamentoRed = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoRed, text="Redação")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePlanejamentoRed.rowconfigure(rows, weight=1)
        pagePlanejamentoRed.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPlanejamentoRedpgsub = ttk.Notebook(pagePlanejamentoRed)
    nbPlanejamentoRedpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPlanejamentoRed = ttk.Frame(nbPlanejamentoRedpgsub)
    nbPlanejamentoRedpgsub.add(pageConteudoPlanejamentoRed, text="Conteúdo")

    ComponentePlanejamentoLabelRed = Label(pageConteudoPlanejamentoRed, text="Componente:", font="Arial 8 bold")
    ComponentePlanejamentoLabelRed.place(x=1, y=5)

    ComponentePlanejamentoTextRed = Text(pageConteudoPlanejamentoRed, width=40, height=1)
    ComponentePlanejamentoTextRed.place(x=80, y=5)

    DetalhesPlanejamentoTextRed = Text(pageConteudoPlanejamentoRed, width=128, height=18)
    DetalhesPlanejamentoTextRed.place(x=5, y=30)

    pageObjetivoPlanejamentoRed = ttk.Frame(nbPlanejamentoRedpgsub)
    nbPlanejamentoRedpgsub.add(pageObjetivoPlanejamentoRed, text="Objetivo")

    ObjetivoPlanejamentoTextRed = Text(pageObjetivoPlanejamentoRed, width=128, height=20)
    ObjetivoPlanejamentoTextRed.place(x=5, y=5)

    pageEstatisticasPlanejamentoRed = ttk.Frame(nbPlanejamentoRedpgsub)
    nbPlanejamentoRedpgsub.add(pageEstatisticasPlanejamentoRed, text="Estatísticas")

    EstatisticasPlanejamentoTextRed = Text(pageEstatisticasPlanejamentoRed, width=128, height=20)
    EstatisticasPlanejamentoTextRed.place(x=5, y=5)

    pageRecursosPlanejamentoRed = ttk.Frame(nbPlanejamentoRedpgsub)
    nbPlanejamentoRedpgsub.add(pageRecursosPlanejamentoRed, text="Recursos")

    RecursosPlanejamentoTextRed = Text(pageRecursosPlanejamentoRed, width=128, height=20)
    RecursosPlanejamentoTextRed.place(x=5, y=5)

    pageMetasGeraisPlanejamentoRed = ttk.Frame(nbPlanejamentoRedpgsub)
    nbPlanejamentoRedpgsub.add(pageMetasGeraisPlanejamentoRed, text="Metas Gerais para a Turma")

    MetasGeraisPlanejamentoTextRed = Text(pageMetasGeraisPlanejamentoRed, width=128, height=20)
    MetasGeraisPlanejamentoTextRed.place(x=5, y=5)

    pagePlanejamentoEFPI = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoEFPI, text="Escuta, Fala, Pensamento e Imaginação")

    pagePlanejamentoPriVal = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamentoPriVal, text="Princípios e Valores")

    pagePlanejamento1 = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamento1, text="1")

    pagePlanejamento2 = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamento2, text="2")

    pagePlanejamento3 = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamento3, text="3")

    pagePlanejamento4 = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamento4, text="4")

    pagePlanejamento5 = ttk.Frame(nbPlanejamentopg)
    nbPlanejamentopg.add(pagePlanejamento5, text="5")



def abrirPNE():
    novoTrabalhoPNE = Toplevel()
    novoTrabalhoPNE.geometry('1090x620+260+70')
    novoTrabalhoPNE.resizable(False,False)
    novoTrabalhoPNE.title('Planejamento Pedagógico Anual PNE')
    novoTrabalhoPNE.configure(bg='sky blue')
    novoTrabalhoPNE.transient(trabalho)
    novoTrabalhoPNE.focus_force()
    novoTrabalhoPNE.grab_set()

    ValidarPeriodoButtonPNE = Button(novoTrabalhoPNE, text='Validar Período', font='negrito 9 bold', bg="Lime")
    ValidarPeriodoButtonPNE.place(x=985, y=35, width=100, height=31)

    PeriodoInicialPNELabel = Label(novoTrabalhoPNE, text="Período Inicial", font="Arial 8 bold", bg='sky blue', foreground='blue')
    PeriodoInicialPNELabel.place(x=725, y=20)

    PeriodoInicialPNE = tkinter.StringVar()
    PeriodoInicialPNEcbbx = ttk.Combobox(novoTrabalhoPNE, width=16, height=1, textvariable=PeriodoInicialPNE)
    PeriodoInicialPNEcbbx.place(x=725, y=40)

    PeriodoFinalPNELabel = Label(novoTrabalhoPNE, text="Período Final", font="Arial 8 bold", bg='sky blue', foreground='red')
    PeriodoFinalPNELabel.place(x=850, y=20)

    PeriodoFinalPNE = tkinter.StringVar()
    PeriodoFinalPNEcbbx = ttk.Combobox(novoTrabalhoPNE, width=16, height=1, textvariable=PeriodoFinalPNE)
    PeriodoFinalPNEcbbx.place(x=850, y=40)

    BimestrePNELabel = Label(novoTrabalhoPNE, text="Bimestre", bg='sky blue')
    BimestrePNELabel.place(x=625, y=20)

    BimestrePNE = tkinter.StringVar()
    BimestrePNEcbbx = ttk.Combobox(novoTrabalhoPNE, width=11, height=1, textvariable=BimestrePNE)
    BimestrePNEcbbx.place(x=625, y=40)

    SeriePNELabel = Label(novoTrabalhoPNE, text="Série", bg='sky blue')
    SeriePNELabel.place(x=410, y=20)

    SeriePNE = tkinter.StringVar()
    SeriePNEcbbx = ttk.Combobox(novoTrabalhoPNE, width=31, height=1, textvariable=SeriePNE)
    SeriePNEcbbx.place(x=410, y=40)

    TurmaPNELabel = Label(novoTrabalhoPNE, text="Turma", bg='sky blue')
    TurmaPNELabel.place(x=315, y=20)

    TurmaPNE = tkinter.StringVar()
    TurmaPNEcbbx = ttk.Combobox(novoTrabalhoPNE, width=11, height=1, textvariable=TurmaPNE)
    TurmaPNEcbbx.place(x=315, y=40)

    AlunoPNELabel = Label(novoTrabalhoPNE, text="Aluno", bg='sky blue')
    AlunoPNELabel.place(x=100, y=20)

    AlunoPNE = tkinter.StringVar()
    AlunoPNEcbbx = ttk.Combobox(novoTrabalhoPNE, width=31, height=1, textvariable=AlunoPNE)
    AlunoPNEcbbx.place(x=100, y=40)

    CodigoPNELabel = Label(novoTrabalhoPNE, text="Código", bg='sky blue', font="Arial 8 bold")
    CodigoPNELabel.place(x=10, y=20)

    CodigoPNEText = Text(novoTrabalhoPNE, width=10, height=1)
    CodigoPNEText.place(x=10, y=40)

    AlunoClassificadoPNEckbt = Checkbutton(novoTrabalhoPNE, text="Aluno Classificado com DI.", font="Arial 8 bold", bg='sky blue', width=20, anchor=W)
    AlunoClassificadoPNEckbt.place(x=100, y=61)

    fr_rolagemPNE = Frame(novoTrabalhoPNE, borderwidth=1, relief="solid")
    fr_rolagemPNE.place(x=7, y=90, width=1070, height=75)

    ### criando o canvas ###
    canvasPNE = Canvas(novoTrabalhoPNE)
    canvasPNE.place(x=8, y=91, width=1051, height=56)

    ### criando a barra de rolagem ###
    barra_de_rolagemPNEVert = ttk.Scrollbar(fr_rolagemPNE, orient=VERTICAL, command=canvasPNE.yview)
    barra_de_rolagemPNEVert.pack(side=RIGHT, fill=Y)

    barra_de_rolagemPNEHoriz = ttk.Scrollbar(fr_rolagemPNE, orient=HORIZONTAL, command=canvasPNE.xview)
    barra_de_rolagemPNEHoriz.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasPNE.configure(yscrollcommand=barra_de_rolagemPNEVert.set)
    canvasPNE.bind('<Configure>', lambda e: canvasPNE.configure(scrollregion=canvasPNE.bbox("all")))

    canvasPNE.configure(xscrollcommand=barra_de_rolagemPNEHoriz.set)
    canvasPNE.bind('<Configure>', lambda e: canvasPNE.configure(scrollregion=canvasPNE.bbox("all")))

    fr_rolagemPNE = Frame(canvasPNE)

    canvasPNE.create_window((0, 0), window=fr_rolagemPNE, anchor="nw")

    ### multipage ###
    rows = 0
    while rows < 50:
        novoTrabalhoPNE.rowconfigure(rows, weight=1)
        novoTrabalhoPNE.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEpg = ttk.Notebook(novoTrabalhoPNE)
    nbPNEpg.grid(row=16, column=0, columnspan=53, rowspan=48, sticky="NESW")

    pagePNEInst = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEInst, text="Instruções")

    fr_rolagemPNEInst = Frame(pagePNEInst, borderwidth=1, relief="solid")
    fr_rolagemPNEInst.place(x=7, y=5, width=1070, height=345)

    ### criando o canvas ###
    canvasPNEInst = Canvas(pagePNEInst)
    canvasPNEInst.place(x=8, y=6, width=1068, height=326)

    ### criando a barra de rolagem ###
    barra_de_rolagemPNEInstHoriz = ttk.Scrollbar(fr_rolagemPNEInst, orient=HORIZONTAL, command=canvasPNEInst.xview)
    barra_de_rolagemPNEInstHoriz.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasPNEInst.configure(xscrollcommand=barra_de_rolagemPNEInstHoriz.set)
    canvasPNEInst.bind('<Configure>', lambda e: canvasPNEInst.configure(scrollregion=canvasPNEInst.bbox("all")))

    fr_rolagemPNEInst = Frame(canvasPNEInst)

    canvasPNEInst.create_window((0, 0), window=fr_rolagemPNEInst, anchor="nw")

    Instrucao1 = Label(fr_rolagemPNEInst, text='1 - Considere adaptar uma rotina da turma/aluno no plano de aula para atender as nescessidades deste aluno', width=400, anchor=W, foreground='red')
    Instrucao1.grid(row=1, column=1)

    Instrucao2 = Label(fr_rolagemPNEInst, text='2 - Considere retirar o excesso de estímulos do ambiente da sala', width=400, anchor=W, foreground='red')
    Instrucao2.grid(row=2, column=1)

    Instrucao3 = Label(fr_rolagemPNEInst, text='3 - Considere adaptar o conteúdo como reduzir, fleibiilidade, dividir, ou adaptações com uso do concreto', width=400, anchor=W, foreground='red')
    Instrucao3.grid(row=3, column=1)

    Instrucao4 = Label(fr_rolagemPNEInst, text='4 - Adaptar os objetivos como reduzir ou flexibilizar', width=400, anchor=W, foreground='red')
    Instrucao4.grid(row=4, column=1)

    Instrucao5 = Label(fr_rolagemPNEInst, text='5 - Avaliar por meio de relatórios. por meio da oralidade, reduzir quantidades de questões, aumentar o tamanho das letras, substituir textos ou parte deles por imagens, usar letras caixa alta, oferecer t', width=400, anchor=W, foreground='red')
    Instrucao5.grid(row=5, column=1)

    pagePNEMat = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEMat, text="Matemática")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEMat.rowconfigure(rows, weight=1)
        pagePNEMat.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEpgsub = ttk.Notebook(pagePNEMat)
    nbPNEpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPNE = ttk.Frame(nbPNEpgsub)
    nbPNEpgsub.add(pageConteudoPNE, text="Conteúdo")

    ComponentePNELabel = Label(pageConteudoPNE, text="Componente:", font="Arial 8 bold")
    ComponentePNELabel.place(x=1, y=5)

    ComponentePNEText = Text(pageConteudoPNE, width=40, height=1)
    ComponentePNEText.place(x=80, y=5)

    DetalhesPNEText = Text(pageConteudoPNE, width=128, height=18)
    DetalhesPNEText.place(x=5, y=30)

    pageObjetivoPNE = ttk.Frame(nbPNEpgsub)
    nbPNEpgsub.add(pageObjetivoPNE, text="Objetivo")

    ObjetivoPNEText = Text(pageObjetivoPNE, width=128, height=19)
    ObjetivoPNEText.place(x=5, y=5)

    pageEstatisticasPNE = ttk.Frame(nbPNEpgsub)
    nbPNEpgsub.add(pageEstatisticasPNE, text="Estatísticas")

    EstatisticasPNEText = Text(pageEstatisticasPNE, width=128, height=19)
    EstatisticasPNEText.place(x=5, y=5)

    pageRecursosPNE = ttk.Frame(nbPNEpgsub)
    nbPNEpgsub.add(pageRecursosPNE, text="Recursos")

    RecursosPNEText = Text(pageRecursosPNE, width=128, height=19)
    RecursosPNEText.place(x=5, y=5)

    pageMetasGeraisPNE = ttk.Frame(nbPNEpgsub)
    nbPNEpgsub.add(pageMetasGeraisPNE, text="Metas Gerais para a Turma")

    MetasGeraisPNEText = Text(pageMetasGeraisPNE, width=128, height=19)
    MetasGeraisPNEText.place(x=5, y=5)

    pagePNEPort = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEPort, text="Português")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEPort.rowconfigure(rows, weight=1)
        pagePNEPort.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEPortpgsub = ttk.Notebook(pagePNEPort)
    nbPNEPortpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoPortPNE = ttk.Frame(nbPNEPortpgsub)
    nbPNEPortpgsub.add(pageConteudoPortPNE, text="Conteúdo")

    ComponentePortPNELabel = Label(pageConteudoPortPNE, text="Componente:", font="Arial 8 bold")
    ComponentePortPNELabel.place(x=1, y=5)

    ComponentePortPNEText = Text(pageConteudoPortPNE, width=40, height=1)
    ComponentePortPNEText.place(x=80, y=5)

    DetalhesPortPNEText = Text(pageConteudoPortPNE, width=128, height=18)
    DetalhesPortPNEText.place(x=5, y=30)

    pageObjetivoPortPNE = ttk.Frame(nbPNEPortpgsub)
    nbPNEPortpgsub.add(pageObjetivoPortPNE, text="Objetivo")

    ObjetivoPortPNEText = Text(pageObjetivoPortPNE, width=128, height=19)
    ObjetivoPortPNEText.place(x=5, y=5)

    pageEstatisticasPortPNE = ttk.Frame(nbPNEPortpgsub)
    nbPNEPortpgsub.add(pageEstatisticasPortPNE, text="Estatísticas")

    EstatisticasPortPNEText = Text(pageEstatisticasPortPNE, width=128, height=19)
    EstatisticasPortPNEText.place(x=5, y=5)

    pageRecursosPortPNE = ttk.Frame(nbPNEPortpgsub)
    nbPNEPortpgsub.add(pageRecursosPortPNE, text="Recursos")

    RecursosPortPNEText = Text(pageRecursosPortPNE, width=128, height=19)
    RecursosPortPNEText.place(x=5, y=5)

    pageMetasGeraisPortPNE = ttk.Frame(nbPNEPortpgsub)
    nbPNEPortpgsub.add(pageMetasGeraisPortPNE, text="Metas Gerais para a Turma")

    MetasGeraisPortPNEText = Text(pageMetasGeraisPortPNE, width=128, height=19)
    MetasGeraisPortPNEText.place(x=5, y=5)

    pagePNECie = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNECie, text="Ciêcias")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNECie.rowconfigure(rows, weight=1)
        pagePNECie.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNECiepgsub = ttk.Notebook(pagePNECie)
    nbPNECiepgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoCiePNE = ttk.Frame(nbPNECiepgsub)
    nbPNECiepgsub.add(pageConteudoCiePNE, text="Conteúdo")

    ComponenteCiePNELabel = Label(pageConteudoCiePNE, text="Componente:", font="Arial 8 bold")
    ComponenteCiePNELabel.place(x=1, y=5)

    ComponenteCiePNEText = Text(pageConteudoCiePNE, width=40, height=1)
    ComponenteCiePNEText.place(x=80, y=5)

    DetalhesCiePNEText = Text(pageConteudoCiePNE, width=128, height=18)
    DetalhesCiePNEText.place(x=5, y=30)

    pageObjetivoCiePNE = ttk.Frame(nbPNECiepgsub)
    nbPNECiepgsub.add(pageObjetivoCiePNE, text="Objetivo")

    ObjetivoCiePNEText = Text(pageObjetivoCiePNE, width=128, height=19)
    ObjetivoCiePNEText.place(x=5, y=5)

    pageEstatisticasCiePNE = ttk.Frame(nbPNECiepgsub)
    nbPNECiepgsub.add(pageEstatisticasCiePNE, text="Estatísticas")

    EstatisticasCiePNEText = Text(pageEstatisticasCiePNE, width=128, height=19)
    EstatisticasCiePNEText.place(x=5, y=5)

    pageRecursosCiePNE = ttk.Frame(nbPNECiepgsub)
    nbPNECiepgsub.add(pageRecursosCiePNE, text="Recursos")

    RecursosCiePNEText = Text(pageRecursosCiePNE, width=128, height=19)
    RecursosCiePNEText.place(x=5, y=5)

    pageMetasGeraisCiePNE = ttk.Frame(nbPNECiepgsub)
    nbPNECiepgsub.add(pageMetasGeraisCiePNE, text="Metas Gerais para a Turma")

    MetasGeraisCiePNEText = Text(pageMetasGeraisCiePNE, width=128, height=19)
    MetasGeraisCiePNEText.place(x=5, y=5)

    pagePNEHist = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEHist, text="História")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEHist.rowconfigure(rows, weight=1)
        pagePNEHist.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEHistpgsub = ttk.Notebook(pagePNEHist)
    nbPNEHistpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoHistPNE = ttk.Frame(nbPNEHistpgsub)
    nbPNEHistpgsub.add(pageConteudoHistPNE, text="Conteúdo")

    ComponenteHistPNELabel = Label(pageConteudoHistPNE, text="Componente:", font="Arial 8 bold")
    ComponenteHistPNELabel.place(x=1, y=5)

    ComponenteHistPNEText = Text(pageConteudoHistPNE, width=40, height=1)
    ComponenteHistPNEText.place(x=80, y=5)

    DetalhesHistPNEText = Text(pageConteudoHistPNE, width=128, height=18)
    DetalhesHistPNEText.place(x=5, y=30)

    pageObjetivoHistPNE = ttk.Frame(nbPNEHistpgsub)
    nbPNEHistpgsub.add(pageObjetivoHistPNE, text="Objetivo")

    ObjetivoHistPNEText = Text(pageObjetivoHistPNE, width=128, height=19)
    ObjetivoHistPNEText.place(x=5, y=5)

    pageEstatisticasHistPNE = ttk.Frame(nbPNEHistpgsub)
    nbPNEHistpgsub.add(pageEstatisticasHistPNE, text="Estatísticas")

    EstatisticasHistPNEText = Text(pageEstatisticasHistPNE, width=128, height=19)
    EstatisticasHistPNEText.place(x=5, y=5)

    pageRecursosHistPNE = ttk.Frame(nbPNEHistpgsub)
    nbPNEHistpgsub.add(pageRecursosHistPNE, text="Recursos")

    RecursosHistPNEText = Text(pageRecursosHistPNE, width=128, height=19)
    RecursosHistPNEText.place(x=5, y=5)

    pageMetasGeraisHistPNE = ttk.Frame(nbPNEHistpgsub)
    nbPNEHistpgsub.add(pageMetasGeraisHistPNE, text="Metas Gerais para a Turma")

    MetasGeraisHistPNEText = Text(pageMetasGeraisHistPNE, width=128, height=19)
    MetasGeraisHistPNEText.place(x=5, y=5)

    pagePNEGeo = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEGeo, text="Geografia")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEGeo.rowconfigure(rows, weight=1)
        pagePNEGeo.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEGeopgsub = ttk.Notebook(pagePNEGeo)
    nbPNEGeopgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoGeoPNE = ttk.Frame(nbPNEGeopgsub)
    nbPNEGeopgsub.add(pageConteudoGeoPNE, text="Conteúdo")

    ComponenteGeoPNELabel = Label(pageConteudoGeoPNE, text="Componente:", font="Arial 8 bold")
    ComponenteGeoPNELabel.place(x=1, y=5)

    ComponenteGeoPNEText = Text(pageConteudoGeoPNE, width=40, height=1)
    ComponenteGeoPNEText.place(x=80, y=5)

    DetalhesGeoPNEText = Text(pageConteudoGeoPNE, width=128, height=18)
    DetalhesGeoPNEText.place(x=5, y=30)

    pageObjetivoGeoPNE = ttk.Frame(nbPNEGeopgsub)
    nbPNEGeopgsub.add(pageObjetivoGeoPNE, text="Objetivo")

    ObjetivoGeoPNEText = Text(pageObjetivoGeoPNE, width=128, height=19)
    ObjetivoGeoPNEText.place(x=5, y=5)

    pageEstatisticasGeoPNE = ttk.Frame(nbPNEGeopgsub)
    nbPNEGeopgsub.add(pageEstatisticasGeoPNE, text="Estatísticas")

    EstatisticasGeoPNEText = Text(pageEstatisticasGeoPNE, width=128, height=19)
    EstatisticasGeoPNEText.place(x=5, y=5)

    pageRecursosGeoPNE = ttk.Frame(nbPNEGeopgsub)
    nbPNEGeopgsub.add(pageRecursosGeoPNE, text="Recursos")

    RecursosGeoPNEText = Text(pageRecursosGeoPNE, width=128, height=19)
    RecursosGeoPNEText.place(x=5, y=5)

    pageMetasGeraisGeoPNE = ttk.Frame(nbPNEGeopgsub)
    nbPNEGeopgsub.add(pageMetasGeraisGeoPNE, text="Metas Gerais para a Turma")

    MetasGeraisGeoPNEText = Text(pageMetasGeraisGeoPNE, width=128, height=19)
    MetasGeraisGeoPNEText.place(x=5, y=5)

    pagePNEArte = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEArte, text="Arte")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEArte.rowconfigure(rows, weight=1)
        pagePNEArte.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEArtpgsub = ttk.Notebook(pagePNEArte)
    nbPNEArtpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoArtPNE = ttk.Frame(nbPNEArtpgsub)
    nbPNEArtpgsub.add(pageConteudoArtPNE, text="Conteúdo")

    ComponenteArtPNELabel = Label(pageConteudoArtPNE, text="Componente:", font="Arial 8 bold")
    ComponenteArtPNELabel.place(x=1, y=5)

    ComponenteArtPNEText = Text(pageConteudoArtPNE, width=40, height=1)
    ComponenteArtPNEText.place(x=80, y=5)

    DetalhesArtPNEText = Text(pageConteudoArtPNE, width=128, height=18)
    DetalhesArtPNEText.place(x=5, y=30)

    pageObjetivoArtPNE = ttk.Frame(nbPNEArtpgsub)
    nbPNEArtpgsub.add(pageObjetivoArtPNE, text="Objetivo")

    ObjetivoArtPNEText = Text(pageObjetivoArtPNE, width=128, height=19)
    ObjetivoArtPNEText.place(x=5, y=5)

    pageEstatisticasArtPNE = ttk.Frame(nbPNEArtpgsub)
    nbPNEArtpgsub.add(pageEstatisticasArtPNE, text="Estatísticas")

    EstatisticasArtPNEText = Text(pageEstatisticasArtPNE, width=128, height=19)
    EstatisticasArtPNEText.place(x=5, y=5)

    pageRecursosArtPNE = ttk.Frame(nbPNEArtpgsub)
    nbPNEArtpgsub.add(pageRecursosArtPNE, text="Recursos")

    RecursosArtPNEText = Text(pageRecursosArtPNE, width=128, height=19)
    RecursosArtPNEText.place(x=5, y=5)

    pageMetasGeraisArtPNE = ttk.Frame(nbPNEArtpgsub)
    nbPNEArtpgsub.add(pageMetasGeraisArtPNE, text="Metas Gerais para a Turma")

    MetasGeraisArtPNEText = Text(pageMetasGeraisArtPNE, width=128, height=19)
    MetasGeraisArtPNEText.place(x=5, y=5)

    pagePNEEdFis = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEEdFis, text="Ed.Física")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEEdFis.rowconfigure(rows, weight=1)
        pagePNEEdFis.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEEdFispgsub = ttk.Notebook(pagePNEEdFis)
    nbPNEEdFispgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoEdFisPNE = ttk.Frame(nbPNEEdFispgsub)
    nbPNEEdFispgsub.add(pageConteudoEdFisPNE, text="Conteúdo")

    ComponenteEdFisPNELabel = Label(pageConteudoEdFisPNE, text="Componente:", font="Arial 8 bold")
    ComponenteEdFisPNELabel.place(x=1, y=5)

    ComponenteEdFisPNEText = Text(pageConteudoEdFisPNE, width=40, height=1)
    ComponenteEdFisPNEText.place(x=80, y=5)

    DetalhesEdFisPNEText = Text(pageConteudoEdFisPNE, width=128, height=18)
    DetalhesEdFisPNEText.place(x=5, y=30)

    pageObjetivoEdFisPNE = ttk.Frame(nbPNEEdFispgsub)
    nbPNEEdFispgsub.add(pageObjetivoEdFisPNE, text="Objetivo")

    ObjetivoEdFisPNEText = Text(pageObjetivoEdFisPNE, width=128, height=19)
    ObjetivoEdFisPNEText.place(x=5, y=5)

    pageEstatisticasEdFisPNE = ttk.Frame(nbPNEEdFispgsub)
    nbPNEEdFispgsub.add(pageEstatisticasEdFisPNE, text="Estatísticas")

    EstatisticasEdFisPNEText = Text(pageEstatisticasEdFisPNE, width=128, height=19)
    EstatisticasEdFisPNEText.place(x=5, y=5)

    pageRecursosEdFisPNE = ttk.Frame(nbPNEEdFispgsub)
    nbPNEEdFispgsub.add(pageRecursosEdFisPNE, text="Recursos")

    RecursosEdFisPNEText = Text(pageRecursosEdFisPNE, width=128, height=19)
    RecursosEdFisPNEText.place(x=5, y=5)

    pageMetasGeraisEdFisPNE = ttk.Frame(nbPNEEdFispgsub)
    nbPNEEdFispgsub.add(pageMetasGeraisEdFisPNE, text="Metas Gerais para a Turma")

    MetasGeraisEdFisPNEText = Text(pageMetasGeraisEdFisPNE, width=128, height=19)
    MetasGeraisEdFisPNEText.place(x=5, y=5)

    pagePNERel = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNERel, text="Religião")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNERel.rowconfigure(rows, weight=1)
        pagePNERel.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNERelpgsub = ttk.Notebook(pagePNERel)
    nbPNERelpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoRelPNE = ttk.Frame(nbPNERelpgsub)
    nbPNERelpgsub.add(pageConteudoRelPNE, text="Conteúdo")

    ComponenteRelPNELabel = Label(pageConteudoRelPNE, text="Componente:", font="Arial 8 bold")
    ComponenteRelPNELabel.place(x=1, y=5)

    ComponenteRelPNEText = Text(pageConteudoRelPNE, width=40, height=1)
    ComponenteRelPNEText.place(x=80, y=5)

    DetalhesRelPNEText = Text(pageConteudoRelPNE, width=128, height=18)
    DetalhesRelPNEText.place(x=5, y=30)

    pageObjetivoRelPNE = ttk.Frame(nbPNERelpgsub)
    nbPNERelpgsub.add(pageObjetivoRelPNE, text="Objetivo")

    ObjetivoRelPNEText = Text(pageObjetivoRelPNE, width=128, height=19)
    ObjetivoRelPNEText.place(x=5, y=5)

    pageEstatisticasRelPNE = ttk.Frame(nbPNERelpgsub)
    nbPNERelpgsub.add(pageEstatisticasRelPNE, text="Estatísticas")

    EstatisticasRelPNEText = Text(pageEstatisticasRelPNE, width=128, height=19)
    EstatisticasRelPNEText.place(x=5, y=5)

    pageRecursosRelPNE = ttk.Frame(nbPNERelpgsub)
    nbPNERelpgsub.add(pageRecursosRelPNE, text="Recursos")

    RecursosRelPNEText = Text(pageRecursosRelPNE, width=128, height=19)
    RecursosRelPNEText.place(x=5, y=5)

    pageMetasGeraisRelPNE = ttk.Frame(nbPNERelpgsub)
    nbPNERelpgsub.add(pageMetasGeraisRelPNE, text="Metas Gerais para a Turma")

    MetasGeraisRelPNEText = Text(pageMetasGeraisRelPNE, width=128, height=19)
    MetasGeraisRelPNEText.place(x=5, y=5)

    pagePNEIng = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEIng, text="Inglês")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEIng.rowconfigure(rows, weight=1)
        pagePNEIng.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEIngpgsub = ttk.Notebook(pagePNEIng)
    nbPNEIngpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoIngPNE = ttk.Frame(nbPNEIngpgsub)
    nbPNEIngpgsub.add(pageConteudoIngPNE, text="Conteúdo")

    ComponenteIngPNELabel = Label(pageConteudoIngPNE, text="Componente:", font="Arial 8 bold")
    ComponenteIngPNELabel.place(x=1, y=5)

    ComponenteIngPNEText = Text(pageConteudoIngPNE, width=40, height=1)
    ComponenteIngPNEText.place(x=80, y=5)

    DetalhesIngPNEText = Text(pageConteudoIngPNE, width=128, height=18)
    DetalhesIngPNEText.place(x=5, y=30)

    pageObjetivoIngPNE = ttk.Frame(nbPNEIngpgsub)
    nbPNEIngpgsub.add(pageObjetivoIngPNE, text="Objetivo")

    ObjetivoIngPNEText = Text(pageObjetivoIngPNE, width=128, height=19)
    ObjetivoIngPNEText.place(x=5, y=5)

    pageEstatisticasIngPNE = ttk.Frame(nbPNEIngpgsub)
    nbPNEIngpgsub.add(pageEstatisticasIngPNE, text="Estatísticas")

    EstatisticasIngPNEText = Text(pageEstatisticasIngPNE, width=128, height=19)
    EstatisticasIngPNEText.place(x=5, y=5)

    pageRecursosIngPNE = ttk.Frame(nbPNEIngpgsub)
    nbPNEIngpgsub.add(pageRecursosIngPNE, text="Recursos")

    RecursosIngPNEText = Text(pageRecursosIngPNE, width=128, height=19)
    RecursosIngPNEText.place(x=5, y=5)

    pageMetasGeraisIngPNE = ttk.Frame(nbPNEIngpgsub)
    nbPNEIngpgsub.add(pageMetasGeraisIngPNE, text="Metas Gerais para a Turma")

    MetasGeraisIngPNEText = Text(pageMetasGeraisIngPNE, width=128, height=19)
    MetasGeraisIngPNEText.place(x=5, y=5)

    pagePNEEsp = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEEsp, text="Espanhol")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEEsp.rowconfigure(rows, weight=1)
        pagePNEEsp.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEEsppgsub = ttk.Notebook(pagePNEEsp)
    nbPNEEsppgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoEspPNE = ttk.Frame(nbPNEEsppgsub)
    nbPNEEsppgsub.add(pageConteudoEspPNE, text="Conteúdo")

    ComponenteEspPNELabel = Label(pageConteudoEspPNE, text="Componente:", font="Arial 8 bold")
    ComponenteEspPNELabel.place(x=1, y=5)

    ComponenteEspPNEText = Text(pageConteudoEspPNE, width=40, height=1)
    ComponenteEspPNEText.place(x=80, y=5)

    DetalhesEspPNEText = Text(pageConteudoEspPNE, width=128, height=18)
    DetalhesEspPNEText.place(x=5, y=30)

    pageObjetivoEspPNE = ttk.Frame(nbPNEEsppgsub)
    nbPNEEsppgsub.add(pageObjetivoEspPNE, text="Objetivo")

    ObjetivoEspPNEText = Text(pageObjetivoEspPNE, width=128, height=19)
    ObjetivoEspPNEText.place(x=5, y=5)

    pageEstatisticasEspPNE = ttk.Frame(nbPNEEsppgsub)
    nbPNEEsppgsub.add(pageEstatisticasEspPNE, text="Estatísticas")

    EstatisticasEspPNEText = Text(pageEstatisticasEspPNE, width=128, height=19)
    EstatisticasEspPNEText.place(x=5, y=5)

    pageRecursosEspPNE = ttk.Frame(nbPNEEsppgsub)
    nbPNEEsppgsub.add(pageRecursosEspPNE, text="Recursos")

    RecursosEspPNEText = Text(pageRecursosEspPNE, width=128, height=19)
    RecursosEspPNEText.place(x=5, y=5)

    pageMetasGeraisEspPNE = ttk.Frame(nbPNEEsppgsub)
    nbPNEEsppgsub.add(pageMetasGeraisEspPNE, text="Metas Gerais para a Turma")

    MetasGeraisEspPNEText = Text(pageMetasGeraisEspPNE, width=128, height=19)
    MetasGeraisEspPNEText.place(x=5, y=5)

    pagePNEQui = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEQui, text="Química")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNEQui.rowconfigure(rows, weight=1)
        pagePNEQui.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNEQuipgsub = ttk.Notebook(pagePNEQui)
    nbPNEQuipgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoQuiPNE = ttk.Frame(nbPNEQuipgsub)
    nbPNEQuipgsub.add(pageConteudoQuiPNE, text="Conteúdo")

    ComponenteQuiPNELabel = Label(pageConteudoQuiPNE, text="Componente:", font="Arial 8 bold")
    ComponenteQuiPNELabel.place(x=1, y=5)

    ComponenteQuiPNEText = Text(pageConteudoQuiPNE, width=40, height=1)
    ComponenteQuiPNEText.place(x=80, y=5)

    DetalhesQuiPNEText = Text(pageConteudoQuiPNE, width=128, height=18)
    DetalhesQuiPNEText.place(x=5, y=30)

    pageObjetivoQuiPNE = ttk.Frame(nbPNEQuipgsub)
    nbPNEQuipgsub.add(pageObjetivoQuiPNE, text="Objetivo")

    ObjetivoQuiPNEText = Text(pageObjetivoQuiPNE, width=128, height=19)
    ObjetivoQuiPNEText.place(x=5, y=5)

    pageEstatisticasQuiPNE = ttk.Frame(nbPNEQuipgsub)
    nbPNEQuipgsub.add(pageEstatisticasQuiPNE, text="Estatísticas")

    EstatisticasQuiPNEText = Text(pageEstatisticasQuiPNE, width=128, height=19)
    EstatisticasQuiPNEText.place(x=5, y=5)

    pageRecursosQuiPNE = ttk.Frame(nbPNEQuipgsub)
    nbPNEQuipgsub.add(pageRecursosQuiPNE, text="Recursos")

    RecursosQuiPNEText = Text(pageRecursosQuiPNE, width=128, height=19)
    RecursosQuiPNEText.place(x=5, y=5)

    pageMetasGeraisQuiPNE = ttk.Frame(nbPNEQuipgsub)
    nbPNEQuipgsub.add(pageMetasGeraisQuiPNE, text="Metas Gerais para a Turma")

    MetasGeraisQuiPNEText = Text(pageMetasGeraisQuiPNE, width=128, height=19)
    MetasGeraisQuiPNEText.place(x=5, y=5)

    pagePNERed = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNERed, text="Redação")

    ### multipage ###
    rows = 0
    while rows < 50:
        pagePNERed.rowconfigure(rows, weight=1)
        pagePNERed.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbPNERedpgsub = ttk.Notebook(pagePNERed)
    nbPNERedpgsub.grid(row=0, column=1, columnspan=48, rowspan=48, sticky="NESW")

    pageConteudoRedPNE = ttk.Frame(nbPNERedpgsub)
    nbPNERedpgsub.add(pageConteudoRedPNE, text="Conteúdo")

    ComponenteRedPNELabel = Label(pageConteudoRedPNE, text="Componente:", font="Arial 8 bold")
    ComponenteRedPNELabel.place(x=1, y=5)

    ComponenteRedPNEText = Text(pageConteudoRedPNE, width=40, height=1)
    ComponenteRedPNEText.place(x=80, y=5)

    DetalhesRedPNEText = Text(pageConteudoRedPNE, width=128, height=18)
    DetalhesRedPNEText.place(x=5, y=30)

    pageObjetivoRedPNE = ttk.Frame(nbPNERedpgsub)
    nbPNERedpgsub.add(pageObjetivoRedPNE, text="Objetivo")

    ObjetivoRedPNEText = Text(pageObjetivoRedPNE, width=128, height=19)
    ObjetivoRedPNEText.place(x=5, y=5)

    pageEstatisticasRedPNE = ttk.Frame(nbPNERedpgsub)
    nbPNERedpgsub.add(pageEstatisticasRedPNE, text="Estatísticas")

    EstatisticasRedPNEText = Text(pageEstatisticasRedPNE, width=128, height=19)
    EstatisticasRedPNEText.place(x=5, y=5)

    pageRecursosRedPNE = ttk.Frame(nbPNERedpgsub)
    nbPNERedpgsub.add(pageRecursosRedPNE, text="Recursos")

    RecursosRedPNEText = Text(pageRecursosRedPNE, width=128, height=19)
    RecursosRedPNEText.place(x=5, y=5)

    pageMetasGeraisRedPNE = ttk.Frame(nbPNERedpgsub)
    nbPNERedpgsub.add(pageMetasGeraisRedPNE, text="Metas Gerais para a Turma")

    MetasGeraisRedPNEText = Text(pageMetasGeraisRedPNE, width=128, height=19)
    MetasGeraisRedPNEText.place(x=5, y=5)

    pagePNEEFPI = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEEFPI, text="Escuta, Fala, Pensamento e Imaginação")



    pagePNEPriVal = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNEPriVal, text="Princípios e Valores")



    pagePNE1 = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNE1, text="1")

    pagePNE2 = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNE2, text="2")

    pagePNE3 = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNE3, text="3")

    pagePNE4 = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNE4, text="4")

    pagePNE5 = ttk.Frame(nbPNEpg)
    nbPNEpg.add(pagePNE5, text="5")

def abrirSondagem():
    novoTrabalhoSondagem = Toplevel()
    novoTrabalhoSondagem.geometry('1090x620+260+70')
    novoTrabalhoSondagem.resizable(False,False)
    novoTrabalhoSondagem.title('Sondagem - Tipo de Aprendizagem')
    novoTrabalhoSondagem.configure(bg='light gray')
    novoTrabalhoSondagem.transient(trabalho)
    novoTrabalhoSondagem.focus_force()
    novoTrabalhoSondagem.grab_set()

    ResultadoLabelSondagem = Label(novoTrabalhoSondagem, text='Resultado', bg='black', font='negrito 17 bold', foreground='white')
    ResultadoLabelSondagem.place(x=755, y=10, width=328, height=40)

    imgGraficoSondagem = Label(novoTrabalhoSondagem, image=imgGrafico)
    imgGraficoSondagem.place(x=755, y=50, width=328, height=285)

    IdentificacaoLabelSondagem = Label(novoTrabalhoSondagem, text='Identificação', bg='light grey', foreground='blue')
    IdentificacaoLabelSondagem.place(x=10, y=10)

    RALabelSondagem = Label(novoTrabalhoSondagem, text='RA', bg='light grey')
    RALabelSondagem.place(x=18, y=35)

    MatriculaTextSondagem = Text(novoTrabalhoSondagem, bg='light yellow', width=6, height=1)
    MatriculaTextSondagem.place(x=20, y=55)

    AlunoLabelSondagem = Label(novoTrabalhoSondagem, text='Aluno', bg='light grey')
    AlunoLabelSondagem.place(x=77, y=35)

    AlunoSondagem = tkinter.StringVar()
    AlunoSondagemcbbx = ttk.Combobox(novoTrabalhoSondagem, width=40, height=1, textvariable=AlunoSondagem)
    AlunoSondagemcbbx.place(x=77, y=55)

    NivelEscolarLabelSondagem = Label(novoTrabalhoSondagem, text='Nível Escolar', bg='light grey')
    NivelEscolarLabelSondagem.place(x=345, y=35)

    NivelEscolarTextSondagem = Text(novoTrabalhoSondagem, width=25, height=1)
    NivelEscolarTextSondagem.place(x=345, y=55)

    TurmaLabelSondagem = Label(novoTrabalhoSondagem, text='Turma', bg='light grey')
    TurmaLabelSondagem.place(x=555, y=35)

    TurmaTextSondagem = Text(novoTrabalhoSondagem, width=10, height=1)
    TurmaTextSondagem.place(x=555, y=55)

    Aluno_FotoSondagem = Label(novoTrabalhoSondagem, image=imgFoto_Aluno)
    Aluno_FotoSondagem.place(x=656, y=10, width=87)

    FrameAzulSondagem = Frame(novoTrabalhoSondagem, bg='lightsteelblue')
    FrameAzulSondagem.place(x=755, y=340, width=330, height=185)

    AnaliseTurmaLabelSondagem = Label(FrameAzulSondagem, text='Analise somente da Turma', bg='lightsteelblue')
    AnaliseTurmaLabelSondagem.place(x=100, y=1)

    AnaliseTurmaSondagem = tkinter.StringVar()
    AnaliseTurmaSondagemcbbx = ttk.Combobox(FrameAzulSondagem, width=21, height=1, textvariable=AnaliseTurmaSondagem)
    AnaliseTurmaSondagemcbbx.place(x=100, y=19)

    VisualLabelSondagem = Label(FrameAzulSondagem, text='Visual', foreground='blue', font="Arial 9 bold", bg='lightsteelblue')
    VisualLabelSondagem.place(x=165, y=45)

    VisualTextSondagem = Text(FrameAzulSondagem, width=5, height=1, bg='blue', foreground='white')
    VisualTextSondagem.place(x=120, y=45)

    AuditivoLabelSondagem = Label(FrameAzulSondagem, text='Auditivo', foreground='darkred', font="Arial 9 bold", bg='lightsteelblue')
    AuditivoLabelSondagem.place(x=165, y=68)

    AuditivoTextSondagem = Text(FrameAzulSondagem, width=5, height=1, bg='darkred', foreground='white')
    AuditivoTextSondagem.place(x=120, y=68)

    CinestesicoLabelSondagem = Label(FrameAzulSondagem, text='Cinestésico', foreground='darkgreen', font="Arial 9 bold", bg='lightsteelblue')
    CinestesicoLabelSondagem.place(x=165, y=91)

    CinestesicoTextSondagem = Text(FrameAzulSondagem, width=5, height=1, bg='darkgreen', foreground='white')
    CinestesicoTextSondagem.place(x=120, y=91)

    ATurmaLabelSondagem = Label(FrameAzulSondagem, text='A Turma é:', foreground='black', font="Arial 9 bold", bg='lightsteelblue')
    ATurmaLabelSondagem.place(x=140, y=116)

    ATurmaeTextSondagem = Text(FrameAzulSondagem, width=27, height=1, bg='white')
    ATurmaeTextSondagem.place(x=60, y=136)

    ### multipage ###
    rows = 0
    while rows < 50:
        novoTrabalhoSondagem.rowconfigure(rows, weight=1)
        novoTrabalhoSondagem.columnconfigure(rows, weight=1)
        rows += 1
    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbSondagem = ttk.Notebook(novoTrabalhoSondagem)
    nbSondagem.grid(row=12, column=0, columnspan=31, rowspan=38, sticky="NESW")

    ### page1 ###
    pageSondagem1 = ttk.Frame(nbSondagem)
    nbSondagem.add(pageSondagem1, text="Lista")

### criando frame ###
    fr_rolagemSondagem = Frame(pageSondagem1, borderwidth=1, relief="solid")
    fr_rolagemSondagem.place(x=1, y=10, width=705, height=395)

    ### criando o canvas ###
    canvasSondagem = Canvas(pageSondagem1)
    canvasSondagem.place(x=2, y=11, width=675, height=393)

    ### criando a barra de rolagem ###
    barra_de_rolagemSondagem = ttk.Scrollbar(fr_rolagemSondagem, orient=VERTICAL, command=canvasSondagem.yview)
    barra_de_rolagemSondagem.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasSondagem.configure(yscrollcommand=barra_de_rolagemSondagem.set)
    canvasSondagem.bind('<Configure>', lambda e: canvasSondagem.configure(scrollregion=canvasSondagem.bbox("all")))

    fr_rolagemSondagem = Frame(canvasSondagem)

    canvasSondagem.create_window((0, 0), window=fr_rolagemSondagem, anchor="nw")

    BotaoRestaurarListaSondagem = Button(pageSondagem1, text='Restaura Lista', font='negrito 8 bold', bg="lightgoldenrodyellow")
    BotaoRestaurarListaSondagem.place(x=625, y=420, width=90, height=31)

    ### page2 ###
    pageSondagem2 = ttk.Frame(nbSondagem)
    nbSondagem.add(pageSondagem2, text="Visual")

    FundoSondagem2 = Frame(pageSondagem2, bg='blue')
    FundoSondagem2.place(x=1, y=1, width=800, height=450)

    VisualSondagem = Label(pageSondagem2, text="Os Visuais: Na sala de aula, os alunos visuais gostam de de sentar nas\nprimeiras carteiras e precisam de silêncio para se concentrar.\nFacilmente interpretam gráficos, mapas e aritigos e aprendem\nmelhor se desenham, fazem anotações grifam e sublinham\nmomentos importantes de um texto, por exemplo. Procure\nrecursos visuais sobre as matérias estudadas, tente fazer\nresumos usando anotações, tabelas, esquemas, desenhos,\nfluxogramas, gráficos e outros recursos parecidos, visualize os\ngestos do professor, o modo como ele ensina, pois, na hora de\nlembrar sobre determinado assunto, você poderá visualizar o\nmodo como foi passada a informação, tente construir imagens\nmentais sobre o que estiver estudando, dê importância às\nleituras, principalmente às que contêm esquemas e resumos\ngráficos." , font="Arial 17", bg='blue', foreground='white', justify=LEFT, anchor=NW)
    VisualSondagem.place(x=0, y=1, width=743, height=450)

    ### page3 ###
    pageSondagem3 = ttk.Frame(nbSondagem)
    nbSondagem.add(pageSondagem3, text="Auditivo")

    FundoSondagem3 = Frame(pageSondagem3, bg='darkred')
    FundoSondagem3.place(x=1, y=1, width=800, height=450)

    VisualSondagem = Label(pageSondagem3, text="Os Auditivos: Os alunos auditivos preferem ouvir a ler coisas. Eles\ncostumam repetir conteúdos em voz alta, com os olhos\nfechados e, para completar o exercício de memorização,\npreferem criar associações de palavras. Bom para explicar ideias\nem voz alta, capacidade de compreender as mudanças no tom\nde voz, hábil em relatórios orais e a presentações acadêmicas,\nsem medo de falar na aula, segue bem as instruções verbais,\nmembro proativo de grupos de estudo, contador de histórias\ntalentoso, capaz de resolver problemas complexos falando em\nvoz alta, aqueles com um estilo de aprendizagem auditiva\ngostam de falar e ouvir os outros falarem para aprender, mas\npodem ter problemas para ler silenciosamente ou permanecer\nocupados em um local completamente silenciosa", font="Arial 17", bg='darkred', foreground='white', justify=LEFT, anchor=NW)
    VisualSondagem.place(x=0, y=1, width=743, height=450)

    ### page4 ###
    pageSondagem4 = ttk.Frame(nbSondagem)
    nbSondagem.add(pageSondagem4, text="Cinestésico")

    FundoSondagem3 = Frame(pageSondagem4, bg='darkgreen')
    FundoSondagem3.place(x=1, y=1, width=800, height=450)

    VisualSondagem = Label(pageSondagem4, text="""Cinestésico: Alunos cinestésicos priorizam as aulas práticas e gostam de\nestudar em pequenos blocos de tempo e sofrem por ter períodos curtos\nde atenção. Para eles, questões de múltipla escolha serão sempre as\nmelhores opções. Na aprendizagem cinestésica, é nescessário usar\no tato, o movimento, o olfato, e o paladar, entre as muitas outras\ncapacidades  que temos. Sem elas, não é possível aprender. Para\naprender por meio dessa técnica, é preciso colocar dinâmicas e\nmovimentos em prática em conjunto com emoções e sentimentos.\nQuando se coloca o conteúdo a ser aprendido em forma de exercícios\ndivertidos e lúdicos, a quantidade dos resultados aumenta tanto\nem crianças quanto em adultos.""", font="Arial 17", bg='darkgreen', foreground='white', justify=LEFT, anchor=NW)
    VisualSondagem.place(x=0, y=1)


def abrirANAMNESE():
    novoTrabalhoAnamnese = Toplevel()
    novoTrabalhoAnamnese.geometry('1090x620+260+70')
    novoTrabalhoAnamnese.resizable(False,False)
    novoTrabalhoAnamnese.title('ANAMNESE - Avaliação Diagnóstica')
    novoTrabalhoAnamnese.configure(bg='light gray')
    novoTrabalhoAnamnese.transient(trabalho)
    novoTrabalhoAnamnese.focus_force()
    novoTrabalhoAnamnese.grab_set()

    DiagnosticoAnamnese = Text(novoTrabalhoAnamnese, bg='light yellow', width=40, height=1)
    DiagnosticoAnamnese.place(x=190, y=25)

    DiagnosticoButaoAnamese = Button(novoTrabalhoAnamnese, bg="light grey", image=imgPlusPEI)
    DiagnosticoButaoAnamese.place(x=514, y=25, width=20, height=20)

    ### multipage ###
    rows = 0
    while rows < 50:
        novoTrabalhoAnamnese.rowconfigure(rows, weight=1)
        novoTrabalhoAnamnese.columnconfigure(rows, weight=1)
        rows += 1

        ### label ###
        Cid11LabelAnamnese = Label(novoTrabalhoAnamnese, text='Marque se for CID-11', font="Arial 7 bold", bg='light grey', foreground='blue')
        Cid11LabelAnamnese.place(x=2, y=3)

        Cid10LabelAnamnese = Label(novoTrabalhoAnamnese, text='3.01 - CID 10', font="Arial 8 bold", bg='light grey')
        Cid10LabelAnamnese.place(x=105, y=3)

        DiagnosticoLabelAnamnese = Label(novoTrabalhoAnamnese, text='Diagnóstico', font="Arial 8", bg='light grey')
        DiagnosticoLabelAnamnese.place(x=190, y=3)

        Data_do_LaudoLabelAnamnese = Label(novoTrabalhoAnamnese, text='3.02 - Data do Laudo', font="Arial 8", bg='light grey')
        Data_do_LaudoLabelAnamnese.place(x=525, y=4)

        MedicoLabelAnamnese = Label(novoTrabalhoAnamnese, text='3.03 - Médico', font="Arial 8", bg='light grey')
        MedicoLabelAnamnese.place(x=640, y=4)

        CRMLabelAnamnese = Label(novoTrabalhoAnamnese, text='3.04 - CRM', font="Arial 8", bg='light grey')
        CRMLabelAnamnese.place(x=788, y=4)

        DataProtocoloLabelAnamnese = Label(novoTrabalhoAnamnese, text='3.05 - Data de Protocolo', font="Arial 8", bg='light grey')
        DataProtocoloLabelAnamnese.place(x=915, y=4)

        ### checkButton ###
        ckbtCid11 = Checkbutton(novoTrabalhoAnamnese, text="Cid 11", bg='light grey', width=6, anchor=W)
        ckbtCid11.place(x=20, y=25)

        ### Combobox ###
        cid10 = tkinter.StringVar()
        cid10cmbbx = ttk.Combobox(novoTrabalhoAnamnese, width=10, height=1, textvariable=cid10)
        cid10cmbbx.place(x=100, y=25)

        Data_do_Laudo = Text(novoTrabalhoAnamnese, width=9, height=1)
        Data_do_Laudo.place(x=540, y=25)

        Medico = Text(novoTrabalhoAnamnese, width=20, height=1)
        Medico.place(x=620, y=25)

        CRM = Text(novoTrabalhoAnamnese, width=15, height=1)
        CRM.place(x=788, y=25)

        Data_de_Protocolo = Text(novoTrabalhoAnamnese, width=18, height=1)
        Data_de_Protocolo.place(x=915, y=25)

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nb1 = ttk.Notebook(novoTrabalhoAnamnese)
    nb1.grid(row=8, column=1, columnspan=48, rowspan=42, sticky="NESW")

    ### page1 ###
    page1anamnese = ttk.Frame(nb1)
    nb1.add(page1anamnese, text="Cadastro")
    ### page 1 ###
    ### Perguntas/Textos ###
    ## ESQUERDA ##
    identificacao = Label(page1anamnese, text="Identificação", font="Negrito 10 bold", foreground='red')
    identificacao.place(x=10, y=35)

    codigotxt= Label(page1anamnese, text='Código', font="Negrito 10 bold")
    codigotxt.place(x=10, y=62)

    matriculatxt= Label(page1anamnese, text='Matrícula', font="Arial 10 bold")
    matriculatxt.place(x=10, y=92)

    Nometxt= Label(page1anamnese, text='Nome', font="Arial 10 bold")
    Nometxt.place(x=10, y=122)

    Idadetxt = Label(page1anamnese, text='Idade', font="Arial 10 bold")
    Idadetxt.place(x=10, y=152)

    Nascimentotxt = Label(page1anamnese, text='Nascimento', font='Arial 10 bold')
    Nascimentotxt.place(x=10, y=182)

    Generotxt = Label(page1anamnese, text='Genero', font='Arial 10 bold')
    Generotxt.place(x=10, y=212)

    Cortxt = Label(page1anamnese, text='Cor', font='Arial 10 bold')
    Cortxt.place(x=10, y=242)

    Naturalidade = Label(page1anamnese, text='Naturalidade', font='Arial 10 bold')
    Naturalidade.place(x=10, y=272)

    Nacionalidade = Label(page1anamnese, text='Nacionalidade', font='Arial 10 bold')
    Nacionalidade.place(x=10, y=302)

    Enderecotxt = Label(page1anamnese, text='Endereço', font='Arial 10 bold')
    Enderecotxt.place(x=10, y=332)

    Unidadetxt = Label(page1anamnese, text='Unidade', font='Arial 10 bold')
    Unidadetxt.place(x=10, y=362)

    Serietxt = Label(page1anamnese, text='Série', font='Arial 10 bold')
    Serietxt.place(x=10, y=392)

    Turmatxt = Label(page1anamnese, text='Turma', font='Arial 10 bold')
    Turmatxt.place(x=10, y=422)

    ## DIREITA ##
    Filiacao = Label(page1anamnese, text="Filiação", font="Negrito 10 bold", foreground='red')
    Filiacao.place(x=480, y=35)

    ## Mãe  ##
    Maetxt = Label(page1anamnese, text='Mãe', font="Negrito 10 bold")
    Maetxt.place(x=480, y=62)

    CPF_Maetxt = Label(page1anamnese, text='Cpf', font="Arial 10 bold")
    CPF_Maetxt.place(x=480, y=92)

    Profiss_Maetxt = Label(page1anamnese, text='Profissão', font="Arial  10 bold")
    Profiss_Maetxt.place(x=480, y=122)

    Idade_Maetxt = Label(page1anamnese, text='Idade', font="Arial 10 bold")
    Idade_Maetxt.place(x=480, y=152)

    GdI_Maetxt = Label(page1anamnese, text='Grau de Instrução', font='Arial 8 bold')
    GdI_Maetxt.place(x=480, y=182)

    ## Pai ##
    Paitxt = Label(page1anamnese, text='Pai', font="Negrito 10 bold")
    Paitxt.place(x=480, y=235)

    CPF_Paitxt = Label(page1anamnese, text='Cpf', font="Arial 10 bold")
    CPF_Paitxt.place(x=480, y=265)

    Profiss_Paitxt = Label(page1anamnese, text='Profissão', font="Arial  10 bold")
    Profiss_Paitxt.place(x=480, y=295)

    Idade_Paitxt = Label(page1anamnese, text='Idade', font="Arial 10 bold")
    Idade_Paitxt.place(x=480, y=325)

    GdI_Paitxt = Label(page1anamnese, text='Grau de Instrução', font='Arial 8 bold')
    GdI_Paitxt.place(x=480, y=355)

    ## Família ##

    RdF_txt = Label(page1anamnese, text='Religião da Família', font='Arial 8 bold')
    RdF_txt.place(x=480, y=405)

    ### caixas de texto ###

    ## ESQUERDA ##
    Cid = Text(page1anamnese, borderwidth=2, relief="solid", width=129, height=1)
    Cid.place(x=8, y=8)

    codigo = Text(page1anamnese, width=9, height=1)
    codigo.place(x=110, y=65)

    Matricula = Text(page1anamnese, width=9, height=1)
    Matricula.place(x=110, y=95)

    Nome = tkinter.StringVar()
    Nomecmbbx = ttk.Combobox(page1anamnese, width=50, height=1, textvariable=Nome)
    Nomecmbbx.place(x=110, y=125)

    Idade = Text(page1anamnese, width=3, height=1)
    Idade.place(x=110, y=155)

    nascimento = Text(page1anamnese, width=18, height=1)
    nascimento.place(x=110, y=185)

    Genero = tkinter.StringVar()
    Generocmbbx = ttk.Combobox(page1anamnese, width=18, height=1, textvariable=Genero)
    Generocmbbx.place(x=110, y=215)

    Cor = tkinter.StringVar()
    Corcmbbx = ttk.Combobox(page1anamnese, width=18, height=1, textvariable=Cor)
    Corcmbbx.place(x=110, y=245)

    Naturalidade = Text(page1anamnese, width=23, height=1)
    Naturalidade.place(x=110, y=275)

    Nacionalidade = Text(page1anamnese, width=23, height=1)
    Nacionalidade.place(x=110, y=305)

    Endereco = Text(page1anamnese, width=38, height=1)
    Endereco.place(x=110, y=335)

    Unidade = tkinter.StringVar()
    Unidadecmbbx = ttk.Combobox(page1anamnese, width=50, height=1, textvariable=Unidade)
    Unidadecmbbx.place(x=110, y=365)

    Serie = tkinter.StringVar()
    Seriecmbbx = ttk.Combobox(page1anamnese, width=40, height=1, textvariable=Serie)
    Seriecmbbx.place(x=110, y=395)

    Turma = tkinter.StringVar()
    Turmacmbbx = ttk.Combobox(page1anamnese, width=10, height=1, textvariable=Turma)
    Turmacmbbx.place(x=110, y=425)

    ## DIREITA ##
    Mae = Text(page1anamnese, width=40, height=1)
    Mae.place(x=600, y=65)

    CPF_Mae = Text(page1anamnese, width=20, height=1)
    CPF_Mae.place(x=600, y=95)

    Profiss_Mae = Text(page1anamnese, width=30, height=1)
    Profiss_Mae.place(x=600, y=125)

    Mae_Idade = Text(page1anamnese, width=15, height=1)
    Mae_Idade.place(x=600, y=155)

    Mae_GdI = Text(page1anamnese, width=40, height=1)
    Mae_GdI.place(x=600, y=185)

    Separacao1 = Label(page1anamnese, text='__________________________________________________________________________________________________________')
    Separacao1.place(x=510, y=205)

    Pai = Text(page1anamnese, width=40, height=1)
    Pai.place(x=600, y=235)

    CPF_Pai = Text(page1anamnese, width=20, height=1)
    CPF_Pai.place(x=600, y=265)

    Profiss_Pai = Text(page1anamnese, width=30, height=1)
    Profiss_Pai.place(x=600, y=295)

    Pai_Idade = Text(page1anamnese, width=15, height=1)
    Pai_Idade.place(x=600, y=325)

    Pai_GdI = Text(page1anamnese, width=40, height=1)
    Pai_GdI.place(x=600, y=355)

    Separacao1 = Label(page1anamnese,
                       text='__________________________________________________________________________________________________________')
    Separacao1.place(x=510, y=375)

    Turma = tkinter.StringVar()
    Turmacmbbx = ttk.Combobox(page1anamnese, width=50, height=1, textvariable=Turma)
    Turmacmbbx.place(x=600, y=405)

    ## BOTÕES ##
    def stepAnam1():
        BarraDeProgressoAnamnese['value'] += 6.6666

    #def stepAnam7():
    #    BarraDeProgressoAnamnese['value'] = 16

    #def stepAnam8():
    #    BarraDeProgressoAnamnese['value'] = 20

    #def stepAnam9():
    #    BarraDeProgressoAnamnese['value'] = 21

    #def stepAnam10():
     #   BarraDeProgressoAnamnese['value'] = 25

    def resetAnam():
        BarraDeProgressoAnamnese['value'] = 0

    BarraDeProgressoAnamnese = ttk.Progressbar(novoTrabalhoAnamnese, orient=HORIZONTAL, length=1070, mode='determinate')
    BarraDeProgressoAnamnese.place(x=10, y=60)

    Bt_Prox_Ident = Button(page1anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red', command=stepAnam1)
    Bt_Prox_Ident.place(x=370, y=430, width=60, height=30)

    Bt_Prox_Filia = Button(page1anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red', command=stepAnam1)
    Bt_Prox_Filia.place(x=984, y=430, width=60, height=30)

    Bt_Calendario = Button(page1anamnese, image=imgCalend)
    Bt_Calendario.place(x=258, y=185, width=20, height=20)

    Foto_Aluno_Anam = Label(page1anamnese, image=imgFoto_Aluno)
    Foto_Aluno_Anam.place(x=950, y=100)

    #############################################################################################

    page2anamnese = ttk.Frame(nb1)
    nb1.add(page2anamnese, text="4 - Questionário")
    ### page2 ###
    ### Textos/Perguntas
    ## 4.0 ##
    Questionario = Label(page2anamnese, text="4 - Questionário:", font="Negrito 10 bold", foreground='red')
    Questionario.place(x=10, y=15)

    ## 4.1 ##
    anamnese_401pergunta = Label(page2anamnese, text="4.01 - Tem alguma deficiência com diagnóstico fechado?", font="Negrito 10 bold")
    anamnese_401pergunta.place(x=10, y=45)

    anamnese_40101pergunta = Label(page2anamnese, text="4.01.01 - se sim, de qual tipo?", foreground='blue')
    anamnese_40101pergunta.place(x=10, y=65)

    ## 4.2 ##
    anamnese_402pergunta = Label(page2anamnese, text="4.02 - Tem algum desturbio da apredizagem fechado?",
                                 font="Negrito 10 bold")
    anamnese_402pergunta.place(x=10, y=185)

    anamnese_40201pergunta = Label(page2anamnese, text="4.02.01 - se sim, de qual tipo?", foreground='blue')
    anamnese_40201pergunta.place(x=10, y=205)

    anamnese_40202pergunta = Label(page2anamnese, text="4.02.02 - Qual?")
    anamnese_40202pergunta.place(x=87, y=328)

    ## 4.3 ##
    anamnese_403pergunta = Label(page2anamnese, text='4.03 - Tem problema crônico ou está em tratamento de saúde\nque implica em afastamentos constantes dos estados?', font="Negrito 10 bold")
    anamnese_403pergunta.place(x=10, y=357)

    anamnese_40301pergunta = Label(page2anamnese, text="4.03.01 - se sim, de qual tipo?", foreground='blue')
    anamnese_40301pergunta.place(x=10, y=395)

    ## 4.4 ##
    anamnese_404pergunta = Label(page2anamnese,
                                 text='4.04 - Tem transtornos psicológicos?',
                                 font="Negrito 10 bold")
    anamnese_404pergunta.place(x=560, y=45)

    anamnese_40401pergunta = Label(page2anamnese, text="4.02.02 - Qual?")
    anamnese_40401pergunta.place(x=640, y=147)

    ## 4.5 ##
    anamnese_405pergunta = Label(page2anamnese,
                                 text='4.05 - Beneficiou ou Beneficia-se de outros apoios,\nfora do âmbito da educação espacial?',
                                 font="Negrito 10 bold", anchor=W)
    anamnese_405pergunta.place(x=560, y=175)

    anamnese_40501pergunta = Label(page2anamnese, text="4.05.01 - se sim, qual?", foreground='blue')
    anamnese_40501pergunta.place(x=560, y=210)

    anamnese_40502pergunta = Label(page2anamnese, text="Outros, especifique abaixo:")
    anamnese_40502pergunta.place(x=565, y=330)

    ### radiobutton ###
    ## vars ##
    Optionint1 = IntVar()
    Optionint2 = IntVar()
    Optionint3 = IntVar()
    Optionint4 = IntVar()
    Optionint5 = IntVar()

    ## 4.01 ##
    simCB401_anamnese = Radiobutton(page2anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1)
    simCB401_anamnese.place(x=415, y=45)

    naoCB401_anamnese = Radiobutton(page2anamnese, text="Não",value=2, width=3, anchor=W, variable=Optionint1)
    naoCB401_anamnese.place(x=465, y=45)

    ## 4.02 ##
    simCB402_anamnese = Radiobutton(page2anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint2)
    simCB402_anamnese.place(x=415, y=185)

    naoCB402_anamnese = Radiobutton(page2anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint2)
    naoCB402_anamnese.place(x=465, y=185)

    ## 4.03 ##
    simCB403_anamnese = Radiobutton(page2anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint3)
    simCB403_anamnese.place(x=415, y=357)

    naoCB403_anamnese = Radiobutton(page2anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint3)
    naoCB403_anamnese.place(x=465, y=357)

    ## 4.04 ##
    simCB404_anamnese = Radiobutton(page2anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint4)
    simCB404_anamnese.place(x=935, y=45)

    naoCB404_anamnese = Radiobutton(page2anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint4)
    naoCB404_anamnese.place(x=985, y=45)

    ## 4.05 ##
    simCB405_anamnese = Radiobutton(page2anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint5)
    simCB405_anamnese.place(x=935, y=175)

    naoCB405_anamnese = Radiobutton(page2anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint5)
    naoCB405_anamnese.place(x=985, y=175)

    ### checkButtons ###
    ## 4.01 ##
    Fisicachkbt_anamnese = Checkbutton(page2anamnese, text="Física", width=6, anchor=W)
    Fisicachkbt_anamnese.place(x=20, y=85)

    Visualchkbt_anamnese = Checkbutton(page2anamnese, text="Visual", width=6, anchor=W)
    Visualchkbt_anamnese.place(x=20, y=105)

    Auditivachkbt_anamnese = Checkbutton(page2anamnese, text="Auditiva", width=6, anchor=W)
    Auditivachkbt_anamnese.place(x=20, y=125)

    intelecchkbt_anamnese = Checkbutton(page2anamnese, text="Intelectual", width=11, anchor=W)
    intelecchkbt_anamnese.place(x=20, y=145)

    multichkbt_anamnese = Checkbutton(page2anamnese, text="Multipla", width=8, anchor=W)
    multichkbt_anamnese.place(x=20, y=165)

    ## 4.02 ##
    Disleixachkbt_anamnese = Checkbutton(page2anamnese, text="Disleixa", width=6, anchor=W)
    Disleixachkbt_anamnese.place(x=20, y=225)

    Discalculachkbt_anamnese = Checkbutton(page2anamnese, text="Discalculia", width=6, anchor=W)
    Discalculachkbt_anamnese.place(x=20, y=245)

    Disgrafiachkbt_anamnese = Checkbutton(page2anamnese, text="Disgrafia", width=6, anchor=W)
    Disgrafiachkbt_anamnese.place(x=20, y=265)

    Deficitchkbt_anamnese = Checkbutton(page2anamnese, text="Transtorno do Deficit de Atenção(TDA)", width=29, anchor=W)
    Deficitchkbt_anamnese.place(x=20, y=285)

    Hiperatichkbt_anamnese = Checkbutton(page2anamnese, text="Hiperatividade", width=12, anchor=W)
    Hiperatichkbt_anamnese.place(x=20, y=305)

    Outroschkbt_anamnese = Checkbutton(page2anamnese, text="Outros: ", width=6, anchor=W)
    Outroschkbt_anamnese.place(x=20, y=325)

    ## 4.04 ##
    Depressaochkbt_anamnese = Checkbutton(page2anamnese, text="Depressão", width=7, anchor=W)
    Depressaochkbt_anamnese.place(x=560, y=65)

    SdPchkbt_anamnese = Checkbutton(page2anamnese, text="Síndrome de Pânico", width=15, anchor=W)
    SdPchkbt_anamnese.place(x=560, y=85)

    Esquizofrechkbt_anamnese = Checkbutton(page2anamnese, text="Esquizofrenia", width=10, anchor=W)
    Esquizofrechkbt_anamnese.place(x=560, y=105)

    Bipolarchkbt_anamnese = Checkbutton(page2anamnese, text="Bipolaridade", width=9, anchor=W)
    Bipolarchkbt_anamnese.place(x=560, y=125)

    Outros2chkbt_anamnese = Checkbutton(page2anamnese, text="Outros: ", width=6, anchor=W)
    Outros2chkbt_anamnese.place(x=560, y=145)

    ## 4.05 ##
    TdFchkbt_anamnese = Checkbutton(page2anamnese, text="Terapia da Fala", width=12, anchor=W)
    TdFchkbt_anamnese.place(x=560, y=225)

    TOchkbt_anamnese = Checkbutton(page2anamnese, text="Terapia Ocupacional", width=15, anchor=W)
    TOchkbt_anamnese.place(x=560, y=245)

    FisioTerapchkbt_anamnese = Checkbutton(page2anamnese, text="Fisioterapia", width=12, anchor=W)
    FisioTerapchkbt_anamnese.place(x=560, y=265)

    Picicolotchkbt_anamnese = Checkbutton(page2anamnese, text="Pisicologia", width=12, anchor=W)
    Picicolotchkbt_anamnese.place(x=560, y=285)

    Hidroterapchkbt_anamnese = Checkbutton(page2anamnese, text="Hidroterapia", width=12, anchor=W)
    Hidroterapchkbt_anamnese.place(x=560, y=305)

    ### TEXT ###
    Texto40202_anamnese = Text(page2anamnese, width=40, height=1)
    Texto40202_anamnese.place(x=170, y=327)

    Texto40301_anamnese = Text(page2anamnese, width=40, height=1)
    Texto40301_anamnese.place(x=170, y=395)

    Texto40401_anamnese = Text(page2anamnese, width=40, height=1)
    Texto40401_anamnese.place(x=730, y=145)

    Texto40401_anamnese = Text(page2anamnese, width=60, height=1)
    Texto40401_anamnese.place(x=570, y=355)

    ### BUTTON ###
    ProximoQuestionario_anamnese = Button(page2anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red', command= stepAnam1)
    ProximoQuestionario_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page3anamnese = ttk.Frame(nb1)
    nb1.add(page3anamnese, text="5 - Queixas")
    ### page3 ###
    ## PERGUNTAS ##
    Queixas = Label(page3anamnese, text="5 - Queixas", font="Negrito 10 bold", foreground='red')
    Queixas.place(x=10, y=15)

    anamnese_5pergunta = Label(page3anamnese, text="5 - Queixas Principais", foreground='blue', font="Negrito 10 bold")
    anamnese_5pergunta.place(x=20, y=35)

    anamnese_501pergunta = Label(page3anamnese, text="5.01 - Há quanto tempo?")
    anamnese_501pergunta.place(x=20, y=125)

    anamnese_502pergunta = Label(page3anamnese, text="5.02 - Causa Atribuida", foreground='blue', font="Negrito 10 bold")
    anamnese_502pergunta.place(x=20, y=185)

    anamnese_503pergunta = Label(page3anamnese, text="5.03 - Atitudes frente as queixas:", foreground='blue', font="Negrito 10 bold")
    anamnese_503pergunta.place(x=20, y=285)

    anamnese_50301pergunta = Label(page3anamnese, text="5.03.01 - Da criança quando relatadas:")
    anamnese_50301pergunta.place(x=20, y=305)

    anamnese_50302pergunta = Label(page3anamnese, text="5.03.02 - Da Mãe:")
    anamnese_50302pergunta.place(x=550, y=35)

    anamnese_50303pergunta = Label(page3anamnese, text="5.03.03 - Do Pai:")
    anamnese_50303pergunta.place(x=550, y=125)

    anamnese_50304pergunta = Label(page3anamnese, text="5.03.04 - Dos Parentes:")
    anamnese_50304pergunta.place(x=550, y=215)

    ## CAIXAS DE TEXTO ##
    Texto5_anamnese = Text(page3anamnese, width=60, height=4)
    Texto5_anamnese.place(x=20, y=55)

    Texto501_anamnese = Text(page3anamnese, width=60, height=1)
    Texto501_anamnese.place(x=20, y=145)

    Texto502_anamnese = Text(page3anamnese, width=60, height=4)
    Texto502_anamnese.place(x=20, y=205)

    Texto50301_anamnese = Text(page3anamnese, width=60, height=4)
    Texto50301_anamnese.place(x=20, y=335)

    Texto50302_anamnese = Text(page3anamnese, width=60, height=4)
    Texto50302_anamnese.place(x=550, y=55)

    Texto50303_anamnese = Text(page3anamnese, width=60, height=4)
    Texto50303_anamnese.place(x=550, y=145)

    Texto50304_anamnese = Text(page3anamnese, width=60, height=4)
    Texto50304_anamnese.place(x=550, y=235)

    ### Button ###
    ProximoQueixa_anamnese = Button(page3anamnese, text='Próximo', font="Negrito 8 bold", bg='white',
                                          foreground='red',command=stepAnam1)
    ProximoQueixa_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page4anamnese = ttk.Frame(nb1)
    nb1.add(page4anamnese, text="6 - Antecedentes Pessoais")
    ### page4 ###
    Antecedentes_Pessoais = Label(page4anamnese, text="6 - Antecedentes Pessoais", font="Negrito 10 bold", foreground='red')
    Antecedentes_Pessoais.place(x=10, y=15)

    anamnese_6pergunta = Label(page4anamnese, text="6 - Concepção", foreground='blue', font="Negrito 10 bold")
    anamnese_6pergunta.place(x=20, y=35)

    anamnese_601pergunta = Label(page4anamnese, text="6.01 - Como era composta a família na época da concepção da criança?")
    anamnese_601pergunta.place(x=20, y=55)

    anamnese_602pergunta = Label(page4anamnese, text="6.02 - Como é composta a família hoje?")
    anamnese_602pergunta.place(x=20, y=105)

    anamnese_603pergunta = Label(page4anamnese, text="6.03 - A criança foi desejada?")
    anamnese_603pergunta.place(x=20, y=165)

    anamnese_604pergunta = Label(page4anamnese, text="6.04 - Qual foi a posição da criança na ordem de nascimento?")
    anamnese_604pergunta.place(x=20, y=205)

    anamnese_605pergunta = Label(page4anamnese, text="6.05 - Idade dos irmãos")
    anamnese_605pergunta.place(x=20, y=245)

    anamnese_606pergunta = Label(page4anamnese, text="6.06 - Pais separados?")
    anamnese_606pergunta.place(x=20, y=285)

    anamnese_607pergunta = Label(page4anamnese,
                                 text="6.07 - Vida Social da Família (amigos, festas, passeios, moradia, nível econômico)")
    anamnese_607pergunta.place(x=550, y=55)

    ### CAIXAS DE TEXTO ###
    Texto601_anamnese = Text(page4anamnese, width=60, height=1)
    Texto601_anamnese.place(x=20, y=75)

    Texto602_anamnese = Text(page4anamnese, width=60, height=1)
    Texto602_anamnese.place(x=20, y=125)

    Texto605_anamnese = Text(page4anamnese, width=60, height=1)
    Texto605_anamnese.place(x=20, y=265)

    Texto606_anamnese = Text(page4anamnese, width=60, height=14)
    Texto606_anamnese.place(x=550, y=75)

    ### RADIOBUTTON ###
    ## VAR ##
    Optionint603 = IntVar()
    Optionint604 = IntVar()
    Optionint606 = IntVar()

    simCB603_anamnese = Radiobutton(page4anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint603)
    simCB603_anamnese.place(x=415, y=165)

    naoCB603_anamnese = Radiobutton(page4anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint603)
    naoCB603_anamnese.place(x=465, y=165)

    CefalicaCB604_anamnese = Radiobutton(page4anamnese, text="Cefálica", value=1, width=8, anchor=W, variable=Optionint604)
    CefalicaCB604_anamnese.place(x=30, y=225)

    PelvicaCB604_anamnese = Radiobutton(page4anamnese, text="Pélvica", value=2, width=8, anchor=W,
                                         variable=Optionint604)
    PelvicaCB604_anamnese.place(x=110, y=225)

    TransversalCB604_anamnese = Radiobutton(page4anamnese, text="Transversal", value=3, width=8, anchor=W,
                                        variable=Optionint604)
    TransversalCB604_anamnese.place(x=180, y=225)

    simCB606_anamnese = Radiobutton(page4anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint606)
    simCB606_anamnese.place(x=415, y=285)

    naoCB606_anamnese = Radiobutton(page4anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint606)
    naoCB606_anamnese.place(x=465, y=285)

    ### Button ###
    ProximoAntecendentes_anamnese = Button(page4anamnese, text='Próximo', font="Negrito 8 bold", bg='white',
                                          foreground='red', command=stepAnam1)
    ProximoAntecendentes_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page5anamnese = ttk.Frame(nb1)
    nb1.add(page5anamnese, text="7 - Gestão")
    ### page5 ###
    ## PERGUNTAS ##
    Gestao = Label(page5anamnese, text="7 - Gestão", font="Negrito 10 bold", foreground='red')
    Gestao.place(x=10, y=15)

    anamnese_701pergunta = Label(page5anamnese, text="7.01 - A gravidez foi planejada pelos pais?")
    anamnese_701pergunta.place(x=20, y=35)

    anamnese_702pergunta = Label(page5anamnese, text="7.02 - Duração da gestação:")
    anamnese_702pergunta.place(x=20, y=65)

    anamnese_703pergunta = Label(page5anamnese, text="7.03 - Quando sentiu a criança mexer?")
    anamnese_703pergunta.place(x=20, y=135)

    anamnese_704pergunta = Label(page5anamnese, text="7.04 - Fez tratamento pré-natal?")
    anamnese_704pergunta.place(x=20, y=165)

    anamnese_705pergunta = Label(page5anamnese, text="7.05 - Foi necessário algum tratamento?")
    anamnese_705pergunta.place(x=20, y=185)

    anamnese_706pergunta = Label(page5anamnese, text="7.06 - A gestação foi uma experiência agradável para a mãe?", font="Negrito 10 bold")
    anamnese_706pergunta.place(x=20, y=225)

    anamnese_70601pergunta = Label(page5anamnese, text="7.06.01 - Se NÃO, descreva:", foreground='blue')
    anamnese_70601pergunta.place(x=20, y=265)

    anamnese_707pergunta = Label(page5anamnese, text="7.07 - Como foi a saúde da sua mãe?")
    anamnese_707pergunta.place(x=20, y=325)

    anamnese_708pergunta = Label(page5anamnese, text="7.08 - E o estado emocional?")
    anamnese_708pergunta.place(x=20, y=385)

    ### CAIXAS DE TEXTO ###
    Texto702_anamnese = Text(page5anamnese, width=60, height=3)
    Texto702_anamnese.place(x=240, y=70)

    Texto703_anamnese = Text(page5anamnese, width=60, height=1)
    Texto703_anamnese.place(x=240, y=135)

    Texto70601_anamnese = Text(page5anamnese, width=65, height=3)
    Texto70601_anamnese.place(x=220, y=265)

    Texto707_anamnese = Text(page5anamnese, width=65, height=3)
    Texto707_anamnese.place(x=220, y=325)

    Texto708_anamnese = Text(page5anamnese, width=65, height=3)
    Texto708_anamnese.place(x=220, y=385)

    ### RADIOBUTTON  ###
    Optionint701 = IntVar()
    Optionint704 = IntVar()
    Optionint705 = IntVar()
    Optionint706 = IntVar()

    simCB701_anamnese = Radiobutton(page5anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint701)
    simCB701_anamnese.place(x=515, y=35)

    naoCB701_anamnese = Radiobutton(page5anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint701)
    naoCB701_anamnese.place(x=565, y=35)

    simCB704_anamnese = Radiobutton(page5anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint704)
    simCB704_anamnese.place(x=515, y=165)

    naoCB704_anamnese = Radiobutton(page5anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint704)
    naoCB704_anamnese.place(x=565, y=165)

    simCB705_anamnese = Radiobutton(page5anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint705)
    simCB705_anamnese.place(x=515, y=185)

    naoCB705_anamnese = Radiobutton(page5anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint705)
    naoCB705_anamnese.place(x=565, y=185)

    simCB706_anamnese = Radiobutton(page5anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint706)
    simCB706_anamnese.place(x=515, y=225)

    naoCB706_anamnese = Radiobutton(page5anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint706)
    naoCB706_anamnese.place(x=565, y=225)

    ### BUTTON ###
    ProximoGestao_anamnese = Button(page5anamnese, text='Próximo', font="Negrito 8 bold", bg='white',
                                           foreground='red', command=stepAnam1)
    ProximoGestao_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page6anamnese = ttk.Frame(nb1)
    nb1.add(page6anamnese, text="8 - Condições do Nascimento")
    ### page6 ###
    CdN = Label(page6anamnese, text="8 - Condições do Nascimento", font="Negrito 10 bold", foreground='blue')
    CdN.place(x=10, y=15)

    anamnese_801pergunta = Label(page6anamnese, text="8.01 - Local de nascimento:")
    anamnese_801pergunta.place(x=20, y=35)

    anamnese_801EspecifiquePergunta = Label(page6anamnese, text="Especifique:")
    anamnese_801EspecifiquePergunta.place(x=130, y=102)

    ## 8.02 ##
    anamnese_802pergunta = Label(page6anamnese, text="8.02 - Tipo de parto:")
    anamnese_802pergunta.place(x=20, y=125)

    anamnese_802EspecifiquePergunta = Label(page6anamnese, text="Especifique:")
    anamnese_802EspecifiquePergunta.place(x=130, y=205)

    ## 8.03 ##
    anamnese_803pergunta = Label(page6anamnese, text="8.03 - Nasceu no tempo normal?")
    anamnese_803pergunta.place(x=20, y=245)

    ## 8.04 ##
    anamnese_804pergunta = Label(page6anamnese, text="8.04 - O bebê ao nascer:")
    anamnese_804pergunta.place(x=20, y=285)

    anamnese_804ObservacaoPergunta = Label(page6anamnese, text="Observação:")
    anamnese_804ObservacaoPergunta.place(x=130, y=368)

    ## 8.05 ##
    anamnese_805pergunta = Label(page6anamnese, text="8.05 - Houve um Trauma Craniano?")
    anamnese_805pergunta.place(x=550, y=35)

    ## 8.06 ##
    anamnese_806pergunta = Label(page6anamnese, text="8.06 - Tipo de anestesia no parto:")
    anamnese_806pergunta.place(x=550, y=65)

    anamnese_806DescrevaPergunta = Label(page6anamnese, text="Descreva:")
    anamnese_806DescrevaPergunta.place(x=680, y=148)

    ## 8.07 ##
    anamnese_807pergunta = Label(page6anamnese, text="8.07 - Duração da gestação:")
    anamnese_807pergunta.place(x=550, y=195)

    ## 8.08 ##
    anamnese_808pergunta = Label(page6anamnese, text="8.08 - Peso ao nascer:")
    anamnese_808pergunta.place(x=550, y=225)

    ## 8.09 ##
    anamnese_809pergunta = Label(page6anamnese, text="8.09 - Durante o parto? (desde os primeiros sinais até o nascimento):")
    anamnese_809pergunta.place(x=550, y=257)

    ## Primeiras Reações ##
    PR = Label(page6anamnese, text="Primeiras Reações:", font="Negrito 10 bold", foreground='blue')
    PR.place(x=550, y=305)

    ## 8.10 ##
    anamnese_810pergunta = Label(page6anamnese, text="8.10 - Chorou logo?")
    anamnese_810pergunta.place(x=550, y=325)

    ## 8.11 ##
    anamnese_811pergunta = Label(page6anamnese, text="8.11 - Quanto tempo?")
    anamnese_811pergunta.place(x=550, y=355)

    ## 8.12 ##
    anamnese_811pergunta = Label(page6anamnese, text="8.12 - Reação após o primiro dia de vida:")
    anamnese_811pergunta.place(x=550, y=385)

    ### radiobutton ###
    ## vars ##
    Optionint801 = IntVar()
    Optionint802 = IntVar()
    Optionint803 = IntVar()
    Optionint805 = IntVar()
    Optionint806 = IntVar()
    Optionint810 = IntVar()

    CasaCB801_anamnese = Radiobutton(page6anamnese, text="Casa", value=1, width=3, anchor=W, variable=Optionint801)
    CasaCB801_anamnese.place(x=40, y=60)

    MaternidadeCB801_anamnese = Radiobutton(page6anamnese, text="Maternidade", value=2, width=10, anchor=W, variable=Optionint801)
    MaternidadeCB801_anamnese.place(x=40, y=80)

    OutroCB801_anamnese = Radiobutton(page6anamnese, text="Outro local:", value=3, width=8, anchor=W, variable=Optionint801)
    OutroCB801_anamnese.place(x=40, y=100)

    ## 8.02 ##
    NormalCB802_anamnese = Radiobutton(page6anamnese, text="Normal", value=1, width=5, anchor=W, variable=Optionint802)
    NormalCB802_anamnese.place(x=40, y=145)

    ForcepesCB802_anamnese = Radiobutton(page6anamnese, text="Fórcepes", value=2, width=7, anchor=W,
                                            variable=Optionint802)
    ForcepesCB802_anamnese.place(x=40, y=165)

    CesarianaCB802_anamnese = Radiobutton(page6anamnese, text="Cesariana", value=3, width=8, anchor=W,
                                      variable=Optionint802)
    CesarianaCB802_anamnese.place(x=40, y=185)

    OutroCB802_anamnese = Radiobutton(page6anamnese, text="Outro:", value=4, width=8, anchor=W,
                                          variable=Optionint802)
    OutroCB802_anamnese.place(x=40, y=205)
    ## 8.03 ##
    simCB803_anamnese = Radiobutton(page6anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint803)
    simCB803_anamnese.place(x=415, y=245)

    naoCB803_anamnese = Radiobutton(page6anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint803)
    naoCB803_anamnese.place(x=465, y=245)

    ## 8.05 ##
    simCB805_anamnese = Radiobutton(page6anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint805)
    simCB805_anamnese.place(x=915, y=35)

    naoCB805_anamnese = Radiobutton(page6anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint805)
    naoCB805_anamnese.place(x=965, y=35)

    ## 8.06 ##
    PeriduralCB806_anamnese = Radiobutton(page6anamnese, text="Peridural", value=1, width=8, anchor=W, variable=Optionint806)
    PeriduralCB806_anamnese.place(x=590, y=85)

    RaquiCB806_anamnese = Radiobutton(page6anamnese, text="Raquidiana", value=2, width=9, anchor=W, variable=Optionint806)
    RaquiCB806_anamnese.place(x=590, y=105)

    GeralCB806_anamnese = Radiobutton(page6anamnese, text="Geral", value=3, width=4, anchor=W, variable=Optionint806)
    GeralCB806_anamnese.place(x=590, y=125)

    CombinadaCB806_anamnese = Radiobutton(page6anamnese, text="Combinada:", value=4, width=9, anchor=W, variable=Optionint806)
    CombinadaCB806_anamnese.place(x=590, y=145)

    ## 8.10 ##
    simCB810_anamnese = Radiobutton(page6anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint810)
    simCB810_anamnese.place(x=915, y=325)

    naoCB810_anamnese = Radiobutton(page6anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint810)
    naoCB810_anamnese.place(x=965, y=325)



    ### CAIXAS DE TEXTO ###
    Texto801_anamnese = Text(page6anamnese, width=40, height=1)
    Texto801_anamnese.place(x=200, y=100)

    Texto802_anamnese = Text(page6anamnese, width=40, height=1)
    Texto802_anamnese.place(x=200, y=205)

    Texto804_anamnese = Text(page6anamnese, width=40, height=1)
    Texto804_anamnese.place(x=200, y=365)

    Texto806_anamnese = Text(page6anamnese, width=40, height=1)
    Texto806_anamnese.place(x=735, y=145)

    Texto807_anamnese = Text(page6anamnese, width=40, height=1)
    Texto807_anamnese.place(x=735, y=195)

    Texto808_anamnese = Text(page6anamnese, width=40, height=1)
    Texto808_anamnese.place(x=735, y=225)

    Texto809_anamnese = Text(page6anamnese, width=18, height=1)
    Texto809_anamnese.place(x=915, y=257)

    Texto811_anamnese = Text(page6anamnese, width=40, height=1)
    Texto811_anamnese.place(x=735, y=355)

    Texto811_anamnese = Text(page6anamnese, width=35, height=1)
    Texto811_anamnese.place(x=775, y=385)

    ### CHACKBUTTONS ###
    NdO_cb804Anamnese = Checkbutton(page6anamnese, text="Necessitou de oxigênio", width=21, anchor=W)
    NdO_cb804Anamnese.place(x=40, y=305)

    TC_cb804Anamnese = Checkbutton(page6anamnese, text="Teve Convunsão", width=13, anchor=W)
    TC_cb804Anamnese.place(x=40, y=325)

    Ictericia_cb804Anamnese = Checkbutton(page6anamnese, text="Ictreícia", width=8, anchor=W)
    Ictericia_cb804Anamnese.place(x=40, y=345)

    Incubadora_cb804Anamnese = Checkbutton(page6anamnese, text="Incubadora:", width=9, anchor=W)
    Incubadora_cb804Anamnese.place(x=40, y=365)

    ## BUTTON ##
    ProximoCdN_anamnese = Button(page6anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoCdN_anamnese.place(x=985, y=430, width=60, height=30)


    #############
    page7anamnese = ttk.Frame(nb1)
    nb1.add(page7anamnese, text="9 - Desenvolvimento Psicomotor")
    ### page7 ###
    ## ESQUERDA ##
    PD = Label(page7anamnese, text="9 - Desenvolvimento Psicomotor", font="Negrito 10 bold", foreground='red')
    PD.place(x=10, y=15)

    anamnese_901pergunta = Label(page7anamnese, text="9.01 - Quando sustentou a cabeça?")
    anamnese_901pergunta.place(x=20, y=45)

    anamnese_902pergunta = Label(page7anamnese, text="9.02 - Quando rolou?")
    anamnese_902pergunta.place(x=20, y=75)

    anamnese_903pergunta = Label(page7anamnese, text="9.03 - Quando sorriu?")
    anamnese_903pergunta.place(x=20, y=105)

    anamnese_904pergunta = Label(page7anamnese, text="9.04 - Quando sentou com ajuda?")
    anamnese_904pergunta.place(x=20, y=135)

    anamnese_905pergunta = Label(page7anamnese, text="9.05 - Quando engatinhou?")
    anamnese_905pergunta.place(x=20, y=165)

    anamnese_906pergunta = Label(page7anamnese, text="9.06 - Quando ficou de pé?")
    anamnese_906pergunta.place(x=20, y=195)

    anamnese_907pergunta = Label(page7anamnese, text="9.07 - Quando andou?")
    anamnese_907pergunta.place(x=20, y=225)

    anamnese_908pergunta = Label(page7anamnese, text="9.08 - Balbuciou com que idade?")
    anamnese_908pergunta.place(x=20, y=255)

    anamnese_909pergunta = Label(page7anamnese, text="9.09 - Quando falou as primeiras palavras?")
    anamnese_909pergunta.place(x=20, y=285)

    anamnese_910pergunta = Label(page7anamnese, text="9.10 - Quando falou corretamente?")
    anamnese_910pergunta.place(x=20, y=315)

    anamnese_911pergunta = Label(page7anamnese, text="9.11 - Trocou letras?")
    anamnese_911pergunta.place(x=20, y=345)

    anamnese_912pergunta = Label(page7anamnese, text="9.12 - Falando ou escrevendo?")
    anamnese_912pergunta.place(x=20, y=375)

    anamnese_913pergunta = Label(page7anamnese, text="9.13 - Falou muito errado?")
    anamnese_913pergunta.place(x=20, y=405)

    anamnese_91301pergunta = Label(page7anamnese, text="9.13.01 - Até quando?", foreground='blue')
    anamnese_91301pergunta.place(x=20, y=435)

    ## DIREITA ##
    ## 9.14 ##
    anamnese_914pergunta = Label(page7anamnese, text="9.14 - Gaguejou?")
    anamnese_914pergunta.place(x=550, y=45)

    ## 9.15 ##
    anamnese_915pergunta = Label(page7anamnese, text="9.15 - Houve alguma dificuldade especial para aprender a ler?")
    anamnese_915pergunta.place(x=550, y=65)

    ## 9.16 ##
    anamnese_916pergunta = Label(page7anamnese, text="9.16 - Houve alguma dificuldade especial para aprender a contar?")
    anamnese_916pergunta.place(x=550, y=85)

    ## 9.17 ##
    anamnese_917pergunta = Label(page7anamnese, text="9.17 - Houve alguma dificuldade especial para aprender a escrever?")
    anamnese_917pergunta.place(x=550, y=105)

    ## 9.18 ##
    anamnese_918pergunta = Label(page7anamnese, text="9.18 - Costuma ou costumava esquecer o que aprendeu?")
    anamnese_918pergunta.place(x=550, y=125)

    ## 9.19 ##
    anamnese_919pergunta = Label(page7anamnese, text="9.19 - Como foi a dentição?")
    anamnese_919pergunta.place(x=550, y=145)

    ## 9.20 ##
    anamnese_920pergunta = Label(page7anamnese, text="9.20 - Quando adiquiriu controle dos esfíncteres anal diurno:")
    anamnese_920pergunta.place(x=550, y=195)

    ## 9.21 ##
    anamnese_921pergunta = Label(page7anamnese, text="9.21 - Quando adiquiriu controle dos esfíncteres vesical diurno:")
    anamnese_921pergunta.place(x=550, y=245)

    ## 9.22 ##
    anamnese_922pergunta = Label(page7anamnese, text="9.22 - Quando adiquiriu controle dos esfíncteres vesical noturno:")
    anamnese_922pergunta.place(x=550, y=295)

    ## 9.23 ##
    anamnese_923pergunta = Label(page7anamnese, text="9.23 - Como foi ensinada o controle dos esfíncteres?")
    anamnese_923pergunta.place(x=550, y=345)

    ### TEXTBOX ##
    Texto901_anamnese = Text(page7anamnese, width=35, height=1)
    Texto901_anamnese.place(x=250, y=45)

    Texto902_anamnese = Text(page7anamnese, width=35, height=1)
    Texto902_anamnese.place(x=250, y=75)

    Texto903_anamnese = Text(page7anamnese, width=35, height=1)
    Texto903_anamnese.place(x=250, y=105)

    Texto904_anamnese = Text(page7anamnese, width=35, height=1)
    Texto904_anamnese.place(x=250, y=135)

    Texto905_anamnese = Text(page7anamnese, width=35, height=1)
    Texto905_anamnese.place(x=250, y=165)

    Texto906_anamnese = Text(page7anamnese, width=35, height=1)
    Texto906_anamnese.place(x=250, y=195)

    Texto907_anamnese = Text(page7anamnese, width=35, height=1)
    Texto907_anamnese.place(x=250, y=225)

    Texto908_anamnese = Text(page7anamnese, width=35, height=1)
    Texto908_anamnese.place(x=250, y=255)

    Texto909_anamnese = Text(page7anamnese, width=35, height=1)
    Texto909_anamnese.place(x=250, y=285)

    Texto910_anamnese = Text(page7anamnese, width=35, height=1)
    Texto910_anamnese.place(x=250, y=315)

    Texto91301_anamnese = Text(page7anamnese, width=35, height=1)
    Texto91301_anamnese.place(x=250, y=435)

    Texto919_anamnese = Text(page7anamnese, width=65, height=1)
    Texto919_anamnese.place(x=550, y=165)

    Texto920_anamnese = Text(page7anamnese, width=65, height=1)
    Texto920_anamnese.place(x=550, y=215)

    Texto921_anamnese = Text(page7anamnese, width=65, height=1)
    Texto921_anamnese.place(x=550, y=265)

    Texto922_anamnese = Text(page7anamnese, width=65, height=1)
    Texto922_anamnese.place(x=550, y=315)

    Texto922_anamnese = Text(page7anamnese, width=65, height=1)
    Texto922_anamnese.place(x=550, y=365)

    ### RadioButtons ###
    Optionint911 = IntVar()
    Optionint912 = IntVar()
    Optionint913 = IntVar()

    Optionint914 = IntVar()
    Optionint915 = IntVar()
    Optionint916 = IntVar()
    Optionint917 = IntVar()
    Optionint918 = IntVar()

    ## 9.11 ##
    simCB911_anamnese = Radiobutton(page7anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint911)
    simCB911_anamnese.place(x=415, y=345)

    naoCB911_anamnese = Radiobutton(page7anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint911)
    naoCB911_anamnese.place(x=465, y=345)

    ## 9.12 ##
    simCB912_anamnese = Radiobutton(page7anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint912)
    simCB912_anamnese.place(x=415, y=375)

    naoCB912_anamnese = Radiobutton(page7anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint912)
    naoCB912_anamnese.place(x=465, y=375)

    ## 9.13 ##
    simCB913_anamnese = Radiobutton(page7anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint913)
    simCB913_anamnese.place(x=415, y=405)

    naoCB913_anamnese = Radiobutton(page7anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint913)
    naoCB913_anamnese.place(x=465, y=405)

    ## 9.14 ##
    simCB914_anamnese = Radiobutton(page7anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint914)
    simCB914_anamnese.place(x=980, y=45)

    naoCB914_anamnese = Radiobutton(page7anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint914)
    naoCB914_anamnese.place(x=1025, y=45)

    ## 9.15 ##
    simCB915_anamnese = Radiobutton(page7anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint915)
    simCB915_anamnese.place(x=980, y=65)

    naoCB915_anamnese = Radiobutton(page7anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint915)
    naoCB915_anamnese.place(x=1025, y=65)

    ## 9.16 ##
    simCB916_anamnese = Radiobutton(page7anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint916)
    simCB916_anamnese.place(x=980, y=85)

    naoCB916_anamnese = Radiobutton(page7anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint916)
    naoCB916_anamnese.place(x=1025, y=85)

    ## 9.17 ##
    simCB917_anamnese = Radiobutton(page7anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint917)
    simCB917_anamnese.place(x=980, y=105)

    naoCB917_anamnese = Radiobutton(page7anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint917)
    naoCB917_anamnese.place(x=1025, y=105)

    ## 9.18 ##
    simCB918_anamnese = Radiobutton(page7anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint918)
    simCB918_anamnese.place(x=980, y=125)

    naoCB918_anamnese = Radiobutton(page7anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint918)
    naoCB918_anamnese.place(x=1025, y=125)

    ## BUTTON ##
    ProximoDP_anamnese = Button(page7anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoDP_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page8anamnese = ttk.Frame(nb1)
    nb1.add(page8anamnese, text="10 - Higiene do sono")
    ### page8 ###
    HdS = Label(page8anamnese, text="10 - Higiene do sono", font="Negrito 10 bold", foreground='blue')
    HdS.place(x=10, y=15)
    ## 10.01 ##
    anamnese_1001pergunta = Label(page8anamnese, text="10.01 - Qualidade do sono:")
    anamnese_1001pergunta.place(x=20, y=45)

    ## 10.02 ##
    anamnese_1002pergunta = Label(page8anamnese, text="10.02 - Dorme bem?")
    anamnese_1002pergunta.place(x=20, y=65)

    ## 10.03 ##
    anamnese_1003pergunta = Label(page8anamnese, text="10.03 - Tem sudorese durante a noite?")
    anamnese_1003pergunta.place(x=20, y=85)

    ## 10.04 ##
    anamnese_1004pergunta = Label(page8anamnese, text="10.04 - Range os dentes quando dorme?")
    anamnese_1004pergunta.place(x=20, y=105)

    ## 10.05 ##
    anamnese_1005pergunta = Label(page8anamnese, text="10.05 - Acorda várias vezes durante a noite?")
    anamnese_1005pergunta.place(x=20, y=125)

    ## 10.06 ##
    anamnese_1006pergunta = Label(page8anamnese, text="10.06 - Volta a dormir facilmente?")
    anamnese_1006pergunta.place(x=20, y=145)

    ## 10.07 ##
    anamnese_1007pergunta = Label(page8anamnese, text="10.07 - Fala dormindo?")
    anamnese_1007pergunta.place(x=20, y=165)

    ## 10.08 ##
    anamnese_1008pergunta = Label(page8anamnese, text="10.08 - Sonâmbulo?")
    anamnese_1008pergunta.place(x=20, y=185)

    ## 10.09 ##
    anamnese_1009pergunta = Label(page8anamnese, text="10.09 - Têm pesadelo?")
    anamnese_1009pergunta.place(x=20, y=205)

    ## 10.10 ##
    anamnese_1010pergunta = Label(page8anamnese, text="10.09 - Apresenta terror noturno?")
    anamnese_1010pergunta.place(x=20, y=225)

    ## 10.11 ##
    anamnese_1011pergunta = Label(page8anamnese, text="10.11 - Dorme sozinho no quarto?")
    anamnese_1011pergunta.place(x=20, y=245)

    ## 10.12 ##
    anamnese_1012pergunta = Label(page8anamnese, text="10.12 - Tem cama individual?")
    anamnese_1012pergunta.place(x=20, y=265)

    ## 10.13 ##
    anamnese_1013pergunta = Label(page8anamnese, text="10.13 - A criança acorda e vai para a camados pais?")
    anamnese_1013pergunta.place(x=20, y=285)

    ## 10.14 ##
    anamnese_1014pergunta = Label(page8anamnese, text="10.14 - Alguma dificuldade na fala?")
    anamnese_1014pergunta.place(x=20, y=305)

    ## 10.15 ##
    anamnese_1015pergunta = Label(page8anamnese, text="10.15 - Apresenta controle dos esfíncteres?")
    anamnese_1015pergunta.place(x=20, y=325)

    ## 10.16 ##
    anamnese_1016pergunta = Label(page8anamnese, text="10.16 - É independente nas atividades da vida diária?")
    anamnese_1016pergunta.place(x=20, y=345)

    ## 10.17 ##
    anamnese_1017pergunta = Label(page8anamnese, text="10.17 - Idade em que andou:")
    anamnese_1017pergunta.place(x=550, y=45)

    ## 10.18 ##
    anamnese_1018pergunta = Label(page8anamnese, text="10.18 - Idade em que falou:")
    anamnese_1018pergunta.place(x=550, y=65)

    ### TEXTS ###
    Texto1017_anamnese = Text(page8anamnese, width=35, height=1)
    Texto1017_anamnese.place(x=710, y=45)

    Texto1018_anamnese = Text(page8anamnese, width=35, height=1)
    Texto1018_anamnese.place(x=710, y=65)

    ### radioButtons ###
    ## VARS ##
    Optionint1001 = IntVar()
    Optionint1002 = IntVar()
    Optionint1003 = IntVar()
    Optionint1004 = IntVar()
    Optionint1005 = IntVar()
    Optionint1006 = IntVar()
    Optionint1007 = IntVar()
    Optionint1008 = IntVar()
    Optionint1009 = IntVar()
    Optionint1010 = IntVar()
    Optionint1011 = IntVar()
    Optionint1012 = IntVar()
    Optionint1013 = IntVar()
    Optionint1014 = IntVar()
    Optionint1015 = IntVar()
    Optionint1016 = IntVar()

    ## 10.01 ##
    CalmCB1001_anamnese = Radiobutton(page8anamnese, text="Calmo", value=1, width=5, anchor=W, variable=Optionint1001)
    CalmCB1001_anamnese.place(x=380, y=45)

    AgitCB1001_anamnese = Radiobutton(page8anamnese, text="Agitado", value=2, width=6, anchor=W, variable=Optionint1001)
    AgitCB1001_anamnese.place(x=445, y=45)

    ## 10.02 até 10.16 ##
    simCB1002_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1002)
    simCB1002_anamnese.place(x=415, y=65)

    naoCB1002_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1002)
    naoCB1002_anamnese.place(x=460, y=65)

    simCB1003_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1003)
    simCB1003_anamnese.place(x=415, y=85)

    naoCB1003_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1003)
    naoCB1003_anamnese.place(x=460, y=85)

    simCB1004_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1004)
    simCB1004_anamnese.place(x=415, y=105)

    naoCB1004_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1004)
    naoCB1004_anamnese.place(x=460, y=105)

    simCB1005_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1005)
    simCB1005_anamnese.place(x=415, y=125)

    naoCB1005_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1005)
    naoCB1005_anamnese.place(x=460, y=125)

    simCB1006_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1006)
    simCB1006_anamnese.place(x=415, y=145)

    naoCB1006_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1006)
    naoCB1006_anamnese.place(x=460, y=145)

    simCB1007_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1007)
    simCB1007_anamnese.place(x=415, y=165)

    naoCB1007_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1007)
    naoCB1007_anamnese.place(x=460, y=165)

    simCB1008_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1008)
    simCB1008_anamnese.place(x=415, y=185)

    naoCB1008_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1008)
    naoCB1008_anamnese.place(x=460, y=185)

    simCB1009_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1009)
    simCB1009_anamnese.place(x=415, y=205)

    naoCB1009_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1009)
    naoCB1009_anamnese.place(x=460, y=205)

    simCB1010_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1010)
    simCB1010_anamnese.place(x=415, y=225)

    naoCB1010_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1010)
    naoCB1010_anamnese.place(x=460, y=225)

    simCB1011_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1011)
    simCB1011_anamnese.place(x=415, y=245)

    naoCB1011_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1011)
    naoCB1011_anamnese.place(x=460, y=245)

    simCB1012_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1012)
    simCB1012_anamnese.place(x=415, y=265)

    naoCB1012_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1012)
    naoCB1012_anamnese.place(x=460, y=265)

    simCB1013_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1013)
    simCB1013_anamnese.place(x=415, y=285)

    naoCB1013_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1013)
    naoCB1013_anamnese.place(x=460, y=285)

    simCB1014_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1014)
    simCB1014_anamnese.place(x=415, y=305)

    naoCB1014_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1014)
    naoCB1014_anamnese.place(x=460, y=305)

    simCB1015_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1015)
    simCB1015_anamnese.place(x=415, y=325)

    naoCB1015_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1015)
    naoCB1015_anamnese.place(x=460, y=325)

    simCB1016_anamnese = Radiobutton(page8anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1016)
    simCB1016_anamnese.place(x=415, y=345)

    naoCB1016_anamnese = Radiobutton(page8anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1016)
    naoCB1016_anamnese.place(x=460, y=345)

    ### BUTTON ##
    ProximoHdS_anamnese = Button(page8anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoHdS_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page9anamnese = ttk.Frame(nb1)
    nb1.add(page9anamnese, text="11 - Lactação")
    ### page9 ###
    Lactacao = Label(page9anamnese, text="11 - Lactação", font="Negrito 10 bold", foreground='red')
    Lactacao.place(x=10, y=15)

    ## 11.01 ##
    anamnese_1101pergunta = Label(page9anamnese, text="11.01 - Foi amamentado?")
    anamnese_1101pergunta.place(x=20, y=45)

    anamnese_1102pergunta = Label(page9anamnese, text="11.02 - Teve problemas com alimentação?")
    anamnese_1102pergunta.place(x=20, y=65)

    anamnese_1103pergunta = Label(page9anamnese, text="11.03 - Apresentou dificuldades na sucção durante a amamentação?")
    anamnese_1103pergunta.place(x=20, y=85)

    anamnese_1104pergunta = Label(page9anamnese, text="11.04 - Quanto tempo se alimetou do seio?")
    anamnese_1104pergunta.place(x=20, y=105)

    anamnese_1105pergunta = Label(page9anamnese, text="11.05 - Usou mamadeira?")
    anamnese_1105pergunta.place(x=20, y=185)

    anamnese_1106pergunta = Label(page9anamnese, text="11.06 - se SIM, responda até quando?")
    anamnese_1106pergunta.place(x=20, y=205)

    anamnese_1107pergunta = Label(page9anamnese, text="11.07 - Descreva a alimentação atual?")
    anamnese_1107pergunta.place(x=20, y=245)

    ### TEXTS ###
    Texto1104_anamnese = Text(page9anamnese, width=65, height=3)
    Texto1104_anamnese.place(x=20, y=125)

    Texto1106_anamnese = Text(page9anamnese, width=65, height=1)
    Texto1106_anamnese.place(x=20, y=225)

    Texto1107_anamnese = Text(page9anamnese, width=65, height=7)
    Texto1107_anamnese.place(x=20, y=265)

    ###  RADIOBUTTONS ###
    Optionint1101 = IntVar()
    Optionint1102 = IntVar()
    Optionint1103 = IntVar()
    Optionint1105 = IntVar()

    simCB1101_anamnese = Radiobutton(page9anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1101)
    simCB1101_anamnese.place(x=445, y=45)

    naoCB1101_anamnese = Radiobutton(page9anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1101)
    naoCB1101_anamnese.place(x=490, y=45)

    simCB1102_anamnese = Radiobutton(page9anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1102)
    simCB1102_anamnese.place(x=445, y=65)

    naoCB1102_anamnese = Radiobutton(page9anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1102)
    naoCB1102_anamnese.place(x=490, y=65)

    simCB1103_anamnese = Radiobutton(page9anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1103)
    simCB1103_anamnese.place(x=445, y=85)

    naoCB1103_anamnese = Radiobutton(page9anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1103)
    naoCB1103_anamnese.place(x=490, y=85)

    simCB1105_anamnese = Radiobutton(page9anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1105)
    simCB1105_anamnese.place(x=445, y=185)

    naoCB1105_anamnese = Radiobutton(page9anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1105)
    naoCB1105_anamnese.place(x=490, y=185)

    ### BUTTON ##
    ProximoLac_anamnese = Button(page9anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoLac_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page10anamnese = ttk.Frame(nb1)
    nb1.add(page10anamnese, text="12 - Antecedentes Fmiliares")
    ### page10 ###
    Lactacao = Label(page10anamnese, text="12 - Antecedentes Fmiliares", font="Negrito 10 bold", foreground='red')
    Lactacao.place(x=10, y=15)

    ## Aviso ##
    anamnese_12Aviso = Label(page10anamnese, text="Estas questões devem ser respondidas considerando-se:\nPai, mãe, avós maternos e paternos,tios, primos maternos e paternos.", font='Negrito 10 bold', foreground='green', borderwidth=2, relief="solid", bg='light gray')
    anamnese_12Aviso.place(x=50, y=45)

    ## 12.01 ##
    anamnese_1201pergunta = Label(page10anamnese, text="12.01 - Há algum nervoso na família?")
    anamnese_1201pergunta.place(x=20, y=105)

    ## 12.02 ##
    anamnese_1202pergunta = Label(page10anamnese, text="12.02 - Há algum deficiente mental na família?")
    anamnese_1202pergunta.place(x=20, y=125)

    ## 12.03 ##
    anamnese_1203pergunta = Label(page10anamnese, text="12.03 - Há alguém internado?")
    anamnese_1203pergunta.place(x=20, y=145)

    ## 12.03.01 ##
    anamnese_1203pergunta = Label(page10anamnese, text="12.03.01 - Se SIM, descreva abaixo, as causas possíveis da internação", foreground='blue')
    anamnese_1203pergunta.place(x=20, y=165)

    ## 12.04 ##
    anamnese_1204pergunta = Label(page10anamnese, text="12.04 - Alguém bebe muito?")
    anamnese_1204pergunta.place(x=550, y=45)

    ## 12.05 ##
    anamnese_1205pergunta = Label(page10anamnese, text="12.05 - Alguém viciado em drogas?")
    anamnese_1205pergunta.place(x=550, y=65)

    ## 12.06 ##
    anamnese_1206pergunta = Label(page10anamnese, text="12.06 - Há alguém com alergia ou asma?")
    anamnese_1206pergunta.place(x=550, y=85)

    ## 12.07 ##
    anamnese_1207pergunta = Label(page10anamnese, text="12.07 - Há alguém com ataques?")
    anamnese_1207pergunta.place(x=550, y=105)

    ## 12.07.01 ##
    anamnese_120701pergunta = Label(page10anamnese, text="12.07.01 - Se SIM, descreva abaixo qual tipo:")
    anamnese_120701pergunta.place(x=550, y=125)

    ### TEXTS ###
    Texto120301_anamnese = Text(page10anamnese, width=65, height=6)
    Texto120301_anamnese.place(x=20, y=195)

    Texto120701_anamnese = Text(page10anamnese, width=65, height=9)
    Texto120701_anamnese.place(x=550, y=145)

    ### RadioButtons ###
    ## VARS ##
    Optionint1201 = IntVar()
    Optionint1202 = IntVar()
    Optionint1203 = IntVar()
    Optionint1204 = IntVar()
    Optionint1205 = IntVar()
    Optionint1206 = IntVar()
    Optionint1207 = IntVar()

    simCB1201_anamnese = Radiobutton(page10anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1201)
    simCB1201_anamnese.place(x=445, y=105)

    naoCB1201_anamnese = Radiobutton(page10anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1201)
    naoCB1201_anamnese.place(x=490, y=105)

    simCB1202_anamnese = Radiobutton(page10anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1202)
    simCB1202_anamnese.place(x=445, y=125)

    naoCB1202_anamnese = Radiobutton(page10anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1202)
    naoCB1202_anamnese.place(x=490, y=125)

    simCB1203_anamnese = Radiobutton(page10anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1203)
    simCB1203_anamnese.place(x=445, y=145)

    naoCB1203_anamnese = Radiobutton(page10anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1203)
    naoCB1203_anamnese.place(x=490, y=145)

    simCB1204_anamnese = Radiobutton(page10anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1204)
    simCB1204_anamnese.place(x=945, y=45)

    naoCB1204_anamnese = Radiobutton(page10anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1204)
    naoCB1204_anamnese.place(x=990, y=45)

    simCB1205_anamnese = Radiobutton(page10anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1205)
    simCB1205_anamnese.place(x=945, y=65)

    naoCB1205_anamnese = Radiobutton(page10anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1205)
    naoCB1205_anamnese.place(x=990, y=65)

    simCB1206_anamnese = Radiobutton(page10anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1206)
    simCB1206_anamnese.place(x=945, y=85)

    naoCB1206_anamnese = Radiobutton(page10anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1206)
    naoCB1206_anamnese.place(x=990, y=85)

    simCB1207_anamnese = Radiobutton(page10anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1207)
    simCB1207_anamnese.place(x=945, y=105)

    naoCB1207_anamnese = Radiobutton(page10anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1207)
    naoCB1207_anamnese.place(x=990, y=105)

    ### BUTTON ##
    ProximoAF_anamnese = Button(page10anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoAF_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page11anamnese = ttk.Frame(nb1)
    nb1.add(page11anamnese, text="13 - Sexualidade")
    ### page11 ###
    Sexualidade = Label(page11anamnese, text="13 - Sexualidade", font="Negrito 10 bold", foreground='red')
    Sexualidade.place(x=10, y=15)

    ## 13.01 ##
    anamnese_1301pergunta = Label(page11anamnese, text="13.01 - Recebe orientação sexual?")
    anamnese_1301pergunta.place(x=20, y=45)

    ## 13.02 ##
    anamnese_1302pergunta = Label(page11anamnese, text="13.02 - Apresenta curiosidade sexual?")
    anamnese_1302pergunta.place(x=20, y=65)

    ## 13.02.01 ##
    anamnese_130201pergunta = Label(page11anamnese, text="13.02.01 - Quando?", foreground='blue')
    anamnese_130201pergunta.place(x=20, y=85)

    ## 13.03 ##
    anamnese_1303pergunta = Label(page11anamnese, text="13.03 - Qual a atitude dos pais?")
    anamnese_1303pergunta.place(x=20, y=225)

    ## 13.04 ##
    anamnese_1304pergunta = Label(page11anamnese, text="13.04 - A criança se masturba?")
    anamnese_1304pergunta.place(x=550, y=45)

    ## 13.04.01 ##
    anamnese_130401pergunta = Label(page11anamnese, text="13.04.01 - Com que frequência?", foreground='blue')
    anamnese_130401pergunta.place(x=550, y=65)

    ## 13.04.02 ##
    anamnese_130402pergunta = Label(page11anamnese, text="13.04.02 - Quando começou?", foreground='blue')
    anamnese_130402pergunta.place(x=550, y=185)

    ## 13.04.03 ##
    anamnese_130403pergunta = Label(page11anamnese, text="13.04.03 - Qual foi a atitude dos pais?", foreground='blue')
    anamnese_130403pergunta.place(x=550, y=305)

    ### TEXTS ###
    Texto130201_anamnese = Text(page11anamnese, width=65, height=7)
    Texto130201_anamnese.place(x=20, y=105)

    Texto1303_anamnese = Text(page11anamnese, width=65, height=7)
    Texto1303_anamnese.place(x=20, y=245)

    Texto130401_anamnese = Text(page11anamnese, width=65, height=6)
    Texto130401_anamnese.place(x=550, y=85)

    Texto130402_anamnese = Text(page11anamnese, width=65, height=6)
    Texto130402_anamnese.place(x=550, y=205)

    Texto130403_anamnese = Text(page11anamnese, width=65, height=6)
    Texto130403_anamnese.place(x=550, y=325)

    ### RadioButtons ###
    ## VARS ##
    Optionint1301 = IntVar()
    Optionint1302 = IntVar()
    Optionint1304 = IntVar()

    simCB1301_anamnese = Radiobutton(page11anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1301)
    simCB1301_anamnese.place(x=445, y=45)

    naoCB1301_anamnese = Radiobutton(page11anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1301)
    naoCB1301_anamnese.place(x=490, y=45)

    simCB1302_anamnese = Radiobutton(page11anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1302)
    simCB1302_anamnese.place(x=445, y=65)

    naoCB1302_anamnese = Radiobutton(page11anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1302)
    naoCB1302_anamnese.place(x=490, y=65)

    simCB1304_anamnese = Radiobutton(page11anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1304)
    simCB1304_anamnese.place(x=945, y=45)

    naoCB1304_anamnese = Radiobutton(page11anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1304)
    naoCB1304_anamnese.place(x=990, y=45)

    ### BUTTON ##
    ProximoSXD_anamnese = Button(page11anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoSXD_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page12anamnese = ttk.Frame(nb1)
    nb1.add(page12anamnese, text="14 - Saúde/Doença")
    ### page12 ###
    SD = Label(page12anamnese, text="14 - Saúde/Doença", font="Negrito 10 bold", foreground='blue')
    SD.place(x=10, y=15)

    ## 14.01 ##
    anamnese_1401pergunta = Label(page12anamnese, text="14.01 - Está com a vacinação atualizada?")
    anamnese_1401pergunta.place(x=20, y=45)

    ## 14.02 ##
    anamnese_1402pergunta = Label(page12anamnese, text="14.02 - Quais doenças teve na infância?")
    anamnese_1402pergunta.place(x=20, y=65)

    ## 14.02.04 ##
    anamnese_140204pergunta = Label(page12anamnese, text="14.02.04 - Expacifique abaixo:")
    anamnese_140204pergunta.place(x=350, y=125)

    ## 14.02.07 ##
    anamnese_140207pergunta = Label(page12anamnese, text="14.02.07 - Expacifique abaixo:")
    anamnese_140207pergunta.place(x=350, y=185)

    ## 14.02.12 ##
    anamnese_140212pergunta = Label(page12anamnese, text="14.02.12 - Expacifique abaixo:")
    anamnese_140212pergunta.place(x=350, y=285)

    ## 14.02.14 ##
    anamnese_140214pergunta = Label(page12anamnese, text="14.02.14 - Expacifique abaixo:")
    anamnese_140214pergunta.place(x=900, y=45)

    ### ChackButtons ###
    FA_cb1402Anamnese = Checkbutton(page12anamnese, text="Febre Alta", width=21, anchor=W)
    FA_cb1402Anamnese.place(x=40, y=85)

    Conc_cb1402Anamnese = Checkbutton(page12anamnese, text="Convunsões", width=20, anchor=W)
    Conc_cb1402Anamnese.place(x=40, y=105)

    FA_cb1402Anamnese = Checkbutton(page12anamnese, text="Cirurgias:", width=20, anchor=W)
    FA_cb1402Anamnese.place(x=40, y=125)

    Acide_cb1202Anamnese = Checkbutton(page12anamnese, text="Acidentes", width=20, anchor=W)
    Acide_cb1202Anamnese.place(x=40, y=165)

    Alerg_cb1202Anamnese = Checkbutton(page12anamnese, text="Alergias:", width=20, anchor=W)
    Alerg_cb1202Anamnese.place(x=40, y=185)

    PcA_cb1402Anamnese = Checkbutton(page12anamnese, text="Problemas com a aldição", width=20, anchor=W)
    PcA_cb1402Anamnese.place(x=40, y=225)

    PdV_cb1402Anamnese = Checkbutton(page12anamnese, text="Problemas de visão", width=20, anchor=W)
    PdV_cb1402Anamnese.place(x=40, y=245)

    Infec_cb1202Anamnese = Checkbutton(page12anamnese, text="Infecções", width=20, anchor=W)
    Infec_cb1202Anamnese.place(x=40, y=265)

    AtdT_cb1202Anamnese = Checkbutton(page12anamnese, text="Algum tipo de tratamento:", width=20, anchor=W)
    AtdT_cb1202Anamnese.place(x=40, y=285)

    Acide_cb1202Anamnese = Checkbutton(page12anamnese, text="14.02.13 - Faz uso contínuo de medicamentos:", width=35, anchor=W)
    Acide_cb1202Anamnese.place(x=585, y=45)

    Acide_cb1202Anamnese = Checkbutton(page12anamnese, text="14.02.15 - Outros:", width=35, anchor=W)
    Acide_cb1202Anamnese.place(x=585, y=145)

    ### TEXTS ###
    Texto140204_anamnese = Text(page12anamnese, width=65, height=1)
    Texto140204_anamnese.place(x=40, y=145)

    Texto140207_anamnese = Text(page12anamnese, width=65, height=1)
    Texto140207_anamnese.place(x=40, y=205)

    Texto140212_anamnese = Text(page12anamnese, width=65, height=5)
    Texto140212_anamnese.place(x=40, y=305)

    Texto140214_anamnese = Text(page12anamnese, width=55, height=5)
    Texto140214_anamnese.place(x=585, y=65)

    Texto140215_anamnese = Text(page12anamnese, width=55, height=5)
    Texto140215_anamnese.place(x=585, y=165)

    ### RadioButtons ###
    ## VARS ##
    Optionint1401 = IntVar()

    simCB1401_anamnese = Radiobutton(page12anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1401)
    simCB1401_anamnese.place(x=445, y=45)

    naoCB1401_anamnese = Radiobutton(page12anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1401)
    naoCB1401_anamnese.place(x=490, y=45)

    ### BUTTON ##
    ProximoSaude_anamnese = Button(page12anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoSaude_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page13anamnese = ttk.Frame(nb1)
    nb1.add(page13anamnese, text="15 - Manipulações e Tiques")
    ### page13 ###
    MeT = Label(page13anamnese, text="15 - Manipulações e Tiques", font="Negrito 10 bold", foreground='red')
    MeT.place(x=10, y=15)

    ## 15.01 ##
    anamnese_1501pergunta = Label(page13anamnese, text="15.01 - Usou chupeta até quando?")
    anamnese_1501pergunta.place(x=20, y=45)

    ## 15.02 ##
    anamnese_1502pergunta = Label(page13anamnese, text="15.02 - Chupou o dedo até quando?")
    anamnese_1502pergunta.place(x=20, y=65)

    ## 15.03 ##
    anamnese_1503pergunta = Label(page13anamnese, text="15.03 - Roeu ou rói unhas?")
    anamnese_1503pergunta.place(x=20, y=85)

    ## 15.04 ##
    anamnese_1504pergunta = Label(page13anamnese, text="15.04 - Puxa as orelhas?")
    anamnese_1504pergunta.place(x=20, y=105)

    ## 15.05 ##
    anamnese_1505pergunta = Label(page13anamnese, text="15.05 - Qual a atitude dos pais, diante hábitos?")
    anamnese_1505pergunta.place(x=20, y=145)

    ## 15.07 ##
    anamnese_1507pergunta = Label(page13anamnese, text="15.07 - A criança apresenta tiques?")
    anamnese_1507pergunta.place(x=580, y=45)

    ## 15.07.01 ##
    anamnese_150701pergunta = Label(page13anamnese, text="15.07.01 - Descreva-os abaixo:", foreground='blue')
    anamnese_150701pergunta.place(x=580, y=65)

    ## 15.08 ##
    anamnese_1508pergunta = Label(page13anamnese, text="15.08 - Atitude tomada pelos pais?")
    anamnese_1508pergunta.place(x=580, y=185)

    ### TEXTS ###
    Texto1501_anamnese = Text(page13anamnese, width=40, height=1)
    Texto1501_anamnese.place(x=215, y=45)

    Texto1502_anamnese = Text(page13anamnese, width=40, height=1)
    Texto1502_anamnese.place(x=215, y=65)

    Texto1506_anamnese = Text(page13anamnese, width=65, height=5)
    Texto1506_anamnese.place(x=20, y=165)

    Texto150701_anamnese = Text(page13anamnese, width=60, height=5)
    Texto150701_anamnese.place(x=580, y=85)

    Texto1508_anamnese = Text(page13anamnese, width=65, height=5)
    Texto1508_anamnese.place(x=580, y=205)

    ### RadioButtons ###
    ## VARS ##
    Optionint1503 = IntVar()
    Optionint1504 = IntVar()
    Optionint1505 = IntVar()
    Optionint1507 = IntVar()

    simCB1503_anamnese = Radiobutton(page13anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1503)
    simCB1503_anamnese.place(x=445, y=85)

    naoCB1503_anamnese = Radiobutton(page13anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1503)
    naoCB1503_anamnese.place(x=490, y=85)

    simCB1504_anamnese = Radiobutton(page13anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1504)
    simCB1504_anamnese.place(x=445, y=105)

    naoCB1504_anamnese = Radiobutton(page13anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1504)
    naoCB1504_anamnese.place(x=490, y=105)

    simCB1505_anamnese = Radiobutton(page13anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1505)
    simCB1505_anamnese.place(x=445, y=125)

    naoCB1505_anamnese = Radiobutton(page13anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1505)
    naoCB1505_anamnese.place(x=490, y=125)

    simCB1507_anamnese = Radiobutton(page13anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1507)
    simCB1507_anamnese.place(x=945, y=45)

    naoCB1507_anamnese = Radiobutton(page13anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1507)
    naoCB1507_anamnese.place(x=990, y=45)

    ### BUTTON ##
    ProximoMeT_anamnese = Button(page13anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoMeT_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page14anamnese = ttk.Frame(nb1)
    nb1.add(page14anamnese, text="16 - Sociabilidade")
    ### page14 ###
    Socia = Label(page14anamnese, text="16 - Sociabilidade", font="Negrito 10 bold", foreground='red')
    Socia.place(x=10, y=15)

    ## 16.01 ##
    anamnese_1601pergunta = Label(page14anamnese, text="16.01 - Faz amigos facilmente?")
    anamnese_1601pergunta.place(x=20, y=45)

    ## 16.02 ##
    anamnese_1602pergunta = Label(page14anamnese, text="16.02 - Gosta de fazer visitas?")
    anamnese_1602pergunta.place(x=20, y=65)

    ## 16.03 ##
    anamnese_1603pergunta = Label(page14anamnese, text="16.03 - Adapta-se facilmente ao meio?")
    anamnese_1603pergunta.place(x=20, y=85)

    ## 16.04 ##
    anamnese_1604pergunta = Label(page14anamnese, text="16.04 - Tem apelido?")
    anamnese_1604pergunta.place(x=20, y=105)

    ## 16.05 ##
    anamnese_1605pergunta = Label(page14anamnese, text="16.05 - É mais dado a liderar?")
    anamnese_1605pergunta.place(x=20, y=125)

    ## 16.06 ##
    anamnese_1606pergunta = Label(page14anamnese, text="16.06 - É autoritário?")
    anamnese_1606pergunta.place(x=20, y=145)

    ## 16.07 ##
    anamnese_1607pergunta = Label(page14anamnese, text="16.07 - Gosta de jogos esportivos?")
    anamnese_1607pergunta.place(x=20, y=165)

    ## 16.08 ##
    anamnese_1608pergunta = Label(page14anamnese, text="16.08 - Tem amigos na vizinhança?")
    anamnese_1608pergunta.place(x=20, y=185)

    ## 16.09 ##
    anamnese_1609pergunta = Label(page14anamnese, text="16.09 - Gosta de passeios e festas?")
    anamnese_1609pergunta.place(x=20, y=205)

    ## 16.10 ##
    anamnese_1610pergunta = Label(page14anamnese, text="16.10 - Preferências de diversão:")
    anamnese_1610pergunta.place(x=20, y=225)

    ## 16.11 ##
    anamnese_1611pergunta = Label(page14anamnese, text="16.11 - Características da crianças?")
    anamnese_1611pergunta.place(x=580, y=45)

    ## 16.10 ##
    anamnese_1610pergunta = Label(page14anamnese, text="16.12 - Tem algum hábito/mania")
    anamnese_1610pergunta.place(x=580, y=225)

    ### TEXTS ###
    Texto1610_anamnese = Text(page14anamnese, width=65, height=6)
    Texto1610_anamnese.place(x=20, y=245)

    Texto1612_anamnese = Text(page14anamnese, width=65, height=6)
    Texto1612_anamnese.place(x=580, y=245)

    ### ChackButtons ###
    Intro_cb1611Anamnese = Checkbutton(page14anamnese, text="Introvertida", width=21, anchor=W)
    Intro_cb1611Anamnese.place(x=600, y=65)

    Afetu_cb1611Anamnese = Checkbutton(page14anamnese, text="Afetuosa", width=21, anchor=W)
    Afetu_cb1611Anamnese.place(x=600, y=85)

    Obed_cb1611Anamnese = Checkbutton(page14anamnese, text="Obediente", width=21, anchor=W)
    Obed_cb1611Anamnese.place(x=600, y=105)

    Resist_cb1611Anamnese = Checkbutton(page14anamnese, text="Resistente", width=21, anchor=W)
    Resist_cb1611Anamnese.place(x=600, y=125)

    Coopera_cb1611Anamnese = Checkbutton(page14anamnese, text="Cooperador", width=21, anchor=W)
    Coopera_cb1611Anamnese.place(x=600, y=145)

    Medrosa_cb1611Anamnese = Checkbutton(page14anamnese, text="Medrosa", width=21, anchor=W)
    Medrosa_cb1611Anamnese.place(x=600, y=165)

    Insegura_cb1611Anamnese = Checkbutton(page14anamnese, text="Insegura", width=21, anchor=W)
    Insegura_cb1611Anamnese.place(x=600, y=185)

    ### RadioButtons ###
    ## VAR ##
    Optionint1601 = IntVar()
    Optionint1602 = IntVar()
    Optionint1603 = IntVar()
    Optionint1604 = IntVar()
    Optionint1605 = IntVar()
    Optionint1606 = IntVar()
    Optionint1607 = IntVar()
    Optionint1608 = IntVar()
    Optionint1609 = IntVar()

    simCB1601_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1601)
    simCB1601_anamnese.place(x=445, y=45)

    naoCB1601_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1601)
    naoCB1601_anamnese.place(x=490, y=45)

    simCB1602_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1602)
    simCB1602_anamnese.place(x=445, y=65)

    naoCB1602_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1602)
    naoCB1602_anamnese.place(x=490, y=65)

    simCB1603_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1603)
    simCB1603_anamnese.place(x=445, y=85)

    naoCB1603_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1603)
    naoCB1603_anamnese.place(x=490, y=85)

    simCB1604_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1604)
    simCB1604_anamnese.place(x=445, y=105)

    naoCB1604_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1604)
    naoCB1604_anamnese.place(x=490, y=105)

    simCB1605_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1605)
    simCB1605_anamnese.place(x=445, y=125)

    naoCB1605_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1605)
    naoCB1605_anamnese.place(x=490, y=125)

    simCB1606_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1606)
    simCB1606_anamnese.place(x=445, y=145)

    naoCB1606_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1606)
    naoCB1606_anamnese.place(x=490, y=145)

    simCB1607_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1607)
    simCB1607_anamnese.place(x=445, y=165)

    naoCB1607_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1607)
    naoCB1607_anamnese.place(x=490, y=165)

    simCB1608_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1608)
    simCB1608_anamnese.place(x=445, y=185)

    naoCB1608_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1608)
    naoCB1608_anamnese.place(x=490, y=185)

    simCB1609_anamnese = Radiobutton(page14anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1609)
    simCB1609_anamnese.place(x=445, y=205)

    naoCB1609_anamnese = Radiobutton(page14anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1609)
    naoCB1609_anamnese.place(x=490, y=205)

    ### BUTTON ##
    ProximoSocial_anamnese = Button(page14anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoSocial_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page15anamnese = ttk.Frame(nb1)
    nb1.add(page15anamnese, text="17 - Autonomia")
    ### page15 ###
    autonomia = Label(page15anamnese, text="17 - Autonomia", font="Negrito 10 bold", foreground='red')
    autonomia.place(x=10, y=15)

    ## 17.01 ##
    anamnese_1701pergunta = Label(page15anamnese, text="17.01 - Com que idade começou a comer sozinha?")
    anamnese_1701pergunta.place(x=20, y=45)

    ## 17.02 ##
    anamnese_1702pergunta = Label(page15anamnese, text="17.02 - Com que idade começou a vestir-se sozinha?")
    anamnese_1702pergunta.place(x=20, y=165)

    ## 17.03 ##
    anamnese_1703pergunta = Label(page15anamnese, text="17.03 - Com que idade começou a tomar banho sozinha?")
    anamnese_1703pergunta.place(x=20, y=285)

    ### TEXTS ###
    Texto1701_anamnese = Text(page15anamnese, width=85, height=5)
    Texto1701_anamnese.place(x=20, y=65)

    Texto1702_anamnese = Text(page15anamnese, width=85, height=5)
    Texto1702_anamnese.place(x=20, y=185)

    Texto1703_anamnese = Text(page15anamnese, width=85, height=5)
    Texto1703_anamnese.place(x=20, y=305)

    ### BUTTON ##
    ProximoAutonomia_anamnese = Button(page15anamnese, text='Próximo', font="Negrito 8 bold", bg='white', foreground='red')
    ProximoAutonomia_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page16anamnese = ttk.Frame(nb1)
    nb1.add(page16anamnese, text="18 - Escolaridade")
    ### page16 ###
    Escolaridade = Label(page16anamnese, text="18 - Escolaridade", font="Negrito 10 bold", foreground='red')
    Escolaridade.place(x=10, y=15)

    ## 18.01 ##
    anamnese_1801pergunta = Label(page16anamnese, text="18.01 - Vai bem na escola?")
    anamnese_1801pergunta.place(x=20, y=45)

    ## 18.02 ##
    anamnese_1802pergunta = Label(page16anamnese, text="18.02 - Com que idade começou a vestir-se sozinha?")
    anamnese_1802pergunta.place(x=20, y=65)

    ## 18.03 ##
    anamnese_1803pergunta = Label(page16anamnese, text="18.03 - Com que idade começou a tomar banho sozinha?")
    anamnese_1803pergunta.place(x=20, y=85)

    ## 18.03.01 ##
    anamnese_180301pergunta = Label(page16anamnese, text="18.03.01 - Se SIM, descreva abaixo, as causas possíveis das faltas ocorrentes?")
    anamnese_180301pergunta.place(x=20, y=105)

    ## 18.04 ##
    anamnese_1804pergunta = Label(page16anamnese, text="18.04 - Os pais estudam com a criança?")
    anamnese_1804pergunta.place(x=20, y=185)

    ## 18.05 ##
    anamnese_1805pergunta = Label(page16anamnese, text="18.05 - Gosta do(a) professor(a)?")
    anamnese_1805pergunta.place(x=20, y=205)

    ## 18.06 ##
    anamnese_1806pergunta = Label(page16anamnese, text="18.06 - É castigado quando não tira notas boas?")
    anamnese_1806pergunta.place(x=20, y=225)

    ## 18.07 ##
    anamnese_1807pergunta = Label(page16anamnese, text="18.07 - Quais matérias apresenta mais felicidade?")
    anamnese_1807pergunta.place(x=20, y=245)

    ## 18.08 ##
    anamnese_1808pergunta = Label(page16anamnese, text="18.08 - Quais matérias apresenta mais dificuldade?")
    anamnese_1808pergunta.place(x=20, y=285)

    ## 18.09 ##
    anamnese_1809pergunta = Label(page16anamnese, text="18.09 - É irrequieta na classe?")
    anamnese_1809pergunta.place(x=20, y=325)

    ## 18.10 ##
    anamnese_1810pergunta = Label(page16anamnese, text="18.10 - Foi reprovado alguma vez?")
    anamnese_1810pergunta.place(x=20, y=345)

    ## 18.10.01 ##
    anamnese_181001pergunta = Label(page16anamnese, text="18.10.01 - Descreva abaixo os motivos da reprovação:")
    anamnese_181001pergunta.place(x=20, y=365)

    ## 18.11 ##
    anamnese_1811pergunta = Label(page16anamnese, text="18.11 - Frequentou creche?")
    anamnese_1811pergunta.place(x=580, y=45)

    ## 18.12 ##
    anamnese_1812pergunta = Label(page16anamnese, text="18.12 - Frequentou Jardim da infância?")
    anamnese_1812pergunta.place(x=580, y=65)

    ## 18.13 ##
    anamnese_1813pergunta = Label(page16anamnese, text="18.13 - Mudou muito de escola?")
    anamnese_1813pergunta.place(x=580, y=85)

    ## 18.14 ##
    anamnese_1814pergunta = Label(page16anamnese, text="18.14 - Qual dessas possui maior habilidade motora?")
    anamnese_1814pergunta.place(x=580, y=105)

    ## 18.15 ##
    anamnese_1815pergunta = Label(page16anamnese, text="18.15 - Como se dá seu relacionamento?")
    anamnese_1815pergunta.place(x=580, y=145)

    ## 18.16 ##
    anamnese_1816pergunta = Label(page16anamnese, text="18.16 - Como se dá seu relacionamento com funcionários da escola?")
    anamnese_1816pergunta.place(x=580, y=225)

    ## 18.17 ##
    anamnese_1817pergunta = Label(page16anamnese, text="18.17 - Como a criança é educada?")
    anamnese_1817pergunta.place(x=580, y=305)

    ### RadioButtons ###
    ## VAR ##
    Optionint1801 = IntVar()
    Optionint1802 = IntVar()
    Optionint1803 = IntVar()
    Optionint1804 = IntVar()
    Optionint1805 = IntVar()
    Optionint1806 = IntVar()
    Optionint1809 = IntVar()
    Optionint1810 = IntVar()
    Optionint1811 = IntVar()
    Optionint1812 = IntVar()
    Optionint1813 = IntVar()

    simCB1801_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1801)
    simCB1801_anamnese.place(x=445, y=45)

    naoCB1801_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1801)
    naoCB1801_anamnese.place(x=490, y=45)

    simCB1802_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1802)
    simCB1802_anamnese.place(x=445, y=65)

    naoCB1802_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1802)
    naoCB1802_anamnese.place(x=490, y=65)

    simCB1803_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1803)
    simCB1803_anamnese.place(x=445, y=85)

    naoCB1803_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1803)
    naoCB1803_anamnese.place(x=490, y=85)

    simCB1804_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1804)
    simCB1804_anamnese.place(x=445, y=185)

    naoCB1804_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1804)
    naoCB1804_anamnese.place(x=490, y=185)

    simCB1805_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1805)
    simCB1805_anamnese.place(x=445, y=205)

    naoCB1805_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1805)
    naoCB1805_anamnese.place(x=490, y=205)

    simCB1806_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1806)
    simCB1806_anamnese.place(x=445, y=225)

    naoCB1806_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1806)
    naoCB1806_anamnese.place(x=490, y=225)

    simCB1809_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1809)
    simCB1809_anamnese.place(x=445, y=325)

    naoCB1809_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1809)
    naoCB1809_anamnese.place(x=490, y=325)

    simCB1811_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1811)
    simCB1811_anamnese.place(x=945, y=45)

    naoCB1811_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1811)
    naoCB1811_anamnese.place(x=990, y=45)

    simCB1810_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1810)
    simCB1810_anamnese.place(x=445, y=45)

    naoCB1810_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1810)
    naoCB1810_anamnese.place(x=490, y=45)

    simCB1811_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1811)
    simCB1811_anamnese.place(x=945, y=45)

    naoCB1811_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1811)
    naoCB1811_anamnese.place(x=990, y=45)

    simCB1812_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1812)
    simCB1812_anamnese.place(x=945, y=65)

    naoCB1812_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1812)
    naoCB1812_anamnese.place(x=990, y=65)

    simCB1813_anamnese = Radiobutton(page16anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint1813)
    simCB1813_anamnese.place(x=945, y=85)

    naoCB1813_anamnese = Radiobutton(page16anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint1813)
    naoCB1813_anamnese.place(x=990, y=85)

    ### ChackButtons ###
    Sermao_cb1811Anamnese = Checkbutton(page16anamnese, text="Sermão (Conversa)", width=21, anchor=W)
    Sermao_cb1811Anamnese.place(x=600, y=325)

    Castigo_cb1811Anamnese = Checkbutton(page16anamnese, text="Põe de castigo", width=21, anchor=W)
    Castigo_cb1811Anamnese.place(x=600, y=345)

    Briga_cb1811Anamnese = Checkbutton(page16anamnese, text="Briga (Grita)", width=21, anchor=W)
    Briga_cb1811Anamnese.place(x=600, y=365)

    Castigocorporal_cb1811Anamnese = Checkbutton(page16anamnese, text="Castigo corporal (Bate)", width=21, anchor=W)
    Castigocorporal_cb1811Anamnese.place(x=600, y=385)

    Abistinencia_cb1811Anamnese = Checkbutton(page16anamnese, text="Abistinência", width=21, anchor=W)
    Abistinencia_cb1811Anamnese.place(x=600, y=405)

    ### TEXTS ###
    Texto1801_anamnese = Text(page16anamnese, width=65, height=3)
    Texto1801_anamnese.place(x=20, y=125)

    Texto1802_anamnese = Text(page16anamnese, width=65, height=1)
    Texto1802_anamnese.place(x=20, y=265)

    Texto1803_anamnese = Text(page16anamnese, width=65, height=1)
    Texto1803_anamnese.place(x=20, y=305)

    Texto181001_anamnese = Text(page16anamnese, width=65, height=1)
    Texto181001_anamnese.place(x=20, y=385)

    Texto1815_anamnese = Text(page16anamnese, width=65, height=3)
    Texto1815_anamnese.place(x=580, y=165)

    Texto1816_anamnese = Text(page16anamnese, width=65, height=3)
    Texto1816_anamnese.place(x=580, y=245)

    ### BUTTON ##
    ProximoEscolaridade_anamnese = Button(page16anamnese, text='Continua', font="Negrito 8 bold", bg='white',
                                       foreground='red')
    ProximoEscolaridade_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page17anamnese = ttk.Frame(nb1)
    nb1.add(page17anamnese, text="19 - Interrelações")
    ### page17 ###
    Interrelacoes = Label(page17anamnese, text="19 - Interrelações", font="Negrito 10 bold", foreground='red')
    Interrelacoes.place(x=10, y=15)

    ## 19.01 ##
    anamnese_1901pergunta = Label(page17anamnese, text="19.01 - Vai bem na escola?")
    anamnese_1901pergunta.place(x=20, y=45)

    anamnese_1902pergunta = Label(page17anamnese, text="19.02 - Qual relação da criança com a mãe?")
    anamnese_1902pergunta.place(x=20, y=125)

    anamnese_1903pergunta = Label(page17anamnese, text="19.03 - Qual relação da criança com o pai?")
    anamnese_1903pergunta.place(x=20, y=165)

    anamnese_1904pergunta = Label(page17anamnese, text="19.04 - Qual relação da criança com as demais pessoas da família?")
    anamnese_1904pergunta.place(x=20, y=205)

    anamnese_1905pergunta = Label(page17anamnese, text="19.05 - Mãe, como se julga?")
    anamnese_1905pergunta.place(x=20, y=245)

    anamnese_1906pergunta = Label(page17anamnese, text="19.06 - Como a mãe trata os filhos?")
    anamnese_1906pergunta.place(x=20, y=265)

    anamnese_1907pergunta = Label(page17anamnese, text="19.07 - Pai, como se julga?")
    anamnese_1907pergunta.place(x=20, y=285)

    anamnese_1908pergunta = Label(page17anamnese, text="19.08 - Como o pai trata os filhos?")
    anamnese_1908pergunta.place(x=20, y=305)

    anamnese_1908pergunta = Label(page17anamnese, text="19.09 - Como é a relação do casal?")
    anamnese_1908pergunta.place(x=20, y=325)

    anamnese_1910pergunta = Label(page17anamnese, text="19.10 - Quem cuida dessa criança?")
    anamnese_1910pergunta.place(x=580, y=45)

    anamnese_1911pergunta = Label(page17anamnese, text="19.11 - Quem leva ao médico?")
    anamnese_1911pergunta.place(x=580, y=125)

    anamnese_1912pergunta = Label(page17anamnese, text="19.12 - Quem leva à escola?")
    anamnese_1912pergunta.place(x=580, y=205)

    ### TEXTS ###
    Texto1902_anamnese = Text(page17anamnese, width=65, height=1)
    Texto1902_anamnese.place(x=20, y=145)

    Texto1903_anamnese = Text(page17anamnese, width=65, height=1)
    Texto1903_anamnese.place(x=20, y=185)

    Texto1904_anamnese = Text(page17anamnese, width=65, height=1)
    Texto1904_anamnese.place(x=20, y=225)

    Texto1909_anamnese = Text(page17anamnese, width=65, height=3)
    Texto1909_anamnese.place(x=20, y=345)

    Texto1910_anamnese = Text(page17anamnese, width=65, height=3)
    Texto1910_anamnese.place(x=580, y=65)

    Texto1911_anamnese = Text(page17anamnese, width=65, height=3)
    Texto1911_anamnese.place(x=580, y=145)

    Texto1912_anamnese = Text(page17anamnese, width=65, height=3)
    Texto1912_anamnese.place(x=580, y=225)

    ### RadioButtons ###
    ## VAR ##
    Optionint1901 = IntVar()
    Optionint1905 = IntVar()
    Optionint1906 = IntVar()
    Optionint1907 = IntVar()
    Optionint1908 = IntVar()

    CasaCB1901_anamnese = Radiobutton(page17anamnese, text="Casa", value=1, width=5, anchor=W, variable=Optionint1901)
    CasaCB1901_anamnese.place(x=40, y=65)

    ApartCB1801_anamnese = Radiobutton(page17anamnese, text="Apartamento", value=2, width=10, anchor=W, variable=Optionint1901)
    ApartCB1801_anamnese.place(x=40, y=85)

    ApartCB1801_anamnese = Radiobutton(page17anamnese, text="Outro", value=3, width=5, anchor=W, variable=Optionint1901)
    ApartCB1801_anamnese.place(x=40, y=105)

    CalmaCB1905_anamnese = Radiobutton(page17anamnese, text="Calma", value=1, width=5, anchor=W, variable=Optionint1905)
    CalmaCB1905_anamnese.place(x=405, y=245)

    NervosaCB1805_anamnese = Radiobutton(page17anamnese, text="Nervosa", value=2, width=10, anchor=W, variable=Optionint1905)
    NervosaCB1805_anamnese.place(x=465, y=245)

    CalmaCB1906_anamnese = Radiobutton(page17anamnese, text="Calma", value=1, width=5, anchor=W, variable=Optionint1906)
    CalmaCB1906_anamnese.place(x=405, y=265)

    NervosaCB1806_anamnese = Radiobutton(page17anamnese, text="Nervosa", value=2, width=10, anchor=W,
                                       variable=Optionint1906)
    NervosaCB1806_anamnese.place(x=465, y=265)

    CalmaCB1907_anamnese = Radiobutton(page17anamnese, text="Calma", value=1, width=5, anchor=W, variable=Optionint1907)
    CalmaCB1907_anamnese.place(x=405, y=285)

    NervosaCB1807_anamnese = Radiobutton(page17anamnese, text="Nervosa", value=2, width=10, anchor=W,
                                         variable=Optionint1907)
    NervosaCB1807_anamnese.place(x=465, y=285)

    CalmaCB1908_anamnese = Radiobutton(page17anamnese, text="Calma", value=1, width=5, anchor=W, variable=Optionint1908)
    CalmaCB1908_anamnese.place(x=405, y=305)

    NervosaCB1808_anamnese = Radiobutton(page17anamnese, text="Nervosa", value=2, width=10, anchor=W,
                                         variable=Optionint1908)
    NervosaCB1808_anamnese.place(x=465, y=305)

    ### BUTTON ##
    ProximoInterrelacoes_anamnese = Button(page17anamnese, text='Próximo', font="Negrito 8 bold", bg='white',
                                          foreground='red')
    ProximoInterrelacoes_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page18anamnese = ttk.Frame(nb1)
    nb1.add(page18anamnese, text="20 - Vida Escolar")
    ### page18 ###
    Vida_Escolar = Label(page18anamnese, text="20 - Vida Escolar", font="Negrito 10 bold", foreground='red')
    Vida_Escolar.place(x=10, y=15)

    ## 20.01 ##
    anamnese_2001pergunta = Label(page18anamnese, text="20.01 - Idade em que entrou na escola")
    anamnese_2001pergunta.place(x=20, y=45)

    anamnese_2002pergunta = Label(page18anamnese, text="20.02 - Como se deu sua adaptação?")
    anamnese_2002pergunta.place(x=20, y=85)

    anamnese_2003pergunta = Label(page18anamnese, text="20.03 - Repetências:")
    anamnese_2003pergunta.place(x=20, y=225)

    anamnese_2004pergunta = Label(page18anamnese, text="20.04 - Quem a levava à escola?")
    anamnese_2004pergunta.place(x=20, y=250)

    anamnese_2005pergunta = Label(page18anamnese, text="20.05 - Se ressente quando mudo o professor?")
    anamnese_2005pergunta.place(x=20, y=285)

    anamnese_2006pergunta = Label(page18anamnese, text="20.06 - Comete a frequência escolar da criança?")
    anamnese_2006pergunta.place(x=20, y=305)

    anamnese_2007pergunta = Label(page18anamnese, text="20.07 - Como a família participa da vida escolar do filho?")
    anamnese_2007pergunta.place(x=580, y=45)

    anamnese_2008pergunta = Label(page18anamnese, text="20.08 - O que acha do atendimeento da escola?")
    anamnese_2008pergunta.place(x=580, y=125)

    anamnese_2009pergunta = Label(page18anamnese, text="20.09 - Acha que o desenvolvimento da criança é compatível com a sua idade?")
    anamnese_2009pergunta.place(x=580, y=205)

    anamnese_2010pergunta = Label(page18anamnese, text="20.10 - Algum comentário complementar?")
    anamnese_2010pergunta.place(x=580, y=285)

    ### TEXTS ###
    Texto2001_anamnese = Text(page18anamnese, width=65, height=1)
    Texto2001_anamnese.place(x=20, y=65)

    Texto2002_anamnese = Text(page18anamnese, width=65, height=6)
    Texto2002_anamnese.place(x=20, y=105)

    Texto2003_anamnese = Text(page18anamnese, width=51, height=1)
    Texto2003_anamnese.place(x=130, y=225)

    Texto2004_anamnese = Text(page18anamnese, width=43, height=1)
    Texto2004_anamnese.place(x=195, y=250)

    Texto2006_anamnese = Text(page18anamnese, width=65, height=3)
    Texto2006_anamnese.place(x=20, y=325)

    Texto2007_anamnese = Text(page18anamnese, width=60, height=3)
    Texto2007_anamnese.place(x=580, y=65)

    Texto2008_anamnese = Text(page18anamnese, width=60, height=3)
    Texto2008_anamnese.place(x=580, y=145)

    Texto2009_anamnese = Text(page18anamnese, width=60, height=3)
    Texto2009_anamnese.place(x=580, y=225)

    Texto2010_anamnese = Text(page18anamnese, width=60, height=4)
    Texto2010_anamnese.place(x=580, y=305)

    ### RadioButtons ###
    ### Vars ###
    Optionint2005 = IntVar()

    simCB2005_anamnese = Radiobutton(page18anamnese, text="Sim", value=1, width=3, anchor=W, variable=Optionint2005)
    simCB2005_anamnese.place(x=445, y=285)

    naoCB2005_anamnese = Radiobutton(page18anamnese, text="Não", value=2, width=3, anchor=W, variable=Optionint2005)
    naoCB2005_anamnese.place(x=490, y=285)

    ### BUTTON ##
    ProximoVidaEscolar_anamnese = Button(page18anamnese, text='Próximo', font="Negrito 8 bold", bg='white',
                                           foreground='red')
    ProximoVidaEscolar_anamnese.place(x=985, y=430, width=60, height=30)

    #############
    page19anamnese = ttk.Frame(nb1)
    nb1.add(page19anamnese, text="Fim")
    ### page19 ###
    ## AVISO ##
    anamnese_Observ = Label(page19anamnese, text="*Observações: todas as informações, comentários espontâneo que jugar importantes devem ser anotados pelo entrevistador",
                            font="Negrito 12")
    anamnese_Observ.place(x=15, y=25)

    anamnese_Assinam = Label(page19anamnese, text="Assinam:", font="Negrito 12")
    anamnese_Assinam.place(x=305, y=105)

    ## 21.01 ##
    anamnese_2101pergunta = Label(page19anamnese, text="Informante:", font="Negrito 12")
    anamnese_2101pergunta.place(x=305, y=125)

    ## 21.02 ##
    anamnese_2102pergunta = Label(page19anamnese, text="Grau de Parentesco:", font="Negrito 12")
    anamnese_2102pergunta.place(x=305, y=145)

    ## 21.03 ##
    anamnese_2103pergunta = Label(page19anamnese, text="Entrevistador:", font="Negrito 12")
    anamnese_2103pergunta.place(x=305, y=165)

    ## 20.04 ##
    anamnese_2104pergunta = Label(page19anamnese, text="Função:", font="Negrito 12")
    anamnese_2104pergunta.place(x=305, y=185)

    ## Data ##
    anamnese_2104pergunta = Label(page19anamnese, text="Brasília, 11 de Janeiro de 2022", font="Negrito 12")
    anamnese_2104pergunta.place(x=480, y=205)

    ### TEXTS ###
    Texto2101_anamnese = Text(page19anamnese, width=45, height=1)
    Texto2101_anamnese.place(x=465, y=125)

    Texto2102_anamnese = Text(page19anamnese, width=45, height=1)
    Texto2102_anamnese.place(x=465, y=145)

    Texto2103_anamnese = Text(page19anamnese, width=45, height=1)
    Texto2103_anamnese.place(x=465, y=165)

    Texto2104_anamnese = Text(page19anamnese, width=45, height=1)
    Texto2104_anamnese.place(x=465, y=185)

    ### BUTTON ##
    Inicio_anamnese = Button(page19anamnese, text='Início', font="Negrito 10 bold", bg='white', command=resetAnam)
    Inicio_anamnese.place(x=855, y=140, width=70, height=50)

    #############

    #Ea_img = Label(novoTrabalhoAnamnese, image=imgEA)
    #Ea_img.place(x=1020, y=30, width=60, height=45)

def abrirCPAluno():
    Jan_CPAluno = Toplevel()
    #Jan_CPAluno.geometry('1367x620+0+0')
    #Jan_CPAluno.resizable(False,False)
    width = Jan_CPAluno.winfo_screenwidth()
    height = Jan_CPAluno.winfo_screenheight()
    Jan_CPAluno.geometry("%dx%d" % (width, height))
    Jan_CPAluno.title('CP - Avaliação de Aluno')
    Jan_CPAluno.configure(bg='light gray')
    Jan_CPAluno.transient(trabalho)
    Jan_CPAluno.focus_force()
    Jan_CPAluno.grab_set()

    DiaMesAnoHoraCPAlunoLabel = Label(Jan_CPAluno, width=69, height=3)
    DiaMesAnoHoraCPAlunoLabel.place(x=860, y=5)

    DiaCPAlunoText = Text(Jan_CPAluno, width=3, height=1)
    DiaCPAlunoText.place(x=930, y=20)

    MesCPAlunoText = Text(Jan_CPAluno, width=15, height=1)
    MesCPAlunoText.place(x=1000, y=20)

    AnoCPAlunoText = Text(Jan_CPAluno, width=5, height=1)
    AnoCPAlunoText.place(x=1175, y=20)

    HoraCPAlunoText = Text(Jan_CPAluno, width=2, height=1)
    HoraCPAlunoText.place(x=1285, y=20)

    MinutoCPAlunoText = Text(Jan_CPAluno, width=2, height=1)
    MinutoCPAlunoText.place(x=1305, y=20)

    OptionintCPAlunoBimestreEameFinal = IntVar()

    CBBimestralCPAluno = Radiobutton(Jan_CPAluno, text="Bimestral", value=1, width=9, bg='Light grey', anchor=W, variable=OptionintCPAlunoBimestreEameFinal)
    CBBimestralCPAluno.place(x=10, y=55)

    CBExameFinalCPAluno = Radiobutton(Jan_CPAluno, text="Exame Final", value=2, width=9, bg='Light grey', anchor=W, variable=OptionintCPAlunoBimestreEameFinal)
    CBExameFinalCPAluno.place(x=10, y=75)

    IdCPAlunoText = Text(Jan_CPAluno, width=5, height=1)
    IdCPAlunoText.place(x=120, y=82)

    IdCPAlunoLabel = Label(Jan_CPAluno, text="Id", font="Arial 9 bold", bg='light grey')
    IdCPAlunoLabel.place(x=120, y=60)

    MatriculaCPAlunoText = Text(Jan_CPAluno, width=7, height=1)
    MatriculaCPAlunoText.place(x=170, y=82)

    MatriculaCPAlunoLabel = Label(Jan_CPAluno, text="Matrícula", font="Arial 9 bold", bg='light grey')
    MatriculaCPAlunoLabel.place(x=170, y=60)

    AlunoCPAluno = tkinter.StringVar()
    AlunoCPAlunocbbx = ttk.Combobox(Jan_CPAluno, width=40, height=1, textvariable=AlunoCPAluno)
    AlunoCPAlunocbbx.place(x=236, y=82)

    AlunoCPAlunoLabel = Label(Jan_CPAluno, text="Aluno em Conselho Participe", font="Arial 9 bold", bg='light grey')
    AlunoCPAlunoLabel.place(x=236, y=60)

    SerieCPAlunoText = Text(Jan_CPAluno, width=23, height=1)
    SerieCPAlunoText.place(x=505, y=82)

    SerieCPAlunoLabel = Label(Jan_CPAluno, text="Série", font="Arial 9 bold", bg='light grey')
    SerieCPAlunoLabel.place(x=505, y=60)

    TurmaCPAlunoText = Text(Jan_CPAluno, width=5, height=1)
    TurmaCPAlunoText.place(x=700, y=82)

    TurmaCPAlunoLabel = Label(Jan_CPAluno, text="Turma", font="Arial 9 bold", bg='light grey')
    TurmaCPAlunoLabel.place(x=700, y=60)

    BimestreCPAluno = tkinter.StringVar()
    BimestreCPAlunocbbx = ttk.Combobox(Jan_CPAluno, width=20, height=1, textvariable=BimestreCPAluno)
    BimestreCPAlunocbbx.place(x=750, y=82)

    BimestreCPAlunoLabel = Label(Jan_CPAluno, text="Bimestre", font="Arial 9 bold", bg='light grey')
    BimestreCPAlunoLabel.place(x=750, y=60)

    ResponsavelCPAlunoText = Text(Jan_CPAluno, width=29, height=1)
    ResponsavelCPAlunoText.place(x=900, y=82)

    ResponsavelCPAlunoLabel = Label(Jan_CPAluno, text="Responsável", font="Arial 9 bold", bg='light grey')
    ResponsavelCPAlunoLabel.place(x=900, y=60)

    DiaCPAlunoLabel = Label(Jan_CPAluno, text="Dia:")
    DiaCPAlunoLabel.place(x=900, y=20)

    MesCPAlunoLabel = Label(Jan_CPAluno, text="Mês:")
    MesCPAlunoLabel.place(x=965, y=20)

    AnoCPAlunoLabel = Label(Jan_CPAluno, text="Ano:")
    AnoCPAlunoLabel.place(x=1140, y=20)

    HoraCPAlunoLabel = Label(Jan_CPAluno, text="Hora:")
    HoraCPAlunoLabel.place(x=1245, y=20)

    Foto_Aluno_CPAluno = Label(Jan_CPAluno, image=imgFoto_Aluno)
    Foto_Aluno_CPAluno.place(x=1200, y=60)

    FaltasCPAlunoLabel = Label(Jan_CPAluno, text='Porcentagem de Faltas', font='negrito 10 bold', bg='light gray')
    FaltasCPAlunoLabel.place(x=1170, y=200)

    FaltasDoAlunoCPAlunoText = Text(Jan_CPAluno, bg='white', font='Arial 53 bold', foreground='green')
    FaltasDoAlunoCPAlunoText.place(x=1144, y=220, width=205, height=90)

    QuadroBimestralCPAlunoLabel = Label(Jan_CPAluno, text="Quadro de Médias Bimestrais", font="Arial 9 bold", bg='light grey', foreground='blue')
    QuadroBimestralCPAlunoLabel.place(x=12, y=105)

    PesoXNotasCPAlunoLabel = Label(Jan_CPAluno, text="Quadro de Notas : Peso x Nota Bimestral", font="Arial 9 bold", bg='light grey', foreground='blue')
    PesoXNotasCPAlunoLabel.place(x=12, y=205)

    ProIntPedCPAlunoLabel = Label(Jan_CPAluno, text="Proposta de Intervenção Pedagógica Pós Conselho Participativo para o Aluno", font="Arial 10 bold", bg='light grey', foreground='blue')
    ProIntPedCPAlunoLabel.place(x=342, y=305)

    cbComunicacao51 = Checkbutton(Jan_CPAluno, text="Seleciona Tudo", font="Arial 9 bold", bg='light grey', foreground='red', width=21, anchor=W)
    cbComunicacao51.place(x=10, y=305)

    ConsideracoesFinaisCPAlunoLabel = Label(Jan_CPAluno, text="Considerações Finais", font="Arial 9 bold", bg='light grey')
    ConsideracoesFinaisCPAlunoLabel.place(x=12, y=515)

### itens novo trabalho 1 ###
### criando frame ###
    fr_rolagemCPAluno_MediaBimestral = Frame(Jan_CPAluno, borderwidth=1, relief="solid")
    fr_rolagemCPAluno_MediaBimestral.place(x=10, y=125, width=1130, height=75)

    ### criando o canvas ###
    canvasCPAluno_MediaBimestral = Canvas(Jan_CPAluno)
    canvasCPAluno_MediaBimestral.place(x=11, y=126, width=1100, height=73)

    ### criando a barra de rolagem ###
    barra_de_rolagemCPAluno_MediaBimestral = ttk.Scrollbar(fr_rolagemCPAluno_MediaBimestral, orient=VERTICAL, command=canvasCPAluno_MediaBimestral.yview)
    barra_de_rolagemCPAluno_MediaBimestral.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasCPAluno_MediaBimestral.configure(yscrollcommand=barra_de_rolagemCPAluno_MediaBimestral.set)
    canvasCPAluno_MediaBimestral.bind('<Configure>', lambda e: canvasCPAluno_MediaBimestral.configure(scrollregion=canvasCPAluno_MediaBimestral.bbox("all")))

    fr_rolagemCPAluno_MediaBimestral = Frame(canvasCPAluno_MediaBimestral)

    canvasCPAluno_MediaBimestral.create_window((0, 0), window=fr_rolagemCPAluno_MediaBimestral, anchor="nw")

### itens novo trabalho 1 ###
### criando frame ###
    fr_rolagemCPAluno_PesoXNotaAlcancada = Frame(Jan_CPAluno, borderwidth=1, relief="solid")
    fr_rolagemCPAluno_PesoXNotaAlcancada.place(x=10, y=225, width=1130, height=75)

    ### criando o canvas ###
    canvasCPAluno_PesoXNotaAlcancada = Canvas(Jan_CPAluno)
    canvasCPAluno_PesoXNotaAlcancada.place(x=11, y=226, width=1100, height=73)

    ### criando a barra de rolagem ###
    barra_de_rolagemCPAluno_PesoXNotaAlcancada = ttk.Scrollbar(fr_rolagemCPAluno_PesoXNotaAlcancada, orient=VERTICAL, command=canvasCPAluno_PesoXNotaAlcancada.yview)
    barra_de_rolagemCPAluno_PesoXNotaAlcancada.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasCPAluno_PesoXNotaAlcancada.configure(yscrollcommand=barra_de_rolagemCPAluno_PesoXNotaAlcancada.set)
    canvasCPAluno_PesoXNotaAlcancada.bind('<Configure>', lambda e: canvasCPAluno_PesoXNotaAlcancada.configure(scrollregion=canvasCPAluno_PesoXNotaAlcancada.bbox("all")))

    fr_rolagemCPAluno_PesoXNotaAlcancada = Frame(canvasCPAluno_PesoXNotaAlcancada)

    canvasCPAluno_PesoXNotaAlcancada.create_window((0, 0), window=fr_rolagemCPAluno_PesoXNotaAlcancada, anchor="nw")

    ### itens novo trabalho 1 ###
    ### criando frame ###
    fr_rolagemCPAluno_ProIntPed = Frame(Jan_CPAluno, borderwidth=1, relief="solid")
    fr_rolagemCPAluno_ProIntPed.place(x=10, y=330, width=1130, height=185)

    ### criando o canvas ###
    canvasCPAluno_ProIntPed = Canvas(Jan_CPAluno)
    canvasCPAluno_ProIntPed.place(x=11, y=331 , width=1100, height=183)

    ### criando a barra de rolagem ###
    barra_de_rolagemCPAluno_ProIntPed = ttk.Scrollbar(fr_rolagemCPAluno_ProIntPed, orient=VERTICAL, command=canvasCPAluno_ProIntPed.yview)
    barra_de_rolagemCPAluno_ProIntPed.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasCPAluno_ProIntPed.configure(yscrollcommand=barra_de_rolagemCPAluno_ProIntPed.set)
    canvasCPAluno_ProIntPed.bind('<Configure>', lambda e: canvasCPAluno_ProIntPed.configure(
        scrollregion=canvasCPAluno_ProIntPed.bbox("all")))

    fr_rolagemCPAluno_ProIntPed = Frame(canvasCPAluno_ProIntPed)

    canvasCPAluno_ProIntPed.create_window((0, 0), window=fr_rolagemCPAluno_ProIntPed, anchor="nw")


    ConsideracoesFinaisTextCPAluno = Text(Jan_CPAluno, bg='aquamarine', font="Arial 9", width=160, height=9)
    ConsideracoesFinaisTextCPAluno.place(x=10, y=535)

    ApontamentoButtonCPAluno = Button(Jan_CPAluno, text='Apontamentos', font='negrito 15', bg="Yellow", command=Apontamento)
    ApontamentoButtonCPAluno.place(x=1180, y=320, width=140, height=50)

    ProposicoesButtonCPAluno = Button(Jan_CPAluno, text='Proposições', font='negrito 15', bg="palegreen", command=Preposicao)
    ProposicoesButtonCPAluno.place(x=1180, y=380, width=140, height=50)

    CarregaButtonCPAluno = Button(Jan_CPAluno, text='Carrega', font='negrito 15', bg="limegreen")
    CarregaButtonCPAluno.place(x=1180, y=520, width=140, height=50)



def abrirCPTurma():
    CPTurma = Toplevel()
    CPTurma.geometry('1090x620+260+70')
    CPTurma.resizable(False,False)
    CPTurma.title('CP - Avaliação das Turmas')
    CPTurma.configure(bg='light gray')
    CPTurma.transient(trabalho)
    CPTurma.focus_force()
    CPTurma.grab_set()

### itens novo trabalho 10 ###
    DiaMesAnoHoraCPTurmaLabel = Label(CPTurma, width=69, height=3)
    DiaMesAnoHoraCPTurmaLabel.place(x=560, y=5)

    DiaCPAlunoLabel = Label(CPTurma, text="Dia:")
    DiaCPAlunoLabel.place(x=600, y=20)

    MesCPAlunoLabel = Label(CPTurma, text="Mês:")
    MesCPAlunoLabel.place(x=670, y=20)

    AnoCPAlunoLabel = Label(CPTurma, text="Ano:")
    AnoCPAlunoLabel.place(x=840, y=20)

    HoraCPAlunoLabel = Label(CPTurma, text="Hora:")
    HoraCPAlunoLabel.place(x=950, y=20)

    DiaCPTurmaText = Text(CPTurma, width=3, height=1)
    DiaCPTurmaText.place(x=630, y=20)

    MesCPTurmaText = Text(CPTurma, width=15, height=1)
    MesCPTurmaText.place(x=700, y=20)

    AnoCPTurmaText = Text(CPTurma, width=5, height=1)
    AnoCPTurmaText.place(x=875, y=20)

    HoraCPTurmaText = Text(CPTurma, width=2, height=1)
    HoraCPTurmaText.place(x=985, y=20)

    MinutoCPTurmaText = Text(CPTurma, width=2, height=1)
    MinutoCPTurmaText.place(x=1005, y=20)

    CodigoCPTurmaLabel = Label(CPTurma, text="Código", font="Arial 9 bold", bg='light grey')
    CodigoCPTurmaLabel.place(x=10, y=60)

    CodigoCPTurma = Text(CPTurma, width=6, height=1)
    CodigoCPTurma.place(x=10, y=80)

    TurmaCPTurmaLabel = Label(CPTurma, text="Turma", font="Arial 9 bold", bg='light grey')
    TurmaCPTurmaLabel.place(x=70, y=60)

    TurmaCPTurma = tkinter.StringVar()
    TurmaCPTurmaCbbx = ttk.Combobox(CPTurma, width=12, height=1, textvariable=TurmaCPTurma)
    TurmaCPTurmaCbbx.place(x=70, y=80)

    SerieCPTurmaLabel = Label(CPTurma, text="Série", font="Arial 9 bold", bg='light grey')
    SerieCPTurmaLabel.place(x=173, y=60)

    SerieCPTurma = Text(CPTurma, width=20, height=1)
    SerieCPTurma.place(x=173, y=80)

    BimestreCPTurmaLabel = Label(CPTurma, text="Bimestre", font="Arial 9 bold", bg='light grey')
    BimestreCPTurmaLabel.place(x=345, y=60)

    BimestreCPTurma = tkinter.StringVar()
    BimestreCPTurmaCbbx = ttk.Combobox(CPTurma, width=12, height=1, textvariable=BimestreCPTurma)
    BimestreCPTurmaCbbx.place(x=345, y=80)

    ProfessorCPTurmaLabel = Label(CPTurma, text="Professor Tutor(Conselheiro)", font="Arial 9 bold", bg='light grey')
    ProfessorCPTurmaLabel.place(x=447, y=60)

    ProfessorCPTurma = Text(CPTurma, width=29, height=1)
    ProfessorCPTurma.place(x=447, y=80)

    RepresentanteCPTurmaLabel = Label(CPTurma, text="Representante da Turma", font="Arial 9 bold", bg='light grey')
    RepresentanteCPTurmaLabel.place(x=693, y=60)

    RepresentanteCPTurma = Text(CPTurma, width=45, height=1)
    RepresentanteCPTurma.place(x=693, y=80)

    TextoDasPages = Label(CPTurma, text="QUESTIONÁRIO DE CONSELHO PARTICIPATIVO CLASSE X ESCOLA", font="Arial 10 bold", bg='light gray', width=58, anchor=W)
    TextoDasPages.place(x=3, y=105)
### criação da multipage ###
    rows = 0
    while rows < 50:
        CPTurma.rowconfigure(rows, weight=1)
        CPTurma.columnconfigure(rows, weight=1)
        rows += 1
    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nb = ttk.Notebook(CPTurma)
    nb.grid(row=20, column=1, columnspan=48, rowspan=35, sticky="NESW")

    page1 = ttk.Frame(nb)
    nb.add(page1, text="1 - Declarações")

    TextoDasPages = Label(page1, text="Seleção anteriores", font="Arial 10 bold",
                          bg='light gray', width=131, anchor=W)
    TextoDasPages.place(x=7, y=250)

    ### itens novo trabalho 1 ###
    ### criando frame ###
    fr_rolagem3 = Frame(page1, borderwidth=1, relief="solid")
    fr_rolagem3.place(x=7, y=270, width=1055, height=155)

    ### criando o canvas ###
    canvas3 = Canvas(page1)
    canvas3.place(x=8, y=271, width=1025, height=153)

    ### criando a barra de rolagem ###
    barra_de_rolagem = ttk.Scrollbar(fr_rolagem3, orient=VERTICAL, command=canvas3.yview)
    barra_de_rolagem.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvas3.configure(yscrollcommand=barra_de_rolagem.set)
    canvas3.bind('<Configure>', lambda e: canvas3.configure(scrollregion=canvas3.bbox("all")))

    fr_rolagem3 = Frame(canvas3)

    canvas3.create_window((0, 0), window=fr_rolagem3, anchor="nw")

    page1Espaco = Label(page1, text=" ")
    page1Espaco.grid(row=1, column=1)

    page1Label = Label(page1, text="1 - Indicações do nível de concordância para as seguintes declarações:",
                       font="Arial 10 bold", foreground='blue', width=58, anchor=W)
    page1Label.grid(row=2, column=1)

    prmLabel = Label(page1, text="1.01 - Os Professores são muito bem informados sobre o assunto que ensinam.",
                     font="Arial 10", width=58, anchor=W)
    prmLabel.grid(row=3, column=1)

    sgnLabel = Label(page1, text="1.02 - Os Professores são muito bons na comunicação.",
                     font="Arial 10", width=58, anchor=W)
    sgnLabel.grid(row=4, column=1)

    trcLabel = Label(page1, text="1.03 - Os Professores são motivados e entusiastas.",
                     font="Arial 10", width=58, anchor=W)
    trcLabel.grid(row=5, column=1)

    qrtLabel = Label(page1, text="1.04 - Os métodos dos Professores ajudam a entender melhor o assunto.",
                     font="Arial 10", width=58, anchor=W)
    qrtLabel.grid(row=6, column=1)

    qntLabel = Label(page1, text="1.05 - As instalações  fornecidas satisfazem as expectativas.",
                     font="Arial 10", width=58, anchor=W)
    qntLabel.grid(row=7, column=1)

    sxtLabel = Label(page1, text="1.06 - O ambiente de ensino na sala de aula ajuda a melhorar a aprendizagem.",
                     font="Arial 10", width=58, anchor=W)
    sxtLabel.grid(row=8, column=1)

    stmLabel = Label(page1, text="1.07 - A higiene nas instalações é mantida.",
                     font="Arial 10", width=58, anchor=W)
    stmLabel.grid(row=9, column=1)

    vOpiniao1 = IntVar()

    vOpiniao2 = IntVar()

    vOpiniao3 = IntVar()

    vOpiniao4 = IntVar()

    vOpiniao5 = IntVar()

    vOpiniao6 = IntVar()

    vOpiniao7 = IntVar()

    naoSei101 = Radiobutton(page1, text="Não Sei", value=1, variable=vOpiniao1)
    naoSei101.grid(row=3, column=2)

    discordo101 = Radiobutton(page1, text="Discordo", value=2, variable=vOpiniao1)
    discordo101.grid(row=3, column=3)

    concordo101 = Radiobutton(page1, text="Concordo", value=3, variable=vOpiniao1)
    concordo101.grid(row=3, column=4)

    naoSei102 = Radiobutton(page1, text="Não Sei", value=4, variable=vOpiniao2)
    naoSei102.grid(row=4, column=2)

    discordo102 = Radiobutton(page1, text="Discordo", value=5, variable=vOpiniao2)
    discordo102.grid(row=4, column=3)

    concordo102 = Radiobutton(page1, text="Concordo", value=6, variable=vOpiniao2)
    concordo102.grid(row=4, column=4)

    naoSei103 = Radiobutton(page1, text="Não Sei", value=7, variable=vOpiniao3)
    naoSei103.grid(row=5, column=2)

    discordo103 = Radiobutton(page1, text="Discordo", value=8, variable=vOpiniao3)
    discordo103.grid(row=5, column=3)

    concordo103 = Radiobutton(page1, text="Concordo", value=9, variable=vOpiniao3)
    concordo103.grid(row=5, column=4)

    naoSei104 = Radiobutton(page1, text="Não Sei", value=10, variable=vOpiniao4)
    naoSei104.grid(row=6, column=2)

    discordo104 = Radiobutton(page1, text="Discordo", value=11, variable=vOpiniao4)
    discordo104.grid(row=6, column=3)

    concordo104 = Radiobutton(page1, text="Concordo", value=12, variable=vOpiniao4)
    concordo104.grid(row=6, column=4)

    naoSei105 = Radiobutton(page1, text="Não Sei", value=13, variable=vOpiniao5)
    naoSei105.grid(row=7, column=2)

    discordo105 = Radiobutton(page1, text="Discordo", value=14, variable=vOpiniao5)
    discordo105.grid(row=7, column=3)

    concordo105 = Radiobutton(page1, text="Concordo", value=15, variable=vOpiniao5)
    concordo105.grid(row=7, column=4)

    naoSei106 = Radiobutton(page1, text="Não Sei", value=16, variable=vOpiniao6)
    naoSei106.grid(row=8, column=2)

    discordo106 = Radiobutton(page1, text="Discordo", value=17, variable=vOpiniao6)
    discordo106.grid(row=8, column=3)

    concordo106 = Radiobutton(page1, text="Concordo", value=18, variable=vOpiniao6)
    concordo106.grid(row=8, column=4)

    naoSei107 = Radiobutton(page1, text="Não Sei", value=19, variable=vOpiniao7)
    naoSei107.grid(row=9, column=2)

    discordo107 = Radiobutton(page1, text="Discordo", value=20, variable=vOpiniao7)
    discordo107.grid(row=9, column=3)

    concordo107 = Radiobutton(page1, text="Concordo", value=21, variable=vOpiniao7)
    concordo107.grid(row=9, column=4)

    page2 = ttk.Frame(nb)
    nb.add(page2, text="2 - Avalie o Professor")

    ### page2 itens ###
    ### criando o frame da barra de rolagem ###
    fr_rolagem1 = Frame(page2, borderwidth=1, relief="solid")
    fr_rolagem1.place(x=10, y=30, width=567, height=400)

    ### criando o canvas ###
    canvas1 = Canvas(page2)
    canvas1.place(x=11, y=31, width=542, height=368)

    ### criando a barra de rolagem ###
    barra_de_rolagem = ttk.Scrollbar(fr_rolagem1, orient=VERTICAL, command=canvas1.yview)
    barra_de_rolagem.pack(side=RIGHT, fill=Y)

    barra_de_rolagem3CPTurma = ttk.Scrollbar(fr_rolagem1, orient=HORIZONTAL, command=canvas1.xview)
    barra_de_rolagem3CPTurma.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvas1.configure(yscrollcommand=barra_de_rolagem.set)
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion= canvas1.bbox("all")))

    canvas1.configure(xscrollcommand=barra_de_rolagem3CPTurma.set)
    canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))

    fr_rolagem2 = Frame(canvas1)

    canvas1.create_window((0,0), window=fr_rolagem2, anchor="nw")

    ### criando a pergunta ###
    pergundaPage2 = Label(page2, text="2 - Avaliação ao corpo docente em como se classificam nos seguintes ponto:", font="Arial 10 bold", width=58, anchor=W, foreground='blue')
    pergundaPage2.place(x=5, y=1)

    ### criando os chackButtons ###
    cb201 = Checkbutton(fr_rolagem2, text="2.01 - Falta prepacação de classes", width=200, anchor=W)
    cb201.grid(row=1, column=1)

    cb202 = Checkbutton(fr_rolagem2, text="2.02 - Falta clareza na explicação do assunto", width=200, anchor=W)
    cb202.grid(row=2, column=1)

    cb203 = Checkbutton(fr_rolagem2, text="2.03 - Falta conhecimento do material disponível", width=200, anchor=W)
    cb203.grid(row=3, column=1)

    cb204 = Checkbutton(fr_rolagem2, text="2.04 - Falta de inovação nos métodos de ensino", width=200, anchor=W)
    cb204.grid(row=4, column=1)

    cb205 = Checkbutton(fr_rolagem2, text="2.05 - Falta entusiasmo pelo ensino", width=200, anchor=W)
    cb205.grid(row=5, column=1)

    cb206 = Checkbutton(fr_rolagem2, text="2.06 - Não acessível para ajuda", width=200, anchor=W)
    cb206.grid(row=6, column=1)

    cb207 = Checkbutton(fr_rolagem2, text="2.07 - Falta agilidade nos atendimentos", width=200, anchor=W)
    cb207.grid(row=7, column=1)

    cb208 = Checkbutton(fr_rolagem2, text="2.08 - Falta cordialidade dos profissionais", width=200, anchor=W)
    cb208.grid(row=8, column=1)

    cb209 = Checkbutton(fr_rolagem2, text="2.09 - Falta esclarecimento de dúvidas", width=200, anchor=W)
    cb209.grid(row=9, column=1)

    cb210 = Checkbutton(fr_rolagem2, text="2.10 - Falta apoio na solução dos problemas", width=200, anchor=W)
    cb210.grid(row=10, column=1)

    cb211 = Checkbutton(fr_rolagem2, text="2.11 - A maioria em nossa turma, tem muita dificuldade de entrosamento", width=200, anchor=W)
    cb211.grid(row=11, column=1)

    cb212 = Checkbutton(fr_rolagem2, text="2.12 - Falamos alto demais", width=200, anchor=W)
    cb212.grid(row=12, column=1)

    cb213 = Checkbutton(fr_rolagem2, text="2.13 - Não esperamos nossa vez de falar", width=200, anchor=W)
    cb213.grid(row=13, column=1)

    cb214 = Checkbutton(fr_rolagem2, text="2.14 - A maioria de nós prefere brincar em grupo", width=200, anchor=W)
    cb214.grid(row=14, column=1)

    cb215 = Checkbutton(fr_rolagem2, text="2.15 - Alguns de nós apresentam dificuldades em desenvolver atividade sozinho", width=200, anchor=W)
    cb215.grid(row=15, column=1)

    cb216 = Checkbutton(fr_rolagem2, text="2.16 - Nas atividades propostas em sala de aula, somos bastante participativos", width=200, anchor=W)
    cb216.grid(row=16, column=1)

    cb217 = Checkbutton(fr_rolagem2, text="2.17 - Realizamos o que é proposto com atenção e capricho", width=200, anchor=W)
    cb217.grid(row=17, column=1)

    cb218 = Checkbutton(fr_rolagem2, text="2.18 - Realizamos o que é proposto com atenção e capricho", width=200, anchor=W)
    cb218.grid(row=18, column=1)

    cb219 = Checkbutton(fr_rolagem2, text="2.19 - Gostamos de participar das atividades pedagógicas e recreativas como, recontar histórias, roda de conversas ou até mesmo discutir um assunto, dramatização, dançar, cantar", width=200, anchor=W)
    cb219.grid(row=19, column=1)

    cb220 = Checkbutton(fr_rolagem2, text="2.20 - Nossa turma é bastante ativa e enérgica. Com exceção do(a) aluno(a) aqui citado(a), que tem sido incentivado a interagir com o grupo", width=200, anchor=W)
    cb220.grid(row=20, column=1)

    cb221 = Checkbutton(fr_rolagem2, text="2.21 - Temos interesse por jogos como jogo de damas, dominós, bingos de sons e letras, caça rimas e caça palavras, dado sonoro enfim jogos variados", width=200, anchor=W)
    cb221.grid(row=21, column=1)

    cb222 = Checkbutton(fr_rolagem2, text="2.22 - A maioria de nossa turma compreende e obedece as normas estabelecidas, e exigimos dos colegas o cumprimento das mesmas", width=200, anchor=W)
    cb222.grid(row=22, column=1)

    cb223 = Checkbutton(fr_rolagem2, text="2.23 - Há aqueles que por momentos desrespeitam normas", width=200, anchor=W)
    cb223.grid(row=23, column=1)

    cb224 = Checkbutton(fr_rolagem2, text="2.24 - Nossa turma conversa muito, uns com tons altos e outros baixos, expressando nossos sentimentos, desejos e insatisfaçõe .\nMas quando o professor se põe em silêncio de pé olhando bem para nós, logo observamos e moderamos nossa voz", width=200, anchor=W)
    cb224.grid(row=24, column=1)

    cb225 = Checkbutton(fr_rolagem2, text="2.25 - A maioria das famílias dos alunos de nossa turma participam ativamente", width=200, anchor=W)
    cb225.grid(row=25, column=1)

    cb226 = Checkbutton(fr_rolagem2, text="2.26 - Nossas famílias deixam a desejar nas reuniões realizadas pela escola no decorrer do ano", width=200, anchor=W)
    cb226.grid(row=26, column=1)

    cb227 = Checkbutton(fr_rolagem2, text="2.27 - Alguns de nossos familiares não costumam buscar informações e esclarecer dúvidas com professores sempre que necessário", width=200, anchor=W)
    cb227.grid(row=27, column=1)

    cb228 = Checkbutton(fr_rolagem2, text="2.28 - No decorrer do ano nossos laços afetivos foram fortalecidos entre alguns de nós", width=200, anchor=W)
    cb228.grid(row=28, column=1)

    cb229 = Checkbutton(fr_rolagem2, text="2.29 - A relação entre os professores e nossa turma é muito boa", width=200, anchor=W)
    cb229.grid(row=29, column=1)

    cb230 = Checkbutton(fr_rolagem2, text="2.30 - Em questão da aprendizagem, apresentamos um bom rendimento no decorrer do ano, com exceções de (aluno(s) aqui citado(s)), que mostram alguma dificuldade", width=200, anchor=W)
    cb230.grid(row=30, column=1)

    cb231 = Checkbutton(fr_rolagem2, text="2.31 - É visível o nosso interesse, onde demonstramos CRIATIVIDADE E EMPENHO", width=200, anchor=W)
    cb231.grid(row=31, column=1)

    ### page2 itens ###
    ### criando o frame da barra de rolagem ###
    fr_rolagemSub = Frame(page2, borderwidth=1, relief="solid")
    fr_rolagemSub.place(x=600, y=30, width=467, height=400)

    ### criando o canvas ###
    canvas3 = Canvas(page2)
    canvas3.place(x=601, y=31, width=442, height=368)

    ### criando a barra de rolagem ###
    barra_de_rolagemCPTurma = ttk.Scrollbar(fr_rolagemSub, orient=VERTICAL, command=canvas3.yview)
    barra_de_rolagemCPTurma.pack(side=RIGHT, fill=Y)

    barra_de_rolagem2CPTurma = ttk.Scrollbar(fr_rolagemSub, orient=HORIZONTAL, command=canvas3.xview)
    barra_de_rolagem2CPTurma.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvas3.configure(yscrollcommand=barra_de_rolagemCPTurma.set)
    canvas3.bind('<Configure>', lambda e: canvas3.configure(scrollregion=canvas3.bbox("all")))

    canvas3.configure(xscrollcommand=barra_de_rolagem2CPTurma.set)
    canvas3.bind('<Configure>', lambda e: canvas3.configure(scrollregion=canvas3.bbox("all")))

    fr_rolagemSub = Frame(canvas3)

    canvas3.create_window((0, 0), window=fr_rolagemSub, anchor="nw")

    ### criando a pergunta ###
    pergundaPage22 = Label(page2, text="Á exceção dos Professores:",
                          font="Arial 10 bold", width=58, anchor=W, foreground='blue')
    pergundaPage22.place(x=600, y=1)
#########################################################################################

    page3 = ttk.Frame(nb)
    nb.add(page3, text="3 - Perguntas Abertas")

### coisas do page 3 ###
    texto_page3 = Label(page3, text="3 - Perguntas abertas para uma pesquisa escolar:", font="Arial 10 bold", width=100, anchor=W, foreground='blue')
    texto_page3.place(x=5, y=1)

    ### txt1 ###
    texto1_page3 = Label(page3, text="3.01 - Indiquem três coisas que mais gostam nas aulas e por quê?", width=100, anchor=W)
    texto1_page3.place(x=50, y=50)

    resposta_page3 = Label(page3, text="Resposta:", width=100, foreground='blue', anchor=W)
    resposta_page3.place(x=53, y=90)

    respostaText1 = Text(page3, width=90, height=2)
    respostaText1.place(x=110, y=75)

    ### txt2 ###
    texto2_page3 = Label(page3, text="3.02 - Indiquem três coisas que não gostam nas aulas e por quê?", width=100, anchor=W)
    texto2_page3.place(x=50, y=120)

    resposta2_page3 = Label(page3, text="Resposta:", width=100, foreground='blue', anchor=W)
    resposta2_page3.place(x=53, y=160)

    respostaText2 = Text(page3, width=90, height=2)
    respostaText2.place(x=110, y=145)

    ### txt3 ###
    texto3_page3 = Label(page3, text="3.03 - O que gostariam de mudar ou modificar nesta classe?", width=100, anchor=W)
    texto3_page3.place(x=50, y=190)

    resposta3_page3 = Label(page3, text="Resposta:", width=100, foreground='blue', anchor=W)
    resposta3_page3.place(x=53, y=230)

    respostaText3 = Text(page3, width=90, height=2)
    respostaText3.place(x=110, y=215)

    ### txt4 ###
    texto4_page3 = Label(page3, text="3.04 - Indique três pontos que tornariam o ensino dos instrutores ainda melhor?", width=100, anchor=W)
    texto4_page3.place(x=50, y=260)

    resposta4_page3 = Label(page3, text="Resposta:", width=100, foreground='blue', anchor=W)
    resposta4_page3.place(x=53, y=300)

    respostaText4 = Text(page3, width=90, height=2)
    respostaText4.place(x=110, y=285)

    ### txt5 ###
    texto5_page3 = Label(page3, text="3.05 - O que de mais importante a turma apreneu com as aulas?", width=100, anchor=W)
    texto5_page3.place(x=50, y=330)

    resposta5_page3 = Label(page3, text="Resposta:", width=100, foreground='blue', anchor=W)
    resposta5_page3.place(x=53, y=370)

    respostaText5 = Text(page3, width=90, height=2)
    respostaText5.place(x=110, y=355)

    ### txt6 ###
    texto6_page3 = Label(page3, text="3.06 - A turma tem algum comentário ou sugestão para ajudar a melhorar as aulas?", width=100,
                         anchor=W)
    texto6_page3.place(x=50, y=400)

    resposta6_page3 = Label(page3, text="Resposta:", width=100, foreground='blue', anchor=W)
    resposta6_page3.place(x=53, y=440)

    respostaText6 = Text(page3, width=90, height=2)
    respostaText6.place(x=110, y=425)



### page4 ###
    page4 = ttk.Frame(nb)
    nb.add(page4, text="4 - Perguntas Abertas")
    ### itens page4 ###
    texto1_page4 = Label(page4, text=' ',)
    texto1_page4.grid(row=1, column=1)

    texto1_page4 = Label(page4, text='4 - Considerando a experiência da classe, quais são as chances de recomendá-la aos amigos e familiares?',
                         font="Arial 10 bold", width=90, anchor=W, foreground='blue')
    texto1_page4.grid(row=2, column=1)

    ### perguntas page4 ###
    ### txt1 ###
    texto2_page4 = Label(page4, text='4.01 - Quão satisfeitos estão com o formato geral da aula?', width=90, anchor=W)
    texto2_page4.grid(row=3, column=1)

    ### chackbox 4.01 ###
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()

    botao1 = Radiobutton(page4, text="1", font="Arial 10 bold", bg='light gray', value=1, variable=var1)
    botao1.grid(row=3, column=2)

    botao2 = Radiobutton(page4, text="2", font="Arial 10 bold", value=2, variable=var1)
    botao2.grid(row=3, column=3)

    botao3 = Radiobutton(page4, text="3", font="Arial 10 bold", bg='light gray', value=3, variable=var1)
    botao3.grid(row=3, column=4)

    botao4 = Radiobutton(page4, text="4", font="Arial 10 bold", value=4, variable=var1)
    botao4.grid(row=3, column=5)

    botao5 = Radiobutton(page4, text="5", font="Arial 10 bold", bg='light gray', value=5, variable=var1)
    botao5.grid(row=3, column=6)

    ### txt3 ###
    texto3_page4 = Label(page4, text='4.02 - Como avaliariam o instrutor pelo conhecimento que ele tem sobre o assunto que ensina?',
                         width=90, anchor=W)
    texto3_page4.grid(row=4, column=1)

    ### chackbox 4.02 ###
    botao1_1 = Radiobutton(page4, text="1", font="Arial 10 bold", value=1, variable=var2)
    botao1_1.grid(row=4, column=2)

    botao2_1 = Radiobutton(page4, text="2", font="Arial 10 bold", bg='light gray', value=2, variable=var2)
    botao2_1.grid(row=4, column=3)

    botao3_1 = Radiobutton(page4, text="3", font="Arial 10 bold", value=3, variable=var2)
    botao3_1.grid(row=4, column=4)

    botao4_1 = Radiobutton(page4, text="4", font="Arial 10 bold", bg='light gray', value=4, variable=var2)
    botao4_1.grid(row=4, column=5)

    botao5_1 = Radiobutton(page4, text="5", font="Arial 10 bold", value=5, variable=var2)
    botao5_1.grid(row=4, column=6)

    ### txt4 ##
    texto4_page4 = Label(page4, text='4.03 - Quão difícil é o programa de aula?', width=90, anchor=W)
    texto4_page4.grid(row=5, column=1)

    ### chackbox 4.03 ###
    botao1_2 = Radiobutton(page4, text="1", font="Arial 10 bold", bg='light gray', value=1, variable=var3)
    botao1_2.grid(row=5, column=2)

    botao2_2 = Radiobutton(page4, text="2", font="Arial 10 bold", value=2, variable=var3)
    botao2_2.grid(row=5, column=3)

    botao3_2 = Radiobutton(page4, text="3", font="Arial 10 bold", bg='light gray', value=3, variable=var3)
    botao3_2.grid(row=5, column=4)

    botao4_2 = Radiobutton(page4, text="4", font="Arial 10 bold", value=4, variable=var3)
    botao4_2.grid(row=5, column=5)

    botao5_2 = Radiobutton(page4, text="5", font="Arial 10 bold", bg='light gray', value=5, variable=var3)
    botao5_2.grid(row=5, column=6)

    ### txt5 ##
    texto5_page4 = Label(page4, text='4.04 - Com que frequência a turma foi avaliada no decorrer das aulas?', width=90, anchor=W)
    texto5_page4.grid(row=6, column=1)

    ### chackbox 4.04 ###
    botao1_3 = Radiobutton(page4, text="1", font="Arial 10 bold", value=1, variable=var4)
    botao1_3.grid(row=6, column=2)

    botao2_3 = Radiobutton(page4, text="2", font="Arial 10 bold", bg='light gray', value=2, variable=var4)
    botao2_3.grid(row=6, column=3)

    botao3_3 = Radiobutton(page4, text="3", font="Arial 10 bold", value=3, variable=var4)
    botao3_3.grid(row=6, column=4)

    botao4_3 = Radiobutton(page4, text="4", font="Arial 10 bold", bg='light gray', value=4, variable=var4)
    botao4_3.grid(row=6, column=5)

    botao5_3 = Radiobutton(page4, text="5", font="Arial 10 bold", value=5, variable=var4)
    botao5_3.grid(row=6, column=6)

    ### txt6 ##
    texto6_page4 = Label(page4, text='4.05 - Quão benéfica é a classe?', width=90, anchor=W)
    texto6_page4.grid(row=7, column=1)

    ### chackbox 4.05 ###
    botao1_4 = Radiobutton(page4, text="1", font="Arial 10 bold", bg='light gray', value=1, variable=var5)
    botao1_4.grid(row=7, column=2)

    botao2_4 = Radiobutton(page4, text="2", font="Arial 10 bold", value=2, variable=var5)
    botao2_4.grid(row=7, column=3)

    botao3_4 = Radiobutton(page4, text="3", font="Arial 10 bold", bg='light gray', value=3, variable=var5)
    botao3_4.grid(row=7, column=4)

    botao4_4 = Radiobutton(page4, text="4", font="Arial 10 bold", value=4, variable=var5)
    botao4_4.grid(row=7, column=5)

    botao5_4 = Radiobutton(page4, text="5", font="Arial 10 bold", bg='light gray', value=5, variable=var5)
    botao5_4.grid(row=7, column=6)

    ### txt7 ##
    texto7_page4 = Label(page4, text='4.06 - Em que nível acham que a escola forneceu a quantidade certa de teoria e prática?', width=90, anchor=W)
    texto7_page4.grid(row=8, column=1)

    ### chackbox 4.06 ###
    botao1_5 = Radiobutton(page4, text="1", font="Arial 10 bold", value=1, variable=var6)
    botao1_5.grid(row=8, column=2)

    botao2_5 = Radiobutton(page4, text="2", font="Arial 10 bold", bg='light gray', value=2, variable=var6)
    botao2_5.grid(row=8, column=3)

    botao3_5 = Radiobutton(page4, text="3", font="Arial 10 bold", value=3, variable=var6)
    botao3_5.grid(row=8, column=4)

    botao4_5 = Radiobutton(page4, text="4", font="Arial 10 bold", bg='light gray', value=4, variable=var6)
    botao4_5.grid(row=8, column=5)

    botao5_5 = Radiobutton(page4, text="5", font="Arial 10 bold", value=5, variable=var6)
    botao5_5.grid(row=8, column=6)

    ### txt8 ##
    texto8_page4 = Label(page4, text='4.07 - Em que nível acham que as lições da aula serão úteis para o crescimento de carreira dos alunos?', width=90, anchor=W)
    texto8_page4.grid(row=9, column=1)

    ### chackbox 4.07 ###
    botao1_6 = Radiobutton(page4, text="1", font="Arial 10 bold", bg='light gray', value=1, variable=var7)
    botao1_6.grid(row=9, column=2)

    botao2_6 = Radiobutton(page4, text="2", font="Arial 10 bold", value=2, variable=var7)
    botao2_6.grid(row=9, column=3)

    botao3_6 = Radiobutton(page4, text="3", font="Arial 10 bold", bg='light gray', value=3, variable=var7)
    botao3_6.grid(row=9, column=4)

    botao4_6 = Radiobutton(page4, text="4", font="Arial 10 bold", value=4, variable=var7)
    botao4_6.grid(row=9, column=5)

    botao5_6 = Radiobutton(page4, text="5", font="Arial 10 bold", bg='light gray', value=5, variable=var7)
    botao5_6.grid(row=9, column=6)

    ### txt9 ##
    texto9_page4 = Label(page4, text='4.08 - Indiquem o quanto estão satisfeitos com a média geral da turma!', width=90, anchor=W)
    texto9_page4.grid(row=10, column=1)

    ### chackbox 4.08 ###
    botao1_7 = Radiobutton(page4, text="1", font="Arial 10 bold", value=1, variable=var8)
    botao1_7.grid(row=10, column=2)

    botao2_7 = Radiobutton(page4, text="2", font="Arial 10 bold", bg='light gray', value=2, variable=var8)
    botao2_7.grid(row=10, column=3)

    botao3_7 = Radiobutton(page4, text="3", font="Arial 10 bold", value=3, variable=var8)
    botao3_7.grid(row=10, column=4)

    botao4_7 = Radiobutton(page4, text="4", font="Arial 10 bold", bg='light gray', value=4, variable=var8)
    botao4_7.grid(row=10, column=5)

    botao5_7 = Radiobutton(page4, text="5", font="Arial 10 bold", value=5, variable=var8)
    botao5_7.grid(row=10, column=6)

    ### txt10 ##
    texto10_page4 = Label(page4, text='4.09 - Em que nível acham que a relação e qualidade e preço da aula estão adequados?', width=90, anchor=W)
    texto10_page4.grid(row=11, column=1)

    ### chackbox 4.09 ###
    botao1_8 = Radiobutton(page4, text="1", font="Arial 10 bold", bg='light gray', value=1, variable=var9)
    botao1_8.grid(row=11, column=2)

    botao2_8 = Radiobutton(page4, text="2", font="Arial 10 bold", value=2, variable=var9)
    botao2_8.grid(row=11, column=3)

    botao3_8 = Radiobutton(page4, text="3", font="Arial 10 bold", bg='light gray', value=3, variable=var9)
    botao3_8.grid(row=11, column=4)

    botao4_8 = Radiobutton(page4, text="4", font="Arial 10 bold", value=4, variable=var9)
    botao4_8.grid(row=11, column=5)

    botao5_8 = Radiobutton(page4, text="5", font="Arial 10 bold", bg='light gray', value=5, variable=var9)
    botao5_8.grid(row=11, column=6)

    TextoDasPages2=Label(page4, text="Seleção anteriores", font="Arial 10 bold", bg='light gray', width=131, anchor=W)
    TextoDasPages2.place(x=7, y=280)

    ### criando frame ###
    fr_rolagemSub4 = Frame(page4, borderwidth=1, relief="solid")
    fr_rolagemSub4.place(x=7, y=300, width=1055, height=155)

    ### criando o canvas ###
    canvasSub4 = Canvas(page4)
    canvasSub4.place(x=8, y=301, width=1025, height=153)

    ### criando a barra de rolagem ###
    barra_de_rolagemSub4 = ttk.Scrollbar(fr_rolagemSub4, orient=VERTICAL, command=canvasSub4.yview)
    barra_de_rolagemSub4.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasSub4.configure(yscrollcommand=barra_de_rolagemSub4.set)
    canvasSub4.bind('<Configure>', lambda e: canvasSub4.configure(scrollregion=canvasSub4.bbox("all")))

    fr_rolagemSub4 = Frame(canvasSub4)

    canvasSub4.create_window((0, 0), window=fr_rolagemSub4, anchor="nw")

### page5 ###
    page5 = ttk.Frame(nb)
    nb.add(page5, text="Auto Avaliação da Turma")
### itens page5 ###
    ### criando o frame da barra de rolagem ###
    fr_rolagem4 = Frame(page5, borderwidth=1, relief="solid")
    fr_rolagem4.place(x=10, y=50, width=1067, height=400)

    ### criando o canvas ###
    canvas2 = Canvas(page5)
    canvas2.place(x=11, y=51, width=1032, height=398)

    ### criando a barra de rolagem ###
    barra_de_rolagem = ttk.Scrollbar(fr_rolagem4, orient=VERTICAL, command=canvas2.yview)
    barra_de_rolagem.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvas2.configure(yscrollcommand=barra_de_rolagem.set)
    canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))

    fr_rolagem5 = Frame(canvas2)

    canvas2.create_window((0, 0), window=fr_rolagem5, anchor="nw")

    ### criando a pergunta ###
    pergunta1Page5 = Label(page5, text="Questionário De Conselho Parcitipativo Classe x Escola",
                          font="Arial 10 bold", width=58, anchor=W, foreground='blue')
    pergunta1Page5.place(x=5, y=1)

    pergunta2Page5 = Label(page5, text="5 - Considerando a vivência em classe, selecione as características que representam melhor a turma",
                          font="Arial 10 bold", bg='yellow', width=133, anchor=W)
    pergunta2Page5.place(x=10, y=27)

    ### criando os chackButtons ###
    cb501 = Checkbutton(fr_rolagem5, text="5.01 - Somos uma turma bem entrosada.", width=150, anchor=W)
    cb501.grid(row=1, column=1)

    cb502 = Checkbutton(fr_rolagem5, text="5.02 - Temos um bom relacionamento uns com os outros.", width=150, anchor=W)
    cb502.grid(row=2, column=1)

    cb503 = Checkbutton(fr_rolagem5, text="5.03 - Temos alguns em nossa turma um pouco agitados.", width=150, anchor=W)
    cb503.grid(row=3, column=1)

    cb504 = Checkbutton(fr_rolagem5, text="5.04 - Temos facilidade em organizar a sala de aula.", width=150, anchor=W)
    cb504.grid(row=4, column=1)

    cb505 = Checkbutton(fr_rolagem5, text="5.05 - As vezes alguns de nós brigamos.", width=150, anchor=W)
    cb505.grid(row=5, column=1)

    cb506 = Checkbutton(fr_rolagem5, text="5.06 - Somos fáceis de perdoar.", width=150, anchor=W)
    cb506.grid(row=6, column=1)

    cb507 = Checkbutton(fr_rolagem5, text="5.07 - Ocorrem alguns casos de agressividade verbal na nossa turma.", width=150, anchor=W)
    cb507.grid(row=7, column=1)

    cb508 = Checkbutton(fr_rolagem5, text="5.08 - A adaptação da nossa turma foi boa.", width=150, anchor=W)
    cb508.grid(row=8, column=1)

    cb509 = Checkbutton(fr_rolagem5, text="5.09 - Alguns de nós temos dificuldades em ser repreendidos.", width=150, anchor=W)
    cb509.grid(row=9, column=1)

    cb510 = Checkbutton(fr_rolagem5, text="5.10 - Desobedecemos normas de boa convivência em grupo, principalmente nos momentos de desenvolver trabalhos em grupos.", width=150, anchor=W)
    cb510.grid(row=10, column=1)

    cb511 = Checkbutton(fr_rolagem5, text="5.11 - A maioria em nossa turma, tem muita dificuldade de entrosamento.", width=150, anchor=W)
    cb511.grid(row=11, column=1)

    cb512 = Checkbutton(fr_rolagem5, text="5.12 - Falamos alto demais.", width=150, anchor=W)
    cb512.grid(row=12, column=1)

    cb513 = Checkbutton(fr_rolagem5, text="5.13 - Não esperamos nossa vez de falar.", width=150, anchor=W)
    cb513.grid(row=11, column=1)

    cb514 = Checkbutton(fr_rolagem5, text="5.14 - A maioria de nós prefere brincar em grupo.", width=150, anchor=W)
    cb514.grid(row=14, column=1)

    cb515 = Checkbutton(fr_rolagem5, text="5.15 - Alguns de nós apresentam dificuldades em desenvolver atividades sozinho.", width=150, anchor=W)
    cb515.grid(row=15, column=1)

    cb516 = Checkbutton(fr_rolagem5, text="5.16 - Nas atividades propostas em sala de aula, somos bastante participativos.", width=150, anchor=W)
    cb516.grid(row=16, column=1)

    cb517 = Checkbutton(fr_rolagem5, text="5.17 - Realizamos o que é proposto com atenção e capricho.", width=150, anchor=W)
    cb517.grid(row=17, column=1)

    cb518 = Checkbutton(fr_rolagem5, text="5.18 - Somos produtivos, exeto aluno(s) aqui citado(s), que demonstra(m) desinteresse, desânimo em desenvolver as atividades roineiras e apresenta não ter acompanhamento famíliar.", width=150, anchor=W)
    cb518.grid(row=18, column=1)

    cb519 = Checkbutton(fr_rolagem5, text="5.19 - Gostamos de participar das atividades pedagógicas e recreativas como, recontar histórias, roda de conversas ou até mesmo discutir um assunto, dramatização, dançar, cantar.", width=150, anchor=W)
    cb519.grid(row=19, column=1)

    cb520 = Checkbutton(fr_rolagem5, text="5.20 - Nossa turma é bastante ativa e enérgica. Com exceção do(a) aluno(a) aqui citado(a), que tem sido incentivado a interagir com o grupo.", width=150, anchor=W)
    cb520.grid(row=20, column=1)

    cb521 = Checkbutton(fr_rolagem5, text="5.21 - .", width=150, anchor=W)
    cb521.grid(row=21, column=1)

    cb522 = Checkbutton(fr_rolagem5, text="5.22 - .", width=150, anchor=W)
    cb522.grid(row=22, column=1)

    cb523 = Checkbutton(fr_rolagem5, text="5.23 - .", width=150, anchor=W)
    cb523.grid(row=23, column=1)

    cb524 = Checkbutton(fr_rolagem5, text="5.24 - .", width=150, anchor=W)
    cb524.grid(row=24, column=1)

    cb525 = Checkbutton(fr_rolagem5, text="5.25 - .", width=150, anchor=W)
    cb525.grid(row=25, column=1)

    cb526 = Checkbutton(fr_rolagem5, text="5.26 - .", width=150, anchor=W)
    cb526.grid(row=26, column=1)

    cb527 = Checkbutton(fr_rolagem5, text="5.27 - .", width=150, anchor=W)
    cb527.grid(row=27, column=1)

    cb528 = Checkbutton(fr_rolagem5, text="5.28 - .", width=150, anchor=W)
    cb528.grid(row=28, column=1)

    cb529 = Checkbutton(fr_rolagem5, text="5.29 - .", width=150, anchor=W)
    cb529.grid(row=29, column=1)

    cb530 = Checkbutton(fr_rolagem5, text="5.30 - .", width=150, anchor=W)
    cb530.grid(row=30, column=1)

    cb531 = Checkbutton(fr_rolagem5, text="5.22 - .", width=150, anchor=W)
    cb531.grid(row=22, column=1)

    cb532 = Checkbutton(fr_rolagem5, text="5.22 - .", width=150, anchor=W)
    cb532.grid(row=22, column=1)

    cb533 = Checkbutton(fr_rolagem5, text="5.33 - .", width=150, anchor=W)
    cb533.grid(row=33, column=1)

    cb534 = Checkbutton(fr_rolagem5, text="5.34 - .", width=150, anchor=W)
    cb534.grid(row=34, column=1)

    cb535 = Checkbutton(fr_rolagem5, text="5.35 - .", width=150, anchor=W)
    cb535.grid(row=35, column=1)

### page6 ###
    page6 = ttk.Frame(nb)
    nb.add(page6, text="Considerações Finais")

    CosideracoesLbl = Label(page6, text="Considerações Finais", font="Arial 9 bold", foreground='blue')
    CosideracoesLbl.place(x=10, y=10)

    ConsideracoesFinaisTextCPTurma = Text(page6, font="Arial 9", width=150, height=19)
    ConsideracoesFinaisTextCPTurma.place(x=10, y=30)
######################################

def abrirCD():
    novoTrabalhoCD = Toplevel()
    novoTrabalhoCD.geometry('1090x620+260+70')
    novoTrabalhoCD.resizable(False,False)
    novoTrabalhoCD.title('Conselho Diciplinar')
    novoTrabalhoCD.configure(bg='light gray')
    novoTrabalhoCD.transient(trabalho)
    novoTrabalhoCD.focus_force()
    novoTrabalhoCD.grab_set()

    BimestreCD = tkinter.StringVar()
    BimestreCDcbbx = ttk.Combobox(novoTrabalhoCD, width=20, height=1, textvariable=BimestreCD)
    BimestreCDcbbx.place(x=350, y=10)

    PeriodoCD1Text = Text(novoTrabalhoCD, width=10, height=1)
    PeriodoCD1Text.place(x=570, y=10)

    PeriodoCD2Text = Text(novoTrabalhoCD, width=10, height=1)
    PeriodoCD2Text.place(x=665, y=10)

    IdCDText = Text(novoTrabalhoCD, width=2, height=1)
    IdCDText.place(x=10, y=56)

    IdCDLabel = Label(novoTrabalhoCD, text='ID', bg='Light Grey', font="Arial 9 bold")
    IdCDLabel.place(x=10, y=35)

    RaCDText = Text(novoTrabalhoCD, width=4, height=1)
    RaCDText.place(x=35, y=56)

    RaCDLabel = Label(novoTrabalhoCD, text='RA', bg='Light Grey')
    RaCDLabel.place(x=35, y=35)

    AlunoCD = tkinter.StringVar()
    AlunoCDcbbx = ttk.Combobox(novoTrabalhoCD, width=30, height=1, textvariable=AlunoCD)
    AlunoCDcbbx.place(x=76, y=56)

    AlunoCDLabel = Label(novoTrabalhoCD, text='Alunos', bg='Light Grey')
    AlunoCDLabel.place(x=76, y=35)

    TurmaCD = tkinter.StringVar()
    TurmaCDcbbx = ttk.Combobox(novoTrabalhoCD, width=6, height=1, textvariable=TurmaCD)
    TurmaCDcbbx.place(x=284, y=56)

    TurmaCDLabel = Label(novoTrabalhoCD, text='Turma', bg='Light Grey')
    TurmaCDLabel.place(x=284, y=35)

    SerieCDText = Text(novoTrabalhoCD, width=28, height=1)
    SerieCDText.place(x=350, y=56)

    SerieCDLabel = Label(novoTrabalhoCD, text='Série', bg='Light Grey')
    SerieCDLabel.place(x=350, y=35)

    ### 2 ###

    UnidadeCDText = Text(novoTrabalhoCD, width=26, height=1)
    UnidadeCDText.place(x=10, y=98)

    UnidadeCDLabel = Label(novoTrabalhoCD, text='Unidade', bg='Light Grey')
    UnidadeCDLabel.place(x=10, y=77)

    CidadeCD = tkinter.StringVar()
    CidadeCDcbbx = ttk.Combobox(novoTrabalhoCD, width=10, height=1, textvariable=CidadeCD)
    CidadeCDcbbx.place(x=228, y=98)

    CidadeCDLabel = Label(novoTrabalhoCD, text='Cidade', bg='Light Grey')
    CidadeCDLabel.place(x=228, y=77)

    EstadoCD = tkinter.StringVar()
    EstadoCDcbbx = ttk.Combobox(novoTrabalhoCD, width=16, height=1, textvariable=EstadoCD)
    EstadoCDcbbx.place(x=315, y=98)

    EstadoCDLabel = Label(novoTrabalhoCD, text='Estado', bg='Light Grey')
    EstadoCDLabel.place(x=315, y=77)

    OrdemCD = tkinter.StringVar()
    OrdemCDcbbx = ttk.Combobox(novoTrabalhoCD, width=19, height=1, textvariable=OrdemCD)
    OrdemCDcbbx.place(x=438, y=98)

    OrdemCDLabel = Label(novoTrabalhoCD, text='Ordem', bg='Light Grey')
    OrdemCDLabel.place(x=438, y=77)

    BimestreCDLabel = Label(novoTrabalhoCD, text="Bimestre:", bg='light grey')
    BimestreCDLabel.place(x=290, y=10)

    PeriodoCD1Label = Label(novoTrabalhoCD, text="Período:", bg='light grey')
    PeriodoCD1Label.place(x=520, y=10)

    PeriodoCD2Label = Label(novoTrabalhoCD, text="à", bg='light grey')
    PeriodoCD2Label.place(x=655, y=10)

    LocalDataFrameCDLabel = Label(novoTrabalhoCD, width=40, height=2)
    LocalDataFrameCDLabel.place(x=785, y=10)

    LocalDataCDLabel = Label(novoTrabalhoCD, text="Local e Data")
    LocalDataCDLabel.place(x=795, y=10)

    DiaMesAnoHoraCDLabel = Label(novoTrabalhoCD, width=69, height=4)
    DiaMesAnoHoraCDLabel.place(x=585, y=55)

    DiaCDLabel = Label(novoTrabalhoCD, text="Dia:")
    DiaCDLabel.place(x=605, y=75)

    DiaCDText = Text(novoTrabalhoCD, width=3, height=1)
    DiaCDText.place(x=630, y=75)

    MesCDLabel = Label(novoTrabalhoCD, text="Mês:")
    MesCDLabel.place(x=660, y=75)

    MesCDText = Text(novoTrabalhoCD, width=15, height=1)
    MesCDText.place(x=690, y=75)

    AnoCDLabel = Label(novoTrabalhoCD, text="Ano:")
    AnoCDLabel.place(x=815, y=75)

    AnoCDText = Text(novoTrabalhoCD, width=5, height=1)
    AnoCDText.place(x=845, y=75)

    HoraCDLabel = Label(novoTrabalhoCD, text="Hora:")
    HoraCDLabel.place(x=950, y=75)

    HoraCDText = Text(novoTrabalhoCD, width=2, height=1)
    HoraCDText.place(x=985, y=75)

    MinutoCDText = Text(novoTrabalhoCD, width=2, height=1)
    MinutoCDText.place(x=1005, y=75)

    Foto_Aluno_CD = Label(novoTrabalhoCD, image=imgFoto_Aluno)
    Foto_Aluno_CD.place(x=975, y=220)

    Foto_Pilar_CD = Label(novoTrabalhoCD, image=Foto_Pilar_CdFoto, bg='light grey')
    Foto_Pilar_CD.place(x=960, y=330)



    ### itens novo trabalho 1 ###
    ### criando frame ###
    fr_rolagemCD = Frame(novoTrabalhoCD, borderwidth=1, relief="solid")
    fr_rolagemCD.place(x=7, y=130, width=1070, height=58)

    ### criando o canvas ###
    canvasCD = Canvas(novoTrabalhoCD)
    canvasCD.place(x=8, y=131, width=1050, height=56)

    ### criando a barra de rolagem ###
    barra_de_rolagemCD = ttk.Scrollbar(fr_rolagemCD, orient=VERTICAL, command=canvasCD.yview)
    barra_de_rolagemCD.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasCD.configure(yscrollcommand=barra_de_rolagemCD.set)
    canvasCD.bind('<Configure>', lambda e: canvasCD.configure(scrollregion=canvasCD.bbox("all")))

    fr_rolagemCD = Frame(canvasCD)

    canvasCD.create_window((0, 0), window=fr_rolagemCD, anchor="nw")

    ### multipage ###
    rows = 0
    while rows < 50:
        novoTrabalhoCD.rowconfigure(rows, weight=1)
        novoTrabalhoCD.columnconfigure(rows, weight=1)
        rows += 1

    ### columnspan(- = esquerda, + = direita), row(- = cima, + = baixo), column(- = direita, + = esquerda),
    ### rowspan(- = cima, + = baixo)
    nbCD = ttk.Notebook(novoTrabalhoCD)
    nbCD.grid(row=17, column=0, columnspan=37, rowspan=39, sticky="NESW")

    ### page1 ###
    page1CD = ttk.Frame(nbCD)
    nbCD.add(page1CD, text="Comissão Disciplinar")

    imgBalanca = Label(page1CD, image=imagemBalanca)
    imgBalanca.place(x=10, y=15)

    ComposicaoCD = Label(page1CD, text= 'Composição da Comissão\ndo Conselho Disciplinar', font='Arial 11 bold', foreground='darkblue')
    ComposicaoCD.place(x=80, y=25)

    DiretoriaCDText = Text(page1CD, width=37, height=1)
    DiretoriaCDText.place(x=10, y=100)

    DiretoriaCDLabel = Label(page1CD, text="Diretoria")
    DiretoriaCDLabel.place(x=10, y=75)

    SecretariaCDText = Text(page1CD, width=37, height=1)
    SecretariaCDText.place(x=10, y=145)

    SecretariaCDLabel = Label(page1CD, text="Secretaria")
    SecretariaCDLabel.place(x=10, y=120)

    CoordenacaoCDLabel = Label(page1CD, text="Coordenação")
    CoordenacaoCDLabel.place(x=10, y=165)

    CoordenacaoCD = tkinter.StringVar()
    CoordenacaoCDcbbx = ttk.Combobox(page1CD, width=46, height=1, textvariable=CoordenacaoCD)
    CoordenacaoCDcbbx.place(x=10, y=187)

    OrientacaoCDLabel = Label(page1CD, text="Orientação")
    OrientacaoCDLabel.place(x=10, y=210)

    OrientacaoCD = tkinter.StringVar()
    OrientacaoCDcbbx = ttk.Combobox(page1CD, width=46, height=1, textvariable=OrientacaoCD)
    OrientacaoCDcbbx.place(x=10, y=234)

    CapelaniaCDText = Text(page1CD, width=37, height=1)
    CapelaniaCDText.place(x=10, y=280)

    CapelaniaCDLabel = Label(page1CD, text="Capelania")
    CapelaniaCDLabel.place(x=10, y=257)

    ### criando frame ###
    fr_rolagemCD1 = Frame(page1CD, borderwidth=1, relief="solid")
    fr_rolagemCD1.place(x=318, y=30, width=345, height=348)

    ### criando o canvas ###
    canvasCD1 = Canvas(page1CD)
    canvasCD1.place(x=319, y=40, width=325, height=335)

    ### criando a barra de rolagem ###
    barra_de_rolagemCD1 = ttk.Scrollbar(fr_rolagemCD1, orient=VERTICAL, command=canvasCD1.yview)
    barra_de_rolagemCD1.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasCD1.configure(yscrollcommand=barra_de_rolagemCD1.set)
    canvasCD1.bind('<Configure>', lambda e: canvasCD1.configure(scrollregion=canvasCD1.bbox("all")))

    fr_rolagemCD1 = Frame(canvasCD1)

    canvasCD1.create_window((0, 0), window=fr_rolagemCD1, anchor="nw")

    ProfessoresPresentesCDLabel = Label(page1CD, text="Professores Presentes:", font='Arial 9 bold',
                                        foreground='darkblue')
    ProfessoresPresentesCDLabel.place(x=316, y=7)

    ResponsavelCDLabel = Label(page1CD, text="Responsável Legal Convocado:", font='Arial 7 bold', foreground='darkblue')
    ResponsavelCDLabel.place(x=670, y=7)

    ResponsavelCDText = Text(page1CD, width=32, height=1)
    ResponsavelCDText.place(x=670, y=30)

    ApresentacaoDemandaCDLabel = Label(page1CD, text="Apresentação da Demanda Conselho Disciplinar", font='Arial 7 bold',
                                 foreground='darkblue')
    ApresentacaoDemandaCDLabel.place(x=670, y=50)

    ApresentacaoDemandaCCText = Text(page1CD, width=32, height=19)
    ApresentacaoDemandaCCText.place(x=670, y=70)

    ### page2 ###
    page2CD = ttk.Frame(nbCD)
    nbCD.add(page2CD, text="Estatísticas do Aluno")

    ### Esquerda ###
    QuantidadeNomesAlunosCDLabel = Label(page2CD, text="Demonstrativo Geral do Quadro de Notas do Aluno", font='Arial 9 bold', foreground='blue')
    QuantidadeNomesAlunosCDLabel.place(x=10, y=7)

    AlunoSelecionadoCDLabel = Label(page2CD, text='Aluno(a) Selecionado(a):')
    AlunoSelecionadoCDLabel.place(x=480, y=27)

    AlunoSelecionadoCDText = Text(page2CD, width=6, height=1)
    AlunoSelecionadoCDText.place(x=618, y=27)

    FaltasDoAlunoCDText = Text(page2CD, bg='white', font='Arial 65 bold', foreground='red')
    FaltasDoAlunoCDText.place(x=685, y=60, width=255, height=100)

    FaltasDoAlunoCDLabel = Label(page2CD, text="Porcentagem de Faltas", font='Impact 14')
    FaltasDoAlunoCDLabel.place(x=728, y=25)

    ### criando frame page 1 ###
    fr_rolagem1CD = Frame(page2CD, borderwidth=1, relief="solid")
    fr_rolagem1CD.place(x=7, y=60, width=665, height=305)

    ### criando o canvas ###
    canvas1CD = Canvas(page2CD)
    canvas1CD.place(x=8, y=61, width=630, height=286)

    ### criando a barra de rolagem ###
    barra_de_rolagem1CD = ttk.Scrollbar(fr_rolagem1CD, orient=HORIZONTAL, command=canvas1CD.xview)
    barra_de_rolagem1CD.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ##
    canvas1CD.configure(xscrollcommand=barra_de_rolagem1CD.set)
    canvas1CD.bind('<Configure>', lambda e: canvas1CD.configure(scrollregion=canvas1CD.bbox("all")))

    fr_rolagem1CD = Frame(canvas1CD)

    canvas1CD.create_window((0, 0), window=fr_rolagem1CD, anchor="nw")

    ### page3 ###
    page3CD = ttk.Frame(nbCD)
    nbCD.add(page3CD, text="Avaliação Prévia do Aluno")

    ### Pergunta1 ###
    FrameCDPergunta1 = Frame(page3CD, bg='Light Grey', width=475, height=70)
    FrameCDPergunta1.place(x=5, y=20)

    QuantoAproveitamentoCDLabel = Label(page3CD, text="1 - Quanto ao Aproveitamento Acadêmico do Aluno:", bg='Light Grey',
                                        font="Arial 9 bold", foreground='blue')
    QuantoAproveitamentoCDLabel.place(x=10, y=30)

    OptionintCD1 = IntVar()

    ExcelenteCD1 = Radiobutton(page3CD, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W,
                               variable=OptionintCD1)
    ExcelenteCD1.place(x=20, y=55)

    SuficienteCD1 = Radiobutton(page3CD, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W,
                                variable=OptionintCD1)
    SuficienteCD1.place(x=100, y=55)

    SatisfatorioCD1 = Radiobutton(page3CD, text="Satisfatório", bg='Light Grey', value=3, width=14, anchor=W,
                                  variable=OptionintCD1)
    SatisfatorioCD1.place(x=180, y=55)

    InsuficienteCD1 = Radiobutton(page3CD, text="Insuficiente", bg='Light Grey', value=4, width=8, anchor=W,
                                  variable=OptionintCD1)
    InsuficienteCD1.place(x=265, y=55)

    ### Pergunta2 ###
    FrameCDPergunta2 = Frame(page3CD, bg='Light Grey', width=475, height=70)
    FrameCDPergunta2.place(x=5, y=130)

    QuantoDisciplinaTurmaCDLabel = Label(page3CD, text="2 - Antecedentes Indeciplinares Anteriores do Aluno:", bg='Light Grey',
                                         font="Arial 9 bold", foreground='blue')
    QuantoDisciplinaTurmaCDLabel.place(x=10, y=140)

    OptionintCD2 = IntVar()

    ExecissivoCD2 = Radiobutton(page3CD, text="Execissivo", bg='Light Grey', value=1, width=14, anchor=W,
                               variable=OptionintCD2)
    ExecissivoCD2.place(x=20, y=160)

    MuitoCD2 = Radiobutton(page3CD, text="Muito", bg='Light Grey', value=2, width=14, anchor=W,
                                variable=OptionintCD2)
    MuitoCD2.place(x=100, y=160)

    PoucoCD2 = Radiobutton(page3CD, text="Pouco", bg='Light Grey', value=3, width=14, anchor=W,
                                  variable=OptionintCD2)
    PoucoCD2.place(x=180, y=160)

    NadaCD2 = Radiobutton(page3CD, text="Nada", bg='Light Grey', value=4, width=8, anchor=W, variable=OptionintCD2)
    NadaCD2.place(x=265, y=160)

    ### Pergunta3 ###
    FrameCDPergunta3 = Frame(page3CD, bg='Light Grey', width=475, height=70)
    FrameCDPergunta3.place(x=5, y=230)

    QuantoParticipacaoTurmaClasseCDLabel = Label(page3CD, text="3 - Quanto a Participação do Aluno em Classe:",
                                                 bg='Light Grey', font="Arial 9 bold", foreground='blue')
    QuantoParticipacaoTurmaClasseCDLabel.place(x=10, y=240)

    OptionintCD3 = IntVar()

    ExcelenteCD3 = Radiobutton(page3CD, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W,
                               variable=OptionintCD3)
    ExcelenteCD3.place(x=20, y=260)

    SuficienteCD3 = Radiobutton(page3CD, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W,
                                variable=OptionintCD3)
    SuficienteCD3.place(x=100, y=260)

    SatisfatorioCD3 = Radiobutton(page3CD, text="Satisfatório", bg='Light Grey', value=3, width=14, anchor=W,
                                  variable=OptionintCD3)
    SatisfatorioCD3.place(x=180, y=260)

    InsuficienteCD3 = Radiobutton(page3CD, text="Insuficiente", bg='Light Grey', value=4, width=8, anchor=W,
                                  variable=OptionintCD3)
    InsuficienteCD3.place(x=265, y=260)

    ### Pergunta4 ###
    FrameCDPergunta4 = Frame(page3CD, bg='Light Grey', width=580, height=70)
    FrameCDPergunta4.place(x=490, y=20)

    QuantoFrequenciaTurmaCDLabel = Label(page3CD, text="4 - Quanto a Frequência do Aluno em Sala:", bg='Light Grey',
                                         font="Arial 9 bold", foreground='blue')
    QuantoFrequenciaTurmaCDLabel.place(x=500, y=30)

    OptionintCD4 = IntVar()

    ExcelenteCD4 = Radiobutton(page3CD, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W,
                               variable=OptionintCD4)
    ExcelenteCD4.place(x=510, y=50)

    SuficienteCD4 = Radiobutton(page3CD, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W,
                                variable=OptionintCD4)
    SuficienteCD4.place(x=590, y=50)

    SatisfatoriaCD4 = Radiobutton(page3CD, text="Satisfatória", bg='Light Grey', value=3, width=14, anchor=W,
                                  variable=OptionintCD4)
    SatisfatoriaCD4.place(x=670, y=50)

    BaixaCD4 = Radiobutton(page3CD, text="Baixa", bg='Light Grey', value=4, width=14, anchor=W, variable=OptionintCD4)
    BaixaCD4.place(x=755, y=50)

    ### Pergunta5 ###
    FrameCDPergunta5 = Frame(page3CD, bg='Light Grey', width=580, height=70)
    FrameCDPergunta5.place(x=490, y=130)

    QuantoComunicacaoTurmaCDLabel = Label(page3CD, text="5 - Relação do Aluno com os Professores:",
                                          bg='Light Grey', font="Arial 9 bold", foreground='blue')
    QuantoComunicacaoTurmaCDLabel.place(x=500, y=140)

    OptionintCD5 = IntVar()

    ExcelenteCD5 = Radiobutton(page3CD, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W,
                               variable=OptionintCD5)
    ExcelenteCD5.place(x=510, y=160)

    SuficienteCD5 = Radiobutton(page3CD, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W,
                                variable=OptionintCD5)
    SuficienteCD5.place(x=590, y=160)

    SatisfatorioCD5 = Radiobutton(page3CD, text="Satisfatório", bg='Light Grey', value=3, width=14, anchor=W,
                                  variable=OptionintCD5)
    SatisfatorioCD5.place(x=670, y=160)

    InsuficienteCD5 = Radiobutton(page3CD, text="Insuficiente", bg='Light Grey', value=4, width=14, anchor=W,
                                  variable=OptionintCD5)
    InsuficienteCD5.place(x=755, y=160)

    ### Pergunta6 ###
    FrameCDPergunta6 = Frame(page3CD, bg='Light Grey', width=580, height=70)
    FrameCDPergunta6.place(x=490, y=230)

    QuantoRelacaoTurmaCDLabel = Label(page3CD, text="6 - Relação Interpessoal do Alunos com os Pares", bg='Light Grey',
                                      font="Arial 9 bold", foreground='blue')
    QuantoRelacaoTurmaCDLabel.place(x=500, y=240)

    OptionintCD6 = IntVar()

    ExcelenteCD6 = Radiobutton(page3CD, text="Excelente", bg='Light Grey', value=1, width=14, anchor=W,
                               variable=OptionintCD6)
    ExcelenteCD6.place(x=510, y=260)

    SuficienteCD6 = Radiobutton(page3CD, text="Suficiente", bg='Light Grey', value=2, width=14, anchor=W,
                                variable=OptionintCD6)
    SuficienteCD6.place(x=590, y=260)

    SatisfatoriaCD6 = Radiobutton(page3CD, text="Satisfatória", bg='Light Grey', value=3, width=14, anchor=W,
                                  variable=OptionintCD6)
    SatisfatoriaCD6.place(x=670, y=260)

    InsuficientaCD6 = Radiobutton(page3CD, text="Baixa", bg='Light Grey', value=4, width=14, anchor=W,
                                  variable=OptionintCD6)
    InsuficientaCD6.place(x=755, y=260)

    page4CD = ttk.Frame(nbCD)
    nbCD.add(page4CD, text="Composição do Código Disciplinar")

    RA_AlunoCDLabel = Label(page4CD, text="RA - Aluno", font="Arial 8 bold")
    RA_AlunoCDLabel.place(x=449, y=10)

    AlunoSelecionadoCD4 = tkinter.StringVar()
    AlunoSelecionadoCD4cbbx = ttk.Combobox(page4CD, width=6, height=1, textvariable=AlunoSelecionadoCD4)
    AlunoSelecionadoCD4cbbx.place(x=449, y=30)

    Salvar_Itens_SelectCDPg4Button = Button(page4CD, image=imgSalvar)
    Salvar_Itens_SelectCDPg4Button.place(x=458, y=60, width=40, height=40)

    Transf_Itens_SelectCDPg4Button = Button(page4CD, image=imgTransferir)
    Transf_Itens_SelectCDPg4Button.place(x=458, y=120, width=40, height=40)

    Limpar_Itens_SelectCDPg4Button = Button(page4CD, image=imgLimpar)
    Limpar_Itens_SelectCDPg4Button.place(x=458, y=170, width=40, height=40)

    Carregar_Itens_SelectCDPg4Button = Button(page4CD, image=imgCarregar)
    Carregar_Itens_SelectCDPg4Button.place(x=458, y=220, width=40, height=40)

    ### criando frame ###
    fr_rolagemCD4 = Frame(page4CD, borderwidth=1, relief="solid")
    fr_rolagemCD4.place(x=9, y=9, width=430, height=261)

    ### criando o canvas ###
    canvasCD4 = Canvas(page4CD)
    canvasCD4.place(x=10, y=10, width=412, height=244)

    ### criando a barra de rolagem ###
    barra_de_rolagem2CD = ttk.Scrollbar(fr_rolagemCD4, orient=VERTICAL, command=canvasCD4.yview)
    barra_de_rolagem2CD.pack(side=RIGHT, fill=Y)

    barra_de_rolagem3CD = ttk.Scrollbar(fr_rolagemCD4, orient=HORIZONTAL, command=canvasCD4.xview)
    barra_de_rolagem3CD.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasCD4.configure(yscrollcommand=barra_de_rolagem2CD.set)
    canvasCD4.bind('<Configure>', lambda e: canvasCD4.configure(scrollregion=canvasCD4.bbox("all")))

    canvasCD4.configure(xscrollcommand=barra_de_rolagem3CD.set)
    canvasCD4.bind('<Configure>', lambda e: canvasCD4.configure(scrollregion=canvasCD4.bbox("all")))

    fr_rolagemCD4 = Frame(canvasCD4)

    canvasCD4.create_window((0, 0), window=fr_rolagemCD4, anchor="nw")

    ### criando frame ###
    fr_rolagemCD401 = Frame(page4CD, borderwidth=1, relief="solid")
    fr_rolagemCD401.place(x=519, y=9, width=430, height=261)

    ### criando o canvas ###
    canvasCD401 = Canvas(page4CD)
    canvasCD401.place(x=520, y=10, width=412, height=244)

    ### criando a barra de rolagem ###
    barra_de_rolagem4CD = ttk.Scrollbar(fr_rolagemCD401, orient=VERTICAL, command=canvasCD401.yview)
    barra_de_rolagem4CD.pack(side=RIGHT, fill=Y)

    barra_de_rolagem5CD = ttk.Scrollbar(fr_rolagemCD401, orient=HORIZONTAL, command=canvasCD401.xview)
    barra_de_rolagem5CD.pack(side=BOTTOM, fill=X)

    ### configurando o canvas ###
    canvasCD401.configure(yscrollcommand=barra_de_rolagem4CD.set)
    canvasCD401.bind('<Configure>', lambda e: canvasCD401.configure(scrollregion=canvasCD401.bbox("all")))

    canvasCD401.configure(xscrollcommand=barra_de_rolagem5CD.set)
    canvasCD401.bind('<Configure>', lambda e: canvasCD401.configure(scrollregion=canvasCD401.bbox("all")))

    fr_rolagemCD401 = Frame(canvasCD401)

    canvasCD401.create_window((0, 0), window=fr_rolagemCD401, anchor="nw")

    CosideracoesCDLbl = Label(page4CD, text="Considerações Finais", font="Arial 9 bold", foreground='blue')
    CosideracoesCDLbl.place(x=10, y=270)

    CosideracoesCD = Text(page4CD, width=117, height=6)
    CosideracoesCD.place(x=10, y=290)

def Apontamento():
    Apontamento = Toplevel()
    Apontamento.geometry('1130x375+10+140')
    Apontamento.resizable(False,False)
    Apontamento.title('Apontamento')
    Apontamento.configure(bg='light gray')
    Apontamento.transient(trabalho)
    Apontamento.focus_force()
    Apontamento.grab_set()

    APONTAMENTOSLabel = Label(Apontamento, text="APONTAMENTOS DO CONSELHO PARCITIPATIVO", font="Arial 8 bold", bg='light grey', foreground='blue')
    APONTAMENTOSLabel.place(x=400, y=4)

### itens novo trabalho 1 ###
### criando frame ###
    fr_rolagemApontamento = Frame(Apontamento, borderwidth=1, relief="solid")
    fr_rolagemApontamento.place(x=7, y=30, width=1115, height=335)

    ### criando o canvas ###
    canvasApontamento = Canvas(Apontamento)
    canvasApontamento.place(x=8, y=31, width=1085, height=333)

    ### criando a barra de rolagem ###
    barra_de_rolagemApontamento = ttk.Scrollbar(fr_rolagemApontamento, orient=VERTICAL, command=canvasApontamento.yview)
    barra_de_rolagemApontamento.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasApontamento.configure(yscrollcommand=barra_de_rolagemApontamento.set)
    canvasApontamento.bind('<Configure>', lambda e: canvasApontamento.configure(scrollregion=canvasApontamento.bbox("all")))

    fr_rolagemApontamento = Frame(canvasApontamento)

    canvasApontamento.create_window((0, 0), window=fr_rolagemApontamento, anchor="nw")


def Preposicao():
    Preposicao = Toplevel()
    Preposicao.geometry('1130x375+10+140')
    Preposicao.resizable(False,False)
    Preposicao.title('Apontamento')
    Preposicao.configure(bg='light gray')
    Preposicao.transient(trabalho)
    Preposicao.focus_force()
    Preposicao.grab_set()

    PreposicaoLabel = Label(Preposicao, text="Proposta de Intervenção Pedagógica Pós Conselho Participativo para o Aluno", font="Arial 9 bold", bg='light grey', foreground='blue')
    PreposicaoLabel.place(x=350, y=4)

### itens novo trabalho 1 ###
### criando frame ###
    fr_rolagemPreposicao = Frame(Preposicao, borderwidth=1, relief="solid")
    fr_rolagemPreposicao.place(x=7, y=30, width=1115, height=335)

    ### criando o canvas ###
    canvasPreposicao = Canvas(Preposicao)
    canvasPreposicao.place(x=8, y=31, width=1085, height=333)

    ### criando a barra de rolagem ###
    barra_de_rolagemPreposicao = ttk.Scrollbar(fr_rolagemPreposicao, orient=VERTICAL, command=canvasPreposicao.yview)
    barra_de_rolagemPreposicao.pack(side=RIGHT, fill=Y)

    ### configurando o canvas ###
    canvasPreposicao.configure(yscrollcommand=barra_de_rolagemPreposicao.set)
    canvasPreposicao.bind('<Configure>', lambda e: canvasPreposicao.configure(scrollregion=canvasPreposicao.bbox("all")))

    fr_rolagemPreposicao = Frame(canvasPreposicao)

    canvasPreposicao.create_window((0, 0), window=fr_rolagemPreposicao, anchor="nw")

### Função que troca a cor dos botões ###
def trocarCor(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

### fazer dowload das imagens ###
imgTurma = PhotoImage(file="icones/turma.png")
imgSondagem = PhotoImage(file="icones/sondagem.png")
imgPNE = PhotoImage(file="icones/pne.png")
imgplanejamento = PhotoImage(file="icones/planejamento.png")
imgindividual = PhotoImage(file="icones/individual.png")
imginclusao = PhotoImage(file="icones/inclusão.png")
imgcdc = PhotoImage(file="icones/conselho de classe.png")
imgGrafico = PhotoImage(file="icones/Gráficopng.png")
imagemBalanca = PhotoImage(file='icones/Balança.png')
imganam = PhotoImage(file="icones/anamnese.png")
imgavdt = PhotoImage(file="icones/avaliação de turma.png")
imgavd = PhotoImage(file="icones/avaliação de aluno .png")
imgEA = PhotoImage(file="icones/Educação Adventista.png")
imgCD = PhotoImage(file="icones/Conselho diciplinar.png")
imgAdita = PhotoImage(file="icones/Aditamento.png")
imgCalend = PhotoImage(file='icones/Calendario.png')
imgFoto_Aluno = PhotoImage(file='icones/Foto.png')
imgPlusPEI = PhotoImage(file='icones/PlusPEI.png')
imgCCpage1 = PhotoImage(file='icones/ImagemConselhoClassePage1SemFundo.png')
imgSalvar = PhotoImage(file='icones/Salvar.png')
imgTransferir = PhotoImage(file='icones/Transferir.png')
imgLimpar = PhotoImage(file='icones/Limpar.png')
imgCarregar = PhotoImage(file='icones/Carregar.png')
Foto_Pilar_CdFoto = PhotoImage(file='icones/Pilar.png')


### colocar imagens ###
adita_img = Label(trabalho, image=imgAdita)
adita_img.place(x=20, y=20, width=40, height=37)

turma_img = Label(trabalho, image=imgTurma)
turma_img.place(x=20, y=60, width=40, height=37)

individual_img = Label(trabalho, image=imgindividual)
individual_img.place(x=20, y=100, width=40, height=37)

PEI_img = Label(trabalho, image=imginclusao)
PEI_img.place(x=20, y=140, width=40, height=37)

CC_img = Label(trabalho, image=imgcdc)
CC_img.place(x=20, y=180, width=40, height=37)

CD_img = Label(trabalho, image=imgCD)
CD_img.place(x=20, y=220, width=40, height=37)

planejamento_img = Label(trabalho, image=imgplanejamento)
planejamento_img.place(x=20, y=260, width=40, height=37)

pne_img = Label(trabalho, image=imgPNE)
pne_img.place(x=20, y=300, width=40, height=37)

sondagem_img = Label(trabalho, image=imgSondagem)
sondagem_img.place(x=20, y=340, width=40, height=37)

anamnese_img = Label(trabalho, image=imganam)
anamnese_img.place(x=20, y=380, width=40, height=37)

av_aluno_img = Label(trabalho, image=imgavd)
av_aluno_img.place(x=20, y=420, width=40, height=37)

av_turma_img = Label(trabalho, image=imgavdt)
av_turma_img.place(x=20, y=460, width=40, height=37)

### barra em cima da área de trabalho ###
barraDoMenu = Menu(trabalho)
menuControle = Menu(barraDoMenu, tearoff=0)
menuControle.add_command(label="Incluir", command=semComando)
menuControle.add_separator()
menuControle.add_command(label="Salvar", command=semComando)
menuControle.add_command(label="Editar", command=semComando)
menuControle.add_separator()
menuControle.add_command(label="Excluir", command=semComando)
menuControle.add_separator()
barraDoMenu.add_cascade(label="Cadastro", menu=menuControle)

trabalho.config(menu=barraDoMenu)

### botões ###
botaoDeAditamento = Button(trabalho, text='Aditamento', font='negrito', bg="grey", command=abrirAditamento)
botaoDeAditamento.place(x=60, y=20, width=200, height=40)

trocarCor(botaoDeAditamento, "cyan", "grey")

botaoDeTurma = Button(trabalho, text='Turma', font='bold', bg='grey', command=abrirTurma)
botaoDeTurma.place(x=60, y=60, width=200, height=40)

trocarCor(botaoDeTurma, "cyan", "grey")

botaoDeIndividual = Button(trabalho, text='Individual', font='negrito', bg="grey", command=abrirIndividual)
botaoDeIndividual.place(x=60, y=100, width=200, height=40)

trocarCor(botaoDeIndividual, "cyan", "grey")

botaoDePEI = Button(trabalho, text='PEI', font='negrito', bg="grey", command=abrirPEI)
botaoDePEI.place(x=60, y=140, width=200, height=40)

trocarCor(botaoDePEI, "cyan", "grey")

botaoDeConselhoClasse = Button(trabalho, text='Conselho de Classe', font='negrito', bg="grey", command=abrirConselhoClasse)
botaoDeConselhoClasse.place(x=60, y=180, width=200, height=40)

trocarCor(botaoDeConselhoClasse, "cyan", "grey")

botaoDeConselhoDiciplinar = Button(trabalho, text='Conselho Diciplinar', font='negrito', bg="grey", command=abrirCD)
botaoDeConselhoDiciplinar.place(x=60, y=220, width=200, height=40)

trocarCor(botaoDeConselhoDiciplinar, "cyan", "grey")

botaoDePlanejamento = Button(trabalho, text='Planejamento', font='negrito', bg="grey", command=abrirPlanejamento)
botaoDePlanejamento.place(x=60, y=260, width=200, height=40)

trocarCor(botaoDePlanejamento, "cyan", "grey")

botaoDePNE = Button(trabalho, text='Plano PNE', font='negrito', bg="grey", command=abrirPNE)
botaoDePNE.place(x=60, y=300, width=200, height=40)

trocarCor(botaoDePNE, "cyan", "grey")

botaoDeSondagem = Button(trabalho, text='Sondagem', font='negrito', bg="grey", command=abrirSondagem)
botaoDeSondagem.place(x=60, y=340, width=200, height=40)

trocarCor(botaoDeSondagem, "cyan", "grey")

botaoDeAnamnese = Button(trabalho, text='ANAMNESE', font='negrito', bg="grey", command=abrirANAMNESE)
botaoDeAnamnese.place(x=60, y=380, width=200, height=40)

trocarCor(botaoDeAnamnese, "cyan", "grey")

botaoDeCPAdA = Button(trabalho, text='CP - Avaliação de Aluno', font='negrito', bg="grey", command=abrirCPAluno)
botaoDeCPAdA.place(x=60, y=420, width=200, height=40)

trocarCor(botaoDeCPAdA, "cyan", "grey")

botaoDeCPAdT = Button(trabalho, text='CP - Avaliação das Turmas', font='negrito', bg="grey", command=abrirCPTurma)
botaoDeCPAdT.place(x=60, y=460, width=200, height=40)

trocarCor(botaoDeCPAdT, "cyan", "grey")

trabalho.mainloop()