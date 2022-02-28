import pyodbc as odbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=WillianLenovo;"
    "Database=PythonSQL;"
)

nome = input("Digite seu nome:\n")
sobrenome = input("\nDigite seu sobrenome:\n")
idade = input("\nDigite sua idade:\n")
sexo = input("\nEscolha o seu sexo:" + """
Digite 1 para Masculino ou Digite 2 para Feminino\n""")
dataNascimento = input(
    "\nDigite sua data de nascimento no formato dd/mm/yyyy:\n")

try:
    conexao = odbc.connect(dados_conexao)
    print("Conectado ao SQL Server")
    cursor = conexao.cursor()
    createUsuario = f"""
        insert into Usuario (nome,sobrenome,idade,sexo,dataNascimento)
        values ('{nome}','{sobrenome}','{idade}','{sexo}','{dataNascimento}')
    """
    cursor.execute(createUsuario)
    cursor.commit()
    print("Usuário Cadastrado")
except Exception as ex:
    print(ex)
