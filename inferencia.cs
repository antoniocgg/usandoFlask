//Exemplo de código para inferência usando C# .NET
//Abaixo, apenas o trecho da comunicação com o Flask


var client = new WebClient();
               
              client.UploadFile(textBoxAdress.Text.ToString(), "POST", "C:\\[path]\\test.png");  // sobe a imagem teste

                texto = client.DownloadString("http://127.0.0.1:5000/file");

                textBoxResponse.Text = texto.ToString();   // exibe o número recebido em uma caixa de texto.
