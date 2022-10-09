import sys
import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QAction, QLabel,QFileDialog, QMainWindow, QApplication, QPushButton
from skimage import io
import cv2
import numpy as np
from PIL import Image as im
from fimage import FImage
from fimage.filters import Sepia
from PyQt5 import uic
from PIL import Image
from PIL.ImageFilter import (
   BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   MaxFilter,MinFilter,MedianFilter,GaussianBlur
)
from skimage.filters import roberts, sobel, scharr, prewitt
from skimage.feature import canny
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Filter.ui", self)

        # =========== start MainWindow    =====================
        self.button = self.findChild(QPushButton, 'pushButton')
        self.real = self.findChild(QLabel, 'label_2')
        self.photo = self.findChild(QLabel, 'label')
        self.savee=self.findChild(QPushButton,'pushButton')
        self.savee.clicked.connect(self.Save_image)
        # =========== End MainWindow    =====================

        # =========== start menuFile    =====================
        self.open = self.findChild(QAction, 'actionOpen')
        self.open.triggered.connect(self.open_File)
        self.Exit = self.findChild(QAction, 'actionExit')
        self.Exit.triggered.connect(self.Exit_)

        # =========== End menuFile    =====================

        # =========== start Edage Filter    =====================
        self.Sobel = self.findChild(QAction, 'actionsobel')
        self.Sobel.triggered.connect(self.Soleb_)

        self.roberts = self.findChild(QAction, 'actionroberts')
        self.roberts.triggered.connect(self.roberts_)
        self.scharr = self.findChild(QAction, 'actionscharr')
        self.scharr.triggered.connect(self.scharr_)
        self.prewitt = self.findChild(QAction, 'actionprewitt')
        self.prewitt.triggered.connect(self.prewitt_)
        self.Edage_Enhance = self.findChild(QAction, 'actionEdage_Enhance')
        self.Edage_Enhance.triggered.connect(self.Edage_Enhance_)
        self.Edage_Enhance_more = self.findChild(QAction, 'actionEdage_Enhance_More')
        self.Edage_Enhance_more.triggered.connect(self.Edage_Enhance_more_)
        self.Find_Edage = self.findChild(QAction, 'actionFind_Edage')
        self.Find_Edage.triggered.connect(self.Find_Edage_)
        self.Canny = self.findChild(QAction, 'actionCanny')
        self.Canny.triggered.connect(self.Canny_)
        # =========== End  Edge Filter     =====================

        # =========== start  Blur Filter      =====================
        self.MinFilter = self.findChild(QAction, 'actionMinFilter')
        self.MinFilter.triggered.connect(self.MinFilter_)
        self.Contour = self.findChild(QAction, 'actionContour')
        self.Contour.triggered.connect(self.Contour_)
        self.Emboss = self.findChild(QAction, 'actionEmboss')
        self.Emboss.triggered.connect(self.Emboss_)
        self.Sepia = self.findChild(QAction, 'actionSepia')
        self.Sepia.triggered.connect(self.Sepia_)
        self.sharpen = self.findChild(QAction, 'actionsharpen')
        self.sharpen.triggered.connect(self.sharpen_)
        self.MaxFilter = self.findChild(QAction, 'actionMaxFilter')
        self.MaxFilter.triggered.connect(self.MaxFilter_)
        self.MedianFilter = self.findChild(QAction, 'actionMedianFilter')
        self.MedianFilter.triggered.connect(self.MedianFilter_)
        # =========== End  Blur Filter     ====================

        # =========== start  smooth Filter      =====================
        self.smooth = self.findChild(QAction, 'actionsmooth')
        self.smooth.triggered.connect(self.smooth_)
        self.smooth_More = self.findChild(QAction, 'actionsmooth_More')
        self.smooth_More.triggered.connect(self.smooth_More_)
        self.bilateralFlter = self.findChild(QAction, 'actionbilateralFlter')
        self.bilateralFlter.triggered.connect(self.bilateralFlter_)
        self.Blur_3 = self.findChild(QAction, 'actionBlur_3')
        self.Blur_3.triggered.connect(self.Blur_3_)
        self.Box_BlUr = self.findChild(QAction, 'actionBox_BlUr')
        self.Box_BlUr.triggered.connect(self.Box_BlUr_)
        self.GaussianBlur_2 = self.findChild(QAction, 'actionGaussianBlur_2')
        self.GaussianBlur_2.triggered.connect(self.GaussianBlur_2_)
        # =========== End  smooth Filter      =====================


        # =========== start  Flip Filter      =====================
        self.Left_Right = self.findChild(QAction, 'actionLeft_Right')
        self.Left_Right.triggered.connect(self.flip_left_right)
        self.top_bootom = self.findChild(QAction, 'actiontop_bootom')
        self.top_bootom.triggered.connect(self.top_bootom_)
        self.rotate_90 = self.findChild(QAction, 'actionrotate_90')
        self.rotate_90.triggered.connect(self.rotate_90_)

        # =========== End  Flip Filter      =====================


        # =========== start  split Filter      =====================
        self.Red_image = self.findChild(QAction, 'actionRed_image')
        self.Red_image.triggered.connect(self.Red_image_)
        self.green_image = self.findChild(QAction, 'actiongreen_image')
        self.green_image.triggered.connect(self.green_image_)
        self.Blue_image = self.findChild(QAction, 'actionBlue_image')
        self.Blue_image.triggered.connect(self.Blue_image_)
        self.Gray_image = self.findChild(QAction, 'actionGray_image')
        self.Gray_image.triggered.connect(self.Gray_image_)
        # =========== End  Split Filter      =====================
        self.show()

    def getFileName(self):
        print("sdfgsdfg")
        file_filter = 'Data File (*.jpg *.png *bmp *jpeg)'
        response = QFileDialog.getOpenFileName(caption='Select a data file', directory=os.getcwd(), filter=file_filter,
                                               initialFilter='Excel File (*.xlsx *.xls)')
        return response[0]

    def closeEvent(self,event):
        folder_path = (r'image')
        test = os.listdir(folder_path)
        for images in test:
            if images.endswith(".png"):
                os.remove(os.path.join(folder_path, images))
    def open_File(self):
        self.File = self.getFileName()
        self.real.setPixmap(QtGui.QPixmap(self.File))

    def Save_image(self):
        folder_path = (r'image')
        print(self.File)
        test = os.listdir(folder_path)
        for images in test:
            n = images
        xx = io.imread(f'{folder_path}\\{n}')
        io.imsave('Image_filter/index.png', xx)

    def Soleb_(self):
        img = io.imread(self.File, as_gray=True)
        blurImage = sobel(img)
        io.imsave('image/Soleb.png',blurImage)
        self.photo.setPixmap(QtGui.QPixmap('image/Soleb.png'))

    def roberts_(self):
        img = io.imread(self.File, as_gray=True)
        blurImage = roberts(img)
        io.imsave('image/Soleb.png', blurImage)
        self.photo.setPixmap(QtGui.QPixmap('image/Soleb.png'))

    def scharr_(self):
        img = io.imread(self.File, as_gray=True)
        blurImage = scharr(img)
        io.imsave('image/Soleb.png', blurImage)
        self.photo.setPixmap(QtGui.QPixmap('image/Soleb.png'))

    def prewitt_(self):
        img = io.imread(self.File, as_gray=True)
        blurImage = prewitt(img)
        io.imsave('image/prewitt.png', blurImage)
        self.photo.setPixmap(QtGui.QPixmap('image/prewitt.png'))

    def Edage_Enhance_(self):
        img = Image.open(self.File)
        img= img.filter(EDGE_ENHANCE)
        img.save('image/Edage_Enhance.png')

        self.photo.setPixmap(QtGui.QPixmap('image/Edage_Enhance.png'))

    def Edage_Enhance_more_(self):
        img = Image.open(self.File)
        img = img.filter(EDGE_ENHANCE_MORE)
        img.save('image/Edage_Enhance_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/Edage_Enhance_.png'))

    def Find_Edage_(self):
        img = Image.open(self.File)
        img = img.filter(FIND_EDGES)
        img.save('image/Find_Edage.png')
        self.photo.setPixmap(QtGui.QPixmap('image/Find_Edage.png'))

    def Canny_(self):
        img = io.imread(self.File, as_gray=True)
        blurImage = canny(img)
        io.imsave('image/canny.png', blurImage)
        self.photo.setPixmap(QtGui.QPixmap('image/canny.png'))

    def MinFilter_(self):
        img = Image.open(self.File)
        img = img.filter(MinFilter)
        img.save('image/MinFilter_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/MinFilter_.png'))

    def MaxFilter_(self):
        img = Image.open(self.File)
        img = img.filter(MaxFilter)
        img.save('image/MaxFilter.png')
        self.photo.setPixmap(QtGui.QPixmap('image/MaxFilter.png'))

    def Contour_(self):
        img = Image.open(self.File)
        img = img.filter(CONTOUR)
        img.save('image/Contour_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/Contour_.png'))

    def Emboss_(self):
        img = Image.open(self.File)
        img = img.filter(EMBOSS)
        img.save('image/Emboss_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/Emboss_.png'))

    def sharpen_(self):
         img = Image.open(self.File)
         img = img.filter(SHARPEN)
         img.save('image/sharpen_.png')
         self.photo.setPixmap(QtGui.QPixmap('image/sharpen_.png'))

    def MedianFilter_(self):
        img = Image.open(self.File)
        img = img.filter(MedianFilter)
        img.save('image/MedianFilter_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/MedianFilter_.png'))

    def Sepia_(self):
        image = FImage(self.File)
        image.apply(Sepia(90))
        image.save('image/my_picture_sepia.png')
        self.photo.setPixmap(QtGui.QPixmap('image/my_picture_sepia.png'))

    def smooth_(self):
        img = Image.open(self.File)
        img = img.filter(SMOOTH)
        img.save('image/Smooth.png')
        self.photo.setPixmap(QtGui.QPixmap('image/smooth.png'))

    def smooth_More_(self):
        img = Image.open(self.File)
        img = img.filter(SMOOTH_MORE)
        img.save('image/SMOOTH_MORE.png')
        self.photo.setPixmap(QtGui.QPixmap('image/SMOOTH_MORE.png'))

    def bilateralFlter_(self):
        img = cv2.imread(self.File)
        bilateral = cv2.bilateralFilter(img, 15, 75, 75)
        cv2.imwrite('image/taj_bilateral.png', bilateral)
        self.photo.setPixmap(QtGui.QPixmap('image/taj_bilateral.png'))



    def Blur_3_(self):
        img = Image.open(self.File)
        img = img.filter(BLUR)
        img.save('image/Blur.png')
        self.photo.setPixmap(QtGui.QPixmap('image/Blur.png'))


    def Box_BlUr_(self):
        print("ffffffffffff")
        img = Image.open(self.File)
        img = img.filter(BLUR)
        img.save('image/GaussianBlur.png')
        self.photo.setPixmap(QtGui.QPixmap('image/GaussianBlur.png'))


    def GaussianBlur_2_(self):
        img = Image.open(self.File)
        img = img.filter(GaussianBlur)
        img.save('image/GaussianBlur.png')
        self.photo.setPixmap(QtGui.QPixmap('image/GaussianBlur.png'))
    def flip_left_right(self):
        img = Image.open(self.File)
        # Do a flip of left and right
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save('image/flip_left_right.png')
        self.photo.setPixmap(QtGui.QPixmap('image/flip_left_right.png'))

    def top_bootom_(self):
        img = Image.open(self.File)
        # Do a flip of left and right
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save('image/top_bootom_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/top_bootom_.png'))

    def rotate_90_(self):
        img = Image.open(self.File)
        # Do a flip of left and right
        img = img.transpose(Image.ROTATE_90)
        img.save('image/rotate_90_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/rotate_90_.png'))

    def Red_image_(self):
        print("dgsdgf")
        img = Image.open(self.File)
        arr = np.array(img)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                for m in range(3):
                    if m == 0:

                        arr[i][j][m] = 0
                    else:

                        arr[i][j][m] = arr[i][j][m]

        R = np.array(arr)
        dataR = im.fromarray(R)
        dataR.save('image/Red_image_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/Red_image_.png'))

    def green_image_(self):
        print("dgsdgf")
        img = Image.open(self.File)
        arr = np.array(img)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                for m in range(3):
                    if m == 1:

                        arr[i][j][m] = 0
                    else:

                        arr[i][j][m] = arr[i][j][m]

        R = np.array(arr)
        dataR = im.fromarray(R)
        dataR.save('image/Red_image_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/Red_image_.png'))

    def Blue_image_(self):
        print("dgsdgf")
        img = Image.open(self.File)
        arr = np.array(img)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                for m in range(3):
                    if m == 2:

                        arr[i][j][m] = 0
                    else:

                        arr[i][j][m] = arr[i][j][m]

        R = np.array(arr)
        dataR = im.fromarray(R)
        dataR.save('image/Blue_image_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/Blue_image_.png'))

    def Gray_image_(self):
        img = Image.open(self.File)
        arr = np.array(img)
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                pp = arr[i][j][0] * 0.299 + arr[i][j][1] * 0.587 + arr[i][j][2] * 0.114
                if arr.shape[2]==4:

                    o = pp / 4
                    arr[i][j] = [o, o, o,o]
                else:
                    o = pp / 3
                    arr[i][j] = [o, o, o]

        R = np.array(arr)
        dataR = im.fromarray(R)
        dataR.save('image/gray_image_.png')
        self.photo.setPixmap(QtGui.QPixmap('image/gray_image_.png'))


    def Exit_(self):
            self.Exit()


app = QApplication(sys.argv)
UIwindow = UI()
app.exec_()
