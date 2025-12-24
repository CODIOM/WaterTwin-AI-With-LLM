from google import genai
import os

class AIAdvisor:
    """
    AIAdvisor: The decision-support layer of the WaterTwin system.
    It utilizes Large Language Models (LLMs) to provide expert-level
    water management strategies based on simulation data.
    """
    def __init__(self):
        # Retrieve the API key from environment variables for security compliance
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # Using the state-of-the-art model for 2025 to ensure high reasoning capabilities
        self.model_id = "gemini-2.0-flash" 

    def get_strategic_advice(self, results):
        """
        Processes simulation results through the Gemini model to generate 
        actionable engineering recommendations.
        """
        # System Prompt: Defines the persona and boundaries for the AI's response
        system_prompt = """
        You are the Senior Water Management Engineer for the WaterTwin AI system. 
        Your task is to analyze simulation data and provide technical, 
        actionable, and water-conservation focused strategic recommendations.
        """
        
        # User Prompt: Feeds the specific numerical outputs from the Digital Twin engine
        user_prompt = f"""
        Analyze the following simulation data:
        - Incoming Inflow: {results['inflow_L']} L
        - Expected Overflow: {results['overflow_L']} L
        - Predicted Fill Rate: {results['final_fill_rate']}%
        
        Please provide a technical report in exactly 3 short sentences.
        """
        
        try:
            # Making the API call to generate content with system instructions
            response = self.client.models.generate_content(
                model=self.model_id,
                config={"system_instruction": system_prompt},
                contents=user_prompt
            )
            # Returning the processed text response from the AI
            return response.text
        except Exception as e:
            # Error handling to ensure the application does not crash during API failures
            return f"A technical issue occurred while generating the analysis report: {e}"