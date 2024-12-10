def solution(genres, plays):
    answer = []
    genreCnt = dict()
    genreIdx = dict()

    genre = []
    for i in range(len(genres)):
        genre.append(genres[i])
    genre = set(genre)
    genre = list(genre)
    for i in range(len(genre)):
        genreCnt[genre[i]] = []
        genreIdx[genre[i]] = []
    # 가장 많이 틀어진 장르 구하기
    for i in range(len(genres)):
        for j in range(len(genre)):
            if genres[i] == genre[j]:
                genreIdx[genre[j]].append(i)
                genreCnt[genre[j]].append(plays[i])
                break
    order = []
    for i in (genreCnt):
        order.append([sum(genreCnt[i]),i])
    order.sort(reverse=True)
    i = 0 
    result = []
    while True:
        if (len(order)) == i:
            break
    # 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다. <<< 반례 처리해야함
        #장르
        result.append(genreIdx[order[i][1]][genreCnt[order[i][1]].index(max(genreCnt[order[i][1]]))])
        del genreIdx[order[i][1]][genreCnt[order[i][1]].index(max(genreCnt[order[i][1]]))]
        del genreCnt[order[i][1]][genreCnt[order[i][1]].index(max(genreCnt[order[i][1]]))]
        
        if not genreIdx[order[i][1]] or len(result) == 2:
            i += 1
            for j in range(len(result)):
                answer.append(result[j])
            result = []
            
    return answer