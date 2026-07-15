import time
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer

# 1. Pre-trained Vision aur Text Transformer Models ko load karna
print("🤖 Loading Vision-Text Transformer Pipeline...")
print("(Pehli baar run hone par models download honge, so it might take 1-2 minutes...)\n")

# Hum use kar rahe hain ViT (Image Feature Extractor) + GPT2 (Text Generator)
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("✅ Systems Online! Model loaded successfully.\n")


def generate_caption(image_path):
    try:
        # Image ko load aur RGB format mein convert karna
        img = Image.open(image_path)
        if img.mode != "RGB":
            img = img.convert(mode="RGB")

        print("👁️  Extracting visual features from the image...")
        time.sleep(1.2)  # Human touch: Realistic delay

        # FEATURE EXTRACTION: Image ko tokens/pixel values mein badalna
        pixel_values = feature_extractor(images=[img], return_tensors="pt").pixel_values

        print("✍️  Transformer Decoder is generating the text description...")
        time.sleep(1.0)

        # CAPTION GENERATION: Agla word predict karna
        output_ids = model.generate(pixel_values, max_length=16, num_beams=4)

        # Output tokens ko wapas text mein decode karna
        preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        return preds[0].strip().capitalize()

    except FileNotFoundError:
        return "❌ Error: Boss, file nahi mili! Check karo ki image folder mein sahi naam se saved hai ya nahi."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"


# --- MAIN LOOP ---
print("📸 Welcome to the AI Image Captioning Tool 📸")
print("Apni koi bhi photo (.png/.jpg) is project folder ke andar daal dein.")

while True:
    file_input = input("\nEnter image filename (e.g., dog.jpg) or type 'exit': ").strip()

    if file_input.lower() == 'exit':
        print("\n🚀 Task 3 Completed! Ready to submit to CodSoft. Goodbye!")
        break

    if not file_input:
        continue

    # Caption nikalna
    caption_result = generate_caption(file_input)

    print("=" * 60)
    print(f"📝 AI Caption: \"{caption_result}\"")
    print("=" * 60)