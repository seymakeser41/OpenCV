import numpy as np
import cv2

def order_points(pts):
    # Döndürülecek koordinatları tutacak bir liste oluştur
    # Listedeki ilk giriş sol üstte olacak şekilde, ikinci giriş sağ üst,
    # üçüncü giriş sağ alt ve dördüncüsü sol alttır
    rect = np.zeros((4, 2), dtype="float32")
    
    # Sol üst nokta en küçük toplama sahip olacaktır
    # Sağ alt nokta en büyük toplama sahip olacaktır
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    
    # Noktalar arasındaki farkı hesaplayın,
    # Sağ üst nokta en küçük farka sahip olacak,
    # Sol alt kısım en büyük farka sahip olacak
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    
    # Seçilen koordinatları döndürür
    return rect

def four_point_transform(image, pts):
    # Noktaların tutarlı bir sırasını elde edin
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    
    # Yeni görüntünün genişliğini hesaplayın
    # Sağ alt ve sol alt arasındaki maksimum mesafe
    # x koordinatları veya sağ üst ve sol üst x koordinatları kullanarak hesaplanır
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    
    # Yeni görüntünün yüksekliğini hesaplayın
    # Sağ üst ve sağ alt arasındaki maksimum mesafe
    # Y koordinatları veya sol üst ve sol alt y koordinatları kullanarak bulunur
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    
    # Yeni görüntünün boyutlarına sahip olduğumuza göre,
    # "Kuş bakışı görünüm" elde etmek için hedef noktalar kümesine bu boyutlar ile noktaları belirtiriz
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")
    
    # Perspektif dönüşüm matrisini hesaplayıp uygulayın
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    # Çıktıyı döndürün
    return warped
