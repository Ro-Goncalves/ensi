# Guia de Configuração de Dependências Python com Poetry

Este documento detalha as dependências e configurações essenciais para o desenvolvimento de projetos Python, focando em qualidade de código, testes e automação.

## Ferramentas Essenciais: Configurando e Entendendo as Dependências de Desenvolvimento

Vamos mergulhar nas ferramentas do `pyproject.toml` para o ambiente de desenvolvimento, explicando como instalá-las e para que cada uma serve.

### Como Configurar Suas Dependências (com Poetry)

O **Poetry**, é uma ferramenta robusta para gerenciar dependências em projetos Python. Para adicionar as dependências de desenvolvimento (que ficam no grupo `[tool.poetry.group.dev.dependencies]`), siga estes passos:

1.  **Localize ou Crie `pyproject.toml`**: Este arquivo é a alma da sua configuração com Poetry. Ele deve estar na pasta raiz do seu projeto. Se estiver começando um projeto novo, use `poetry new meu_projeto_novo` no terminal para que o Poetry crie a estrutura básica, incluindo o `pyproject.toml`.

2.  **Insira o Bloco de Dependências**: Abra o `pyproject.toml` e cole o bloco de dependências de desenvolvimento. Ele deve ser aninhado dentro da seção `[tool.poetry]`, se já existir, ou ser adicionado como uma nova seção. Certifique-se de que a versão do Python (`python = ">=3.x,<3.y"`) em `[tool.poetry.dependencies]` esteja alinhada com a versão que o projeto usa.

    ```toml
    # Exemplo simplificado de pyproject.toml
    [tool.poetry]
    name = "meu-projeto-python"
    version = "0.1.0"
    description = "Um projeto Python incrível!"
    authors = ["Seu Nome <email@example.com>"]
    readme = "README.md"

    [tool.poetry.dependencies]
    python = ">=3.9,<3.13" # Verifique e ajuste a versão do Python

    # --- Dependências de desenvolvimento aqui ---
    [tool.poetry.group.dev.dependencies]
    pytest = "^8.0.1"
    pytest-cov = "^4.1.0"
    blue = "^0.9.1"
    isort = "^5.13.2"
    taskipy = "^1.12.2"
    # -------------------------------------------------

    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"
    ```

3.  **Instale as Dependências**: Após salvar o `pyproject.toml`, vá até o terminal na pasta raiz do seu projeto e execute:

    ```bash
    poetry install --group dev
    ```

    Este comando instruirá o Poetry a ler seu arquivo, resolver as dependências (incluindo as de desenvolvimento) e instalá-las no ambiente virtual isolado do seu projeto. Se você quiser instalar todas as dependências, incluindo as de produção, basta usar `poetry install`.

### Para Que Serve Cada Biblioteca

Essas bibliotecas são pilares para um fluxo de trabalho de desenvolvimento Python eficiente, garantindo **qualidade, consistência e automação**.

  * **`pytest`**: Um **framework de testes** amplamente adotado e poderoso para Python.

      * **Propósito**: Simplifica a escrita de testes, tornando-a intuitiva e escalável. O `pytest` automaticamente **descobre testes** (geralmente arquivos começando com `test_` ou `_test`, ou funções/métodos começando com `test_`), oferece **mensagens de erro detalhadas** (introspecção de asserções) e suporta um vasto ecossistema de **plugins**. É a base para garantir que seu código funcione como esperado, prevenindo bugs e regressions.
      * **Detalhe para o estudo**: Ao invés de `assert False` que simplesmente indica falha, o `pytest` mostra `assert x == y` e o valor de `x` e `y`, facilitando a depuração.

  * **`pytest-cov`**: Uma extensão essencial para o `pytest` que mede a **cobertura de código**.

      * **Propósito**: Trabalha em conjunto com o `pytest` para relatar qual porcentagem do seu código-fonte é executada pelos seus testes. Uma alta cobertura de código geralmente indica que seus testes são abrangentes, cobrindo mais cenários e, consequentemente, reduzindo a probabilidade de bugs não detectados. Ele ajuda a **identificar áreas não testadas** que precisam de atenção.
      * **Detalhe para o estudo**: Não confunda cobertura com qualidade. Alta cobertura não significa ausência de bugs, apenas que mais linhas de código foram executadas pelos testes. Testes bem escritos são mais importantes do que apenas alta cobertura.

  * **`blue`**: Um **formatador de código** Python, derivado do popular Black.

      * **Propósito**: Aplica automaticamente um estilo de código consistente a todo o seu projeto. Ele cuida de detalhes como indentação, quebras de linha e espaçamento, liberando os desenvolvedores de preocupações com formatação manual. Isso garante que todo o código pareça o mesmo, **melhorando a legibilidade** e facilitando a revisão de código, pois as diferenças em *diffs* de Git serão apenas mudanças reais, não de formatação.
      * **Detalhe para o estudo**: O `blue` segue os princípios do Black: "Uncompromising code formatter." Ele tem pouquíssimas opções de configuração, forçando a consistência. A ideia é eliminar o tempo gasto discutindo sobre estilo.

  * **`isort`**: Um utilitário para **ordenar e organizar importações** em arquivos Python.

      * **Propósito**: Reorganiza automaticamente suas declarações `import` no topo dos arquivos Python, agrupando-as por tipo (por exemplo, módulos da biblioteca padrão, módulos de terceiros, módulos do seu próprio projeto) e ordenando-as alfabeticamente dentro desses grupos. Isso mantém suas importações **limpas, consistentes e fáceis de navegar**.
      * **Detalhe para o estudo**: A ordenação padrão geralmente é: standard library -\> third-party -\> first-party/local. Isso ajuda a identificar rapidamente de onde vem cada dependência.

  * **`taskipy`**: Um **executor de tarefas** simples e direto para projetos Python.

      * **Propósito**: Permite definir e executar comandos personalizados (tarefas) diretamente do seu `pyproject.toml`. Em vez de digitar longos comandos no terminal (como `pytest --cov=meu_modulo tests/`), você pode definir uma tarefa abreviada (ex: `test`) e executá-la com `poetry run task test`. Isso **agiliza e padroniza a execução de operações comuns** de desenvolvimento, como rodar testes, linters, ou scripts de build, tornando o onboarding de novos membros da equipe mais fácil.
      * **Detalhe para o estudo**: `taskipy` é uma alternativa leve a ferramentas como `Makefile` para projetos Python, sendo mais Python-centric.

## Harmonizando o Código: A Configuração do `isort`

A seção `[tool.isort]` no seu `pyproject.toml` (ou em um arquivo `.isort.cfg` ou `setup.cfg`) controla como o `isort` organiza suas importações.

```toml
[tool.isort]
profile = "black"
line_length = 79
```

### O Que Essa Configuração Significa

  * **`profile = "black"`**

      * **Significado**: Esta é a opção mais crítica. Ela define um conjunto predefinido de regras para o `isort` que são **totalmente compatíveis com o estilo de formatação do Black**. O Black é um formatador de código "opinionado", o que significa que ele tem suas próprias regras rígidas de estilo. Ao usar `profile = "black"`, você garante que o `isort` organizará suas importações de uma maneira que o Black não irá reverter ou considerar inconsistente. Isso cria uma **sinergia perfeita** entre as duas ferramentas: `isort` cuida das importações, e `blue` (ou Black) cuida do resto do código, sem conflitos de estilo.
      * **Detalhe para o estudo**: A compatibilidade entre formatadores é essencial para evitar que ferramentas "briguem" por mudanças de estilo, resultando em *commits* desnecessários de formatação.

  * **`line_length = 79`**

      * **Significado**: Esta opção especifica o **comprimento máximo da linha** que o `isort` deve tentar respeitar ao formatar suas importações. Se uma linha de importação exceder 79 caracteres, o `isort` tentará dividi-la em várias linhas para se ajustar a esse limite, aumentando a legibilidade.
      * **Por que 79?**: Este número é o limite de linha **recomendado pela PEP 8**, o guia de estilo oficial para código Python. Embora o Black (e, por extensão, o `blue`) use um padrão de 88 caracteres, manter 79 para importações é uma prática conservadora que garante alta legibilidade, especialmente em terminais ou ao visualizar diferenças de código.
      * **Detalhe para o estudo**: A PEP 8 recomenda 79 caracteres para código e 72 para docstrings e comentários. O limite de 88 do Black é uma escolha pragmática para acomodar códigos mais modernos e complexos sem quebrar linhas excessivamente.

### Outras Opções Comuns e Úteis do `isort`

O `isort` oferece diversas opções para personalizar a ordenação, mas a simplicidade costuma ser a melhor escolha.

1.  **`skip_glob` e `skip_paths` (Ignorar Arquivos/Pastas)**

      * **Uso**: Exclui arquivos ou diretórios específicos do processamento do `isort`. Útil para código gerado, bibliotecas de terceiros ou pastas de testes que você não quer que sejam reformatadas.
      * **Exemplo**:
        ```toml
        [tool.isort]
        # ... outras configurações
        skip_glob = ["**/migrations/*.py", "docs/*"] # Ignora arquivos em 'migrations' e tudo na pasta 'docs'
        skip_paths = ["venv/", "node_modules/"] # Ignora pastas inteiras
        ```
      * **Detalhe para o estudo**: Use `skip_glob` para padrões de arquivos (glob patterns) e `skip_paths` para caminhos de diretórios literais.

2.  **`known_first_party` e `known_third_party` (Definir Grupos de Módulos)**

      * **Uso**: Ajuda o `isort` a classificar corretamente seus módulos. `known_first_party` são módulos que fazem parte do seu próprio projeto, e `known_third_party` são módulos de bibliotecas externas que o `isort` pode não reconhecer automaticamente.
      * **Exemplo**:
        ```toml
        [tool.isort]
        # ... outras configurações
        known_first_party = ["meu_app", "shared_components"] # Define estes como módulos do seu projeto
        ```
      * **Detalhe para o estudo**: Ao classificar corretamente, o `isort` pode agrupar suas importações de forma mais lógica, melhorando a estrutura visual.

3.  **`force_single_line = true` (Forçar Importações em Linha Única)**

      * **Uso**: Se preferir que todas as importações (mesmo as múltiplas de um único módulo) fiquem em uma única linha.
      * **Exemplo**:
        ```toml
        [tool.isort]
        # ... outras configurações
        force_single_line = true # `from os import path, environ` em vez de múltiplas linhas
        ```
      * **Detalhe para o estudo**: Embora possa economizar linhas, pode criar linhas excessivamente longas se houver muitas importações, contrariando o `line_length`. Use com cautela.

4.  **`include_trailing_comma = true` (Vírgula Final em Importações Multilinhas)**

      * **Uso**: Adiciona uma vírgula após o último item em importações que se estendem por várias linhas.
      * **Exemplo**:
        ```python
        # Antes (sem vírgula final):
        # from meu_modulo import (
        #     funcao_a,
        #     funcao_b
        # )

        # Com include_trailing_comma = true:
        # from meu_modulo import (
        #     funcao_a,
        #     funcao_b, # Vírgula adicionada
        # )
        ```
      * **Detalhe para o estudo**: Essa prática é comum e recomendada (inclusive pelo Black) porque facilita a adição/remoção de itens sem alterar linhas já existentes e melhora a clareza em *diffs* de controle de versão.

## Garantindo a Qualidade: A Configuração do Pytest

A seção `[tool.pytest.ini_options]` no seu `pyproject.toml` (ou em um arquivo `pytest.ini` ou `setup.cfg`) permite configurar o comportamento do Pytest.

```toml
[tool.pytest.ini_options]
pythonpath = "."
addopts = "--doctest-modules"
```

### O Que Essa Configuração Significa

  * **`pythonpath = "."`**

      * **Significado**: Esta opção adiciona o diretório atual (que geralmente é a raiz do seu projeto) ao **`PYTHONPATH`** que o Pytest usa ao executar seus testes.
      * **Propósito**: Essencial para que as **importações internas** do seu projeto funcionem corretamente durante a execução dos testes. Quando você tem uma estrutura de projeto como `seu_projeto/meu_modulo/arquivo.py` e um teste em `seu_projeto/tests/test_arquivo.py` que importa `from meu_modulo.arquivo import minha_funcao`, o Python precisa saber onde encontrar `meu_modulo`. Ao adicionar `.` (a raiz do projeto) ao `PYTHONPATH`, você garante que o Pytest encontrará todos os seus módulos internos. Sem isso, você enfrentaria erros como `ModuleNotFoundError`.
      * **Detalhe para o estudo**: O `PYTHONPATH` é uma variável de ambiente que diz ao interpretador Python onde procurar módulos. `.` representa o diretório atual.

  * **`addopts = "--doctest-modules"`**

      * **Significado**: Este argumento é adicionado automaticamente à linha de comando do Pytest sempre que você o executa.
      * **Propósito**: A opção `--doctest-modules` instrui o Pytest a **encontrar e executar os "doctests"** que estão embutidos nas `docstrings` (strings de documentação) dos seus módulos, funções e classes.
          * **Doctests**: São exemplos de uso de código que você inclui diretamente nas docstrings. Eles se parecem com interações de console Python (com `>>>` para comandos e a linha seguinte para a saída esperada). O Pytest executa esses exemplos e verifica se a saída real corresponde à saída esperada na docstring.
          * **Benefícios**:
              * **Documentação Viva e Testável**: Seus exemplos de uso na documentação se tornam automaticamente testes, garantindo que a documentação esteja sempre atualizada e que os exemplos funcionem.
              * **Testes Leves**: Para funções simples, um doctest pode ser suficiente, eliminando a necessidade de um arquivo de teste `.py` separado.
      * **Detalhe para o estudo**: Doctests são ótimos para testar pequenas unidades de código e para garantir que sua documentação esteja precisa. Para lógica mais complexa, testes dedicados no `pytest` (usando `assert`) são mais adequados.

### Outras Opções Comuns e Úteis do Pytest

O Pytest é incrivelmente flexível. Aqui estão mais algumas opções que podem refinar seu processo de teste:

1.  **`testpaths` (Onde Procurar por Testes)**

      * **Uso**: Define quais diretórios o Pytest deve escanear em busca de arquivos de teste. Isso pode acelerar a descoberta de testes em projetos grandes ou ajudar a organizar os testes em subdiretórios específicos.
      * **Exemplo**:
        ```toml
        [tool.pytest.ini_options]
        # ... outras configurações
        testpaths = [
            "tests",         # Procura testes na pasta 'tests'
            "app/modules",   # Também procura em 'app/modules' se houver testes lá
        ]
        ```
      * **Detalhe para o estudo**: O padrão do Pytest é procurar por `test_*.py` ou `*_test.py` em todas as subpastas, mas `testpaths` restringe essa busca.

2.  **`norecursedirs` (Diretórios para Ignorar na Busca de Testes)**

      * **Uso**: Lista diretórios que o Pytest deve explicitamente ignorar ao procurar por testes. Isso é útil para pastas como ambientes virtuais, caches de build, etc., que podem conter arquivos `.py` mas não são testes.
      * **Exemplo**:
        ```toml
        [tool.pytest.ini_options]
        # ... outras configurações
        norecursedirs = [
            ".git",
            "build",
            "dist",
            "venv*", # Ignora qualquer pasta que comece com 'venv'
            "*.egg-info"
        ]
        ```
      * **Detalhe para o estudo**: O Pytest já tem uma lista padrão de diretórios para ignorar, mas esta opção permite que você adicione mais.

3.  **`filterwarnings` (Controle de Warnings)**

      * **Uso**: Permite que você controle como os warnings (avisos) são tratados durante a execução dos testes. Você pode elevá-los a erros (fazendo o teste falhar) ou silenciá-los.
      * **Exemplo**:
        ```toml
        [tool.pytest.ini_options]
        # ... outras configurações
        filterwarnings = [
            "error::DeprecationWarning",    # Transforma 'DeprecationWarning' em erro
            "ignore::UserWarning:some_lib"  # Ignora 'UserWarning' específico de 'some_lib'
        ]
        ```
      * **Detalhe para o estudo**: Transformar warnings em erros é uma prática rigorosa em Integração Contínua (CI) para garantir que seu código não esteja usando APIs obsoletas.

4.  **`markers` (Definição de Marcadores Personalizados)**

      * **Uso**: Permite que você defina marcadores `@pytest.mark.<nome>` personalizados para categorizar seus testes (ex: `@pytest.mark.web`, `@pytest.mark.slow`). Você pode então executar apenas testes com marcadores específicos usando `pytest -m <nome_do_marcador>`.
      * **Exemplo**:
        ```toml
        [tool.pytest.ini_options]
        # ... outras configurações
        markers = [
            "web: marca testes que fazem requisições de rede",
            "slow: marca testes que demoram para executar (ex: integração com DB)"
        ]
        ```
      * **Detalhe para o estudo**: Marcadores são excelentes para organizar e executar subconjuntos de testes, como rodar testes rápidos em cada *commit* e testes lentos apenas durante a noite.

## Para o LLM

Este é um resumo conciso das dependências e configurações para um modelo de linguagem que automatizará tarefas relacionadas a um projeto Python.

**Projeto Python**: Configurações de dependências de desenvolvimento usando **Poetry** em `pyproject.toml`.

  * **`[tool.poetry.group.dev.dependencies]`**:

      * **`pytest`**: Framework de testes Python. Descobre e executa testes (`test_*.py`, `test_*()`). Essencial para validar a lógica do código.
      * **`pytest-cov`**: Plugin para `pytest`. Mede a **cobertura de código** dos testes, indicando a porcentagem de código exercitada. Usado para identificar áreas não testadas.
      * **`blue`**: Formatador de código Python. Padroniza o estilo do código automaticamente (indentação, quebras de linha). Garante **consistência visual** e minimiza discussões de estilo.
      * **`isort`**: Ferramenta de ordenação de importações. Organiza as declarações `import` em grupos e ordem alfabética. Promove **clareza e consistência** nas importações.
      * **`taskipy`**: Executor de tarefas Python. Permite definir e rodar comandos personalizados (scripts, testes, linters) via `poetry run task <nome_da_tarefa>`. **Automatiza fluxos de trabalho** comuns.

  * **`[tool.isort]`**: Configuração de `isort`.

      * **`profile = "black"`**: Define regras de ordenação de importações **compatíveis com o formatador Black**. Garante que `isort` e `blue` (ou Black) não criem conflitos de estilo.
      * **`line_length = 79`**: Limite de caracteres por linha para importações. Segue a **PEP 8** para legibilidade.
      * **Outras opções**: `skip_glob`/`skip_paths` (ignorar arquivos/pastas), `known_first_party` (classificar módulos próprios), `include_trailing_comma` (vírgula em multi-linhas).

  * **`[tool.pytest.ini_options]`**: Configuração de `pytest`.

      * **`pythonpath = "."`**: Adiciona a raiz do projeto ao `PYTHONPATH` para que o Pytest possa encontrar **módulos internos** durante os testes.
      * **`addopts = "--doctest-modules"`**: Ativa a execução de **doctests** (testes embutidos em `docstrings`). Transforma exemplos de documentação em testes vivos.
      * **Outras opções**: `testpaths` (diretórios de testes), `norecursedirs` (ignorar diretórios), `filterwarnings` (controle de warnings), `markers` (categorização de testes).

**Objetivo Geral**: Estas ferramentas estabelecem uma base para **desenvolvimento robusto**, garantindo código **limpo, testado e com tarefas automatizadas**, facilitando a manutenção e colaboração.
