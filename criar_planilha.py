import openpyxl

# Cria um novo arquivo do Excel
workbook = openpyxl.Workbook()

# Seleciona a primeira planilha
sheet = workbook.active

# Preenche alguns dados na planilha
sheet['A1'] = 'Nome'
sheet['B1'] = 'Idade'
sheet['A2'] = 'João'
sheet['B2'] = 25
sheet['A3'] = 'Maria'
sheet['B3'] = 30

# Salva o arquivo do Excel
workbook.save('planilha.xlsx')

print("Planilha criada com sucesso!")
