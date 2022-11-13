import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from functions import search_post

main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_word = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = search_post(search_word)
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Проблема с файлом"

    return render_template('post_list.html', search_word=search_word, posts=posts)
