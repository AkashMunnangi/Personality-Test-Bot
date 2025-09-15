import json
import numpy as np

class PersonalityTest:
    def __init__(self):
        self.questions = [
            {
                "text": "I am the life of the party.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Extraversion"
            },
            {
                "text": "I feel little concern for others.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Agreeableness"
            },
            {
                "text": "I am always prepared.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Conscientiousness"
            },
            {
                "text": "I get stressed out easily.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Neuroticism"
            },
            {
                "text": "I have a rikch vocabulary.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Openness"
            },
            {
                "text": "I don't talk a lot.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Extraversion"
            },
            {
                "text": "I am interested in people.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Agreeableness"
            },
            {
                "text": "I leave my belongings around.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Conscientiousness"
            },
            {
                "text": "I am relaxed most of the time.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Neuroticism"
            },
            {
                "text": "I have difficulty understanding abstract ideas.",
                "options": ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                "trait": "Openness"
            }
        ]

    def get_questions(self):
        return self.questions

    def analyze_responses(self, responses):
        try:
            # Convert responses to integers if they're strings
            responses = {int(k): int(v) for k, v in responses.items()}
            
            # Initialize scores for each trait
            scores = {
                "Openness": 0,
                "Conscientiousness": 0,
                "Extraversion": 0,
                "Agreeableness": 0,
                "Neuroticism": 0
            }

            # Calculate scores based on responses
            for i, response in responses.items():
                trait = self.questions[i]["trait"]
                # Convert response (0-4) to score (1-5)
                score = response + 1
                scores[trait] += score

            # Calculate average scores
            trait_counts = {
                "Openness": 2,
                "Conscientiousness": 2,
                "Extraversion": 2,
                "Agreeableness": 2,
                "Neuroticism": 2
            }

            for trait in scores:
                scores[trait] = round(scores[trait] / trait_counts[trait], 1)

            # Determine personality type based on scores
            personality_type = self.determine_personality_type(scores)

            return {
                "scores": scores,
                "personality_type": personality_type,
                "strengths": self.get_strengths(scores),
                "growth_areas": self.get_growth_areas(scores),
                "communication_style": self.get_communication_style(scores)
            }
        except Exception as e:
            print(f"Error in analyze_responses: {str(e)}")
            raise

    def determine_personality_type(self, scores):
        # Simple personality type determination based on highest scores
        max_trait = max(scores.items(), key=lambda x: x[1])[0]
        return f"Your personality is most aligned with {max_trait}"

    def get_strengths(self, scores):
        strengths = []
        for trait, score in scores.items():
            if score >= 4:
                strengths.append(f"Strong {trait.lower()}")
        return strengths

    def get_growth_areas(self, scores):
        growth_areas = []
        for trait, score in scores.items():
            if score <= 2:
                growth_areas.append(f"Develop {trait.lower()}")
        return growth_areas

    def get_communication_style(self, scores):
        styles = []
        if scores["Extraversion"] >= 4:
            styles.append("Outgoing and expressive")
        elif scores["Extraversion"] <= 2:
            styles.append("Reserved and thoughtful")
        
        if scores["Agreeableness"] >= 4:
            styles.append("Empathetic and supportive")
        elif scores["Agreeableness"] <= 2:
            styles.append("Direct and assertive")
        
        return styles
