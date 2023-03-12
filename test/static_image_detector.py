import torch

# Import the model
## Loading in Local Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/kessmith/Documents/Projects/Thesis/NN_RealTime_Detector/weights/best.pt', force_reload=True)

## Loading in Local yolov5 repo
model = torch.hub.load('/Users/kessmith/Documents/Projects/Thesis/yolov5', 'custom', path='/Users/kessmith/Documents/Projects/Thesis/NN_RealTime_Detector/weights/best.pt', source='local')

# Static Image validation
img = ['resources/sample_image.jpg']

# Inference
results = model(img)

# Results
results.print()
results.show()