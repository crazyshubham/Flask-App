# 🧠 NLP App – Named Entity Recognition (NER) Web Application

## 📌 Overview

This project is a **Flask-based web application** that demonstrates **Named Entity Recognition (NER)** using Natural Language Processing (NLP).

Users can:

* Register and log in securely
* Input text
* Extract named entities like **Person, Organization, Location (GPE)**

---

## 🚀 Features

* 🔐 User Authentication (Register & Login)
* 🧾 Named Entity Recognition (NER)
* 🧠 NLP using NLTK
* 🎨 Clean UI with CSS styling
* 🔒 Session-based access control
* 📊 Displays extracted entities in table format

---

## 🧠 What is NER?

Named Entity Recognition (NER) is a Natural Language Processing technique used to identify and classify important information in text.

### Example:

Input:

```
Elon Musk founded SpaceX in California
```

Output:

* Elon Musk → PERSON
* SpaceX → ORGANIZATION
* California → GPE (Location)

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS (Jinja2 Templates)
* **NLP Library:** NLTK
* **Database:** Custom DB module (`db.py`)

---

## 📁 Project Structure

```
project/
│
├── app.py
├── db.py
├── static/
│   └── styles.css
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   └── ner.html
└── README.md
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository

```
git remote add origin https://github.com/crazyshubham/Flask-App.git
cd your-repo-name
```

### 2️⃣ Install dependencies

```
pip install flask nltk
```

### 3️⃣ Download NLTK data

```
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

### 4️⃣ Run the application

```
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🔐 Authentication Flow

1. User registers
2. Data stored via `db.py`
3. User logs in
4. Session created
5. Access granted to protected pages

---

## 🔍 How NER Works (In This Project)

1. Text input from user
2. Tokenization using `word_tokenize`
3. POS tagging using `pos_tag`
4. Chunking using `ne_chunk`
5. Extract entities and display

---

## 📊 Example Output

| # | Entity  | Type   |
| - | ------- | ------ |
| 1 | Shubham | PERSON |
| 2 | India   | GPE    |

---

## ⚠️ Limitations

* Uses basic NLTK model (not highly accurate)
* No password hashing (for demo purposes)
* Simple UI (can be improved)

---

## 🔮 Future Improvements

* 🔐 Add password hashing (bcrypt)
* 🤖 Use advanced models (SpaCy / Transformers)
* 🎨 Improve UI (React / Tailwind)
* 📊 Add more NLP features (Sentiment Analysis, Summarization)
* ☁️ Deploy on cloud (Render / AWS)

---

## 👨‍💻 Author

**Shubham Upadhyay**

---

## 📜 License

This project is for **educational purposes**.
