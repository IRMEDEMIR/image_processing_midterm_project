import cv2
import numpy as np
import matplotlib.pyplot as plt

######################## 1.SORU ##############################
# Sigmoid fonksiyonu
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Standart S-Curve metodu
def standard_s_curve(image):
    # Görüntüyü 0 ile 1 arasında normalize et
    normalized_image = image.astype(float) / 255.0
    # Sigmoid fonksiyonunu uygula
    transformed_image = sigmoid((normalized_image - 0.5) * 10)
    # 0-255 arasında yeniden ölçekle
    transformed_image = (transformed_image * 255).astype(np.uint8)
    return transformed_image

# Yatay kaydırılmış S-Curve metodu
def shifted_s_curve(image, shift_amount):
    normalized_image = image.astype(float) / 255.0
    transformed_image = sigmoid((normalized_image - 0.5 + shift_amount) * 10)
    transformed_image = (transformed_image * 255).astype(np.uint8)
    return transformed_image

# Eğimli S-Curve metodu
def sloped_s_curve(image, slope):
    normalized_image = image.astype(float) / 255.0
    transformed_image = sigmoid((normalized_image - 0.5) * slope)
    transformed_image = (transformed_image * 255).astype(np.uint8)
    return transformed_image

# Kendi fonksiyonum
def custom_s_curve(image):
    normalized_image = image.astype(float) / 255.0
    transformed_image = sigmoid((normalized_image - 0.5) * 20)
    transformed_image = (transformed_image * 255).astype(np.uint8)
    return transformed_image

# Görüntüyü yükle
image = cv2.imread("gc4.jpg", cv2.IMREAD_GRAYSCALE)

# Standart S-Curve uygula
standard_result = standard_s_curve(image)

# Yatay kaydırılmış S-Curve uygula
shifted_result = shifted_s_curve(image, 0.2)

# Eğimli S-Curve uygula
sloped_result = sloped_s_curve(image, 20)

# Kendi fonksiyonumu kullanarak S-Curve uygula
custom_result = custom_s_curve(image)

# Sonuçları görselleştir
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Orjinal Görüntü')

plt.subplot(2, 3, 2)
plt.imshow(standard_result, cmap='gray')
plt.title('Standart S-Curve')

plt.subplot(2, 3, 3)
plt.imshow(shifted_result, cmap='gray')
plt.title('Yatay Kaydırılmış S-Curve')

plt.subplot(2, 3, 4)
plt.imshow(sloped_result, cmap='gray')
plt.title('Eğimli S-Curve')

plt.subplot(2, 3, 5)
plt.imshow(custom_result, cmap='gray')
plt.title('Kendi Fonksiyonum')

plt.show()

