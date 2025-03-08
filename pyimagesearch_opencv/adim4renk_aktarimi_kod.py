
# gerekli paketleri yükle 
from adim4renk_aktarimi import color_transfer
import numpy as np
import argparse
import cv2

def show_image(title, image, width = 300):
	# görüntüyü oranlarını bozmadan boyutlandırın
	r = width / float(image.shape[1])
	dim = (width, int(image.shape[0] * r))
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

	# resmi göster
	cv2.imshow(title, resized)

#boolen değerlerini yönetmek için yardımcı fonksiyondur
# Bu, kullanıcıdan alınan clip ve preservePaper argümanlarının boolean olarak işlenmesini sağlar.
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

#argüman ayrıştıcısını oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required = True,help = "Path to the source image")
ap.add_argument("-t", "--target", required = True,help = "Path to the target image")
ap.add_argument("-c", "--clip", type = str2bool, default = 't',help = "Should np.clip scale L*a*b* values before final conversion to BGR? ""Approptiate min-max scaling used if False.")
ap.add_argument("-p", "--preservePaper", type = str2bool, default = 't',help = "Should color transfer strictly follow methodology layed out in original paper?")
ap.add_argument("-o", "--output", help = "Path to the output image (optional)")
args = vars(ap.parse_args())

#resimleri yükle
source = cv2.imread(args["source"])
target = cv2.imread(args["target"])

# renk dağılımını kaynak görüntüden hedef resime aktarın
#clip ve preserve_paper parametreleri, renk aktarımının nasıl yapılacağını belirler.
transfer = color_transfer(source, target, clip=args["clip"], preserve_paper=args["preservePaper"])

# çıktı görüntüsünün kaydedidilip kaydedilmeyeceğini kontrol edin , eğer -o ile bir yol belirtildiyse oraya kaydeder
if args["output"] is not None:
	cv2.imwrite(args["output"], transfer)

# resimleri görüntüleyin
show_image("Source", source)
show_image("Target", target)
show_image("Transfer", transfer)
cv2.waitKey(0)