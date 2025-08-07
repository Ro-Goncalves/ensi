# Guia de Referência de Testes: Doctests vs. Testes Unitários

Este guia ajuda a decidir a melhor abordagem de teste para diferentes partes do seu código, garantindo que a documentação seja precisa e que a lógica seja robusta.

## **Doctests: Para Exemplos de Código na Documentação**

Use **doctests** para validar exemplos simples e diretos de uso. Eles são mais sobre **documentação viva** do que sobre testes completos de cobertura.

**O que testar com Doctests:**

  * **Funções e Métodos de Propósito Único:** Ideal para funções que recebem uma entrada e produzem uma saída previsível, sem efeitos colaterais.
      * `somar(2, 3)` -\> `5`
      * `formatar_nome("joão")` -\> `"João"`
  * **Aparência da Saída:** Use-o para garantir que a saída de uma função `print()` ou a representação de um objeto (`__repr__`) tenha a formatação esperada.
      * `print(saudacao("Maria"))` -\> `Olá, Maria!`
  * **Tutoriais Simples:** Servem como pequenos tutoriais dentro da `docstring`, mostrando rapidamente como uma função funciona. São úteis para funções com lógica trivial.

**Exemplo:**

```python
def elevar_ao_quadrado(numero):
    """
    Retorna o quadrado de um número.

    >>> elevar_ao_quadrado(4)
    16
    >>> elevar_ao_quadrado(0)
    0
    >>> elevar_ao_quadrado(-2)
    4
    """
    return numero ** 2
```

**Quando evitar:**

  * Qualquer teste que envolva recursos externos (arquivos, banco de dados, rede).
  * Testes que precisam de setup complexo ou de simular comportamentos externos (mocks).
  * Testes com lógica de controle (loops, condicionais) ou que exigem mais de uma ou duas linhas de código para serem executados.

## **Testes Unitários (`pytest`): Para a Lógica Principal e Complexidade**

Use **testes unitários** (com um framework como o `pytest`) para testar a lógica do seu código de forma aprofundada, garantindo sua **robustez, confiabilidade e estabilidade**. Eles são a base da sua suíte de testes.

**O que testar com Testes Unitários:**

  * **Efeitos Colaterais:** Métodos que alteram o estado de um objeto, escrevem em um arquivo ou interagem com um banco de dados. Testes unitários com **fixtures** (`pytest.fixture`) são ideais para preparar o ambiente antes do teste e limpá-lo depois.
  * **Casos de Borda e Erro:** Cenários que podem quebrar sua aplicação, como entradas inválidas, valores nulos (`None`), strings vazias, ou erros de I/O.
      * Testar se uma função levanta a exceção correta (`pytest.raises`).
  * **Dependências Externas:** Funções que se comunicam com a internet, APIs externas ou outros serviços. Use **mocks** para simular as respostas dessas dependências, garantindo que seus testes sejam rápidos e isolados do mundo exterior.
  * **Lógica de Negócios Complexa:** Testes que cobrem múltiplos cenários com diferentes entradas, garantindo que sua lógica de negócios funcione como esperado em todas as situações.
  * **Classes e Interações de Objetos:** Testar o comportamento de uma classe e como seus métodos interagem entre si.

**Exemplo:**

```python
import pytest
from meu_modulo import DatabaseConnector, MeuAplicativo

@pytest.fixture
def mock_db_connection(mocker):
    # Usa um mock para simular a conexão com o banco de dados
    return mocker.patch.object(DatabaseConnector, 'connect')

def test_get_user_by_id_success(mock_db_connection):
    # Configura o mock para retornar um valor específico
    mock_db_connection.return_value = {"id": 1, "name": "Alice"}
    
    app = MeuAplicativo()
    user = app.get_user(1)
    
    assert user["name"] == "Alice"
    mock_db_connection.assert_called_once_with(1)

def test_get_user_by_id_not_found(mock_db_connection):
    # Configura o mock para simular que o usuário não foi encontrado
    mock_db_connection.return_value = None
    
    app = MeuAplicativo()
    user = app.get_user(999)
    
    assert user is None
```

## **Resumo da Estratégia**

| Característica | Doctest | Teste Unitário (`pytest`) |
| :--- | :--- | :--- |
| **Finalidade** | Documentação e exemplos vivos | Cobertura e validação de lógica |
| **Complexidade** | Simples, direto, sem efeitos colaterais | Cenários complexos, de erro e de borda |
| **Setup/Teardown** | Inexistente (criação de arquivos temporários polui a docstring) | Uso de **fixtures** para ambiente controlado |
| **Dependências** | Evita dependências externas | Usa **mocks** para isolar e simular |
| **Depuração** | Saídas simples, pode ser difícil de depurar | Saídas detalhadas e com informações sobre a falha |
| **Onde Fica** | Dentro da `docstring` do código | Em arquivos separados na pasta `tests/` |

**Conclusão:** Use **doctests** como uma camada leve de verificação de sanidade para sua documentação. E use **testes unitários** como a sua principal ferramenta para garantir que seu código principal seja confiável e robusto. Combinar os dois é a melhor prática para um projeto de alta qualidade.