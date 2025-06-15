import praw # 라이브러리는 import되지 않는다.

 reddit= praw.Reddit('case' )# case 에 해당하는 설정을 사용하여 reddit API 객체 생성


 subreddit = reddit.subreddit("Python")# Python이라는 이름의 서브레딧 객체를 생성

for submission in subreddit.hot(limit=1): # 해당 서브레딧에서 인기 글 1개 순회
    print("제목: ", submission.title)# 게시글의 제목 출력
    print("내용: ", submission.selftext)# 게시글의 내용 출력
    print("점수: ", submission.score)# 게시글의 추천 점수 출력
    print("------------\n")# 구분선 출력