import tabula
import pandas as pd
from zipfile import ZipFile

from time import sleep

inputA1 = "Anexo1.pdf"
outputA1 = "Anexo1.csv"

cores = {
    "verde": "\033[32m",
    "laranja": "\033[33m",
    "lilas": "\033[94m"
}

# Extraindo dados da tabela:
print(f"\n{cores['lilas']}Extraindo dados da sua tabela... (1/4)\033[m")

originalA1 = tabula.read_pdf(input_path=inputA1, pages="all", encoding='utf-8', lattice=True, stream=True)

# Concatenando tabelas para que se unam em apenas uma:
updatedA1 = pd.concat(originalA1, ignore_index=True)

# Substituindo nomes COLUNAS:
sleep(1)
print(f"\n{cores['lilas']}Substituindo abreviações necessárias... (2/4)\033[m")

updatedA1.rename(
    columns = {
    "OD": "SEG. ODONTOLÓGICA",
    "AMB": "SEG. AMBULATORIAL"
}, inplace=True)

# Substituindo nomes LINHAS
abrev = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
    }

updatedA1.replace(abrev, inplace=True)

"""
# PARA VISUALIZAR O CÓDIGO NO TERMINAL:

df = pd.DataFrame(updatedA1)
pd.set_option('display.max_columns', None)
print(df)
"""

# salvando em csv:
sleep(1)
print(f"\n{cores['lilas']}Convertendo seu arquivo para csv... (3/4)\033[m")
updatedA1.drop(columns=updatedA1.columns[0], axis=1, inplace=True)
updatedA1.to_csv(outputA1, index=False, encoding='utf-8')


# compactando para zip:
sleep(1)
print(f"\n{cores['lilas']}Compactando seu arquivo... (4/4)\033[m")

nome = "Jessica_Vieira"
with ZipFile(f"Teste_{nome}.zip", "w") as zip:
    zip.write(outputA1)

print(f"{cores['verde']}Arquivo csv compactado com sucesso!\033[m")
print(f"\n{cores['laranja']}Finalizando a tarefa!!\033[m\n")