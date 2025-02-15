# Fine-Tuning Stable Diffusion

This repository contains scripts for fine-tuning a Stable Diffusion model on a custom dataset.

## Project Structure

```
.
├── dataset/                 # Raw images for training
│   ├── ganesha1.jpg
│   ├── .....
│   ├── metadata.jsonl       # Metadata file with text descriptions
├── processed_dataset/       # Preprocessed images (resized)
├── fine_tuned_model/       # Output directory for the fine-tuned model
├── main.py                 # Script to generate images using the fine-tuned model
├── preprocess_images.py     # Script to preprocess images for training
├── run_training.py          # Script to train the model
├── requirements.txt         # List of dependencies
└── README.md               # Project documentation
```

## Setup Instructions

### 1. Install Dependencies

Clone the diffuesers repo from hugging face 
```sh
git clone https://github.com/huggingface/diffusers
```
Ensure you have the required Python libraries installed:

```sh
pip install -r requirements.txt
```

### 2. Preprocess Images

Resize and prepare images for training<br>
Copy your metadata.jsonl file in this folder 

```sh
python preprocess_images.py
```

### 3. Train the Model

Start the fine-tuning process:

```sh
python run_training.py
```

### 4. Generate Images

Use the fine-tuned model to generate images:

```sh
python main.py
```

## Dataset Format

The dataset consists of images of Lord Ganesha along with a metadata file (`metadata.jsonl`) containing textual descriptions for each image. Example format:

```json
{
  "file_name": "ganesha1.jpg",
  "text": "a image of lord ganesha with his four hands"
}
```

## Notes

- Ensure you have a GPU with sufficient VRAM for training.
- Modify `run_training.py` parameters to adjust batch size, learning rate, and training steps.
---

### Author

himanshuacharya22

