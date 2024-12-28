# **AI Financial Multi-Agent System**

This project is an advanced AI-powered multi-agent system designed to handle financial and market-related queries. It integrates multiple specialized agents to provide accurate and real-time responses to user queries about stock prices, company fundamentals, market news, and more.

# **Features**
**1. Web Search Agent:** 

Searches the web for general information.


**2. Finance AI Agent:** 

Provides financial data, including stock prices, market capitalization, company fundamentals, and analyst recommendations.


**3. Google Search Agent:** 

Fetches the latest financial news and insights.


**4. Multi-Agent System:** 

Combines all agents to deliver comprehensive and concise answers to user queries.

# **How It Works**


**User Input:**

Users enter their query.

**Agent Routing:**

**Financial queries** (e.g., stock prices, company fundamentals) are handled by the Finance AI Agent.

**Web Search Agent or Google Search Agent** are handled General or market-related questions.

**Multi-Agent System** combines insights from all relevant agents and displays the response to the user.

# **Obtaining the Groq API**

Visit https://console.groq.com/keys and sign up for an account.

Navigate to the API section to generate your API key.

Copy the API key for integration into the application.
# **Technologies Used**

**Programming Language:** 

Python

**Framework:** 

Streamlit

**AI Model:** 

**Groq Llama3 (70B preview)**

**Tools:**

**DuckDuckGo Search API**

**Yahoo Finance API**

**Google Search API**

**Environment Management:**

Python dotenv


# **Clone the Repository**

git clone https://github.com/Ali-Zia3500/ai-financial-multi-agent-system.git  
# **Install Dependencies** 

pip install -r requirements.txt  

# **Run the Application**

streamlit run app.py
