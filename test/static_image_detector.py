import torch

# Import the model
## Loading in Local Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights\weight_v2.pt', force_reload=True)

## Loading in Local yolov5 repo
model = torch.hub.load('yolov5', 'custom', path="weights\weight_v2.pt", source='local')

# Static Image validation
img = ['resources/test_image_01.jpg', 'resources/test_image_02.jpg','resources/test_image_03.jpg','resources/test_image_04.jpg','resources/test_image_05.jpg']
# img = 'resources/test_image_01.jpg'
# Inference
results = model(img)

# Results
results.print()
print(results.pandas().xyxy[0])