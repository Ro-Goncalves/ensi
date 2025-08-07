# tests/test_substack_downloader.py
import os
import tempfile

import pytest

from ensi.substack.substack_downloader import SubstackDownloader


# Fixture para criar e limpar o arquivo HTML de teste
@pytest.fixture
def local_html_file():
    # Conteúdo HTML de exemplo
    html_content = """
    <!DOCTYPE html>
    <html>
    <head><title>Teste Local</title></head>
    <body>
        <article>
            <h1>Título do Artigo Teste</h1>
            <p>Este é um parágrafo de teste.</p>
        </article>
    </body>
    </html>
    """
    # Cria um arquivo temporário
    with tempfile.NamedTemporaryFile(
        mode='w', delete=False, encoding='utf-8', suffix='.html'
    ) as f:
        f.write(html_content)
        file_path = f.name

    # O 'yield' faz com que o arquivo exista durante o teste
    yield file_path

    # Código após o 'yield' é executado para limpeza (teardown)
    os.remove(file_path)


# Teste para fetch_content de um arquivo local
def test_fetch_content_local_file(local_html_file):
    downloader = SubstackDownloader()
    # Formata o caminho para ser reconhecido pela função
    local_url = f'file://{local_html_file}'
    content = downloader.fetch_content(local_url)

    assert content is not None
    assert 'Título do Artigo Teste' in content
    assert 'Este é um parágrafo de teste.' in content


# Teste para fetch_content com uma URL HTTP válida (exemplo.com)
# Requer que 'requests_mock' seja instalado para mocks avançados,
# mas um teste simples contra example.com pode ser útil.
def test_fetch_content_http_success():
    downloader = SubstackDownloader()
    # Usamos uma URL que é garantida para responder com HTML básico
    url = 'https://example.com'
    content = downloader.fetch_content(url)

    assert content is not None
    assert 'Example Domain' in content      # Texto esperado de example.com
    assert '<!doctype html>' in content


# Teste para fetch_content com URL inválida (simula erro de rede/HTTP 404)
def test_fetch_content_http_error():
    downloader = SubstackDownloader()
    # Uma URL que certamente resultará em 404 ou erro de conexão
    url = 'https://httpstat.us/404'
    content = downloader.fetch_content(url)

    assert content is None      # Esperamos None em caso de erro


# Teste para arquivo local não encontrado
def test_fetch_content_local_file_not_found():
    downloader = SubstackDownloader()
    non_existent_path = 'file:///path/to/non_existent_file.html'
    content = downloader.fetch_content(non_existent_path)

    assert content is None
