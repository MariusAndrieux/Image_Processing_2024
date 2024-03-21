import cv2
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Chemin relatif ou absolu vers l'image
chemin_image = "img_test.png"

# Taille image
larg_image_pix = 800

# Lecture de l'image
image = cv2.imread(chemin_image)

# Vérifier si la lecture de l'image a réussi
if image is not None:
    # Obtenir les dimensions originales de l'image
    hauteur, largeur = image.shape[:2]

    # Facteur de redimensionnement souhaité (par exemple, 0.5 pour réduire de moitié)
    facteur_redimensionnement = larg_image_pix/largeur

    # Calculer les nouvelles dimensions en maintenant le même rapport hauteur/largeur
    nouvelle_largeur = int(largeur * facteur_redimensionnement)
    nouvelle_hauteur = int(hauteur * facteur_redimensionnement)

    # Redimensionner l'image
    image = cv2.resize(image, (nouvelle_largeur, nouvelle_hauteur))

    # Convertir l'image en niveaux de gris
    image_en_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou pour réduire le bruit et améliorer la détection des contours
    image_en_gris_flou = cv2.GaussianBlur(image_en_gris, (5, 5), 0)

    # Détection des contours avec Canny
    contours = cv2.Canny(image_en_gris, 50, 150)

    # Trouver les contours
    contours, _ = cv2.findContours(contours, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Créer une copie de l'image pour dessiner les contours
    image_contours = image.copy()

    # Dessiner les contours sur l'image
    cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 2)  # Couleur verte, épaisseur de 2 pixels

    # Créer une image noire pour afficher uniquement les contours
    image_contours_seuls = np.ones_like(image) * 255  # Fond blanc
    cv2.drawContours(image_contours_seuls, contours, -1, (0, 0, 255), 1)  # Couleur blanche, épaisseur de 1 pixel

    # Afficher les quatre images dans chaque coin avec matplotlib
    plt.figure(figsize=(16, 9))
'''
    # Image originale avec pointeur de souris interactif
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Imagen original")
'''
    plt.subplot(1,1,1)
    plt.imshow(cv2.cvtColor(image_en_gris_flou, cv2.COLOR_BGR2RGB))
    plt.title("Imagen en desenfoque gris")
'''
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(image_contours, cv2.COLOR_BGR2RGB))
    plt.title("Contornos")

    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(image_contours_seuls, cv2.COLOR_BGR2RGB))
    plt.title("Sólo contornos")
    # plt.axis('off')  # Désactive les axes pour le coin inférieur droit
'''
    plt.tight_layout()
    plt.show()
    
else:
    print(f"Impossible de lire l'image à partir du chemin : {chemin_image}")
