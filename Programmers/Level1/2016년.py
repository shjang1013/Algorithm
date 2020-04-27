def solution(a,b):
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    namuji = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # 월, 일의 합
    hap = sum(day[:a-1]) + b
    answer = namuji[hap % 7-1]
    
    return answer
