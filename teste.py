from instapy import InstaPy
from instapy import smart_run

insta_username = ('')
insta_password = ('')
session = InstaPy(username=insta_username,
password=insta_password,
headless_browser=True)

with smart_run(session):

#session.set_dont_include(["friend1", "friend2", "friend3"])
session.like_by_tags(["natgeo"], amount=10)
session.set_do_comment(enabled=True, percentage=35)
session.set_comments(comments)
session.join_pods(topic='sports', engagement_mode='no_comments')
comments = ['Nice shot! @{}',
'I love your profile! @{}',
'Your feed is an inspiration 👍',
'Just incredible 😮',
'What camera did you use @{}?',
'Love your posts @{}',
'Looks awesome @{}',
'Getting inspired by you @{}',
'🙌 Yes!',
'I can feel your passion @{} 💪']