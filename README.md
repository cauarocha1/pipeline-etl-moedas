# 📈 Pipeline ETL de Moedas
Automação de extração, transformação e carga de dados financeiros para análise histórica.

Este repositório contém um projeto de Engenharia de Dados focado no fluxo ETL (Extract, Transform, Load). O script consome dados em tempo real de uma API de economia, processa as informações utilizando Python/Pandas e realiza a persistência em um banco de dados relacional SQLite.

## Objetivo
O projeto visa demonstrar competências técnicas fundamentais em Engenharia de Dados, como o consumo de APIs REST, manipulação de dados semi-estruturados (JSON), tipagem de dados e persistência via comandos SQL.

## Funcionalidades principais
- **Extração automatizada:** Coleta de cotações em tempo real (Dólar, Euro e Bitcoin) via AwesomeAPI.
- **Transformação com Pandas:** Conversão de dados brutos para formato tabular e limpeza de campos.
- **Normalização:** Conversão de strings para tipos numéricos (float) e tratamento de timestamps.
- **Carga (Load):** Persistência dos dados em banco SQLite utilizando comandos SQL estruturados.
- **Logs de Execução:** Monitoramento das etapas do pipeline diretamente no console.

## Stack técnica
- **Python 3.10+**
- **Pandas:** Manipulação e estruturação de dados.
- **Requests:** Consumo de API REST.
- **SQLite3:** Banco de dados relacional embarcado.
- **Datetime:** Tratamento de janelas temporais e auditoria de carga.

## Requisitos
- Python 3.8+
- pip (Gerenciador de pacotes)

## Autor
Cauã Rocha
