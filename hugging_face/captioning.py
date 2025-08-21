#install the transformers library
!pip install transformers Pillow torch torchvision torchaudio
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

#Initialise the processor and model from Hugging face
print("hello world")

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

image = Image.open("C:/Users/anush/Downloads/cat.jpg")

inputs = processor(image, return_tensors="pt")

outputs = model.generate(**inputs)
caption = processor.decode(outputs[0], skip_special_tokens=True)

print("Generated captions:", caption)

#run on the terminal. and look for the output string Generated Captions:
#Generated captions: a cat sitting on a wooden table with a watermel
