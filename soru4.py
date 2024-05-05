import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Görüntüyü yükle
image = cv2.imread('say.jpg')

# RGB formatı
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Koyu yeşil pikselleri tespit etmek için bir eşik değeri belirle
lower_green = np.array([0, 100, 0])
upper_green = np.array([50, 255, 50])

# Maske oluştur
mask = cv2.inRange(rgb, lower_green, upper_green)

# Etiketleme yap
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Kırmızıyla işaretle
result = rgb.copy()
cv2.drawContours(result, contours, -1, (255, 0, 0), 2)

# Orijinal görüntüyü ve maskeyi yan yana göster
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap='Greens')
plt.title('Sadece Koyu Yeşil Pikseller')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(result)
plt.title('işaretli')
plt.axis('off')

plt.show()


# Özellikler için boş bir liste oluştur
data = []

# Konturları işle
for i, contour in enumerate(contours, start=1):
    # Konturun merkezi, boyutları ve alanını hesapla
    M = cv2.moments(contour)
    if M["m00"] == 0:
        continue  # Sıfıra bölme hatasını önlemek için devam et
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    x, y, w, h = cv2.boundingRect(contour)
    diagonal = np.sqrt(w**2 + h**2)
    area = cv2.contourArea(contour)
    
    # Piksellerin enerjisini ve entropisini hesapla
    energy = np.linalg.norm(rgb[y:y+h, x:x+w])
    entropy = np.linalg.norm(mask[y:y+h, x:x+w])
    
    # Piksellerin ortalama ve medyan değerlerini hesapla
    mean_val = np.mean(rgb[y:y+h, x:x+w])
    median_val = np.median(rgb[y:y+h, x:x+w])
    
    # Verileri listeye ekle
    data.append([i, f"{cx},{cy}", f"{w} px", f"{h} px", f"{diagonal:.0f} px", f"{energy:.3f}", f"{entropy:.2f}", int(mean_val), int(median_val)])

# Pandas DataFrame oluştur
df = pd.DataFrame(data, columns=["No", "Center", "Length", "Width", "Diagonal", "Energy", "Entropy", "Mean", "Median"])

# Excel dosyasına yaz
df.to_excel('koyu_yesil_pikseller.xlsx', index=False)
