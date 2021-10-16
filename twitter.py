"""Test script for Twitter API."""
from dotenv import load_dotenv
from icecream import ic

# from tweepy import attachments

import os
import queue
import requests
import tweepy


class TwitterClient:
    def __init__(self, api_key: str, secret: str, bearer_token: str):
        self.__client = tweepy.Client(
            bearer_token=bearer_token, consumer_key=api_key, consumer_secret=secret
        )

    def get_tweet_texts(self, username: str, limit: int = 10) -> list[str]:
        resp = self.__client.get_user(username=username)
        user = resp.data
        tweet_texts: list[str] = []
        for tweet in tweepy.Paginator(
            self.__client.get_users_tweets,
            user.id,
            expansions="attachments.media_keys",
            media_fields="preview_image_url,url",
            max_results=5,
        ).flatten(limit=limit):
            ic(tweet)
            ic(tweet.includes)
            tweet_texts.append(tweet.text)
        return tweet_texts

    def get_text_for_tweet(self, tweet_id: str):
        resp = self.__client.get_tweet(
            tweet_id,
            expansions="attachments.media_keys",
            media_fields="preview_image_url,url",
        )
        ic(resp)
        ic(resp.data)
        ic(resp.includes["media"][0].url)
        return resp.data.text

    def get_text_for_tweets(self, tweet_ids: list[str]):
        resp = self.__client.get_tweets(tweet_ids)
        for tweet in resp.data:
            ic(tweet.text)
        return [t.text for t in resp.data]


def get_original_tweet_id(url):
    r = requests.get(url, allow_redirects=False)
    ic(r.status_code, r.headers["Location"])
    parts = r.headers["Location"].split("/")
    # ic(parts)
    tweet_id = parts[5]
    return tweet_id


def main():
    load_dotenv()  # take environment variables from .env.

    api_key: str = os.getenv("TWITTER_API_KEY")
    api_key_secret: str = os.getenv("TWITTER_API_KEY_SECRET")
    bearer_token: str = os.getenv("TWITTER_BEARER_TOKEN")

    twitter = TwitterClient(api_key, api_key_secret, bearer_token)

    twitter.get_text_for_tweet("1447185173284630528")
    # tweet_texts = twitter.get_tweet_texts("hourlyFox", limit=1)

    # q = queue.Queue()
    # original_tweet_texts = []
    #
    # for tweet_text in tweet_texts:
    #     ic(tweet_text)
    #     if tweet_text.startswith("https://t.co"):
    #         original_tweet_id = get_original_tweet_id(tweet_text)
    #         ic(original_tweet_id)
    #         q.put(original_tweet_id)
    #     else:
    #         original_tweet_texts.append(tweet_text)
    #
    # for tweet_id in iter(q.get, None):
    #     ic(f"Removing from queue: {tweet_id}")
    #     tweet_text = twitter.get_text_for_tweet(tweet_id)
    #     if tweet_text.startswith("https://t.co"):
    #         original_tweet_id = get_original_tweet_id(tweet_text)
    #         ic(original_tweet_id)
    #         q.put(original_tweet_id)
    #     else:
    #         original_tweet_texts.append(tweet_text)
    #
    # ic(original_tweet_texts)


if __name__ == "__main__":
    main()
