from selenium import webdriver as uc
import time
from wordcloud import WordCloud, STOPWORDS

url = input("Enter Url:---")
max_reviews = int(input("Enter Max Number Of reviews:--"))
star_review = input("Enter review with rating you want [one, two, three, four, five, all]")

output_file = "wordCloud.png"


def get_reviews(link):
    print("Starting the program")
    options = uc.ChromeOptions()
    options.headless = True
    browser = uc.Chrome(options=options)
    browser.get(link)
    browser.implicitly_wait(3)
    browser.find_element_by_xpath("//a[@data-hook='see-all-reviews-link-foot']").click()
    review_url = browser.current_url
    time.sleep(1)
    reviews = []
    page_num = 1
    while True:
        if star_review!="all":
            browser.get(review_url + f"&pageNumber={page_num}"+f"&filterByStar={star_review}_star")
        else:
            browser.get(review_url + f"&pageNumber={page_num}")
        page_num += 1
        reviews_span = browser.find_elements_by_xpath("//span[@data-hook='review-body']")
        for x in reviews_span:
            reviews.append(str(x.text).replace("\n", " "))
        if len(reviews_span) == 0 or len(reviews) >= max_reviews:
            break
        else:
            print(len(reviews))
    print(f"Found {len(reviews)} reviews and saved word cloud in {output_file}")
    return reviews


def create_word_cloud(string):
    cloud = WordCloud(background_color="white", max_words=200, stopwords=set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file(output_file)


reviews_list = get_reviews(url)
reviews_string = " ".join(reviews_list)
create_word_cloud(reviews_string)
