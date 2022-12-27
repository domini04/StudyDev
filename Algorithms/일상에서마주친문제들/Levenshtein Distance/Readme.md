# 이름이 살짝 다른 데이터들 merge

### 문제 정리

- **Goal**
    - [boxstats.com](http://boxstats.com) & [boxrec.com](http://boxrec.com) 에서 크롤링한 각 선수 데이터를 merge하려는 중
- **Problem**
    - 각 사이트에서 크롤링 해온 데이터를 <선수명>을 기준으로 합치려는데, 이름이 살짝씩 다름
![Levensthein3](https://user-images.githubusercontent.com/107534459/192491268-ad9afb3d-bb5b-4a8c-8431-c0916190b803.png)

    ![boxrec vs. boxstats 기준으로 한 글자 정도씩 다름](일상에서마주친문제들/Levenshtein Distance/이름이 살짝 다른 데이터들 merge 74f0c6cf8a16494eaf0f67a692eaa4f6/Untitled 1.png)
    
    boxrec vs. boxstats 기준으로 한 글자 정도씩 다름
    
     
    

### 해결

- **approach 1**
    - **regex를 사용한 매칭** → **nein**
    - abc가 있다면 a,b,c가 다름 및 a-b 사이, a-c사이 다른 글자가 들어있는 등 모든 경우의 수를 연산해야 함
- **approach 2**
    - **Levenshtein Distance**
        - [https://towardsdatascience.com/text-similarity-w-levenshtein-distance-in-python-2f7478986e75](https://towardsdatascience.com/text-similarity-w-levenshtein-distance-in-python-2f7478986e75)
        
![Levensthein1](https://user-images.githubusercontent.com/107534459/192491258-76bdc391-01c1-4f03-ae54-025b62c8e2d6.png)
        
        ```python
        def lev_dist(a, b):
            '''
            This function will calculate the levenshtein distance between two input
            strings a and b
            
            params:
                a (String) : The first string you want to compare
                b (String) : The second string you want to compare
                
            returns:
                This function will return the distnace between string a and b.
                
            example:
                a = 'stamp'
                b = 'stomp'
                lev_dist(a,b)
                >> 1.0
            '''
            
            def min_dist(s1, s2): #s1, s2는 pointer의 위치
        
                if s1 == len(a) or s2 == len(b):
                    return len(a) - s1 + len(b) - s2
        	
                # no change required
                if a[s1] == b[s2]: #맨 앞 글자가 같다면
                    return min_dist(s1 + 1, s2 + 1) #그 다음 글자로 넘어가면서 같은지 검사
        
                return 1 + min(  
                    min_dist(s1, s2 + 1),      # insert character
                    min_dist(s1 + 1, s2),      # delete character
                    min_dist(s1 + 1, s2 + 1),  # replace character
                ) #그 다음 글자가 다르다면 위 경우의 수 중 최솟값을 return
        					#Levenshtein 알고리즘 그대로 적용한거
        
            return min_dist(0, 0)
        ```
        
        - [https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0](https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0)
        
        ![행렬 버전]
![Levensthein2](https://user-images.githubusercontent.com/107534459/192491266-e93c2486-b7ad-497a-9c34-224643f376ee.png)

        
        행렬 버전
        
        - **string1 → string2으로 가기 필요한 edit횟수를 거리로 나타낸 알고리즘**
        - 파이썬에서는 **python-Levenshtein 라이브러리 사용(visual c++필요)**
            - **fuzzywuzzy 모듈도 사용 가능할듯?**
            - [https://towardsdatascience.com/fuzzywuzzy-basica-and-merging-datasets-on-names-with-different-transcriptions-e2bb6e179fbf](https://towardsdatascience.com/fuzzywuzzy-basica-and-merging-datasets-on-names-with-different-transcriptions-e2bb6e179fbf)
    - **lastname으로 합치기**
        - 모두 확인 한 것은 아니지만, 일반적으로 lastname의 철자는 동일한 것 같다.
        - 위 가정이 맞다면
            - **lastname으로 potential merge 검색 → Levenshtein Distance로 가장 가까운 데이터와 merge** 가능할듯?
        - 고려사항
            - 우선 몇 개의 data로 테스팅 필요
            - 합칠 후보군들의 log를 남겨놓자. 제대로 머지 되는지 확인차.
    - **approach 3**
        - **fuzzywuzzy 라이브러리 사용**
        - Levenshtein Distance 알고리즘을 파이썬에 구현해 놓았음
        

### 응용

- NLP에 사용가능할듯?
- Plagiarism Checker 만드는데도 사용 가능할듯!
