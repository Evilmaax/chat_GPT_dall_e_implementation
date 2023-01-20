# Chat GPT and Dall-e implementation

This is a small implementation to consume Chat GPT and Dall-E image generator through the OpenAI API.

To use you need Python and the OpenAI library on your machine. In order tu install the OpenAI lib, run the following command: 

`pip install openai`

## Basic configuration

To use this tool you need a OpenAI api key. [You can generate your key here][1].
After that, place your key in the specified place in code:

`MY_KEY = "xxxxxxxxxxxxxxxxxxxxxx"`

Be aware that the usage of this API **may incur in billing**. 
If you're creating your account, don't worry: New users receive sufficient credit to run hundreds of tests. 

## Usage

After setting the API key you just need to run one of the main files: 

* **main.ipynb** in your prefered notebook platform or 
* **main.py** in your IDE of choice or even in the terminal.

The tool has a menu which you can navigate to perform the actions:

* 1 - Chat GPT
* 2 - Dall-E

Each option has its own configurable values:

### Chat GPT config

* **model**: Model to be used in text generation. Eg: 'text-davinci-003', 'text-curie-001', etc. Default value -> 'text-davinci-003'. [Details of each one can be found here][2];
* **n**: Number of responses to be generated. Default value -> 1;
* **max_tokens**: Maximum number of tokens used for prompt and responses. Notice that ponctuation and prompt also count. Max value vary according to the model you're uisng. Max value for 'text-davinci-003' is 4000, for others is 2048. Default value -> 4000;
* **temperature**: The temperature level vary between 0 - generates a more conservative response - and 1 - generates a more 'creative' response. Default value -> 0.7;
* **best_of**: Number of responses to be displayed from the 'N' generated answers you set before, Default value -> 1;

### Dall-E config

[1]:https://beta.openai.com/account/api-keys
[2]:https://beta.openai.com/docs/models/gpt-3
