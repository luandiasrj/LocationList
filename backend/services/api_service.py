# -*- coding: utf-8 -*-
"""
Módulo de serviço para API QWeather (Async).
"""
import aiohttp

async def buscar_cidade(cidade, estado, api_key, session):
    """
    Busca uma cidade na API QWeather de forma assíncrona.
    
    Args:
        cidade (str): Nome da cidade
        estado (str): Sigla ou nome do estado
        api_key (str): Chave da API QWeather
        session (aiohttp.ClientSession): Sessão HTTP para reutilização
        
    Returns:
        dict: Dados da resposta (status_code, json)
    """
    url = f"https://geoapi.qweather.com/v2/city/lookup?location={cidade}&key={api_key}&range=br&lang=pt"
    
    try:
        async with session.get(url) as response:
            status_code = response.status
            if status_code == 200:
                data = await response.json()
            else:
                data = {}
            return {"status_code": status_code, "data": data}
    except Exception as e:
        return {"status_code": 500, "data": {}, "error": str(e)}
