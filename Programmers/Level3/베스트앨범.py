# 수정한 코드(참고)

# 속한 노래가 많이 재생된 장르를 먼저 수록
# 장르 내에서 많이 재생된 노래를 먼저 수록
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])
    
    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])
    
    answer = []
    for g, _ in sorted(genres_list, key=lambda x:x[1], reverse=True):
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer

