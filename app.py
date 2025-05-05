import os
GOOGLE_API_KEY = os.getenv("AIzaSyDTgJIkx0nyKYIRRm98pMQNt1oGdWaGIuw")

from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Replace with your real API key
API_KEY = "AIzaSyDTgJIkx0nyKYIRRm98pMQNt1oGdWaGIuw"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    title = request.form['title']
    keywords = request.form['keywords']
    word_count = request.form['word_count']

    prompt = f"Write a blog with approximately {word_count} words on the topic '{title}' using keywords: {keywords}."

    try:
        response = model.generate_content(prompt)
        blog_text = response.text
        return render_template('result.html', blog=blog_text, title=title)
    except Exception as e:
        return f"Error generating blog: {e}"

if __name__ == '__main__':
    app.run(debug=True)