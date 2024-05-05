import cv2
import numpy as np

def detect_lines(image_path):
    # Resmi yükle
    image = cv2.imread(image_path)
    
    # Gri tonlamalıya dönüştür
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Gürültüyü azaltmak için Gaussian blur uygula
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Kenarları tespit etmek için Canny kenar algılama uygula
    edges = cv2.Canny(blurred, 50, 150, apertureSize=3)
    
    # Hough Transform'u kullanarak çizgileri tespit et
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=80, maxLineGap=10)
    
    # Çizgiler varsa işaretle
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # Sonuçları göster
    cv2.imshow('Detected Lines', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Örnek bir görüntü üzerinde işlem yapalım
image_path = 'otoban.jpg'
detect_lines(image_path)
