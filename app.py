import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


from flask import Flask

import dill as pickle
import os
import numpy as np
from PIL import Image , ImageOps
import sklearn


UPLOAD_FOLDER = 'C:/caminho/para/o/arquivo_temporario_com _a_imagem_a_ser_inferida/hello_flask/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'pkl'])

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#carrega o modelo de machine learning criado com o scikit learn  e salvo com picke
#model=pickle.load(open("svm.pkl",'rb'))   # suport vector machine
model=pickle.load(open("svmModel.pk",'rb'))
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


preds=0  
@app.route('/file', methods=['GET','POST'])
def index():
    preds=[1]  
    numero=str(preds[0])
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # salva a imagem no cache do Flask. 
    picture=Image.open('C:/caminho/para/o/arquivo_temporario_com _a_imagem_a_ser_inferida/hello_flask/tmp/test.png')
    picture=picture.convert('L') # trata  a imagem
    picture=picture.resize((28,28), Image.LANCZOS) 
    picture = 255-np.array(picture)  # transforma  a imagem em uma matriz (elimina os cabeçalhos, etc, etc)
    data=np.int64(picture)
    data= data.reshape(1,-1)  #coloca no formato do modelo
    data=data/255.0           # normaliza (foi feito para trainar o modelo)
    preds= model.predict(data)    # FAZ A INFERÊNCIA
    print(preds[0])               #exibe na linha de comando somente para verificar. Pode suprimir, se quiser
    numero=str(int(preds[0]))     # transforma para string
    return  numero                # retorna o número para o cliente

#para levantar seu servidor FLASK, digite: python3 -m flask run   na linha de comando.

