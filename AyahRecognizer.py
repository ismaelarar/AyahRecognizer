from openai import OpenAI, APIConnectionError
import AyahRecognizerUtils as utils

client = OpenAI(
    api_key=utils.get_api_key()
)

def recognize_ayaat(text):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                utils.get_system_prompt(),
                utils.get_user_prompt(text)
            ]
        )
        utils.log_response(completion)

        result = completion.choices[0].message.content
        return utils.matches_formatter(result)
    except APIConnectionError:
        raise Exception("Error al conectar con OpenAI, revisa el fichero ./assistant_config/API.txt")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
