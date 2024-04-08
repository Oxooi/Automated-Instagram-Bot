import base64
import requests

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def describe_image(image_path, openai_api_key):

    # Getting the b64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Envision a captivating scene unfolding before you. Create a compelling title for this scene as if you were naming a piece of art (don't add the Title:). Additionally, generate a description and a list of hashtags that capture the essence of the scene (seperate them), the themes, the main objects, and the mood. Include the following hashtags in your list: #ai, #dalle-3, #openai, #python, #bot, #gpt. Ensure the title is evocative and suitable for captivating an audience on Instagram. and add after the title this disclaimer : Disclaimer: This content, including the image creation, analysis for generating descriptions and hashtags, and the posting process to Instagram, was fully automated by a bot developed in Python, utilizing DALL-E 3 and GPT Vision. This project serves as a demonstration of AI capabilities in digital content creation for educational purposes. #AIPowered #PythonBot #DallE3 #GPTVision #StudentProject #AIBot",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "max_tokens": 300,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )

    # Convert the response in JSON format
    json_reponse = response.json()

    # Extract the 'content' value
    if json_reponse.get("choices"):  # Vérifie si 'choices' existe
        first_choice = json_reponse["choices"][0]
        if first_choice.get(
            "message"
        ):  # Vérifie si 'message' existe dans la première 'choice'
            content = first_choice["message"]["content"]

            # Print in the console the result
            print(content.encode("utf-8", errors="replace").decode("utf-8"))

            # Write the result in the "./content.txt"
            with open("content.txt", "w") as fileH:
                fileH.write(content)

            return content
        else:
            print("Aucun 'message' trouvé dans la première 'choice'.")
    else:
        print("Aucune 'choice' trouvée dans la réponse.")
