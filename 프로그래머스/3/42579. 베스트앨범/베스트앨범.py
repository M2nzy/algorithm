def solution(genres, plays):
    answer = []
    genreCnt = dict()
    genreIdx = dict()

    genre = []
    # 장르 총 개수를 구하기 위해 일단 중복제거
    for i in range(len(genres)):
        genre.append(genres[i])
    genre = set(genre)
    genre = list(genre)
    
    # 딕셔너리 초기화
    for i in range(len(genre)):
        genreCnt[genre[i]] = []
        genreIdx[genre[i]] = []
        
    # 가장 많이 틀어진 장르 및 횟수 구하기
    for i in range(len(genres)):
        for j in range(len(genre)):
            if genres[i] == genre[j]:
                genreIdx[genre[j]].append(i)
                genreCnt[genre[j]].append(plays[i])
                break
                
    # 장르의 개수 구하기 (중복 X)
    order = []
    for i in (genreCnt):
        order.append([sum(genreCnt[i]),i])
    # 많이 틀어진 순서대로 해야하니 반대로 정렬
    order.sort(reverse=True)
    
    i = 0 
    result = []
    # 일단 while문을 돌린다
    while True:
        # 장르의 총 개수만큼 다 돌렸으면 break
        if (len(order)) == i:
            break
            
        # 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다. <<< 반례 처리해야함
        # 그래서 result 라는 배열을 따로 두고, 거기에 2개씩 추가함
        # 가장 큰 값을 result에 추가하고, 그 값을 dict에서 지워버림
        result.append(genreIdx[order[i][1]][genreCnt[order[i][1]].index(max(genreCnt[order[i][1]]))])
        del genreIdx[order[i][1]][genreCnt[order[i][1]].index(max(genreCnt[order[i][1]]))]
        del genreCnt[order[i][1]][genreCnt[order[i][1]].index(max(genreCnt[order[i][1]]))]
        
        # 원래 1개 데이터였던 상태에서 지우고 나면 배열이 비어있을테니 다음 장르로 넘어가거나
        # 해당 장르에서 2개의 결과를 이미 구해서 result 배열이 2개라면
        # 다음 장르로 넘어감 (i += 1) 그리고 result를 answer에 추가해준 후 다음 장르를 구하기 위해 초기화
        if not genreIdx[order[i][1]] or len(result) == 2:
            i += 1
            for j in range(len(result)):
                answer.append(result[j])
            result = []
            
    return answer