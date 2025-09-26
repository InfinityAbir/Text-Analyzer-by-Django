# views.py
from django.http import HttpResponse
from django.shortcuts import render
import re
from collections import Counter
from textblob import TextBlob

# optional stopwords for keyword density
STOPWORDS = {
    "the", "and", "is", "in", "of", "to", "a", "for", "on", "with", "that",
    "this", "it", "as", "are", "was", "at", "by", "an", "be", "or", "from"
}

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # read inputs
    djtext = request.GET.get('text', '')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    wordcount = request.GET.get('wordcount', 'off')
    summary = request.GET.get('summary', 'off')
    # new features
    readingtime = request.GET.get('readingtime', 'off')
    keyworddensity = request.GET.get('keyworddensity', 'off')
    sentiment = request.GET.get('sentiment', 'off')

    original_text = djtext or ''
    processed = original_text  # work on this for transformations

    # if no operation selected -> prompt user
    if (
        removepunc != "on"
        and fullcaps != "on"
        and newlineremover != "on"
        and wordcount != "on"
        and summary != "on"
        and readingtime != "on"
        and keyworddensity != "on"
        and sentiment != "on"
    ):
        return HttpResponse("Please Select Any Operation")

    operations = []

    # SUMMARY: compute from original_text to preserve sentence boundaries
    summary_text = None
    if summary == "on":
        sentences = re.split(r'(?<=[.!?])\s+', original_text.strip())
        if len(sentences) >= 2:
            summary_text = " ".join(sentences[:2]).strip()
        elif len(sentences) == 1:
            words = original_text.split()
            summary_text = " ".join(words[:30]).strip()
        else:
            summary_text = ""
        operations.append("Summary")

    # Apply transformations to processed text (final analyzed_text)
    if newlineremover == "on":
        processed = processed.replace("\r", "").replace("\n", " ")
        operations.append("Removed New Lines")

    if removepunc == "on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        processed = "".join([ch for ch in processed if ch not in punctuation])
        operations.append("Removed Punctuation")

    if fullcaps == "on":
        processed = processed.upper()
        operations.append("Uppercase")

    # normalize whitespace
    processed = " ".join(processed.split()).strip()

    # WORD COUNT
    word_count = None
    if wordcount == "on":
        words_list = processed.split() if processed else []
        word_count = len(words_list)
        operations.append("Word Count")

    # READING TIME
    reading_time_val = None
    if readingtime == "on":
        words_for_reading = processed.split() if processed else []
        reading_time_val = round(len(words_for_reading) / 200, 2)  # 200 words/min
        operations.append("Reading Time")

    # KEYWORD DENSITY
    top_keywords = None
    if keyworddensity == "on":
        words_for_keywords = re.findall(r'\b\w+\b', processed.lower())
        filtered_words = [w for w in words_for_keywords if w not in STOPWORDS]
        top_keywords = Counter(filtered_words).most_common(5)
        operations.append("Keyword Density")

    # SENTIMENT ANALYSIS
    sentiment_label = None
    if sentiment == "on":
        if processed:
            polarity = TextBlob(processed).sentiment.polarity
            if polarity > 0:
                sentiment_label = "Positive"
            elif polarity < 0:
                sentiment_label = "Negative"
            else:
                sentiment_label = "Neutral"
            operations.append("Sentiment Analysis")

    # prepare context for template
    params = {
        "purpose": ", ".join(operations) if operations else "Processed",
        "analyzed_text": processed if processed else "(empty)",
        "extra_text": original_text,
        "summary_text": summary_text,
        "word_count": word_count,
        "reading_time": reading_time_val,
        "top_keywords": top_keywords,
        "sentiment_label": sentiment_label
    }

    return render(request, "analyze.html", params)
