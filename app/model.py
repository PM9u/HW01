from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# 간단한 더미 학습 데이터 정의
X_train = [
    "Free money now",
    "Win a lottery today",
    "Meeting at 10 am",
    "Can we reschedule our sync?",
    "Claim your free gift card",
    "Project update attached",
    "Congratulations, you won a free car",
    "Hey, what's for dinner?"
]
y_train = ["spam", "spam", "ham", "ham", "spam", "ham", "spam", "ham"]

# TfidfVectorizer와 Naive Bayes를 연결한 파이프라인
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

def train_model():
    """서버 시작 시 더미 데이터를 기반으로 모델을 학습합니다."""
    pipeline.fit(X_train, y_train)
    return pipeline

# 모듈이 임포트될 때 한 번 학습 (서버 기동 시)
trained_model = train_model()

def predict(text: str) -> str:
    """주어진 텍스트에 대해 스팸 여부를 예측합니다."""
    prediction = trained_model.predict([text])
    return prediction[0]

KOREAN_SPAM_KEYWORDS = ['광고', '무료', '적중']

def is_korean_spam(text: str) -> bool:
    """한국어 스팸 키워드가 포함되어 있는지 확인합니다."""
    return any(keyword in text for keyword in KOREAN_SPAM_KEYWORDS)
