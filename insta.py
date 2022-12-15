from code import interact
from instapy import InstaPy
from instapy import smart_run
import selenium

session = InstaPy('', '')

with smart_run(session):
    session.set_do_follow(enabled = True, percentage = 100)
    session.set_do_like(enabled = True, percentage= 100)

    session.like_by_feed(amount=3, randomize=True, unfollow=False, interact=True)

    comentarios = ['haha']
    session.set_do_coments(enable=True, percentage=1)
    session.set_coments(comentarios, media= 'Photo')
    session.join_pods()

