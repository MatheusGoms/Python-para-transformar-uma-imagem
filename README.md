Instalação da Biblioteca
Caso você não tenha o OpenCV instalado, basta rodar o seguinte comando no ambiente Colab ou no terminal:

pip install opencv-python

Explicação do Código
Carregamento da Imagem:

A imagem é carregada com a função cv2.imread(), que retorna uma imagem no formato BGR (Blue, Green, Red). Para exibir corretamente com o Matplotlib, ela é convertida para RGB com cv2.cvtColor().
Conversão para Níveis de Cinza:

A função cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY) transforma a imagem colorida em uma escala de cinza, onde cada pixel tem um valor entre 0 e 255 (0 = preto, 255 = branco).
Binarização (Preto e Branco):

Para transformar a imagem em preto e branco, é aplicada a técnica de limiarização (thresholding) com cv2.threshold(). Pixels com valor acima de 127 são convertidos para 255 (branco), enquanto os abaixo são convertidos para 0 (preto).
Exibição das Imagens:

Utilizamos o Matplotlib para exibir as imagens colorida, em escala de cinza e binarizada lado a lado.

Teste no Google Colab

from google.colab import files
uploaded = files.upload()
