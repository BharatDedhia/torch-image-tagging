resnet = models.resnet50(pretrained=True)
from torchvision import transforms
transform = transforms.Compose([           
 transforms.Resize(256),                    
 transforms.CenterCrop(224),                
 transforms.ToTensor(),                    
 transforms.Normalize(                   
 mean=[0.485, 0.456, 0.406],               
 std=[0.229, 0.224, 0.225]                 
 )])
from PIL import Image
img = Image.open()
img_t = transform(img)
batch_t = torch.unsqueeze(img_t, 0)
resnet.eval()
out = resnet(batch_t)
print(out.shape)
with open() as f:
  classes = [line.strip() for line in f.readlines()]
_, index = torch.max(out, 1)
percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
_, indices = torch.sort(out, descending=True)
[(classes[idx], percentage[idx].item()) for idx in indices[0][:5]]