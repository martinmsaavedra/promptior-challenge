from flask import Flask, request, jsonify, render_template
from langchain_processor.langchain_processor import process_question_with_langchain

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question', '')
    answer = process_question_with_langchain(question)
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
