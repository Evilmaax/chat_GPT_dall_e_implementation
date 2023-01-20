import openai

class OpenAIRequest:

    def __init__(self, key):
        openai.api_key = key

    @staticmethod
    def callGPT(prompt, model, n, maxtokens, temperature, best_of):

        response = openai.Completion.create(
            prompt = prompt,
            model = model,
            n = n,
            max_tokens = maxtokens,
            temperature = temperature, 
            best_of = best_of
        )

        resp = []
        for x in range(len(response.choices)):
            print(response.choices[x].text)
            resp.append(response.choices[x].text)

        return resp   

    @staticmethod
    def callDalle(prompt, n, size, response_format="url"):

        response = openai.Image.create(
            prompt = prompt,
            n = n,
            size=size,
            response_format = response_format
        )

        resp = []
        for x in range(len(response.data)):
            resp.append(response.data[x].url)
        
        return resp   