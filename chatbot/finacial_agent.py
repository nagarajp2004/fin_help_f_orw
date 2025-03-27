from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Define the agent
web_agent = Agent(
    name="web search agent",
    role="search web for information",
    model=Groq(id="llama-3.2-3b-preview"),
 
    instructions=["Give in one line", "Everything must be related to finance"],
   # ✅ Disable tool calls output
    markdown=True
)

# Function to get the response
def get_financial_response(query):
    response = web_agent.run(message=query, stream=False)
    
    # ✅ Extracting the response content properly
    if hasattr(response, 'content'):
        return response.content
    else:
        return "No valid response received."

# ✅ Testing it
if __name__ == "__main__":
    print(get_financial_response("What is EMI in 5 sentences?"))
