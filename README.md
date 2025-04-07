# Amazon Review WordCloud Generator

This project is a Python tool that generates a **word cloud** image from **Amazon product reviews**, allowing you to visually analyze customer feedback.

---

## 🎯 Features
- Scrapes Amazon reviews using Selenium.
- Filters reviews by star rating (1–5 or all).
- Generates a word cloud image from review text.
- Saves the image as `wordCloud.png` in the project directory.

---

## 📦 Requirements
- Google Chrome (installed on your system)
- Chrome WebDriver (place it in the same directory as the script)
- Python 3.x

### Python Packages
Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage
Run the script and follow prompts:
```bash
python main.py
```

Then provide the following inputs:
- Amazon product URL
- Maximum number of reviews to fetch
- Desired review rating (options: `one`, `two`, `three`, `four`, `five`, `all`)

### 🔍 Example
```
python main.py
Enter Url:---https://www.amazon.com/dp/B01MZA3Z3O
Enter Max Number Of reviews:--100
Enter review with rating you want [one, two, three, four, five, all]:--four
```

✅ This will scrape the first 100 four-star reviews and generate a word cloud saved as `wordCloud.png`.

---

## 🧠 How It Works
- Navigates to the Amazon product's review page using Selenium.
- Iterates through review pages, filtering by selected rating.
- Extracts review text and compiles it into a single string.
- Uses the `wordcloud` package to generate and save the image.

---

## 🛠 File Overview
| File             | Description                             |
|------------------|-----------------------------------------|
| `main.py`        | Main script to scrape reviews & generate word cloud |
| `requirements.txt` | Python dependencies                    |
| `README.md`      | Project documentation                   |

---

## 📌 Notes
- Works only with Amazon product pages that use standard review layout.
- Some manual tweaking may be needed for non-US Amazon domains.
- Requires stable internet and browser setup.

---

## 💡 Why Use This?
Use this tool to:
- Analyze recurring keywords in product feedback.
- Make more informed buying decisions.
- Understand customer sentiment visually.

---

## 🧾 License
Open source – feel free to contribute or adapt!

---

## 🙋 Author
Just a Pythoneer contributing to open-source – enjoy the tool!
