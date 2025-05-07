
from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Use the API key from an environment variable
API_KEY = os.getenv("API_KEY")  # Make sure this matches the name you set in Render

if not API_KEY:
    raise ValueError("API_KEY environment variable not set")

genai.configure(api_key=API_KEY)

# ✅ Initialize model
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

# ✅ Bind to host=0.0.0.0 and use PORT from Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 for local dev
    app.run(host='0.0.0.0', port=port)