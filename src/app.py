import torch
from torchvision import models 
from torchvision import transforms
from flask import Flask, render_template, jsonify, request
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from os import path

app = Flask(__name__, static_folder=path.join("..","static")) 
from PIL import Image
model = models.resnet50(pretrained = True)
model.eval()

@app.route('/')  
def upload():  
    return render_template("index.html") 


transform = transforms.Compose([            
 transforms.Resize(256),                    
 transforms.CenterCrop(224),                
 transforms.ToTensor(),                     
 transforms.Normalize(                      
 mean=[0.485, 0.456, 0.406],                
 std=[0.229, 0.224, 0.225]                  
 )])

def get_tags(img_file):
    img = Image.open(img_file).convert('RGB')
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)
    out = model(batch_t)

    classes_file = path.join("static","files","imagenet_classes.txt")
    with open(classes_file) as f:
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

    return cls, str1, synonyms


@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        img_file = path.join("static","images",f.filename)
        f.save(img_file)
        tags = get_tags(img_file)
        return render_template("success.html", name = f.filename, tags = tags, path = img_file)
  

if __name__ == '__main__':  
    app.run(debug = True) 
