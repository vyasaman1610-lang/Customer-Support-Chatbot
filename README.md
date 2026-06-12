# 💬 Customer Support Chatbot (NLP-Based)

An AI-powered **Customer Support Chatbot** built using **Natural Language Processing (NLP)** techniques.  
It uses **TF-IDF vectorization and Cosine Similarity** to match user queries with the most relevant FAQ responses.

The chatbot is deployed using **Streamlit** and supports an interactive chat interface.

---

## 🚀 Features

- 🧠 NLP-based query understanding
- 🔍 TF-IDF + Cosine Similarity for response matching
- 💬 Interactive chat UI (Streamlit)
- ✨ Word-by-word typing effect
- 🧹 Chat history with clear chat option
- 🤖 Basic spell correction support

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- NLTK
- TextBlob
- Streamlit

---

## 📂 Project Structure



Customer-Support-Chatbot/
│
├── app.py # Streamlit frontend
├── chatbot_model.py # NLP model and chatbot logic
├── customer_support.csv # Dataset (FAQ data)
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ How It Works

1. User enters a question in the chatbot
2. Text is preprocessed (lowercasing, stopword removal, lemmatization)
3. TF-IDF converts text into numerical vectors
4. Cosine similarity finds the closest matching question
5. The corresponding answer is returned

---

## 🧪 Example

**User Input:**
> What are symptoms of mental illness?

**Bot Response:**
> Mental illness affects how people think, feel, behave, or interact with others...


---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/customer-support-chatbot.git
cd customer-support-chatbot


## ▶️ How to Run

```bash
streamlit run app.py


---

## 4. ⭐ Add final polish (makes it look professional)

Add this:

```md id="fix4"
## 👨‍💻 Author

Aman Vyas  
Aspiring AI/ML Engineer  

---

## ⭐ If you like this project

Give this repo a star ⭐ on GitHub!
