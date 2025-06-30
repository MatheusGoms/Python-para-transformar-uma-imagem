import cv2  # Biblioteca para manipulação de imagens
import matplotlib.pyplot as plt  # Para exibir as imagens

# Função para exibir imagens lado a lado
def exibir_imagens(titulos, imagens):
    plt.figure(figsize=(12, 4))
    for i in range(len(imagens)):
        plt.subplot(1, len(imagens), i + 1)
        plt.imshow(imagens[i], cmap='gray')
        plt.title(titulos[i])
        plt.axis('off')
    plt.show()

# Etapa 1: Carregar a imagem colorida
# Substitua o caminho pela imagem que você deseja processar
imagem_colorida = cv2.imread('/content/sua_imagem.jpg')  # Caminho da imagem
imagem_colorida = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB)  # Converter de BGR para RGB

# Etapa 2: Converter para níveis de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_RGB2GRAY)

# Etapa 3: Binarização (preto e branco)
# Utilize o método de limiarização (thresholding)
_, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Exibir as imagens
exibir_imagens(
    ["Imagem Colorida", "Imagem em Níveis de Cinza", "Imagem Binarizada (Preto e Branco)"],
    [imagem_colorida, imagem_cinza, imagem_binarizada]
)
