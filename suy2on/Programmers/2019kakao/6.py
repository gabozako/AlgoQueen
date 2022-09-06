def solution(word, pages):
    ## url파싱
    def parse_url(html):
        for line in html:
            if line.strip()[:23] == "<meta property=\"og:url\"":
                for w in line.strip().split("\""):
                    if w[:5] == "https":
                        return w

    ## body파싱
    def parse_body(html):
        try:
            head = html.index("<body>")
            tail = html.index("</body>")
            return html[head + 1:tail]
        except:
            return []

    ## 외부링크 파싱
    def parse_link(body):
        links = []
        for line in body:
            start = line.find("<a")
            if start != -1:
                finish = line.find(">")
                line = line[start:finish]
                for w in line.split("\""):
                    if w[:5] == "https":
                        links.append(w)
                        break
        return links

    ## 검색어찾기
    def search_word(body):
        cnt = 0
        for line in body:
            start = line.find("<a")
            # 중간에 태그 있으면 삭제
            if start != -1:
                finish = line.find(">")
                line = line[:start] + line[finish + 1:]
                start = line.find("</a")
                finish = line.find(">", start)
                line = line[:start] + line[finish + 1:]
            # 알파벳 제외 공백으로 바꾸기
            rline = line.strip()
            for c in line.strip():
                if not c.isalpha():
                    rline = rline.replace(c, " ")
            # 단어검사
            for w in rline.split():
                if word.lower() == w.lower():
                    cnt += 1

        return cnt

    link_score = [0] * len(pages)
    basic_score = []
    url = {}
    outlink_score = []


    for i, page in enumerate(pages):
        url[parse_url(page.split("\n"))] = i

    for page in pages:
        body = parse_body(page.split("\n"))
        basic = search_word(body)
        basic_score.append(basic)

        links = parse_link(body)
        outlink = len(links)
        outlink_score.append(outlink)

        for link in links:
            print(link)
            if link in url.keys():
                link_score[url[link]] += basic / outlink

    answer = []
    for i in range(len(pages)):
        answer.append([basic_score[i] + link_score[i], i])

    return sorted(answer, key=lambda x: (-x[0], x[1]))[0][1]

print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
