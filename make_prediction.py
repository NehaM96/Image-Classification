from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from gui_mi import Ui_Dialog
import os
import glob
import cv2
import caffe
import lmdb
import numpy as np
from caffe.proto import caffe_pb2
IMAGE_WIDTH = 227
IMAGE_HEIGHT = 227
class MyDialog(QDialog):
    
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.predict_btn.clicked.connect(self.Predict)
        self.ui.selectImage_btn.clicked.connect(self.Browse)
        self.filename=""
        

    def transform_img(self,img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT):

        #Histogram Equalization
        img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
        img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
        img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])

    #Image Resizing
        img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_CUBIC)

        return img

    def Browse(self):
        self.filename += QFileDialog.getOpenFileName()
        self.ui.image.setPixmap(QPixmap(self.filename))
        self.ui.image.show()
    
    def Predict(self):
        
        
        colours={1:'black',2:'blue',3:'brown',4:'darkblue',5:'gold',6:'green',7:'maroon',8:'orange',9:'red',10:'silver',11:'white',12:'yellow'}
        types={'suv':1,'hatchback':2,'sedan':3,'carrier':4,'van':5}
        mean_blob = caffe_pb2.BlobProto()
        with open('input/mean.binaryproto') as f:
            mean_blob.ParseFromString(f.read())
        mean_array = np.asarray(mean_blob.data, dtype=np.float32).reshape((mean_blob.channels, mean_blob.height, mean_blob.width))
        net = caffe.Net('deploy.prototxt','caffe_model_iter_100.caffemodel',caffe.TEST)
        net2= caffe.Net('deploy2.prototxt','caffe_type_iter_100.caffemodel',caffe.TEST)

        transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
        #transformer.set_mean('data', mean_array)
        transformer.set_transpose('data', (2,0,1))

        test_img_paths = [str(self.filename)]


        test_ids = []
        preds = []
        preds2=[]
        for img_path in test_img_paths:
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            img = self.transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)
    
            net.blobs['data'].data[...] = transformer.preprocess('data', img)
            net2.blobs['data'].data[...] = transformer.preprocess('data', img)
            out = net.forward(data=np.asarray(net.blobs['data'].data[...]))
            out2 = net2.forward(data=np.asarray(net.blobs['data'].data[...]))
            pred_probas = out['prob']
            pred_probas2 = out2['prob']
            highest = pred_probas[0][0]
            highest2 = pred_probas2[0][0]
            index=0
            index2=0
            test_ids = test_ids + [img_path]
            
            result_string=""
            for x in range(len(colours)):
                if pred_probas[0][x]>highest:
                    highest = pred_probas[0][x]
                    index=x
            for x in range(len(types)):
                if pred_probas2[0][x]>highest2:
                    highest2 = pred_probas[0][x]
                    index2=x
            print img_path
            print colours[index+1]
            print types[index2]
            print '-------'
            result_string=colours[index+1]+" "+types[index2+1]
     
        
        with open("results.csv","w") as f:
            
            f.write("id,label\n")
            for i in range(len(test_ids)):
                
                f.write(str(test_ids[i])+","+str(preds[i])+"\n")
        self.ui.result.setText(result_string)
        f.close()

    
if __name__ == "__main__":
        app = QApplication(sys.argv)
        myapp = MyDialog()
        myapp.show()
        
        
        sys.exit(app.exec_())
