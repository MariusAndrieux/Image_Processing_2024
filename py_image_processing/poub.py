import cv2

# Affiche la version d'OpenCV installée
print("Version d'OpenCV :", cv2.__version__)

image =  cv2.imread("rect_cont_black.png")

if image is not None:    
    
    # Convertir l'image en niveaux de gris
    image_en_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Binariser l'image si nécessaire
    _, image_binaire = cv2.threshold(image_en_gris, 128, 255, cv2.THRESH_BINARY)
    
    # Détection des contours    
    contours, _ = cv2.findContours(image_binaire, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Créer une copie de l'image pour dessiner les contours
    image_contours = image.copy()

    #print(contours) # Verif si les contours sont bien pris
    
    # Dessiner les contours sur l'image
    cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 2)  # Couleur verte, épaisseur de 2 pixels

    # Afficher l'image originale et l'image avec les contours
    #cv2.imshow("Image Originale", image)
    cv2.imshow("Contours", image_contours)

    # S'il y a des contours détectés
    if contours:
        # Trouver le contour avec la plus grande aire (assumant que c'est le rectangle)
        plus_grand_contour = max(contours, key=cv2.contourArea)

        # Obtenir les coordonnées du rectangle englobant
        x, y, w, h = cv2.boundingRect(plus_grand_contour)

        # Récupérer le sous-image (carré)
        image_carré = image[y:y+h, x:x+w]

        # Afficher l'image originale et l'image rognée
        cv2.imshow("Image Originale", image)
        cv2.imshow("Image Rognée", image_carré)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("Aucun contour trouvé dans l'image.")
else :
    print("Impossible d'ouvrir l'image.")