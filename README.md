# Matematica-brow-Gerador-certificados
 
# Gerador de Certificados Personalizados

Este é um projeto simples que visa automatizar a geração de certificados únicos para o **Curso Matemática Brow**. A ideia surgiu após concluir o curso de "Python Básico", ministrado por **Saulo Coelho** e oferecido pela **DEV SAMURAI**, onde decidi aplicar os conhecimentos adquiridos para facilitar meu trabalho como designer.

## Problema
Anteriormente, para criar certificados personalizados, o processo era manual, exigindo abrir e modificar cada certificado individualmente, o que gerava muito trabalho. Agora, com a ajuda das bibliotecas **openpyxl** e **Pillow**, é possível acessar os dados de cada aluno em uma planilha Excel e automaticamente "desenhar" essas informações em um modelo de certificado.

## Solução
Este projeto automatiza a inserção das informações dos alunos, como nome e curso, em um certificado base, gerando arquivos de imagem personalizados para cada um. O código utiliza a biblioteca **openpyxl** para acessar os dados em uma planilha Excel e a **Pillow** para manipulação gráfica e desenho dos dados no certificado.

## Funcionalidades
- **Leitura de dados de uma planilha Excel**: Através da biblioteca **openpyxl**, os dados dos alunos são extraídos diretamente de uma planilha.
- **Geração automática de certificados**: Usando a biblioteca **Pillow**, o script insere os dados de cada aluno em um template de certificado, gerando uma imagem única para cada um.
- **Economia de tempo**: O processo que antes era manual agora é automatizado, permitindo a geração em massa de certificados personalizados.

## Tecnologias Utilizadas
- **Python Python 3.12.4**
- **openpyxl**: Para manipulação e leitura de arquivos Excel.
- **Pillow**: Para manipulação e geração de imagens.

## Como usar
1. Clone este repositório.
2. Certifique-se de ter o Python 3.x instalado em sua máquina.
3. Instale as dependências do projeto:
   ```bash
   pip install openpyxl pillow
   ```
4. Insira os dados dos alunos no arquivo Excel que será utilizado (exemplo: `alunos.xlsx`).
5. Prepare o modelo de certificado (`certificado_base.png`) para ser usado como template.
6. Execute o script Python:
   ```bash
   python gerar_certificados.py
   ```
7. Os certificados gerados serão salvos em uma pasta especificada no código.

## Conclusão
Embora seja um projeto simples, ele já facilita bastante o processo de criação de certificados, economizando tempo e reduzindo o trabalho manual. É uma ótima aplicação prática dos conhecimentos adquiridos no curso de Python.
