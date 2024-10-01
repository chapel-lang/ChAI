import torch.nn as nn
import torch
import sys
import os

from resnet import resnet50

model = resnet50(pretrained=True, progress=True, num_classes=1000)

# Add the scripts directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts')))

import chai

# model.chai_dump('models/resnet50','resnet50', with_json=False, verbose=True)



class Dummy(nn.Module):
    def __init__(self):
        super(Dummy, self).__init__()

        self.model = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False),
        )



class DummyTwo(nn.Module):
    def __init__(self, input_model):
        super(DummyTwo, self).__init__()
        self.model = nn.Sequential(
            input_model,
        )

dummy = Dummy()

dummy_two = DummyTwo(dummy)

dummy.chai_dump('models/dummy', 'dummy', with_json=False, verbose=True)
dummy_two.chai_dump('models/dummy_two', 'dummy_two', with_json=False, verbose=True)