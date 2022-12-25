# Amazon Review WordCloud Generator
This script is a simple Python program that generates a word cloud image from Amazon product reviews.

## To use this script, you will need to have the following packages installed:

- selenium
- wordcloud
To install these packages, you can use cpip install selenium wordcloud```.

## How to use
To use the script, you will need the URL of an Amazon product page. You can then run the script and enter the URL when prompted. The script will also ask for the maximum number of reviews to include in the word cloud, and the rating of the reviews you want to include (one to five stars, or "all" for all ratings).

The script will then use the selenium package to scrape the reviews from the Amazon product page, and use the wordcloud package to generate a word cloud image from the reviews. The word cloud image will be saved to a file called "wordCloud.png" in the same directory as the script.

## Example
```
python amazon_review_wordcloud.py
Enter Url:---https://www.amazon.com/dp/B01MZA3Z3O
Enter Max Number Of reviews:--100
Enter review with rating you want [one, two, three, four, five, all]:--four
This will generate a word cloud image from the first 100 four-star reviews of the product at the specified URL. The image will be saved to "wordCloud.png" in the same directory as the script.
```
This will generate a word cloud image from the first 100 four-star reviews of the product at the specified URL. The image will be saved to "wordCloud.png" in the same directory as the script.
