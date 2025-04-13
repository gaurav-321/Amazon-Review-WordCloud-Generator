# Amazon Review WordCloud Generator

This project is a Python tool that generates a **word cloud** image from **Amazon product reviews**, allowing you to visually analyze customer feedback.

---

## ✨ Description
Generate a word cloud from Amazon product reviews using Selenium, filter by star ratings, and visually analyze customer feedback. This tool helps in making more informed buying decisions and understanding customer sentiment through data visualization.

---

## 🚀 Features
- **Scrapes Amazon reviews** using Selenium.
- Filters reviews by star rating (1–5 or all).
- Generates a word cloud image from review text.
- Saves the image as `wordCloud.png` in the project directory.

---

## ⛓ Installation

### Prerequisites
- Google Chrome (installed on your system)
- Chrome WebDriver (place it in the same directory as the script)
- Python 3.x

### Python Packages
Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📦 Usage
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

## 🔧 Configuration
No configuration options are required. Ensure that Chrome and Chrome WebDriver are installed correctly.

---

## 🧪 Tests
Testing is not available for this project.

---

## 📁 Project Structure
```
.
├── main.py        # Main script to scrape reviews & generate word cloud
├── requirements.txt  # Python dependencies
└── README.md      # Project documentation
```

---

## 🙋 Contributing
Contributions are welcome! Please follow these guidelines:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## 📄 License
This project is open source, licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙋 Author
Just a Pythoneer contributing to open-source – enjoy the tool!