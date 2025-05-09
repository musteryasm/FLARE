import torch
from ultralytics.nn.tasks import DetectionModel

torch.serialization.add_safe_globals([DetectionModel])

# Now you can load the model
model = torch.load('../best_nano_111.pt')
print(model)
