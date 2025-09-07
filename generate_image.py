from huggingface_hub import InferenceClient


TOKEN = "hf_your_TOKEN"

# Connect to the Hugging Face Together model
client = InferenceClient(
    provider="together",
    api_key=TOKEN,
)

# Generate an image from text
image = client.text_to_image(
    prompt="A field with pink roses",
    model="black-forest-labs/FLUX.1-dev",
)

# Save the image
image.save("generated_image.png")
print("✅ Image generated and saved as generated_image.png")
