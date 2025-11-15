import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size) # First layer
        self.relu = nn.ReLU() # Activation function
        self.fc2 = nn.Linear(hidden_size, output_size) # Output layer

    def forward(self, x):
        x = self.fc1(x) # Pass through first layer
        x = self.relu(x) # Apply ReLU activation
        x = self.fc2(x) # Pass through output layer
        return x

# Example usage
input_size = 10
hidden_size = 20
output_size = 5
model = MyModel(input_size, hidden_size, output_size)

# Example input data
x = torch.randn(32, input_size) # Batch size of 32
output = model(x)
print(output.shape) # Output shape: (32, 5)