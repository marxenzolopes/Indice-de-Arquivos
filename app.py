from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import os
import subprocess
import shutil

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Diretório do arquivo Python atual
diretorio_atual = os.path.dirname(__file__)

# Diretório onde estão os arquivos Python
diretorio_arquivos = os.path.join(diretorio_atual, "arquivos_python")

# Diretório temporário para execução dos arquivos
diretorio_temp = os.path.join(diretorio_atual, "temp")

def listar_arquivos_python(diretorio):
    arquivos_python = []
    if os.path.exists(diretorio):
        for arquivo in os.listdir(diretorio):
            if arquivo.endswith(".py"):
                arquivos_python.append(arquivo)
    return arquivos_python

def upload_arquivo(file):
    filename = file.filename
    filepath = os.path.join(diretorio_arquivos, filename)
    file.save(filepath)
    flash('Arquivo enviado com sucesso!')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
        else:
            upload_arquivo(file)
        return redirect(url_for('index'))
    arquivos = listar_arquivos_python(diretorio_arquivos)
    return render_template('index.html', arquivos=arquivos)

@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    return send_file(os.path.join(diretorio_arquivos, filename), as_attachment=True)

@app.route('/executar/<path:filename>', methods=['GET'])
def executar(filename):
    filepath = os.path.join(diretorio_arquivos, filename)
    if os.path.exists(filepath):
        try:
            # Copia o arquivo para o diretório temporário
            shutil.copy(filepath, diretorio_temp)
            # Executa o arquivo no diretório temporário
            subprocess.Popen(["python", filename], cwd=diretorio_temp)
            return 'Arquivo executado com sucesso!'
        except Exception as e:
            return f'Erro ao executar o arquivo: {str(e)}'
    else:
        return 'Arquivo não encontrado'

if __name__ == '__main__':
    # Cria o diretório temporário se não existir
    if not os.path.exists(diretorio_temp):
        os.makedirs(diretorio_temp)
    app.run(debug=True)
