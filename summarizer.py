import openai

# Replace with your OpenAI API Key
openai.api_key = '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'

def summarize_article(article_body):
    """
    Summarize a news article using OpenAI GPT.
    
    Args:
        article_body (str): The content of the article to summarize.
    
    Returns:
        str: The summary of the article.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize this article:\n\n{article_body}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Test the summarization function
if __name__ == "__main__":
    article_text = "The stock market showed strong gains today, driven by optimism over economic growth and a drop in unemployment rates."
    summary = summarize_article(article_text)
    print("Summary:", summary)
