from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# encontrando e lendo o arquivo csv
caminho_csv = './src/operadoras/Relatorio_cadop.csv'
tabela = pd.read_csv(caminho_csv, sep=',', encoding='latin1')

# criando uma coluna da razão social em maiúsculo
tabela['Razao_Social'] = tabela['Razao_Social'].str.upper()

@app.route("/")
def home():
    return "Olá, seja bem-vindo(a)! Para buscar informações adicione: '/buscar?q=NOME_DA_OPERADORA' ao final da URL acima"

# definindo uma rota no método GET para encontrar dados no sistema
@app.route("/buscar", methods=['GET'])
def SearchOperadora():
    query = request.args.get('q', '').upper()
    
    # caso não encontre o parâmetro buscado, retorna vazio
    if not query:
        return jsonify([])

    # Se encontrar o valor buscado, retorna os 15 primeiros encontrados
    else:
        find = tabela[tabela['Razao_Social'].str.contains(query)].head(10)

        # resposta do que foi encontrado pelo nome pesquisado
        response = find[['Nome_Fantasia', "Registro_ANS", 'Razao_Social']].to_dict(orient='records')
        return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

