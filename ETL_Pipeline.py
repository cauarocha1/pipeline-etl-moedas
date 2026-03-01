import requests
import pandas as pd
import sqlite3
from datetime import datetime

def executar_pipeline_dados():
    
   
    # Script de ETL: Extrai dados de API, transforma com Pandas 
    # e carrega em um banco SQLite local.

    
    print("--- Iniciando Extração ---")
    # 1. EXTRAÇÃO (Extract)
    # Consumindo API pública de cotações
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Verifica se a requisição deu erro
        data = response.json()
    except Exception as e:
        print(f"Erro ao acessar API: {e}")
        return

    # 2. TRANSFORMAÇÃO (Transform)
    print("--- Iniciando Transformação ---")
    dados_processados = []
    
    for chave, info in data.items():
        dados_processados.append({
            "par_moedas": info["name"],
            "sigla": info["code"],
            "valor_compra": float(info["bid"]),
            "valor_venda": float(info["ask"]),
            "data_extracao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    df = pd.DataFrame(dados_processados)
    
    # 3. CARGA (Load)
    print("--- Iniciando Carga no Banco de Dados (INSERTS) ---")
    # Criando conexão com banco SQLite (arquivo será criado automaticamente)
    conn = sqlite3.connect("dados_estagio.db")
    cursor = conn.cursor()
    
    # Criando a tabela caso ela não exista
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_cotacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            par_moedas TEXT,
            sigla TEXT,
            valor_compra REAL,
            valor_venda REAL,
            data_extracao TEXT
        )
    ''')

    # Executando os INSERTS para cada linha do DataFrame
    for index, linha in df.iterrows():
        cursor.execute('''
            INSERT INTO tb_cotacoes (par_moedas, sigla, valor_compra, valor_venda, data_extracao)
            VALUES (?, ?, ?, ?, ?)
        ''', (linha['par_moedas'], linha['sigla'], linha['valor_compra'], linha['valor_venda'], linha['data_extracao']))
    
    # Commit para salvar as alterações
    conn.commit()
    
    # Demonstração do resultado no console
    print("\n[SUCESSO] Dados inseridos na tabela 'tb_cotacoes'.")
    print("Visualizando os últimos registros inseridos:")
    df_verificacao = pd.read_sql_query("SELECT * FROM tb_cotacoes ORDER BY id DESC LIMIT 5", conn)
    print(df_verificacao)
    
    conn.close()
    print("\n--- Pipeline Finalizado ---")

if __name__ == "__main__":
    executar_pipeline_dados()