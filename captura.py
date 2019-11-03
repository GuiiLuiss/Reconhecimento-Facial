import cv2 #Biblioteca do Opencv
import numpy as np

################# Detecção das faces pela webcam ########################

camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml") #Arquivo haarcascade faz o treinamento para a detecção de rostos
classificadorOlho = cv2.CascadeClassifier("haarcascade-eye.xml") #Arquivo haarcascade faz o treinamento para a detecção de olhos
amostra = 1 #Contador
numeroAmostras = 50 #Quantidade de fotos tiradas
id = input('Digite seu identificador: ')

'''
##Captura das fotos de treinamento##
Formato:

pessoa.id.numerofoto.jpg
'''
largura,altura = 220,220 # Tamanho da foto que será tirada
print("Capturando as faces...")


while (True):
    conectado, imagem = camera.read() # Passando leitura da camera para variável "conectado" e "imagem"
    imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY) #Para melhor desempenho de detecção estou transformando a imagem em cinza
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor= 1.5, minSize=(150,150))  #Definindo scala do quadrado de captura e tamanho mínimo para captura
    
    for (x,y,l,a) in facesDetectadas: #l = largura e a = altura
        cv2.rectangle(imagem, (x,y),(x+l,y+a),(0,0,156),2) #Retangulo que aparece a detecção
        regiao = imagem[y:y + a, x:x +l]
        regiaoCinzaOlho = cv2.cvtColor(regiao,cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
        for (ox,oy,ol,oa) in olhosDetectados:
            cv2.rectangle(regiao,(ox,oy),(ox+ol,oy+oa),(0,255,0),2)

        ###### Coletar dos dados (captura das faces pela webcam) ########
            if cv2.waitKey(1) & 0xFF == ord('a'):
                if np.average(imagemCinza) > 170:
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x +l],(largura,altura))
                    cv2.imwrite("fotos/pessoa."+str(id)+"."+str(amostra)+".jpg",imagemFace)
                    print("[foto " + str(amostra)+ "captura com sucesso]")
                    amostra = amostra +1

    cv2.imshow("Face",imagem) # Mostrando a imagem da webcam
    cv2.waitKey(1)
    if (amostra >= numeroAmostras +1):
        break

print("Faces capturadas com sucesso")
camera.release() # Libera a memória
cv2.destroyAllWindows() # Para fechar a janela