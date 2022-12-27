import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#Levenshtein Distance = LD
#ratio() : 두 문자열의 유사도를 측정  -> LD / len(string) 인듯
Str_A = 'FuzzyWuzzy is a lifesaver!'
Str_B = 'fuzzy wuzzy is a LIFE SAVER.' 

ratio = fuzz.ratio(Str_A.lower(), Str_B.lower())
print('Similarity score: {}'.format(ratio))

#partial_ratio() : allows for substring matching -> 더 짧은 string을 가져다가 긴 string에서 all possible substrings of same length를 비교
Str_A = 'Chicago, Illinois' 
Str_B = 'Chic go'
ratio = fuzz.partial_ratio(Str_A.lower(), Str_B.lower())
print('Similarity score: {}'.format(ratio))

#token_sort_ratio() : 문자열을 토큰화하고 토큰을 정렬한 다음 두 문자열의 유사도를 측정 -> 이후 ratio()와 동일
Str_A = 'Gunner William Kline' 
Str_B = 'Kline, Gunner William'
ratio = fuzz.token_sort_ratio(Str_A, Str_B)
print('Similarity score: {}'.format(ratio))

#token_set_ratio() : token_sort_ratio()와 유사하지만, 두 문자열의 토큰을 정렬한 다음 중복을 제거 -> 이후 ratio()와 동일
Str_A = 'The 3000 meter steeplechase winner, Soufiane El Bakkali' 
Str_B = 'Soufiane El Bakkali'
ratio = fuzz.token_set_ratio(Str_A, Str_B)
print('Similarity score: {}'.format(ratio))

print(fuzz.token_sort_ratio("mariners vs angels", "los angeles angels of anaheim at seattle mariners"))
print(fuzz.token_set_ratio("mariners vs angels", "los angeles angels of anaheim at seattle mariners"))
