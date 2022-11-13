import json


def load_posts():
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_post(input_word: str):
    find_posts = []
    posts = load_posts()
    for post in posts:
        if input_word.lower() in post['content'].lower():
            find_posts.append(post)
    return find_posts


def add_post(post: dict):
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
