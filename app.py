import openpyxl
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Abrir a planilha
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    # Pegar os dados de cada célula
    nome_curso = linha[0].value  
    nome_participante = linha[1].value  
    tipo_participacao = linha[2].value  
    carga_horaria = linha[5].value  

    data_inicio = linha[3].value  
    data_final = linha[4].value  
    data_emissao = linha[6].value  

    # Converta as datas para string no formato desejado

    data_inicio_str = data_inicio.strftime('%d/%m/%Y') if isinstance(data_inicio, datetime) else str(data_inicio)
    data_final_str = data_final.strftime('%d/%m/%Y') if isinstance(data_final, datetime) else str(data_final)
    data_emissao_str = data_emissao.strftime('%d/%m/%Y') if isinstance(data_emissao, datetime) else str(data_emissao)

    # Transferir os dados da planilha para a imagem do certificado
    # Definindo a fonte a ser usada

    fonte_nome = ImageFont.truetype('./Poppins-Bold.ttf', 80)
    fonte_geral = ImageFont.truetype('./Poppins-Regular.ttf', 60)
    fonte_data = ImageFont.truetype('./Poppins-Regular.ttf', 55)

    image = Image.open('./Certificado-alunos.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((1020, 827), nome_participante, fill='#2c2c2c', font=fonte_nome)
    desenhar.text((1022, 960), nome_curso, fill='#2c2c2c', font=fonte_geral)
    desenhar.text((1435, 1065), tipo_participacao, fill='#2c2c2c', font=fonte_geral)
    desenhar.text((1480, 1182), str(carga_horaria), fill='#2c2c2c', font=fonte_geral)

    desenhar.text((750, 1770), data_inicio_str, fill='#0074ff', font=fonte_data)
    desenhar.text((750, 1930), data_final_str, fill='#0074ff', font=fonte_data)

    desenhar.text((2220, 1930), data_emissao_str, fill='#0074ff', font=fonte_data)

    image.save(f'./Certificado-alunos/{indice} {nome_participante} certificado.png')
    