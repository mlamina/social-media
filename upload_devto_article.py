import os
import webbrowser
from pathlib import Path

import requests
import json

from dotenv import load_dotenv

load_dotenv()

# API headers including the DEV API key
headers_dev = {
    "Content-Type": "application/json",
    "api-key": os.getenv('DEVTO_API_KEY'),
}


def get_markdown_content(markdown_path):
    """Read Markdown content from a file"""
    with open(markdown_path, 'r') as file:
        return file.read()


def get_title_from_markdown(markdown_content):
    """Extract the title from the Markdown content"""
    title = None
    for line in markdown_content.split('\n'):
        if line.startswith('# '):
            title = line[2:]
            break
    return title


# Function to publish an article to DEV
def publish_article_dev(markdown_content):
    # Set up the payload with article data
    article_payload = {
        "article": {
            "title": get_title_from_markdown(markdown_content),
            "body_markdown": markdown_content,
            "published": False,
        }
    }

    # Make a POST request to DEV's API to publish the article
    response = requests.post(
        url='https://dev.to/api/articles',
        headers=headers_dev,
        data=json.dumps(article_payload)
    )

    # Check if the request was successful
    if response.status_code == 201:
        article_id = response.json()['id']
        print(f"Article published successfully! ID: {article_id}")
        # Open the DEV dashboard in the browser
        webbrowser.open('https://dev.to/dashboard')
        return article_id
    else:
        print(f"Failed to publish article. Status code: {response.status_code}")
        print("Response:", response.json())


def update_existing_article(article_id, markdown_content):
    # Set up the payload with updated article data
    article_payload = {
        "article": {
            "title": get_title_from_markdown(markdown_content),
            "body_markdown": markdown_content,
            "published": False,
        }
    }

    # Make a PUT request to DEV's API to update the article
    response = requests.put(
        url=f'https://dev.to/api/articles/{article_id}',
        headers=headers_dev,
        data=json.dumps(article_payload)
    )

    # Check if the request was successful
    if response.status_code == 200:
        print("Article updated successfully!")
        # Open the DEV dashboard in the browser
        webbrowser.open('https://dev.to/dashboard')
    else:
        print(f"Failed to update article. Status code: {response.status_code}")
        print("Response:", response.json())


# Let user select Markdown file from posts/
posts = os.listdir('posts/')
for i, post in enumerate(posts):
    print(f"{i + 1}. {post}")

post_number = int(input("Select a post to publish: ")) - 1
selected_post = posts[post_number]

distribution_map = json.loads(Path('distribution.json').read_text())

if selected_post not in distribution_map:
    print("Creating new article...")
    markdown_content = get_markdown_content(f'posts/{selected_post}')
    article_id = publish_article_dev(markdown_content)
    if not article_id:
        exit(1)
    distribution_map[selected_post] = article_id
    Path('distribution.json').write_text(json.dumps(distribution_map))
else:
    article_id = distribution_map[selected_post]
    print(f"Article already published with ID {article_id}, updating...")
    markdown_content = get_markdown_content(f'posts/{selected_post}')
    update_existing_article(article_id, markdown_content)
