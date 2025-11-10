# 🤖 Generic Automated Tweet Poster (Scheduled Only)

This project is a clean, secure, and scheduled Python bot designed to post automated text updates to X (Twitter). It uses **GitHub Actions** for automation and **GitHub Secrets** for security, ensuring your API keys are never visible in the code.

---

## 🛡️ Key Features

* **Secure Credentials:** API keys are never stored in the code. They are retrieved securely using **GitHub Secrets**.
* **Pure Automation:** The bot runs **only** according to the time defined in the workflow schedule (`cron`).
* **Minimalist Design:** The core logic focuses only on establishing the connection and posting a static tweet.

---

## 🚀 Step-by-Step Setup Guide

### 1. Create Your Own Repository (Start Here!)

To start using the bot, create a clean copy of this template in your own GitHub account:

1.  Go to the original repository page (where you found this file).
2.  Click the green **"Use this template"** button at the top.
3.  Name your new repository and click **"Create repository from template"**.

### 2. Secure Your Credentials (The CRITICAL Step)

**Your bot will not run unless you set up your OWN API keys in your new repository's Secrets.**

#### ⚠️ Why You MUST Use GitHub Secrets

It is crucial that you **do not** paste your keys directly into the `auto_tweet.py` file.

* **Security Risk:** If you paste your keys into the code and commit them, your sensitive API credentials will be **publicly visible to everyone on the internet** in your GitHub repository history.
* **Best Practice:** This bot loads secrets as environment variables, which are provided securely by the GitHub Secrets vault at runtime.

#### How to Add Your Secrets:

1.  Go to your new repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2.  Click the **"Secrets"** tab and then **"New repository secret"**.
3.  Add the following four secrets exactly as named, using **YOUR OWN** key values:
    * `TWITTER_API_KEY`
    * `TWITTER_API_SECRET`
    * `TWITTER_ACCESS_TOKEN`
    * `TWITTER_ACCESS_TOKEN_SECRET`

---

## 🛠️ Configuration & Customization

### A. Repository File Structure

Your repository must contain the following files and folders for GitHub Actions to work:

| File / Folder                | Type   | Description                                                 |
| :--------------------------- | :----- | :---------------------------------------------------------- |
| **`auto_tweet.py`**          | File   | The core Python script containing the tweeting logic.       |
| **`requirements.txt`**       | File   | Lists Python dependencies (e.g., `tweepy`).                 |
| **`.github/`**               | Folder | Contains configuration files for GitHub services.           |
| **`.github/workflows/`**     | Folder | Holds the GitHub Actions workflow files.                    |
| **`tweet_bot_workflow.yml`** | File   | Defines the automation schedule (`cron`) and the job steps. |

### B. Customizing Content and Time

* **Change Tweet Content:**
    Modify the `tweet_content` variable inside **`auto_tweet.py`**.
* **Adjust Posting Time (Schedule):**
    The bot runs automatically every day at 07:00 UTC (10:00 AM Turkish Time) by default. To change this time, edit the `cron` expression in the **`.github/workflows/tweet_bot_workflow.yml`** file.

## ▶️ Verification

The bot runs completely automatically based on the schedule you defined.

* **Verification:** To check if the bot ran successfully, go to the **Actions** tab in your repository and check the workflow history. A green checkmark indicates a successful automated run.