# usandoFlask
Utilização do Flask para inferências em modelos de machine learning


O Flask é um micro servidor onde podemos testar e hospedar nossos modelos de machine learning. É leve, bem documentado e fácil de usar. Além disso, podemos expandir suas funcionalidades para utiliza-lo em cenários mais complexos, que exijam segurança.

Neste repositório está o exemplo de um código fonte para realizar inferências em imagens 28X28, formato png para identificação de dígitos. 
O modelo foi treinado com o conhecido dataset MNIST, hospedado no servidor FLASK e faz a inferência através do método POST. 

Serve como base e pode ser modificado para realizar inferências em quaisquer tipos de dados. 


O primeiro passo é a criação de um ambiente virtual python, descrito em:  https://flask.palletsprojects.com/en/1.1.x/installation/#virtual-environments


No Windows, para utilizar com VS Code, navegue até onde o Python está instalado :  

C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64 

 

E digitei o seguinte comando:                             

python -m venv c:\[path]\[to]\[myenv] 

 

No meu caso ficou assim: 

C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64>python –m venv C:\[Users]\[User]\Documents\pyhton\Hello_Flask 

 
Depois, clique no env e mande executar no terminal. 
Em seguida, clique em View -> Command Pallete -> Python: Selecionar interpretador e escolhi o do ambiente env 


Qualquer dúvida, acesse https://code.visualstudio.com/docs/python/tutorial-flask
