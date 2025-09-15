from flask import Flask, render_template, jsonify, request, send_from_directory
from personality_test import PersonalityTest
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static')
personality_test = PersonalityTest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    try:
        logger.debug("Fetching questions from PersonalityTest")
        questions = personality_test.get_questions()
        
        if not questions:
            logger.error("No questions returned from PersonalityTest")
            return jsonify({"error": "No questions available"}), 500
            
        logger.debug(f"Successfully retrieved {len(questions)} questions")
        return jsonify(questions)
    except Exception as e:
        logger.error(f"Error fetching questions: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze_responses():
    try:
        responses = request.json
        if not responses:
            return jsonify({"error": "No responses provided"}), 400
            
        results = personality_test.analyze_responses(responses)
        return jsonify(results)
    except Exception as e:
        logger.error(f"Error analyzing responses: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True) 