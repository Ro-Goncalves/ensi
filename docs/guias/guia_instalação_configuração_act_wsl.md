# Guia de Instalação e Configuração do `act` no WSL

Este guia foi criado para instalar o `act`, a ferramenta que permite rodar workflows do GitHub Actions localmente no WSL (Windows Subsystem for Linux), resolvendo os principais problemas de configuração e permissão.

#### 1\. Pré-requisitos

O `act` depende do Docker para funcionar. Certifique-se de que o Docker Desktop está instalado e configurado corretamente para o WSL.

1.  **Instale o Docker Desktop para Windows.**
2.  Abra o **Docker Desktop** e vá em **Settings \> Resources \> WSL Integration**.
3.  Verifique se a opção de integração com a sua distribuição WSL está ativada.

#### 2\. Instalação do `act`

1.  Abra o seu terminal WSL.
2.  Crie um diretório para o `act` (opcional, mas recomendado para organização):
    ```bash
    mkdir -p ~/github-actions-locally/bin
    cd ~/github-actions-locally/bin
    ```
3.  Execute o script de instalação do `act` dentro da pasta:
    ```bash
    curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
    ```

#### 3\. Configuração do `PATH`

Após a instalação, o terminal não conseguirá encontrar o comando `act` de forma automática. Para resolver isso, adicione o diretório onde o `act` foi instalado (`~/github-actions-locally/bin`) ao seu `$PATH`.

1.  Execute o seguinte comando no seu terminal:
    ```bash
    echo 'export PATH="$PATH:$HOME/github-actions-locally/bin"' >> ~/.bashrc
    ```
2.  Recarregue as configurações do terminal:
    ```bash
    source ~/.bashrc
    ```

#### 4\. Resolução de Problemas de Permissão (Erro `permission denied`)

Este é o passo mais importante para que o `act` consiga se comunicar com o Docker. Se você tentar usar o `act` e receber um erro de "permission denied", a solução é adicionar seu usuário ao grupo do Docker.

1.  **Adicione seu usuário ao grupo `docker`:**
    ```bash
    sudo usermod -aG docker $USER
    ```
2.  **Reinicie o computador.**
    Esta é a etapa mais crítica. As mudanças de grupo não são aplicadas de forma confiável apenas reiniciando o terminal no WSL. **Reiniciar o Windows** garantirá que a nova permissão seja reconhecida.
3.  (Opcional) Para verificar se seu usuário foi adicionado corretamente ao grupo, execute:
    ```bash
    groups $USER
    ```
    A saída deve incluir `docker` na lista de grupos.

#### 5\. Verificação Final

Após reiniciar o computador, abra o terminal WSL e verifique se tudo está funcionando.

  * **Teste o Docker:**
    ```bash
    docker run hello-world
    ```
    Você deve ver uma mensagem de sucesso do Docker.
  * **Teste o `act`:**
    ```bash
    act --version
    ```
    Você deve ver a versão do `act` instalada.