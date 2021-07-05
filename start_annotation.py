#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2 
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import os
import xml.etree.ElementTree as ET

CONFIDENCE_THRESHOLD = 0.4
NMS_THRESHOLD = 0.5


# In[7]:


def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem


# In[8]:


To_detect = []
with open("configuration/Annotations.names", "r") as f:
    To_detect = [cname.strip() for cname in f.readlines()]


# In[9]:


class_names = []
with open("configuration/coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]


# In[10]:


net = cv2.dnn.readNet("configuration/yolov4-csp.weights", "configuration/yolov4-csp.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)


# In[11]:


model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(640, 640), scale=1/255, swapRB=True)


# In[12]:


path = os.path.abspath('images')
path


# In[13]:


for file in os.listdir(path):
    #root element
    root = ET.Element('annotation')
    colors = np.random.uniform(0,255,size=(len(class_names),3))


    #book sub-element
    folder = ET.SubElement(root, 'folder')
    folder.text='Images'

    filename = ET.SubElement(root, 'filename')
    filename.text=file

    size = ET.SubElement(root, 'size')

    width = ET.SubElement(size, 'width')
    width.text = '416'
    height = ET.SubElement(size, 'height')
    height.text = '416'
    depth = ET.SubElement(size, 'depth')
    depth.text = '3'

    segmented = ET.SubElement(root, 'segmented')
    segmented.text='0'
    print(file)
    img = cv2.imread(os.path.join(path, file) )
    classes, scores, boxes = model.detect(img, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    for (classid, score, box) in zip(classes, scores, boxes):
        if class_names[classid[0]] in detect_classes:
            color=colors[classid[0]]
            label = "%s : %f" % (class_names[classid[0]], score)
            cv2.rectangle(img, box,color, 2)
            cv2.putText(img, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 2)
            object = ET.SubElement(root, 'object')

            name = ET.SubElement(object, 'name')
            name.text=class_names[classid[0]]

            pose = ET.SubElement(object, 'pose')
            pose.text='Unspecified'

            turncated = ET.SubElement(object, 'turncated')
            turncated.text='0'

            occluded = ET.SubElement(object, 'occluded')
            occluded.text='0'

            difficult = ET.SubElement(object, 'difficult')
            difficult.text='0'

            bndbox = ET.SubElement(object, 'bndbox')

            xmin = ET.SubElement(bndbox, 'xmin')
            xmin.text = str(box[0])

            ymin = ET.SubElement(bndbox, 'ymin')
            ymin.text = str(box[1])

            xmax = ET.SubElement(bndbox, 'xmax')
            xmax.text = str(box[0]+box[2])

            ymax = ET.SubElement(bndbox, 'ymax')
            ymax.text = str(box[1]+box[3])

            tree = ET.ElementTree(indent(root))
            tree.write('annotations/'+file[0:-3:]+'xml', xml_declaration=True, encoding='utf-8')

        
        
        


# In[ ]:




