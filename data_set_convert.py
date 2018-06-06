# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:27:17 2018

@author: Administrator
"""
import xml.etree.ElementTree as ET

#classes = ["花", "鸟", "虫", "鱼"]

def convert(size, box):  
#    dw = 1./size[0] # 归一化的时候就是使用宽度除以整个image_size的宽度   
#    dh = 1./size[1] # 归一化的时候就是使用高度除以整个image_size的高度  
    x = (box[0] + box[1])/2.0 # 使用(xmin+xmax)/2得到x的中心点  
    y = (box[2] + box[3])/2.0 # 使用(ymin+ymax)/2得到y的中心点  
    w = box[1] - box[0] # 然后宽度就是使用xmax-xmin计算得到  
    h = box[3] - box[2] # 然后高度就是使用ymax-ymin计算得到  
#    x = x*dw # 归一化中心坐标x  
#    w = w*dw # 归一化bbox宽度  
#    y = y*dh # 归一化中心坐标y  
#    h = h*dh # 归一化bbox高度  
    return (x,y,w,h)  
  
def convert_annotation():
    out_file = open('img00002.txt', 'w')     
    tree=ET.parse('img00002.xml')
    root = tree.getroot()  
    size = root.find('size')
    w = int(size.find('width').text)  
    h = int(size.find('height').text)  
  
    for obj in root.iter('object'):  
#        difficult = obj.find('difficult').text  
        cls = obj.find('name').text  
#        if cls not in classes or int(difficult) == 1:  
#            continue  
#        cls_id = classes.index(cls)  
        xmlbox = obj.find('bndbox')  
    # 获取标注中bbox的数据并以元组方式返回  
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))  
    # 向convert传入size = (w,h),和b,注释中分别是(xmin,xmax,ymin,ymax)     
        bb = convert((w,h), b)
        print(bb)
        out_file.write("-".join([str(a) for a in bb])+ "|" + str(cls) + '\n')

if __name__ == "__main__":
    convert_annotation()

