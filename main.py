import openai, requests
from myopenai import OpenAIRequest
from io import BytesIO
from PIL import Image 
from IPython.display import display

# Insert your auth key in the next line. You can generate the key in https://beta.openai.com/account/api-keys
openai = OpenAIRequest("xxxxxxxxxxxxxxxxxxxxxx")
model = "text-davinci-003"
n = 1
max_tokens = 4000
temperature = 0.7
best_of = 1
size = "512x512"
op = 0

while op != 3:
    op = int(input("\nChose which OpenAI feature you want to use:\n\n1 - Chat GPT\n2 - Dall-E\n3 - Exit\n\nAnswer: "))
    
    if op == 1:
        prompt = input("\nInsert the prompt for chat GPT or 'Options' to change default values: ")
        if prompt == 'Options':
            model = input("\nModel to be used in text generation (default value -> 'text-davinci-003'): ")
            n = int(input("Number of responses to be generated (default value -> 1): "))
            max_tokens = int(input("Number of tokens used for prompt and responses. Max to 4096  (default value -> 4000): "))
            print(type(max_tokens))
            temperature = float(input("Set the temperature level between 0 - more conservative response - and 1 - more 'creative' response (default value -> 0.7): "))
            best_of = int(input("Number of responses to be displayed from the generated answers (default value -> 1): "))
            prompt = input("\nInsert the prompt for chat GPT: ")
        
        chat = openai.callGPT(prompt, model, n, max_tokens, temperature, best_of)

    if op == 2:
        prompt = input("\nInsert the description of the image you want to generate or 'Options' to change default configuration values: ")
        if prompt == 'Options':
            size = input("\nInsert the size to be used in generated images. Must be one of '256x256', '512x512', or '1024x1024' (default value -> '512x512'): ")
            prompt = input("Insert the description of the image you want to generate: ")
        number_of_images = int(input("Insert the number of images to be generated: "))
        
        images = openai.callDalle(prompt, number_of_images, size)
        for url in images:
            print(url)
            response = requests.get(url)
            display(Image.open(BytesIO(response.content)))
