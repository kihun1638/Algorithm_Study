def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    MAX=min(max(citations),len(citations))
    for i in range(MAX):
        if citations[i]<=i+1:
            answer=max(citations[i],i)
            break
        if i ==(len(citations)-1):
            answer = len(citations)

    return answer