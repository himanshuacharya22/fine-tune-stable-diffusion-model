from diffusers import StableDiffusionPipeline
import torch

# Path to your fine-tuned model
model_path = "fine_tuned_model"  # Change this if needed

# Load the fine-tuned model
pipe = StableDiffusionPipeline.from_pretrained(
    model_path,
    torch_dtype=torch.float16  # Use float16 for efficiency
)

# Move the model to GPU if available
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Generate an image using the fine-tuned model
prompt = "a painting of lord ganesha he is standing with one leg lifted in air"
images = pipe(prompt).images

# Save and display the generated images
for i,image in enumerate(images):
  image.save(f"fine_tuned_output {i}.png")
  image.show()


