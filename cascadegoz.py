import sys
import cv2 as cv

def main(argv):
    default_file = 'bc06.webp'
    filename = argv[0] if len(argv) > 0 else default_file
    
    # Resmi yükle
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    
    # Resmin başarıyla yüklendiğini kontrol et
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    # Gri tonlamalıya dönüştür
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    # Göz algılama modelini yükle
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    
    # Gözleri tespit et
    eyes = eye_cascade.detectMultiScale(gray)
    
    # Gözleri işaretle
    for (x,y,w,h) in eyes:
        # Gözü sınırlayan dikdörtgenin merkezini ve ekseni uzunluklarını hesapla
        center = (x + w//2, y + h//2)
        axes_length = (w//2, h//2)
        # Elipsi çiz
        cv.ellipse(src, center, axes_length, 0, 0, 360, (255, 0, 0), 2)
    
    # Tespit edilen gözleri göster
    cv.imshow("detected eyes", src)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])