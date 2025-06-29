import gradio as gr
from openai import OpenAI
import os

openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key)

def generate_career_advice(name, background, interests, values, preferences, pain_points):
    try:
        system_prompt = """
        You are a thoughtful and strategic career coach. When a user describes their background, interests, values, and frustrations, you suggest 3 realistic career paths. For each path, include:
        - a short description
        - why it's a good fit for them
        - 2-3 next steps they can take to explore it.

        Keep the tone clear, encouraging, and practical.
        """
        user_prompt = f"""
        Name: {name}
        Background: {background}
        Interests: {interests}
        Values: {values}
        Work Preferences: {preferences}
        Pain Points / Frustrations: {pain_points}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


iface = gr.Interface(
    fn=generate_career_advice,
    inputs=[
        gr.Textbox(label="Your Name"),
        gr.Textbox(label="Your Background (education, job experience, skills)", lines=3),
        gr.Textbox(label="Your Interests (what excites you?)", lines=2),
        gr.Textbox(label="Your Core Values (e.g., impact, freedom, money)", lines=2),
        gr.Textbox(label="Your Preferences (e.g., remote, small teams, flexible hours)", lines=2),
        gr.Textbox(label="Your Frustrations (e.g., burnout, boredom, stuck)", lines=2),
    ],
    outputs=gr.Textbox(label="Career Advice", lines=15),
    title="🧭 AI Career Pathfinder",
    description="Get 3 customized career paths based on your background, interests, and goals."
)

iface.launch()
