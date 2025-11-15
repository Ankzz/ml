import torch
import torch.nn as nn
import matplotlib.pyplot as plt
# Set random seed for reproducibility
torch.manual_seed(42)
# Create random features and target variable
num_samples = 1000
x = torch.randn(num_samples, 2)
true_weights = torch.tensor([1.3, -1])
true_bias = torch.tensor([-3.5])
y = x @ true_weights.T + true_bias
# Define the model
class LinearRegression(nn.Module):
   def __init__(self, input_size, output_size):
       super(LinearRegression, self).__init__()
       self.linear = nn.Linear(input_size, output_size)
   def forward(self, x):
       return self.linear(x)
# Instantiate the model
input_size = x.shape[1]
output_size = 1
model = LinearRegression(input_size, output_size)
# Define the loss function
def mean_squared_error(prediction, actual):
   error = (actual - prediction) ** 2
   return error.mean()
# Training loop
num_epochs = 1000
learning_rate = 0.01
for epoch in range(num_epochs):
   # Forward pass
   y_p = model(x)
   loss = mean_squared_error(y_p, y)
   # Backpropagation
   loss.backward()
   with torch.no_grad():
       for param in model.parameters():
           param -= learning_rate * param.grad
       model.zero_grad()
   if (epoch + 1) % 100 == 0:
       print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
# Print the final weights and bias
w = model.linear.weight
b = model.linear.bias
print(f'Weight: {w.detach().numpy()}, Bias: {b.detach().numpy()}')