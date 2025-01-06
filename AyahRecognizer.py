from openai import OpenAI
import AyahRecognizerUtils as utils

class AyahRecognizer:

    def __init__(self, client_name="openai"):

        self.client_name = client_name.strip().lower()
        self.system_prompt = utils.get_system_prompt()

        if self.client_name == "openai":
            self.client = OpenAI(
                api_key=utils.get_api_key()
            )
            self.model = "gpt-4o"
        else:
            raise Exception(f"El cliente {client_name} no está soportado. Clientes soportados: 'OpenAI'.")

    def recognize_ayaat(self, text):
        try:

            completion = self.get_completion(text)
            utils.log_response(completion)

            result = completion.choices[0].message.content
            return utils.matches_formatter(result)
            
        except Exception as e:
            print("Error al conectar con la API, revisa el fichero ./assistant_config/API.txt")
            print(f"Error inesperado: {str(e)}")

    def get_completion(self, text):
        user_prompt = utils.get_user_prompt(text)

        if self.client_name == "openai":
            return self.client.chat.completions.create(
                model=self.model,
                messages=[
                    self.system_prompt,
                    user_prompt
                ]
            )
        else:
            return None