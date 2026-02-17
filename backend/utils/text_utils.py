# -*- coding: utf-8 -*-
"""
Módulo de utilitários de texto.
"""
import unicodedata

def normalizar_texto(texto):
    """
    Normaliza o texto removendo acentos, convertendo para minúsculas e tratando hifens.
    
    Args:
        texto (str): Texto a ser normalizado
        
    Returns:
        str: Texto normalizado
    """
    if not texto:
        return ""
    # Normaliza para forma NFD e remove diacríticos
    texto_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', texto)
                              if not unicodedata.combining(c))
    # Remove hifens e substitui por espaços
    texto_sem_hifens = texto_sem_acentos.replace('-', ' ')
    # Converte para minúsculas
    return texto_sem_hifens.lower()

def diferenca_minima(str1, str2):
    """
    Verifica se duas strings diferem apenas por preposições ou por um caractere.
    
    Args:
        str1 (str): Primeira string
        str2 (str): Segunda string
        
    Returns:
        bool: True se a diferença for mínima, False caso contrário
    """
    # Lista de preposições comuns em nomes de cidades
    preposicoes = ['de', 'da', 'do', 'das', 'dos']
    
    # Dividir as strings em palavras
    palavras1 = str1.split()
    palavras2 = str2.split()
    
    # Verificar diferença de um único caractere entre as strings completas
    if len(str1) == len(str2):
        difs = sum(1 for a, b in zip(str1, str2) if a != b)
        if difs == 1:
            return True
    elif abs(len(str1) - len(str2)) == 1:  # Uma string tem um caractere a mais
        # Verificar se removendo um caractere de qualquer posição da string maior, obtemos a menor
        if len(str1) > len(str2):
            return any(str1[:i] + str1[i+1:] == str2 for i in range(len(str1)))
        else:
            return any(str2[:i] + str2[i+1:] == str1 for i in range(len(str2)))
    
    # Se a diferença for apenas uma preposição
    if abs(len(palavras1) - len(palavras2)) <= 1:
        # Caso 1: str2 tem uma preposição a mais
        if len(palavras2) == len(palavras1) + 1:
            for i in range(len(palavras2)):
                temp = palavras2.copy()
                temp.pop(i)
                if temp == palavras1 and palavras2[i] in preposicoes:
                    return True
        
        # Caso 2: str1 tem uma preposição a mais
        elif len(palavras1) == len(palavras2) + 1:
            for i in range(len(palavras1)):
                temp = palavras1.copy()
                temp.pop(i)
                if temp == palavras2 and palavras1[i] in preposicoes:
                    return True
        
        # Caso 3: mesmo número de palavras, mas uma preposição diferente
        elif len(palavras1) == len(palavras2):
            difs = 0
            for i in range(len(palavras1)):
                if palavras1[i] != palavras2[i]:
                    if palavras1[i] in preposicoes or palavras2[i] in preposicoes:
                        difs += 1
                    else:
                        difs += 2  # Diferença não é preposição
            if difs <= 1:  # Apenas uma preposição diferente
                return True
    
    return False
