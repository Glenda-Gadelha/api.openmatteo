# Extração de Dados Meteorológicos com Python

Este projeto consiste em um script Python que extrai dados meteorológicos da API Open-Meteo e transforma esses dados em um DataFrame organizado com pandas. O foco é obter dados horários de temperatura e probabilidade de precipitação para uma localização específica.

---

## Tecnologias Utilizadas

- Python 3
- pandas
- requests

---

## Funcionalidades

- Realiza requisição à API Open-Meteo para obter dados meteorológicos horários.
- Extrai informações de latitude, longitude, horários e probabilidade de precipitação.
- Organiza os dados em um DataFrame pandas.
- Formata a data para o formato `dd/mm/yyyy`.

---

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/forecast.py.git
   ```
2. Instale as dependências:
   ```bash
   pip install pandas requests
   ```
3. Execute o script:
   ```bash
   python forecast.py
   ```
4. O script irá imprimir o DataFrame com os dados formatados.

---

## Observações

- A localização configurada no script é fixa (latitude -23.6073924, longitude -46.715247115).
- A API utilizada não requer autenticação.
- O horário retornado é ajustado para o fuso horário "America/Sao_Paulo".

---
