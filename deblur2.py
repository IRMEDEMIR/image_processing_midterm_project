import cv2
import numpy as np
from matplotlib import pyplot as plt

def richardson_lucy_deconv(image, psf, iterations=30):
    # Richardson-Lucy Deconvolution için varsayılan PSF oluştur
    psf /= psf.sum()
    img_deconv = np.full(image.shape, 0.5)
    psf_mirror = psf[::-1, ::-1]
    
    # Iteratif olarak Richardson-Lucy Deconvolution uygula
    for _ in range(iterations):
        estimate = cv2.filter2D(img_deconv, -1, psf)
        estimate = np.divide(image, estimate, out=np.ones_like(image), where=estimate != 0)
        img_deconv *= cv2.filter2D(estimate, -1, psf_mirror)
    
    return img_deconv

def deblur_image(image_path, psf_size=(5, 5), iterations=30):
    # Görüntüyü yükle
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Hareket bulanıklığı için PSF oluştur
    psf = np.ones(psf_size) / np.prod(psf_size)
    
    # Richardson-Lucy Deconvolution'u uygula
    deblurred_image = richardson_lucy_deconv(image.astype(float), psf, iterations)
    deblurred_image = np.clip(deblurred_image, 0, 255).astype(np.uint8)

    
    # Sonuçları göster
    plt.subplot(121),plt.imshow(image, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(deblurred_image, cmap='gray')
    plt.title('Deblurred Image'), plt.xticks([]), plt.yticks([])
    plt.show()

# Örnek olarak bir görüntü üzerinde deneyelim
image_path = 'araba.jpg'
deblur_image(image_path, psf_size=(5, 5), iterations=30)
