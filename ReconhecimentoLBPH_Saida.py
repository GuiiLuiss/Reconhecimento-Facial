import cv2
import Banco

detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read('classificadorLBPH.yml')

largura, altura = 220,220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture (0)


while (True):
    conectado,imagem  = camera.read()
    imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor= 1.5, minSize=(30,30))
    for (x,y,l,a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y+a,x:x+l],(largura,altura))
        cv2.rectangle(imagem,(x,y),(x+l,y+a),(0,0,156),2)
        id,confianca = reconhecedor.predict(imagemFace)
        nome = "Desconhecido"
        status = "Saida"
        if id == 11:
            nome = 'Wesley'
        elif id == 2:
            nome = 'Guilherme'
        elif id == 3:
            nome = 'Neri'
        cv2.putText(imagem,nome,(x,y+(a+30)),font,2,(0,0,255))
        cv2.putText(imagem,status,(x,y+(a+50)),font,1,(0,0,255))
    cv2.imshow("Face",imagem)
    if cv2.waitKey(1) == ord('a'):
        break

camera.release()
cv2.destroyAllWindows()