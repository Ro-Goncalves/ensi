import os
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class SubstackDownloader:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

    def fetch_content(self, url):
        """
        Busca o conteúdo HTML de uma URL ou de um arquivo local.

        Se a URL começar com 'file://', tenta ler o conteúdo de um arquivo local.
        Caso contrário, tenta buscar o conteúdo de uma URL via HTTP.

        Parameters:
            url (str): A URL ou o caminho do arquivo (prefixado com 'file://').

        Returns:
            str or None: O conteúdo HTML como string se a operação for bem-sucedida,
                        ou None em caso de erro.
        """
        if url.startswith('file://'):
            file_path = url[len('file://') :]
            if not os.path.isabs(
                file_path
            ):      # Garante que o caminho é absoluto para segurança
                file_path = os.path.abspath(file_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            except FileNotFoundError:
                print(f"Erro: Arquivo local não encontrado em '{file_path}'")
                return None
            except Exception as e:
                print(f"Erro ao ler arquivo local '{file_path}': {e}")
                return None
        else:
            try:
                response = requests.get(url, headers=self.headers, timeout=30)
                response.raise_for_status()     # Lança HTTPError para respostas de erro (4xx ou 5xx)
                return response.text
            except requests.RequestException as e:
                print(f"Erro ao buscar conteúdo da URL '{url}': {e}")
                return None
