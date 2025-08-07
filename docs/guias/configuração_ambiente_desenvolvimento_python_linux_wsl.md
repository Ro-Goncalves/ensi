# Guia de Configuração de Ambiente de Desenvolvimento Linux (WSL)

Este guia documenta o processo de configuração de um ambiente de desenvolvimento no Linux, incluindo a criação e gerenciamento de usuários, instalação de ferramentas essenciais de Python e a configuração de projetos com o Poetry.

## Gerenciando Usuários e Senhas

### Redefinir a senha do usuário

Se você precisar redefinir a senha do seu usuário (por exemplo, `rodrigo`), você pode usar o comando `passwd` como `root`.

1.  Acesse o terminal com privilégios de `root` (usando `sudo -i` ou `sudo su`).
2.  Use o comando `passwd` seguido do nome do usuário.
    ```bash
    passwd rodrigo
    ```
3.  Digite e confirme a nova senha quando solicitado.

### Trocar de usuário

Para sair do usuário `root` e fazer login como outro usuário (`rodrigo`), use o comando `su`.

```bash
su - rodrigo
```

A opção `-` garante que você inicie uma nova sessão com todas as configurações do usuário `rodrigo`.

## Preparando o Ambiente Python

### Instalar o `pip` e o `venv`

Para que o seu usuário possa instalar pacotes Python e criar ambientes virtuais, é necessário instalar o `pip` e o pacote `venv`.

```bash
sudo apt update
sudo apt install python3-pip python3.8-venv
```

  * `python3-pip`: Instala o gerenciador de pacotes pip para Python 3.
  * `python3.8-venv`: Instala o módulo necessário para criar ambientes virtuais com o `venv`.

## Configurando Ferramentas de Gerenciamento de Projetos

### Instalar o `pipx`

O **pipx** é uma ferramenta para instalar e gerenciar executáveis de Python em ambientes isolados. Isso é ideal para ferramentas como o Poetry.

1.  Instale o `pipx` usando o `pip`.
    ```bash
    python3 -m pip install --user pipx
    ```
2.  Adicione o `pipx` ao seu `PATH`.
    ```bash
    python3 -m pipx ensurepath
    ```
    Feche e reabra o terminal, ou execute `source ~/.bashrc` para aplicar as mudanças.

### Instalar o Poetry

Com o `pipx` configurado, você pode instalar o Poetry de forma limpa e isolada.

```bash
pipx install poetry
```

## Gerenciando Múltiplas Versões do Python com `pyenv`

Para ter a flexibilidade de usar diferentes versões do Python em cada projeto, use o `pyenv`.

1.  **Instale as dependências** de compilação.

    ```bash
    sudo apt update
    sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils tk-dev \
    libffi-dev liblzma-dev python3-openssl git
    ```

2.  **Instale o `pyenv`** usando o script de instalação.

    ```bash
    curl https://pyenv.run | bash
    ```

3.  **Configure o `pyenv`** no seu shell (`~/.bashrc`).

    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init --path)"\nfi' >> ~/.bashrc
    source ~/.bashrc
    ```

4.  **Instale e use uma versão do Python**.

      * Liste as versões disponíveis: `pyenv install --list`.
      * Instale a versão desejada (ex: `3.10.0`): `pyenv install 3.10.0`.
      * Defina a versão para o projeto: navegue até a pasta do projeto e use o comando `pyenv local`.
        ```bash
        cd /home/rodrigo/projetos/ensi
        pyenv local 3.10.0
        ```

## Configurando o Poetry na Pasta do Projeto

Para que o Poetry crie o ambiente virtual dentro da sua pasta de projeto (`.venv`), configure a opção `in-project`.

```bash
poetry config virtualenvs.in-project true
```

Após essa configuração, use o `poetry install` dentro da pasta do projeto para criar o ambiente virtual com a versão de Python que você definiu com o `pyenv`.
