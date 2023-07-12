import torch

def predict(X):
    X = torch.tensor(X,dtype=torch.float32)
    existing_model_path = "epoch_1000.pt"
    model = torch.load(existing_model_path)
    with torch.no_grad():
        return model(X)
    