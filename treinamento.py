import cv2
import os
import numpy as np


##Algoritmos classificadores
eigenface = cv2.face.EigenFaceRecognizer_create(num_components = 50,threshold=0)
fisherface = cv2.face.FisherFaceRecognizer_create(num_components = 50,threshold=0) #Melhor em relação a iluminação comparado ao EigenFaces
lbph = cv2.face.LBPHFaceRecognizer_create() #Mais robusto em relação a variação da iluminação

def getImagemComId(): #Vai percorrer a pasta de fotos
    caminhos = [os.path.join('fotos',f) for f in os.listdir('fotos')]
    #print(caminhos) #-- Mostra todas as fotos 
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem),cv2.COLOR_BGR2GRAY) # Convertendo para cinza
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1]) # Pegando os ID's
        ids.append(id)
        faces.append(imagemFace)
        #print(ids)
        #print(id)
        #cv2.imshow("Face",imagemFace)
        #cv2.waitKey(50)
    return np.array(ids),faces

#Imagem vai sair como uma matriz
ids, faces = getImagemComId()
#print(faces)

print("Treinando....")
eigenface.train(faces,ids)
eigenface.write('classificadorEigen.yml') # Arquivo que será gerado para o reconhecimento facial 

fisherface.train(faces,ids)
fisherface.write('classificadorFisher.yml')

lbph.train(faces,ids)
lbph.write('classificadorLBPH.yml')

print("Treinamento realizado")
