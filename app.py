import customtkinter as ctk

# Lambda

operacoes = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    'x': lambda x,y: x*y,
    '÷': lambda x,y: x/y
}

# Variáveis Globais

numVezesClick = 0
calculo1 = ''
calculo2 = ''
operador = ''

# Blocos.

def mostrarResultado():
    global numVezesClick, calculo1, calculo2, operador
    if not calculo1 and not operador:
        ...
    else:
        if operador == '÷':
            if float(mostrarCalculoTextbox.get('1.0', 'end').replace(',', '.')) > 0:
                calculo2 = float(mostrarCalculoTextbox.get('1.0', 'end').replace(',', '.'))
                resultadoConta = f'{operacoes[operador](calculo1, calculo2):.2f}'
                mostrarCalculoTextbox.delete('1.0', 'end')
                mostrarCalculoTextbox.insert('1.0', str(resultadoConta).replace('.', ','))
                numVezesClick = 0
                calculo1 = ''
                calculo2 = ''
                operador = ''
            else:
                mostrarCalculoTextbox.delete('1.0', 'end')
                mostrarCalculoTextbox.insert('1.0', 'Erro: Divisão!')
        else:
            calculo2 = float(mostrarCalculoTextbox.get('1.0', 'end').replace(',', '.'))
            resultadoConta = f'{operacoes[operador](calculo1, calculo2):.1f}'
            mostrarCalculoTextbox.delete('1.0', 'end')
            mostrarCalculoTextbox.insert('1.0', str(resultadoConta).replace('.', ','))
            numVezesClick = 0
            calculo1 = ''
            calculo2 = ''
            operador = ''

def aplicarOperador(op):
    global calculo1, calculo2, operador, numVezesClick
    if not calculo1:
        calculo1 = float(mostrarCalculoTextbox.get('1.0', 'end').replace(',', '.'))
        operador = op
        mostrarCalculoTextbox.delete('1.0', 'end')
        mostrarCalculoTextbox.insert('1.0', '0')
        numVezesClick = 0
    else:
        if op == '÷':
            if float(mostrarCalculoTextbox.get('1.0', 'end').replace(',', '.')) > 0:
                calculo2 = float(mostrarCalculoTextbox.get('1.0', 'end').replace(',', '.'))
                resultadoConta = f'{operacoes[operador](calculo1, calculo2):.1f}'
                mostrarCalculoTextbox.delete('1.0', 'end')
                mostrarCalculoTextbox.insert('1.0', str(resultadoConta).replace('.', ','))
                numVezesClick = 0
                calculo1 = ''
                calculo2 = ''
                operador = ''
            else:
                mostrarCalculoTextbox.delete('1.0', 'end')
                mostrarCalculoTextbox.insert('1.0', 'Erro: Divisão!')
        else:
            calculo2 = float(mostrarCalculoTextbox.get('1.0', 'end').replace(',', '.'))
            resultadoConta = f'{operacoes[operador](calculo1, calculo2):.1f}'
            mostrarCalculoTextbox.delete('1.0', 'end')
            mostrarCalculoTextbox.insert('1.0', str(resultadoConta).replace('.', ','))
            numVezesClick = 0
            calculo1 = ''
            calculo2 = ''
            operador = ''
    
def resetarCalculadora():
    global numVezesClick, calculo1, calculo2, operador
    numVezesClick = 0
    calculo1 = ''
    calculo2 = ''
    operador = ''
    mostrarCalculoTextbox.delete('1.0', 'end')
    mostrarCalculoTextbox.insert('1.0', '0')

def apagarCaractere():
    global numVezesClick, calculo1, calculo2
    if numVezesClick == 1:
        if mostrarCalculoTextbox.get('1.0', 'end').count('0') == 1:
            mostrarCalculoTextbox.delete('end-2c', 'end-1c')
            numVezesClick -= 1
        else:
            mostrarCalculoTextbox.delete('end-2c', 'end-1c')
            mostrarCalculoTextbox.insert('1.0', '0')
            numVezesClick -= 1
            if operador:
                calculo2 = ''
            else:
                calculo1 = ''
    elif numVezesClick != 0:
        mostrarCalculoTextbox.delete('end-2c', 'end-1c')
        numVezesClick -= 1

def mostrarCaractere(caractere):
    global numVezesClick
    if numVezesClick == 0 and caractere == '0':
        ...
    elif caractere == ',':
        if mostrarCalculoTextbox.get('1.0', 'end').count(',') == 0:
            mostrarCalculoTextbox.insert('end', caractere)
            numVezesClick += 1
    else:
        if numVezesClick == 0:
            mostrarCalculoTextbox.delete('1.0', 'end')
            mostrarCalculoTextbox.insert('end', caractere)
            numVezesClick += 1
        else:
            mostrarCalculoTextbox.insert('end', caractere)
            numVezesClick += 1

# Configs. da Janela

root = ctk.CTk()

root.title('Calculadora CTk')
root.geometry('350x320')

# Caixa de Números

mostrarCalculoTextbox = ctk.CTkTextbox(root, corner_radius=5, font=('Consolas', 30), width=310, height=2, border_width=1, border_color='white')
mostrarCalculoTextbox.place(x=175, y=40, anchor='center')

mostrarCalculoTextbox.insert('1.0', '0')

# Números

numZeroButton = ctk.CTkButton(root, text='0', font=('Consolas', 20), width=110, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('0'))
numZeroButton.place(x=75, y=280, anchor='center')

numUmButton = ctk.CTkButton(root, text='1', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('1'))
numUmButton.place(x=45, y=220, anchor='center')

numDoisButton = ctk.CTkButton(root, text='2', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('2'))
numDoisButton.place(x=105, y=220, anchor='center')

numTresButton = ctk.CTkButton(root, text='3', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('3'))
numTresButton.place(x=165, y=220, anchor='center')

numQuatroButton = ctk.CTkButton(root, text='4', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('4'))
numQuatroButton.place(x=45, y=160, anchor='center')

numCincoButton = ctk.CTkButton(root, text='5', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('5'))
numCincoButton.place(x=105, y=160, anchor='center')

numSeisButton = ctk.CTkButton(root, text='6', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('6'))
numSeisButton.place(x=165, y=160, anchor='center')

numSeteButton = ctk.CTkButton(root, text='7', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('7'))
numSeteButton.place(x=45, y=100, anchor='center')

numOitoButton = ctk.CTkButton(root, text='8', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('8'))
numOitoButton.place(x=105, y=100, anchor='center')

numNoveButton = ctk.CTkButton(root, text='9', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere('9'))
numNoveButton.place(x=165, y=100, anchor='center')

# Operadores da Calc.

adicaoButton = ctk.CTkButton(root, text='+', font=('Consolas', 20), width=60, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: aplicarOperador('+'))
adicaoButton.place(x=230, y=160, anchor='center')

subtracaoButton = ctk.CTkButton(root, text='-', font=('Consolas', 20), width=60, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: aplicarOperador('-'))
subtracaoButton.place(x=300, y=160, anchor='center')

multiplicacaoButton = ctk.CTkButton(root, text='x', font=('Consolas', 20), width=60, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: aplicarOperador('x'))
multiplicacaoButton.place(x=230, y=220, anchor='center')

divisaoButton = ctk.CTkButton(root, text='÷', font=('Consolas', 20), width=60, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: aplicarOperador('÷'))
divisaoButton.place(x=300, y=220, anchor='center')

resultadoButton = ctk.CTkButton(root, text='=', font=('Consolas', 20), width=130, height=50, border_width=1, border_color='black', corner_radius=5, command=mostrarResultado)
resultadoButton.place(x=265, y=280, anchor='center')

# Botões Especiais

deletarButton = ctk.CTkButton(root, text='<', font=('Consolas', 20), width=60, height=50, border_width=1, border_color='black', corner_radius=5, command=apagarCaractere)
deletarButton.place(x=230, y=100, anchor='center')

resetarButton = ctk.CTkButton(root, text='C', font=('Consolas', 20), width=60, height=50, border_width=1, border_color='black', corner_radius=5, command=resetarCalculadora)
resetarButton.place(x=300, y=100, anchor='center')

virgulaButton = ctk.CTkButton(root, text=',', font=('Consolas', 20), width=50, height=50, border_width=1, border_color='black', corner_radius=5, command=lambda: mostrarCaractere(','))
virgulaButton.place(x=165, y=280, anchor='center')

# Rodando a Janela

root.mainloop()
