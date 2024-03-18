#include <opencv2/opencv.hpp>
#include <Windows.h>

void afficherImage(const cv::Mat& image, const std::string& nom_fenetre) {
    // Afficher l'image dans une fenêtre avec le nom spécifié
    cv::namedWindow(nom_fenetre, cv::WINDOW_NORMAL);
    cv::imshow(nom_fenetre, image);
    cv::waitKey(0);
    cv::destroyWindow(nom_fenetre);
}

int main() {
    // Chemin relatif ou absolu vers l'image
    std::string chemin_image = "C:/Users/Marius/Documents/code/Image_Processing_2024/cpp_image_processing/test_cont.png";

    // Taille image
    int larg_image_pix = 800;

    // Obtenir la taille de l'écran
    int largeur_ecran = GetSystemMetrics(SM_CXSCREEN);
    int hauteur_ecran = GetSystemMetrics(SM_CYSCREEN);

    // Lecture de l'image
    cv::Mat image = cv::imread(chemin_image);

    // Vérifier si la lecture de l'image a réussi
    if (!image.empty()) {
        // Obtenir les dimensions originales de l'image
        int hauteur = image.rows;
        int largeur = image.cols;

        // Facteur de redimensionnement souhaité (par exemple, 0.5 pour réduire de moitié)
        float facteur_redimensionnement = (float)larg_image_pix / largeur;

        // Calculer les nouvelles dimensions en maintenant le même rapport hauteur/largeur
        int nouvelle_largeur = cvRound(largeur * facteur_redimensionnement);
        int nouvelle_hauteur = cvRound(hauteur * facteur_redimensionnement);
        
        //Coeff ecran
        float coeff_larg = (largeur_ecran/2 - nouvelle_largeur) / 2;
        float coeff_haut = (hauteur_ecran/2 - nouvelle_hauteur) / 2;

        // Convertir l'image en niveaux de gris
        cv::Mat image_en_gris;
        cv::cvtColor(image, image_en_gris, cv::COLOR_BGR2GRAY);

        // Appliquer un flou pour réduire le bruit et améliorer la détection des contours
        cv::Mat image_en_gris_flou;
        cv::GaussianBlur(image_en_gris, image_en_gris_flou, cv::Size(5, 5), 0);

        // Détection des contours avec Canny
        cv::Mat contours;
        cv::Canny(image_en_gris, contours, 50, 150);

        // Trouver les contours
        std::vector<std::vector<cv::Point>> contours_vect;
        cv::findContours(contours, contours_vect, cv::RETR_LIST, cv::CHAIN_APPROX_SIMPLE);

        // Créer une copie de l'image pour dessiner les contours
        cv::Mat image_contours = image.clone();

        // Dessiner les contours sur l'image
        cv::drawContours(image_contours, contours_vect, -1, cv::Scalar(0, 255, 0), 2); // Couleur verte, épaisseur de 2 pixels

        // Créer une image noire pour afficher uniquement les contours
        cv::Mat image_contours_seuls = cv::Mat::zeros(image.size(), CV_8UC3); // Fond noir
        image_contours_seuls.setTo(cv::Scalar(255, 255, 255)); // Fond blanc
        cv::drawContours(image_contours_seuls, contours_vect, -1, cv::Scalar(0, 0, 255), 2); // Couleur rouge, épaisseur de 1 pixel

        // Afficher les quatre images
        cv::namedWindow("Image originale", cv::WINDOW_NORMAL);
        cv::resizeWindow("Image originale", nouvelle_largeur, nouvelle_hauteur); // Spécifiez la taille personnalisée
        cv::imshow("Image originale", image);
        cv::moveWindow("Image originale", 0 + coeff_larg, 0 + coeff_haut); // Coin supérieur gauche

        cv::namedWindow("Image en desenfoque gris", cv::WINDOW_NORMAL);
        cv::resizeWindow("Image en desenfoque gris", nouvelle_largeur, nouvelle_hauteur); // Spécifiez la taille personnalisée
        cv::imshow("Image en desenfoque gris", image_en_gris_flou);
        cv::moveWindow("Image en desenfoque gris", image.cols - coeff_larg -100, 0 + coeff_haut); // Coin supérieur gauche

        cv::namedWindow("Contornos", cv::WINDOW_NORMAL);
        cv::resizeWindow("Contornos", nouvelle_largeur, nouvelle_hauteur); // Spécifiez la taille personnalisée
        cv::imshow("Contornos", image_contours);
        cv::moveWindow("Contornos", 0 + coeff_larg, image.rows - coeff_haut-75); // Coin supérieur gauche

        cv::namedWindow("Sólo contornos", cv::WINDOW_NORMAL);
        cv::resizeWindow("Sólo contornos", nouvelle_largeur, nouvelle_hauteur); // Spécifiez la taille personnalisée
        cv::imshow("Sólo contornos", image_contours_seuls);
        cv::moveWindow("Sólo contornos", image.cols - coeff_larg -100, image.rows - coeff_haut-75); // Coin supérieur gauche

        cv::waitKey(0);
        cv::destroyAllWindows();
    } else {
        std::cout << "Impossible de lire l'image à partir du chemin : " << chemin_image << std::endl;
    }

    return 0;
}