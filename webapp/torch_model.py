
import torch
import torch.nn as nn

# Check if CUDA is available and select device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

class SimpleNet(nn.Module):
    """
    A simple linear model: y = 2x + 1
    """
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        return self.fc(x)

# Initialize the model and set dummy weights
model = SimpleNet().to(device)
with torch.no_grad():
    model.fc.weight.fill_(2.0)
    model.fc.bias.fill_(1.0)

async def predict_async(x_value: float) -> float:
    """
    Run inference asynchronously on a single float input.

    Args:
        x_value (float): Input value.

    Returns:
        float: Model output.
    """
    # PyTorch is synchronous, but we can wrap in an async function
    x_tensor = torch.tensor([[x_value]], dtype=torch.float32, device=device)
    y_tensor = model(x_tensor)
    return y_tensor.item()
