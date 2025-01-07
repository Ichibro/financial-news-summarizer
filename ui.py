import streamlit as st
from news_api import fetch_financial_news
import matplotlib.pyplot as plt

def plot_article_trends(articles):
    dates = [article['date'][:10] for article in articles]  # Extract date (YYYY-MM-DD)
    date_counts = {date: dates.count(date) for date in set(dates)}

    # Plot data
    fig, ax = plt.subplots()
    ax.bar(date_counts.keys(), date_counts.values(), color="skyblue")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Articles")
    ax.set_title("Articles Over Time")
    plt.xticks(rotation=45)

    return fig

# Streamlit app
st.title("Financial News Summarizer")
query = st.text_input("Search for financial news:")

if st.button("Fetch Articles"):
    if query:
        # Fetch articles
        articles = fetch_financial_news(query, max_items=50)
        
        if articles:
            # Display the chart
            st.write("### Articles Over Time")
            st.pyplot(plot_article_trends(articles))
            
            # Display the articles
            st.write("### News Articles")
            for article in articles:
                st.subheader(article['title'])
                st.write(article['description'])
                st.write(f"[Read More]({article['url']})")
                st.write("---")
        else:
            st.write("No articles found. Try a different query.")
    else:
        st.write("Please enter a search term.")
