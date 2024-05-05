import cv2
import numpy as np
import matplotlib.pyplot as plt

def wiener_deconvolution(image, psf, noise_var):
    """
    Wiener Deconvolution algoritmasını uygular.

    Args:
        image (numpy.ndarray): Görüntü.
        psf (numpy.ndarray): Point Spread Function (PSF).
        noise_var (float): Gürültü varyansı.

    Returns:
        numpy.ndarray: Deconvolved görüntü.
    """
    # PSF'yi giriş görüntüsü boyutuna yeniden boyutlandır
    psf_resized = cv2.resize(psf, (image.shape[1], image.shape[0]))

    # Wiener filtresi uygula
    H = np.fft.fft2(psf_resized)
    G = np.fft.fft2(image)
    H_conj = np.conj(H)
    F_hat = (H_conj / (np.abs(H) ** 2 + noise_var)) * G
    f_hat = np.fft.ifft2(F_hat)
    deconvolved = np.abs(f_hat)

    return deconvolved

# Örnek bir görüntü yükle
image = cv2.imread('araba.jpg', cv2.IMREAD_GRAYSCALE)

# Motion blur PSF oluştur
psf = np.zeros((15, 15))
psf[7, :] = 1 / 15  # Yatay blur

# Wiener Deconvolution uygula
deconvolved_image = wiener_deconvolution(image, psf, noise_var=0.01)

# Sonuçları göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Bulanık Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(deconvolved_image, cmap='gray')
plt.title('Netleştirilmiş Görüntü')
plt.axis('off')

plt.show()
