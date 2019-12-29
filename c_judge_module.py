import cnn_load_hantei_module as cnn_load
import cnn_load_hantei_module_cp2 as cnn_load2
import cnn_load_hantei_module_cp1 as cnn_load1
from pprint import pprint
import csv
import cv2

# while(cnn1.cnn(112,4)<0.85):pass
# while(cnn2.cnn(112,4)<0.85):pass
# while(cnn.cnn(112,4)<0.85):pass
def judge(img):
    hantei=0
    kekka=[]
    kekka.append(cnn_load1.cnn(128,4,img))
    kekka.append(cnn_load2.cnn(128,4,img))
    kekka.append(cnn_load.cnn(128,4,img))
    if(sum(kekka)<=1):
        hantei=1
    return(hantei)

# acc_kekka=[[None]]
# for cf in range(1,17):
#     acc_kekka[0].append(cf*16)
#     acc_kekka.append([cf*4])
#     for px in range(1,17):
#         print(cf,px)
#         acc_kekka[cf].append(cnn.cnn(px*16,cf*4))
#
# filename=('./kekka_c.csv')#csvファイルの名前を設定
# with open(filename, 'w') as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerows(acc_kekka)#csvファイルに結果を書き込む
