import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def send_to_gemini(prompt):
    try:
        print("Consultando Gemini ...")
        genai.configure(api_key=os.getenv("GEMINI_API_KEY")) 
        model = genai.GenerativeModel('gemini-1.5-flash') 
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "Error in Gemini response."

def create_prompt(role, task, topic, specific_question):
    prompt = f"""<prompt>
                    <role>Your new role is {role}</role>
                    <topic>The topic of the task is {topic}</topic>
                    <task>
                        <description>Your task is to {task}</description>
                        <question>And the question that you need answers for is {specific_question}</question>
                    </task>
                    <format>
                        <instruction>Use this format to make it easy to understand:</instruction>
                            {{the answer generated by you}}
                    </format>
                </prompt>"""

    return prompt

def main():
    role = "especialista em filosofia e história da ciência"
    task = "explicar o pensamento de Descartes e sua influência para iniciantes em filosofia"
    topic = "René Descartes e o Método Cartesiano"
    specific_question = "Quem foi René Descartes e qual é o significado da frase 'Penso, logo existo'?"
    prompt = create_prompt(role, task, topic, specific_question)
    print("\n" + prompt)
    print("\n")
    response = send_to_gemini(prompt)
    print("\nResposta do Gemini 1.5 Flash:")
    print(response)

if __name__ == "__main__":
    main()