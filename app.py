# app.py

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Nenhum arquivo enviado.'
        
        file = request.files['file']
        if file.filename == '':
            return 'Nenhum arquivo selecionado.'
        
        # Salva o arquivo temporariamente
        filepath = '/tmp/' + file.filename
        file.save(filepath)

        try:
            # Executa o script Python e captura a saída
            result = subprocess.run(['python3', filepath], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f'Erro ao executar o script: {str(e)}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

