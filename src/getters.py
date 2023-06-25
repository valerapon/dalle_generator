from typing import Optional
from src.dicts import CAT_TO_NUM, CAT_TO_PROMPT
import openai


def generate_image(
        cat_id: int,
        api_key: str,
        prompt: str,
) -> str:
        '''
        Генерируем картинку по текстовому запросу prompt.
        
        :param cat_id: номер категории
        :type cat_id: int
        :param api_key: API-ключ к системе OpenAI
        :type api_key: str
        :param prompt: текст запроса (промпт)
        :type prompt: str, optional
        
        :rtype: str
        :return: ссылка на изображение 
        '''

        if cat_id < 0 or cat_id >= len(CAT_TO_NUM):
                return 101, 'Incorrect value of cat_id: {0}'.format(cat_id)

        if prompt.strip() == '':
                prompt = CAT_TO_PROMPT[cat_id]

        try:
                openai.api_key = api_key
                response = openai.Image.create(
                        prompt=prompt,
                        n=1,
                        size="512x512"
                )
        except openai.error.AuthenticationError:
                return 102, 'Incorrect API key provided: {0}'.format(api_key)
        except openai.error.InvalidRequestError:
                return 103, 'Your request was rejected as a result of our safety system: {0}'.format(prompt)

        return 200, response['data'][0]['url']
