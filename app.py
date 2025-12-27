from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <body style="background: #1a1a1a; color: gold; text-align: center; font-family: sans-serif; padding-top: 50px;">
        <h1>💰 CRYPTO-KING INVESTMENT 💰</h1>
        <p>Invista R$ 100 e receba R$ 1.000 em 24h!</p>
        <div style="border: 2px solid gold; padding: 20px; display: inline-block;">
            <h3>Acesse sua conta</h3>
            <form action="/login" method="post">
                <input type="text" name="user" placeholder="Usuário" required><br><br>
                <input type="password" name="pw" placeholder="Senha" required><br><br>
                <button type="submit" style="background: gold; padding: 10px; cursor: pointer;">ENTRAR</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/login', methods=['POST'])
def login():
    return "Erro no servidor: Saques suspensos. Tente novamente em 24h."

if __name__ == "__main__":
    app.run()