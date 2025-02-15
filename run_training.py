import os
import subprocess
import torch

# Set environment variables for optimized GPU memory allocation
os.environ["TORCH_GPU_ALLOC_CONF"] = "max_split_size_mb:256"
# Enable TF32 for better CUDA performance

torch.backends.cuda.matmul.allow_tf32 = True

# Define the command to run training
train_command = [
    "accelerate", "launch", "diffusers/examples/text_to_image/train_text_to_image.py",
    "--pretrained_model_name_or_path=CompVis/stable-diffusion-v1-4",
    "--train_data_dir=processed_dataset/",
    "--use_ema",
    "--train_batch_size=2",
    "--gradient_accumulation_steps=2",
    "--gradient_checkpointing",
    "--mixed_precision=fp16",
    "--max_train_steps=1000",
    "--learning_rate=5e-6",
    "--max_grad_norm=1",
    "--lr_warmup_steps=0",
    "--use_8bit_adam",
    "--output_dir=fine_tuned_model"
]

# Execute the training command
subprocess.run(train_command)
