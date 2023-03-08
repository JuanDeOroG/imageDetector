import cv2
import numpy as np
import pyautogui

#Cargar imagenes
image= cv2.imread("bola.png",0)  

while True:
    #Captura de pantalla
    screenshot = pyautogui.screenshot()

    template = np.asarray(screenshot)

    template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8

    locations= np.where(result >= threshold)

    if locations[0].size >0:

        for pt in zip(*locations[::-1]):
            print("Las coordenadas son: ", pt[0], pt[1])
            pyautogui.moveTo(pt[0],pt[1])

            break 










