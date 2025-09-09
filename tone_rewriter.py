def rewrite_text(original_text: str, tone: str) -> str:
    if tone == "Neutral":
        return original_text
    elif tone == "Suspenseful":
        return f"Suddenly, it all changed. {original_text.strip().capitalize()}..."
    elif tone == "Inspiring":
        return f"Believe in this: {original_text.strip().capitalize()}!"
    else:
        return original_text
