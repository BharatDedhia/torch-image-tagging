import torch
from torchvision import models 
from torchvision import transforms
from flask import Flask, render_template, jsonify, request
import nltk
from nltk.corpus import wordnet

app = Flask(__name__) 
from PIL import Image
img = Image.open("/Users\hp\Pictures\Saved Pictures\pexels-lumn-406014.jpg").convert('RGB')
model = models.resnet50(pretrained = True)
model.eval()

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html") 


transform = transforms.Compose([            
 transforms.Resize(256),                    
 transforms.CenterCrop(224),                
 transforms.ToTensor(),                     
 transforms.Normalize(                      
 mean=[0.485, 0.456, 0.406],                
 std=[0.229, 0.224, 0.225]                  
 )])


img_t = transform(img)
batch_t = torch.unsqueeze(img_t, 0)
out = model(batch_t)

with open("/Users\hp\Downloads\imagenet_class_index.txt") as f:
  classes = [line.strip() for line in f.readlines()]

_, index = torch.max(out, 1)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
_, indices = torch.sort(out, descending=True)
cls = [(classes[idx], percentage[idx].item()) for idx in indices[0][:2]]
print("\n",cls,"\n")


a = [(classes[idx]) for idx in indices[0][:1]]
str1 = ''.join(a)
print(str1,"\n")

synonyms = []
for syn in wordnet.synsets(str1):
    for lm in syn.lemmas():
             synonyms.append(lm.name())#adding into synonyms
print(synonyms)


@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)
  

if __name__ == '__main__':  
    app.run(debug = True) 

# @app.route('/percentage', methods=['POST']) 
# def percentage():
#     if request.method == 'POST':
#         file = request.files['file']



# from flask import *  
# app = Flask(__name__)  
 
# @app.route('/')  
# def upload():  
#     return render_template("file_upload_form.html")  
 
# @app.route('/success', methods = ['POST'])  
# def success():  
#     if request.method == 'POST':  
#         f = request.files['file']  
#         f.save(f.filename)  
#         return render_template("success.html", name = f.filename)  
  
# if __name__ == '__main__':  
#     app.run(debug = True) 