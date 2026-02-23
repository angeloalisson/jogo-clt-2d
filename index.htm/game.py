import subprocess
import sys
from flask import Flask, render_template

app = Flask(__name__)

# --- PARTE DO SITE ---

@app.route('/')
def home():
    # Isso abre o seu index.html que está na pasta templates
    return render_template('index.html')

@app.route('/rodar-jogo')
def rodar_jogo():
    # Esta linha tenta abrir o próprio script como um jogo Pygame
    # É um truque para manter tudo em um arquivo só por enquanto
    subprocess.Popen([sys.executable, 'jogo_pygame.py'])
    return "Jogo iniciado! Verifique sua barra de tarefas."

if __name__ == '__main__':
    # Se você rodar este arquivo normalmente, ele abre o Site (Flask)
    app.run(debug=True)