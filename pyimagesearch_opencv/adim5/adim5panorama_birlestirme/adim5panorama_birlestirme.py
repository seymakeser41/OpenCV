"""
Adım #1: Anahtar noktaları (DoG, Harris, vb.) algılayın ve iki giriş görüntüsünden yerel değişmez tanımlayıcıları (SIFT, SURF, vb.) çıkarın.
# 2 Adım: İki görüntü arasındaki tanımlayıcıları eşleştirin.
# 3 Adım: Eşleşen özellik vektörlerimizi kullanarak bir homografi matrisini tahmin etmek için RANSAC algoritmasını kullanın.
#4 Adım: Adım #3'ten elde edilen homografi matrisini kullanarak bir çarpıtma dönüşümü uygulayın.
"""

# gerekli paketleri içeri aktar
import numpy as np
import imutils
import cv2
class Stitcher:
	def __init__(self):
		# OpenCV v3.X kullanıp kullanmadığımızı belirleyin.
		#OpenCV 2.4 ve OpenCV 3'ün anahtar nokta algılama ve yerel değişmez tanımlayıcıları nasıl işlediği 
        # konusunda büyük farklılıklar olduğundan, kullandığımız OpenCV sürümünü belirlememiz önemlidir
		self.isv3 = imutils.is_cv3(or_better=True)
	
	def stitch(self, images, ratio=0.75, reprojThresh=4.0,showMatches=False):
		# Görüntüleri paketinden çıkarın, ardından anahtar noktaları tespit edin ve onlardan yerel değişmez tanımlayıcılar ayıklayın
		
		(imageB, imageA) = images
		(kpsA, featuresA) = self.detectAndDescribe(imageA)
		(kpsB, featuresB) = self.detectAndDescribe(imageB)
		# İki görüntü arasındaki özellikleri eşleştirin
		M = self.matchKeypoints(kpsA, kpsB,
			featuresA, featuresB, ratio, reprojThresh)
		#  eşleşme Yok ise, o zaman eşleşme için yeterli  panorama oluşturmak için anahtar noktalar yok demektir
	
		if M is None:
			return None
		
        # görüntüleri birleştirmek için bir perspektif çarpıtma uygulayın
		(matches, H, status) = M
		result = cv2.warpPerspective(imageA, H,
			(imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
		result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
		# Anahtar nokta eşleşmelerinin görselleştirilmesi gerekip gerekmediğini kontrol edin
		if showMatches:
			vis = self.drawMatches(imageA, imageB, kpsA, kpsB, matches,status)
			# Dikişli görüntünün bir demetini döndürür 
			return (result, vis)
		# Dikişli görüntüyü geri getirin
		return result
	
	def detectAndDescribe(self, image):
		# gri tonlamaya çevir
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# OpenCV 3.X kullanıp kullanmadığınızı kontrol edin
		if self.isv3:
			# Görüntüdeki özellikleri algılayın ve çıkarın
			descriptor = cv2.xfeatures2d.SIFT_create()
			(kps, features) = descriptor.detectAndCompute(image, None)
		# aksi takdirde, OpenCV 2.4.X kullanıyoruz
		else:
			# Görüntüdeki anahtar noktaları algıla
			detector = cv2.FeatureDetector_create("SIFT")
			kps = detector.detect(gray)
			# extract features from the image
			extractor = cv2.DescriptorExtractor_create("SIFT")
			(kps, features) = extractor.compute(gray, kps)
		# KeyPoint nesnelerinden anahtar noktaları NumPy kullanarak diziye dönüştürün
		kps = np.float32([kp.pt for kp in kps])
		# Bir dizi anahtar nokta ve özellik döndürün
		return (kps, features)
	
	def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB,
		ratio, reprojThresh):
		# ham eşleşmeleri hesaplayın ve gerçek eşleşmelerin listesini başlatın
	
		matcher = cv2.DescriptorMatcher_create("BruteForce")
		rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
		matches = []
		# ham eşleşmeler üzerinde döngü
		for m in rawMatches:
			# mesafenin her birinin diğerinden belirli bir oranı içinde olduğundan emin olun
			if len(m) == 2 and m[0].distance < m[1].distance * ratio:
				matches.append((m[0].trainIdx, m[0].queryIdx))
				
            # Bir homografinin hesaplanması en az 4 eşleşme gerektirir
		if len(matches) > 4:
			# iki nokta kümesini oluşturun
			ptsA = np.float32([kpsA[i] for (_, i) in matches])
			ptsB = np.float32([kpsB[i] for (i, _) in matches])
			# iki nokta kümesi arasındaki homografiyi hesaplayın
			(H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,reprojThresh)
			#  Eşleşmeleri ,homograpy matrisini ve eşleşen her noktanın durumunu birlikte döndürün
			return (matches, H, status)
		# Aksi takdirde, herhangi bir homograpy hesaplanamazdı
		return None
	
	def drawMatches(self, imageA, imageB, kpsA, kpsB, matches, status):
		# Çıktı görselleştirme görüntüsünü başlatın
		(hA, wA) = imageA.shape[:2]
		(hB, wB) = imageB.shape[:2]
		vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
		vis[0:hA, 0:wA] = imageA
		vis[0:hB, wA:] = imageB
		# eşleşmler üzerinde döngü
		for ((trainIdx, queryIdx), s) in zip(matches, status):
			# Eşleşmeyi yalnızca kilit nokta başarılı bir şekilde işlendiyse eşleştirin
			if s == 1:
				# eşleştirmeyi çizin
				ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
				ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
				cv2.line(vis, ptA, ptB, (0, 255, 0), 1)
		# görselleştirmeyi döndürün
		return vis
	
   
	
