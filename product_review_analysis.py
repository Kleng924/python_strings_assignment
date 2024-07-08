## 1. **Product Review Analysis** **Objective:** The aim of this assignment is to extract insights 
# from product reviews by using string manipulation to categorize and summarize customer feedback 
# for a SaaS product. 
# **Task 1:** Keyword Highlighter - Write a program that searches through a series of product reviews 
# for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the 
# keywords in uppercase so they stand out.

python_reviews_1 = "This product is really good. I'm impressed with its quality."
keyword_review_1 = python_reviews_1.replace("good", "GOOD")
print(keyword_review_1)

python_reviews_2 = "The performance of this product is excellent. Highly recommended!"
keyword_review_2 = python_reviews_2.replace("excellent", "EXCELLENT")
print(keyword_review_2)

python_reviews_3 = "I had a bad experience with this product. It didn't meet my expectations."
keyword_review_3 = python_reviews_3.replace("bad", "BAD")
print(keyword_review_3)

python_reviews_4 = "Poor quality product. Wouldn't recommend it to anyone."
keyword_review_4 = python_reviews_4.replace("Poor", "POOR")
print(keyword_review_4)

python_reviews_5 = "The product was average. Nothing extraordinary about it."
keyword_review_5 = python_reviews_5.replace("average", "AVERAGE")
print(keyword_review_5)


# **Task 2:** Sentiment Tally - Develop a function that tallies the number of positive and negative words 
# in each review. Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.
    
python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 

def tally(python_positive_words):
    tally_dict = {}
    for positive_words in python_positive_words:
        if positive_words in tally_dict:
            tally_dict[positive_words] += 1
        else:
            tally_dict[positive_words] = 1
    return tally_dict

tally_result = tally(python_positive_words)
print(tally_result)

python_negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally(python_negative_words):
    tally_dict = {}
    for negative_words in python_negative_words:
        if negative_words in tally_dict:
            tally_dict[negative_words] += 1
        else:
            tally_dict[negative_words] = 1
    return tally_dict

tally_result = tally(python_negative_words)
print(tally_result)

# **Task 3:** Review Summary - Implement a script that takes the first 30 characters of a review and appends 
# "..." to create a summary. Ensure that the summary does not cut off in the middle of a word. ---

reviews = ["This product is really good. I'm impressed with its quality.",
        " The  performance  of  this   product is excellent. Highly recommended!",
        " I had  a  bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        " The  product  was  average.   Nothing extraordinary about it."]

def summarize_reviews(reviews):
    summaries = [review[:30] + "..." for review in reviews]
    return summaries

summaries = summarize_reviews(reviews)
for summary in summaries:
    print(summary)
