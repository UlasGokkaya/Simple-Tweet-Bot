# 🤖 Generic Automated Tweet Poster (Scheduled Only)

This project is a clean, secure, and scheduled Python bot designed to post automated text updates to X (Twitter). It is built on **GitHub Actions** and is configured to run **automatically on a fixed schedule** without any manual triggers.

---

## 🛡️ Key Features

* **Secure Credentials:** API keys are never stored in the code. They are retrieved securely using **GitHub Secrets**.
* **Pure Automation:** The bot runs **only** according to the time defined in the workflow schedule (`cron`).
* **Minimalist Design:** The core logic focuses only on establishing the connection and posting a static tweet.

## 🚀 Getting Started: Use This Template

This guide shows you how to securely use this bot with your own API keys.

### 1. Create Your Own Repository (Start Here!)

To start using the bot, create a clean copy of this template in your own GitHub account:

1.  Go to the original repository page.
2.  Click the green **"Use this template"** button.
3.  Name your new repository and click **"Create repository from template"**.

### 2. Secure Your Credentials (The CRITICAL Step)

**Your bot will not run unless you set up your OWN API keys in your new repository's Secrets.**

1.  Go to your new repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2.  Click **New repository secret**.
3.  Add the following four secrets exactly as named, using **YOUR OWN** key values:
    * `TWITTER_API_KEY`
    * `TWITTER_API_SECRET`
    * `TWITTER_ACCESS_TOKEN`
    * `TWITTER_ACCESS_TOKEN_SECRET`

---

## 🛠️ Bot Configuration & Customization

### A. Repository File Structure

Your repository must contain the following files and folders for GitHub Actions to work:

* **`auto_tweet.py`**: The main Python script (the bot itself).
* **`requirements.txt`**: Lists Python dependencies (e.g., `tweepy`).
* **`.github/`** (Folder)
    * **`workflows/`** (Folder)
        * **`tweet_bot_workflow.yml`**: Defines the automation schedule and job execution.

### B. Customizing Content and Time

* **Change Tweet Content:**
    Modify the `tweet_content` variable inside **`auto_tweet.py`**.
* **Adjust Posting Time (Schedule):**
    The bot runs automatically every day at 07:00 UTC (10:00 AM Turkish Time) by default. To change this time, edit the `cron` expression in the **`.github/workflows/tweet_bot_workflow.yml`** file.

## ▶️ Running and Verification

The bot runs completely automatically based on the schedule you defined.

* **Verification:** To check if the bot ran successfully, go to the **Actions** tab in your repository and check the workflow history. A green checkmark indicates a successful automated run.