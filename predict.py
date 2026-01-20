import joblib
import numpy as np
from urllib.parse import urlparse
import re
import os

# Load the trained model
# Using absolute path check to avoid FileNotFoundError
if os.path.exists("phishing_model.pkl"):
    model_path = "phishing_model.pkl"
else:
    print("❌ ERROR: 'phishing_model.pkl' not found. Please run 'train_model.py' first.")
    exit()

model = joblib.load(model_path)


def extract_features(url):
    features = []

    # Parse the URL
    parsed_url = urlparse(url)

    # 1. having_IP_Address
    # Check if IP address is used in domain
    ip_pattern = r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\/)|'
    match = re.search(ip_pattern, url)
    if match:
        features.append(-1)  # Phishing
    else:
        features.append(1)  # Legit

    # 2. URL_Length
    if len(url) < 54:
        features.append(1)
    elif 54 <= len(url) <= 75:
        features.append(0)
    else:
        features.append(-1)

    # 3. Shortining_Service
    shorteners = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                 r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                 r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                 r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                 r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                 r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                 r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                 r"tr\.im|link\.zip\.net"

    if re.search(shorteners, url):
        features.append(-1)
    else:
        features.append(1)

    # 4. having_At_Symbol
    if '@' in url:
        features.append(-1)
    else:
        features.append(1)

    # 5. double_slash_redirecting
    if url.rfind('//') > 7:
        features.append(-1)
    else:
        features.append(1)

    # 6. Prefix_Suffix
    if '-' in parsed_url.netloc:
        features.append(-1)
    else:
        features.append(1)

    # 7. having_Sub_Domain
    domain = parsed_url.netloc.replace("www.", "")
    dot_count = domain.count('.')
    if dot_count == 1:
        features.append(1)
    elif dot_count == 2:
        features.append(0)
    else:
        features.append(-1)

        # 8. HTTPS_token
    if 'https' in parsed_url.netloc:
        features.append(-1)
    else:
        features.append(1)

    return np.array(features).reshape(1, -1)


def predict_url(url):
    features = extract_features(url)
    prediction = model.predict(features)[0]

    # -1: Phishing, 1: Legit, 0: Suspicious
    if prediction == -1:
        return "⚠️ PHISHING DETECTED!"
    elif prediction == 1:
        return "✅ SAFE URL"
    else:
        return "❓ SUSPICIOUS URL"


# Test Code
if __name__ == "__main__":
    test_url = "http://google.com"
    print(f"Testing: {test_url}")
    print(f"Result: {predict_url(test_url)}")