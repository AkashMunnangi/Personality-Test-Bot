# OCEAN Personality Test Chatbot

A web-based personality test application that analyzes responses based on the OCEAN (Big Five) personality model. The application provides insights into five major personality traits:

- **O**penness to Experience
- **C**onscientiousness
- **E**xtraversion
- **A**greeableness
- **N**euroticism

## Features

- Interactive web interface
- Real-time response analysis
- Detailed personality trait descriptions
- Visual representation of results
- Responsive design

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Click "Start Test" to begin
2. Answer each question by selecting a number from 1 to 5
   - 1: Strongly Disagree
   - 2: Disagree
   - 3: Neutral
   - 4: Agree
   - 5: Strongly Agree
3. Click "Submit Answers" to see your results
4. Review your personality trait scores and descriptions

## Project Structure

- `app.py`: Main Flask application
- `personality_test.py`: OCEAN model implementation
- `templates/index.html`: Web interface
- `requirements.txt`: Project dependencies