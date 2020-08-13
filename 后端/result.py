#!/usr/bin/python 
# -*- coding: utf-8 -*-
import base64
from flask import request
from flask import Response    
from flask import Flask
import os
    
app=Flask(__name__)
#返回简笔画
@app.route("/image/<imageid>")           
def index(imageid):
    fileName="C:\\Users\\lwwwwww\\Desktop\\magic\\results\\edges2shoes_pretrained\\test_latest\\images\\"+imageid+"_fake_B.png"
    with open(fileName, 'rb') as f:                    
        image = f.read()
    resp = Response(image, mimetype="image/jpeg")
    return resp
  
#返回风格转换
@app.route("/image2/<imageid>")           
def index2(imageid):
    fileName="C:\\Users\\lwwwwww\\Desktop\\magic\\results\\horse2zebra_pretrained\\test_latest\\images\\"+imageid+"_fake.png"
    with open(fileName, 'rb') as f:                    
        image = f.read()
    resp = Response(image, mimetype="image/jpeg")
    return resp                                    


# 定义路由 简笔画
@app.route("/photo", methods=['POST'])
def get_frame():              
    # 接收图片         
    upload_file = request.files['file']
    # 获取图片名            
    file_name = upload_file.filename
    # 文件保存目录（桌面）
    file_path=r'C:\Users\lwwwwww\Desktop\magic\datasets\edges2shoes\test'       
    if upload_file:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)              
        os.chdir(r"C:\Users\lwwwwww\Desktop\magic")
        os.system("python test.py  --dataroot ./datasets/edges2shoes/   --model pix2pix --name edges2shoes_pretrained")
        file_name=file_name.replace(".jpg","")
        return "http://192.168.1.106:5000/image/"+file_name     


# 定义路由 风格转换
@app.route("/photo2", methods=['POST'])
def get_frame2():              
    # 接收图片
    upload_file = request.files['file']
    # 获取图片名            
    file_name = upload_file.filename
    # 文件保存目录（桌面）
    file_path=r'C:\Users\lwwwwww\Desktop\magic\datasets\horse2zebra\testA'       
    if upload_file:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)              
        os.chdir(r"C:\Users\lwwwwww\Desktop\magic")
        os.system("python test.py --dataroot datasets/horse2zebra/testA --name horse2zebra_pretrained --model test --no_dropout")
        file_name=file_name.replace(".jpg","")
        return "http://192.168.1.106:5000/image2/"+file_name    
if __name__ == "__main__":
    app.run(host='192.168.1.106', port=5000)
