import srt
from openai import OpenAI 
import json

#Authorization: Bearer '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'

client = OpenAI()

subtitle_dir = '/home/mackintosh/Projects/Shop/Ucontent_subs'
output_dir = subtitle_dir
#openai.api_key = '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'
original_language = 'english'
translate_languages = ['german']



with open(f'{subtitle_dir}/Friends_Everybody_Hates_Chandler_en.srt') as f:
    subs = list(srt.parse(f))


def translate_subs(subs, language):
    input_text = {
        'role': 'user',
        'content': subs
    }
    messages = [
        {
        'role': 'system',
        'content' : f"""You are a great translator responsible for translating subtitles from english to {language}. 
        Translate the following subtitle. Target language is: {language}"""},
        input_text]
    completion= client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = messages)
    
    result = completion.choices[0].message.content
    
    
    try:
        result =  json.loads(result)['choices'][0]['messages']['content']
    except:
        print("[] Things went badly.")
    
    
    translated_sub = result.strip()
    return translated_sub



for sub in subs:

    print(f"""subs in english: {sub.content} for sub index {sub.index}\n translation to german: {translate_subs(sub.content, translate_languages[0])} """)





