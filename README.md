# 🤖 Generic Automated Twitter (X) Bot

A simple, secure, and scheduled Python bot designed to post automated tweets to X (Twitter). This project prioritizes **API key security** by utilizing **GitHub Secrets** for credentials and **GitHub Actions** for automation and scheduling.

---

## 🛡️ Key Features

* **Secure Credential Management:** All sensitive API keys and access tokens are stored securely outside of the code using **GitHub Secrets**.
* **Automation:** The bot is automatically executed on a schedule using **GitHub Actions**.
* **Minimalist Design:** Focuses purely on posting a static tweet, making it easy to adapt for more complex content later.

## 🛠️ Setup and Installation

### 1. Secure Your Credentials (GitHub Secrets)

The bot will **NOT** run unless you set up your API keys in GitHub Secrets.

1.  Go to your GitHub Repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2.  Click **New repository secret**.
3.  Add the following four secrets exactly as named:
    * `TWITTER_API_KEY`
    * `TWITTER_API_SECRET`
    * `TWITTER_ACCESS_TOKEN`
    * `TWITTER_ACCESS_TOKEN_SECRET`

### 2. File Structure

Ensure your repository contains the following files:
/ (root) ├── .github/ │ └── workflows/ │ └── tweet_bot_workflow.yml # Defines the schedule and job execution ├── auto_tweet.py # The main Python script └── requirements.txt # Lists Python dependencies (e.g., tweepy)

### 3. Customization

* **Change Tweet Content:** Modify the `tweet_content` variable inside **`auto_tweet.py`**.
* **Change Schedule:** Edit the `cron` expression in the **`.github/workflows/tweet_bot_workflow.yml`** file to set a new posting time.

## ▶️ Running and Testing

The bot is designed to run automatically.

To manually trigger a test run:

1.  Go to the **Actions** tab in your repository.
2.  Select the **"Automated Tweet Bot Runner"** workflow.
3.  Click the **"Run workflow"** button and select the appropriate branch (`main`).