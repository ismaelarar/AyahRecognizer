import json
import os
from datetime import datetime

CONF_DIR = './AyahRecognizer/assistant_config'
API_FILE = f'{CONF_DIR}/API.txt'
SYSTEM_PROMPT_FILE = f'{CONF_DIR}/systemPrompt.json'
SYSTEM_PROMPT_MDFILE = f'{CONF_DIR}/systemPrompt.md'
USER_PROMPT_FILE = f'{CONF_DIR}/userPrompt.json'
LOGGER_FILE = f'{CONF_DIR}/responseLogger.log'

def check_file_exists(file_path, create_if_missing=False):
    if not os.path.exists(file_path):
        if create_if_missing:
            with open(file_path, 'w') as file:
                file.write('')
        else:
            raise FileNotFoundError(f"El archivo requerido '{file_path}' no se encuentra.")

def get_api_key():
    check_file_exists(API_FILE)
    with open(API_FILE) as api_file:
        return api_file.readline()

def get_system_prompt():
    check_file_exists(SYSTEM_PROMPT_MDFILE)
    check_file_exists(SYSTEM_PROMPT_FILE)
    with open(SYSTEM_PROMPT_MDFILE, "r") as md_file:
        md_text = json.dumps(md_file.read())[1:-1]

        with open(SYSTEM_PROMPT_FILE, "r") as file:
            return json.loads(file.read().replace("{text}", md_text))

def get_user_prompt(text):
    check_file_exists(USER_PROMPT_FILE)
    with open(USER_PROMPT_FILE, "r") as file:
        return json.loads(file.read().replace("{text}", text))
    
def get_completion(self, text):
        user_prompt = get_user_prompt(text)

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

def log_response(response):
    check_file_exists(LOGGER_FILE, True)
    logs=''
    with open(LOGGER_FILE, 'r') as log_file:
        logs = log_file.readlines()
        if (len(logs) >= 50):
            logs = logs[1:]

    with open(LOGGER_FILE, 'w') as log_file:
        logs.append(f'[{datetime.now()}] \t {response.model_dump_json()}\n')
        log_file.writelines(logs)

def matches_formatter(matches, split):
    spl = split.strip().lower()
    if (matches.strip().lower() != 'none'):
        if (spl == 'none'):
            return matches
        
        elif (spl == 'medium'):
            return matches.split("\n")
        
        elif (spl == 'full'):
            matches_dict = {}
            line_matches = matches.split("\n")
            for line in line_matches:
                if line != '':
                    match = line.split("|")
                    matches_dict[match[0].strip()] = match[1].strip()
            return matches_dict

        else:
            print(f"AVISO: El valor '{split}' no es un valor válido para 'split'. Los valores válidos son: 'none', 'medium' y 'full'. Se devolvió el resultado sin dividir.")
            return matches
    else:
        return None
