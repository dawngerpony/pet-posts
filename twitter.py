"""Test script for Twitter API."""
from dotenv import load_dotenv
from icecream import ic

import os
import tweepy


class TwitterClient:
    def __init__(self, api_key: str, secret: str, bearer_token: str):
        self.__client = tweepy.Client(
            bearer_token=bearer_token, consumer_key=api_key, consumer_secret=secret
        )

    def get_user_id(self, username: str):
        return self.__client.get_user(username=username).data.id

    def get_image_urls_for_user(self, username: str, limit: int = 10) -> list[str]:
        user_id = self.get_user_id(username)
        tweet_ids: list[str] = []
        for tweet in tweepy.Paginator(
            self.__client.get_users_tweets,
            user_id,
            max_results=5,
        ).flatten(limit=limit):
            tweet_ids.append(tweet.id)
        image_urls = self.get_image_urls_for_tweets(tweet_ids)
        return image_urls

    def get_image_urls_for_tweets(self, tweet_ids: list[str]):
        resp = self.__client.get_tweets(
            tweet_ids,
            expansions="attachments.media_keys",
            media_fields="preview_image_url,url",
        )
        image_urls = []
        for media in resp.includes["media"]:
            image_urls.append(media.url)
        return image_urls


def main():
    load_dotenv()  # take environment variables from .env.

    api_key: str = os.getenv("TWITTER_API_KEY")
    api_key_secret: str = os.getenv("TWITTER_API_KEY_SECRET")
    bearer_token: str = os.getenv("TWITTER_BEARER_TOKEN")

    twitter = TwitterClient(api_key, api_key_secret, bearer_token)

    image_urls = twitter.get_image_urls_for_user("hourlyFox", limit=10)
    ic(image_urls)


if __name__ == "__main__":
    main()
