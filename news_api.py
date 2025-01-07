from eventregistry import EventRegistry, QueryArticlesIter
from database import initialize_database, save_articles

# Replace YOUR_API_KEY with your actual Event Registry API key
API_KEY = '0a0fae97-893e-4c71-8d23-c68b97126df7'
er = EventRegistry(apiKey=API_KEY)

def fetch_financial_news(query, max_items=20):
    """
    Fetch financial news articles using Event Registry.
    
    Args:
        query (str): The search query (e.g., "stock market").
        max_items (int): Maximum number of articles to fetch.

    Returns:
        list: A list of articles with titles, descriptions, and URLs.
    """
    # Define the query
    q = QueryArticlesIter(
        keywords=query,          # Search for the given keywords
        categoryUri=er.getCategoryUri("business"),  # Limit to the "business" category
        dataType=["news"],       # Only fetch news articles
        lang="eng"               # Only fetch English articles
    )

    # Fetch articles
    articles = []
    for art in q.execQuery(er, sortBy="date", maxItems=max_items):
        articles.append({
            "title": art["title"],
            "description": art.get("body", ""),
            "url": art["url"],
            "date": art["date"]
        })
    
    return articles


if __name__ == "__main__":
    
    initialize_database()
    articles = fetch_financial_news("stock market", max_items=10)
    save_articles(articles)
    # Example: Fetch financial news related to the stock market
    

