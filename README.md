# 🧭 AI Career Pathfinder

**AI Career Pathfinder** is a web-based tool that offers personalized career advice using OpenAI's GPT-3.5 and Gradio. 
It helps users explore career directions based on their background, interests, values, and frustrations — all in a few easy steps.

## 🚀 Live Demo

👉 [Try the app here](https://huggingface.co/spaces/AminPourmohammadi/career-pathfinder)

## 🧠 What It Does

- Collects user input on their background, interests, values, and preferences
- Uses GPT to generate 3 career path suggestions
- Provides rationale and practical next steps for each path
- Offers guidance in a friendly, accessible way — no resume required

## 💡 Motivation

Many people feel lost in their career direction. This app was designed to:
- Offer structured guidance without overwhelming detail
- Use the power of LLMs to simulate personalized coaching
- Explore how prompt design can replace complex logic in early-stage AI tools

## 🛠 Tech Stack

- [OpenAI GPT-3.5](https://platform.openai.com/)
- [Gradio](https://www.gradio.app/) for the frontend UI
- [Hugging Face Spaces](https://huggingface.co/spaces) for deployment

## 📦 How to Run Locally

```bash
pip install gradio openai

Add your OpenAI key securely:

export OPENAI_API_KEY=sk-...

Then run the app:

python app.py
