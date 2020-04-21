
# if vindex in range(1 ,19):  # 스크롤 내려가게 하기 위한 편법
#     video_btn = browser.find_elements_by_xpath \
#         ('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[' + str
#             (vindex) + ']/div[1]/div/div[1]/div/h3/a')
#     browser.implicitly_wait(delay)
#     video_btn[0].click()
#     time.sleep(2)
#     browser.back()
#     time.sleep(2)
#     continue

#    필터 옵션 [이번주]
#    browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[3]/a/div/yt-formatted-string').click()
#    필터 옵션 [오늘]
#    browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[2]/a/div/yt-formatted-string').click()

# 매끄러운 크롤링을 위한 사전 작업
# - 스크롤을 사전에 20번 내린 후 다시 올림
# - 내린 상태에서 첫번째 주소를 찾으면 못찾음
    # for vindex in range(1,25) :
    #     body.send_keys((Keys.PAGE_DOWN))
    #     time.sleep(2)
    #
    # for vindex in range(1,25):
    #     body.send_keys(Keys.PAGE_UP)
    #     time.sleep(2)

#   원래 고안했던 방법
#   20영상마다 한번씩 스크롤 내려주는 방법 - 로딩하는데 생각보다 시간이 오래걸림
#         if vindex % 20 == 1 :
#             body.send_keys(Keys.PAGE_DOWN)
#             time.sleep(2)
#             body.send_keys(Keys.PAGE_UP)
#             time.sleep(2)

# 원래는 아래로 내린 후 위로 올라갔는데 홈키를 누르니 1초만에 올라가서 그걸로 바꿨어요
# for vindex in range(30):
#     body.send_keys(Keys.PAGE_UP)
#     time.sleep(1)

# 100개 이상 되도록 수정
# 숫자 단위로 받아오도록 수정
# csv에 읽고 쓰기를 하면 인코딩이 잘 안되는 오류가 발생하여 dataframe 형식으로 바꿈
# ect 파일 장착
# float 형으로 바꿔서 한글->숫자로 정확한 표현을 위해 각 단어에 해당되는 숫자를 곱해줬으나 정확한 값으로 전환되지 않음 (ex.4.99명->40000.0명)