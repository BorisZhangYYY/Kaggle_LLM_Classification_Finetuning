# Kaggle Competition: LLM Classification Finetuning
Link: https://www.kaggle.com/competitions/llm-classification-finetuning/overview
Tips: (For Windows Users)
1. Run `python` in PowerShell; it will open the Microsoft Store Python page. Click install to get Python.
2. Then create a virtual environment with `python -m venv .venv`.
3. In PowerShell, run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`. After that, you can run the activation script. Use `Get-ExecutionPolicy -List` to verify that RemoteSigned is active.
4. Activate the virtual environment with `.\.venv\Scripts\Activate.ps1`. If you see `(.venv)` on the left of the prompt, it worked.
5. Run `pip install -r requirements.txt` to install the project dependencies.

## Overview
This competition challenges you to predict which responses users will prefer in a head-to-head battle between chatbots powered by large language models (LLMs). You'll be given a dataset of conversations from the Chatbot Arena, where different LLMs generate answers to user prompts. By developing a winning machine learning model, you'll help improve how chatbots interact with humans and ensure they better align with human preferences.

## Description
Large language models (LLMs) are rapidly entering our lives, but ensuring their responses resonate with users is critical for successful interaction. This competition presents a unique opportunity to tackle this challenge with real-world data and help us bridge the gap between LLM capability and human preference.

We utilized a large dataset collected from Chatbot Arena, where users chat with two anonymous LLMs and choose the answer they prefer. Your task in this competition is to predict which response a user will prefer in these head-to-head battles.

This challenge aligns with the concept of "reward models" or "preference models" in reinforcement learning from human feedback (RLHF). Previous research has identified limitations in directly prompting an existing LLM for preference predictions. These limitations often stem from biases such as favoring responses presented first (position bias), being overly verbose (verbosity bias), or exhibiting self-promotion (self-enhancement bias).

We encourage you to explore various machine-learning techniques to build a model that can effectively predict user preferences. Your work will be instrumental in developing LLMs that can tailor responses to individual user preferences, ultimately leading to more user-friendly and widely accepted AI-powered conversation systems.

This competition challenges you to predict which responses users will prefer in a head-to-head battle between chatbots powered by large language models (LLMs).

## Dataset Description
The competition dataset consists of user interactions from the ChatBot Arena. In each user interaction a judge provides one or more prompts to two different large language models, and then indicates which of the models gave the more satisfactory response. The goal of the competition is to predict the preferences of the judges and determine the likelihood that a given prompt/response pair is selected as the winner.

Please note that this is a Code Competition. When your submission is scored, this example test data will be replaced with the full test set. There are 55K rows in the training data, and you can expect roughly 25,000 rows in the test set.

## Files
- **rain.csv**
  - `id` - A unique identifier for the row.
  - `model_[a/b]` - The identity of model_[a/b]. Included in train.csv but not test.csv.
  - `prompt` - The prompt that was given as an input (to both models).
  - `response_[a/b]` - The response from model_[a/b] to the given prompt.
  - `winner_model_[a/b/tie]` - Binary columns marking the judge's selection. The ground truth target column.

- **test.csv**
  - `id`
  - `prompt`
  - `response_[a/b]`

- **sample_submission.csv** - A submission file in the correct format.
  - `id`
  - `winner_model_[a/b/tie]` - This is what is predicted from the test set.
