import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")  
print(f"CUDA version: {torch.version.cuda}")           
print(f"GPU model: {torch.cuda.get_device_name(0)}")   
print(f"Current device: {torch.cuda.current_device()}")
