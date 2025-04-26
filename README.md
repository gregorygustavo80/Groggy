# Groggy 💤
Groggy é uma calculadora de sono feita em Flask que ajuda você a encontrar os melhores horários para acordar, considerando ciclos completos de sono.  O app também conta com um modo escuro e uma seção explicativa sobre como o sono funciona.

## ✨ Funcionalidades
- Cálculo de horários ideais para acordar
- Explicação do método usado
- Interface moderna com animações suaves
- Modo Claro/Escuro (salvo no navegador)
- Responsivo para desktop e mobile

## 🛠 Tecnologias Utilizadas
- Python 3
- Flask
- HTML5, CSS3 e JavaScript
- LocalStorage para salvar o tema

## ⚙️ Como Rodar Localmente

1. Clone o repositório:

    ```bash
    git clone https://github.com/gregorygustavo80/Groggy.git
    cd Groggy
    ```

2. Crie e ative o ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate    # Linux/macOS
    venv\Scripts\activate       # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:

    ```bash
    flask run --app app.py
    ```
