import cv2
import cv2
import os

# Cargamos el clasificador pre-entrenado para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iniciamos la captura de video
cap = cv2.VideoCapture(0)

# Creamos el directorio para guardar las imágenes de los rostros detectados
if not os.path.exists('rostros_detectados'):
    os.makedirs('rostros_detectados')

i = 0
while True:
    # Leemos un frame
    ret, frame = cap.read()

    # Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectamos los rostros
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Guardamos las imágenes de los rostros detectados
    for (x, y, w, h) in faces:
        # Dibujamos un rectángulo verde alrededor del rostro detectado
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Limitamos el número de capturas a 10
        if i < 10:
            rostro = cv2.resize(gray[y:y+h, x:x+w], (150, 150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite('rostros_detectados/rostro_{}.jpg'.format(i), rostro)
            i += 1

    # Mostramos la imagen
    cv2.imshow('img', frame)

    # Si se presiona la tecla 'q', salimos del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberamos la cámara y cerramos todas las ventanas
cap.release()
cv2.destroyAllWindows()
