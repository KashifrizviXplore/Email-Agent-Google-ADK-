from google.adk.agents import Agent
from pydantic import BaseModel, Field
from google.adk.agents import SequentialAgent



# Step 1: Root Email Generator Agent
root_email_agent_step = Agent(
    name="EmailGeneratorAgent",
    model="gemini-2.0-flash",
    instruction="""
        You are an Email Generation Assistant.
        Generate a professional email based on the user's request.
        Output JSON only with:
        {
            "subject": "...",
            "body": "..."
        }
    """,
    description="Generates the initial email subject and body.",
    output_key="generated_email"
)

# Step 2: Grammar Polisher Agent
grammar_polisher_agent = Agent(
    name="GrammarPolisherAgent",
    model="gemini-2.0-flash",
    instruction="""
        You are a grammar expert.
        Take the email body and polish it:
        - Correct grammar mistakes
        - Improve clarity and readability
        - Keep tone consistent
        Respond ONLY with the corrected email body.
    """,
    description="Polishes grammar of the email body.",
    output_key="polished_body"
)

# Step 3: Email Formatter Agent
formatter_agent = Agent(
    name="EmailFormatterAgent",
    model="gemini-2.0-flash",
    instruction="""
        You are an email formatting assistant.
        Format the polished email body for professional readability:
        - Add proper line breaks and paragraphs
        - Ensure clean structure with greeting, content, and closing
        Respond ONLY with the formatted email body.
    """,
    description="Formats email body for professional presentation.",
    output_key="formatted_body"
)

# --- 2. Create the SequentialAgent ---
email_pipeline_agent = SequentialAgent(
    name="EmailPipelineAgent",
    sub_agents=[
        root_email_agent_step,
        grammar_polisher_agent,
        formatter_agent
    ],
    description="Runs email generation, grammar polishing, and formatting sequentially."
)

# The root agent that will be called by your system
root_agent = email_pipeline_agent






