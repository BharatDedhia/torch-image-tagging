<h1>IMAGE TAGGING</h1>
<b>Domain:</b> AI, ML/DL, Image Processing.<br>
<b>Description:</b>
There are already popular models that will allow to find and determine what objects are present in an image. This use case takes the same one level further, it also contains association of tags to the images to improve their searchability. The same can be done on 2 levels, the basic level being to tag using similar meaning words which is quite simple. And the more advanced version of the same being that the interns will have to find associated words too. So, for example, if crown is an object detected, king and queen should also be tagged.


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Objectives and Features Completed](#Objectives-and-Features-Completed)
- [Usage](#usage)
  - [Installation](#installation)
- [Strengths And Weaknesses](#Strengths-And-Weaknesses)
  - Strengths(#strengths)
  - Weaknesses(#weaknesses)
- [Team](#team)
  - [Mentors:](#mentors)
  - [Members:](#members)
- [Conclusion](#Conclusion)


## Objectives and Features Completed:

1.	Loaded a pretrained model - We have successfully loaded a pretrained model - RESNET 50 (Residual Network with 50 layers) which is trained on imagenet dataset.
2.	Loaded a dataset - ImageNet dataset has over 14 million images maintained by Stanford University. It is extensively used for a large variety of Image related deep learning projects. The images belong to various classes or labels.
3.	Specify image transformations- Various transformations like resize, center crop, normalization, etc are specified.
4.	Load the image and pre-process it - Read the input image and perform the image transformations specified.
5.	Model Interference - Use the pre-trained weights to find out the output vector. Each element in this output vector describes the confidence with which the model predicts the input image to belong to a particular class.
6.	Forward Pass: Based on the scores obtained, display the predictions.
7.	Give the synonyms for the prediction of the image using Natural Language Toolkit (NLTK) Library.

## Usage

### Installation 
Initially we installed TorchVision module using the command given below

 <i>pip install torchvision</i>

Next, we imported models from torchvision module

 <i>from torchvision install models<br>
 import torch<br>
 dir (models)</i>

Once we have the model with us, the next step is to transform the input image so that they have the right shape and other characteristics like mean and standard deviation. We can pre-process the input image with the help of transforms present in TochVision module.

 <i>from torchvision import transforms<br>
 transform = transforms.Compose([<br>
 transforms.Resize(256),<br>
 transforms.CenterCrop(224),<br>
 transforms.ToTensor(),<br>
 transforms.Normalize(<br>
 mean = [0.485, 0.456, 0.406],<br>
 std = [0.229, 0.224, 0.225],<br>
 )])</i>

Now to input image and carry out the image transformations we have specified above. We have used Pillow (PIL) module extensively with TorchVision as it’s the default image backend supported by TorchVision.

 (# Import Pillow)<br>
from PIL import Image

Next, we imported NTLK library and installed Wordnet to get a collection of words and vocabulary from English language that are related to each other and grouped in some other ways.

 <i>import nltk<br>
 nltk.download('wordnet')</i>

## Strengths And Weaknesses:

We can here summaries some of the strength and weaknesses of our project.

### Strengths:
•	Human error and bias are minimized (fewer decisions are required by the user).<br>
•	More uniform classes are produced as output.<br>
•	Spectrally distinct classes present in the data may be revealed which were not initially apparent to the user.<br>
•	Our project goes one step further and has an added advantage over other pre-trained models; In the output our model gives out words related to object in the image instead of just stating the obvious.<br>
•	We have to keep the backbone part obtained from the pretrained model fixed and only allow the parameters of the classifier to change. This approach is ideal when you want to train a model quickly or without much computational resources.

### Weaknesses:
•	Spectral grouping produced by the classifier may not correspond to the information classes of interest to the user.<br>
•	There is limited control over the 'menu' of classes.<br>
•	The performance of our model in this case might not be the best because the pretrained backbone may suffer from domain adaptation.

## Team

### Mentors:
Irfan Siddavatam [ irfansiddavatam@somaiya.edu ]<br>
Ashwini Dalvi [ ashwinidalvi@somaiya.edu ]<br>
Hetul Mehta [ hetul.mehta@somaiya.edu ]<br>
Burhan Plumber [ b.plumber@somaiya.edu ]

### Members:
| Sr No. | Name            | E-mail                      | Git-Profile                     |
| ------ | --------------- | --------------------------- | ------------------------------- |
| 1.     | Bharat Dedhia   | bharat.dedhia@somaiya.edu   | https://github.com/BharatDedhia |
| 2.     | Hetvi Shah      | hetvi.shah6@somaiya.edu     | https://github.com/Hetvishah24  |
| 3.     | Ankit Jha       | jha.an@somaiya.edu          | https://github.com/AnkitJha06   |
| 4.     | Preeti Shah     | preeti.shah@somaiya.edu     | https://github.com/PreetiShah09 |
| 5.     | Siddhant Chopda | siddhant.chopda@somaiya.edu | https://github.com/siddhant7890 |
| 6.     | Riddhi Gandhi   | riddhi.ng@somaiya.edu       | http://github.com/Riddhi-Gandhi |

## Conclusion:

In a nutshell, this internship has been an excellent and rewarding experience. We can conclude that there has been a lot that we’ve learnt from our work here. Two skills that we developed during the course of this internship are <b>managing time efficiently and secondly working together in a group environment</b>. We were able to build a good connection with each other and we have a much better understanding in regards to deep learning and more specifically <b>object detection</b>. Moreover, we would like to thank our mentors <b>Hetul Mehta, Burhan Plumber, Irfan Siddavatam sir and Ashwini Dalvi Ma’am</b>; they left no stone unturned in guiding us to the best of their knowledge. Overall, our internship has been a success and being a part of such a great organization speaks for itself, we couldn't be more thankful.
