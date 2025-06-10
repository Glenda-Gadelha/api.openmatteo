import pandas as pd
import requests
from datetime import datetime

#********* Criação de Funções *****************#

def extrair_dados():

	url = "https://api.open-meteo.com/v1/forecast"

	params = {
		"latitude": -23.6073924,
		"longitude": -46.715247115,
		"hourly": ["temperature_2m", "precipitation_probability"],
		"timezone": "America/Sao_Paulo"
	}

	try:
		print("Iniciando a extração dos dados.")

		response = requests.get(url, params=params)
		
		if response.status_code != 200:
			print(f"Erro na extração dos dados. Status: {response.status_code}")
		else:
			print("Requisição bem sucessida!")
			return response.json()

	except Exception as e:
		print(f"Erro ao extrair dados. {e}")


def create_df(response):
	try:
		try:
			print("Iniciando processo de extração de dados do JSON")
			times = response.get('hourly', {}).get('time', -1)
			precip_probs = response.get('hourly', {}).get('precipitation_probability', -1)
			latitude = response.get('latitude', -1)
			longitude = response.get('longitude', -1)
			print("Processo de extração de dados do JSON finalizado")
		except:
			print("Erro na extração dos dados do JSON.")

		try:
			print("Criando DataFrame.")
			df = pd.DataFrame({
			'latitude': latitude,
			'longitude': longitude,
			'time': pd.to_datetime(times),
			'precipitation_probability': precip_probs
			})

			df['time'] = pd.to_datetime(df['time']).dt.strftime('%d/%m/%Y')

			print("DataFrame criado com sucesso.")
			return df
		except:
			print("Erro ao gerar DataFrame.")
	except Exception as e:
		print(f"Erro ao gerar DF. {e}")




response = extrair_dados()
df = create_df(response)
print(df)