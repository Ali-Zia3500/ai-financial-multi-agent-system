import streamlit as st
import phi
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.getenv("GROQ_API_KEY")


# Web Search Agent
websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(
        id="llama3-groq-70b-8192-tool-use-preview"
    ),
    tools=[DuckDuckGo()],
    instructions=[
        "Provide only the direct answer to the query.",
        "Include sources when relevant but keep the response concise.",
        "Avoid unnecessary details or explanations."
    ],
    show_tool_calls=True,  
    markdown=True  
)

# Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(
        id="llama3-groq-70b-8192-tool-use-preview"
    ),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
            company_info=True
        )
    ],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=[
        "Provide concise answers.",
        "Use tables for financial data where applicable.",
        "Focus on clarity and directness."
    ],
    show_tool_calls=True,  
    markdown=True  
)

##GooGle Search AGent
google_search_agent = Agent(
    name = "Google Search Agent", 
    model=Groq(
        id="llama3-groq-70b-8192-tool-use-preview"
    ),
    tools=[GoogleSearch()],
    description="""You are a news agent that helps users find the latest news."""
,
    instructions=[
        "Given a topic by the user, respond with 4 latest news items about that topic.",
        "Search for 10 news items and select the top 4 unique items.",
        "Search in English."
    ],
    show_tool_calls=True,
    markdown=True
)



# Multi-Agent System
multi_ai_agent = Agent(
    name="Multi_Model_AI_Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    team=[websearch_agent, finance_agent,google_search_agent],

    instructions=[
    "First, gather general information related to the user's query using the Web Search Agent and Google Search Agent.",
    "Then, use the Finance AI Agent to provide financial data and insights if the query pertains to stocks, company fundamentals, or analyst recommendations.",
    "If the query is focused on financial news or updates, route it to the Google Search Agent to fetch the latest relevant news.",
    "For queries involving specific company names or analysts, ensure that the data is fetched from the appropriate agents (Finance AI Agent or Google Search Agent).",
    "Finally, compile and present a concise and clear response combining insights from all relevant agents."
    
    """
    Your primary goal is to deliver accurate, concise, and clear responses to user queries. You can handle:
    - Financial queries such as stock prices, market capitalization, or company fundamentals.
    - General knowledge questions by searching the web.
    - Latest news updates on financial or general topics.

   When a query involves multiple domains, you seamlessly integrate insights from all relevant agents to provide a comprehensive answer.
   If the requested information is unavailable or unclear, you suggest alternative reliable sources or steps for the user to find it.
    """

     ],
    show_tool_calls=True,  
    markdown=True  
)


#UI
def main():
    st.title("Multi-Agent Finance Hub📊")
    st.subheader("Your one-stop solution for financial data, news, and insights!")
    st.markdown("""
      Welcome! This platform brings together AI-powered agents to answer your queries about stocks, financial news, 
     and market trends. Start by typing your question below!
    """)
   
    with st.sidebar:
        st.title("Agents Overview")
        st.markdown("""
        -  **Web Search Agent🌐**: Searches the web for information.
        -  **Finance AI Agent📈**: Provides financial data and insights.
        -  **Google Search Agent📰**: Helps find the latest financial news.
        -  **Multi-Agent System🤝**: Combines all agents for comprehensive responses.
        """)


    query = st.text_input("Enter your query:🔍")
    if st.button("Submit Query"):
        if query:
            with st.spinner("Processing Your Query..."):

              response = multi_ai_agent.run(query)
              st.success("Done!")
              cleaned_response = response.content.replace("Note that the provided function is in Python.", "")
              st.write("Response:✨", cleaned_response)

    

if __name__ == "__main__":
    main()