#Python에서는 array같은 contiguous data structure가 존재하지 않으므로, list를 사용해서 구현한다.
  #open addressing을 사용한 hash table 구현

class HashMap :
  def __init__(self, array_size) :
    self.array_size = array_size
    self.array = [None for item in range(array_size)] # array라는 instance var.을 정의하고, array_size만큼의 None으로 채워진 list를 할당한다.

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode() # key를 byte로 변환한다. .encode() : string을 byte로 이루어진 List로 변환해주는 메소드
    hash_code = sum(key_bytes) # key를 byte로 변환한 List의 각 요소를 더한다.
    return hash_code + count_collisions # Open Addressing : 기본 hash값에 count_collisions를 더해서 해싱한다.

  def compressor(self, hash_code):
    return hash_code % self.array_size # modulus operation을 통해 array_size로 hash_code를 압축한다

  def assign(self, key, value, num_collisions=0):
    array_index = self.compressor(self.hash(key)) # key를 hash_code로 변환한 후, array_size로 압축된 값을 array_index로 할당한다.
    current_array_value = self.array[array_index] 
    #3가지 경우가 존재
      #1. current_array_value(cav)가 None이라면 -> cav에 key와 value를 할당한다.
      #2. cav의 key와 찾는 key가 같다면 -> cav의 value를 찾는 value로 바꾼다. (update)
      #3. cav의 key와 찾는 key가 다르다면 -> cav의 key와 value를 key와 value로 바꾼다.
    if current_array_value is None: #1. 할당
      self.array[array_index] = [key, value] 
      return

    elif current_array_value[0] == key: # 2. update
      self.array[array_index] = [key, value] 
      return 

    else : # 3. collision 발생
      # 3-1 재귀함수 버전
        # 재귀함수 버전의 경우 num_collisions를 1씩 증가시키면서 다시 assign()을 호출한다.
      number_collisions = 1 # number_collisions을 1로 초기화한다.
      return self.assign(key, value, number_collisions)

      # 3-2 반복문 버전
        # 반복문 버전의 경우, 따로 assign()을 호출하지 않고, while문을 통해 num_collisions를 1씩 증가시키면서 hash_code를 다시 계산한다.
        # compressor(hash())를 통해 hash코드를 계산하는게 생략되서 좀 더 빠를지도?
      ## 먼저 assign()이 num_collisions 받는 것 삭제
      # number_collisions = 1 # number_collisions을 1로 초기화한다.
      # while (current_array_value[0] != key):  
      #   new_hash_code = self.hash(key, number_collisions) 
      #   new_array_index = self.compressor(new_hash_code)
      #   current_array_value = self.array[new_array_index]
      #   if current_array_value is None: 
      #     self.array[new_array_index] = [key, value]
      #     return
      #   if current_array_value[0] == key: 
      #     self.array[new_array_index] = [key, value] 
      #     return
      #   number_collisions += 1
      




  def retrieve(self, key):
    array_index = self.compressor(self.hash(key)) # 먼저 key가 저장된 array_index를 찾는다.
    payload = self.array[array_index] # array_index에 저장된 key와 value를 payload에 할당한다.  
    #3가지 경우의 수
      #1. payload가 None이라면 -> None을 return한다.
      #2. payload의 key와 찾는 key가 같다면 -> payload의 value를 return한다.
      #3. payload의 key와 찾는 key가 다르다면 -> 
    if payload is None: # 1. array_index에 아무것도 저장되어 있지 않다면,
      return None
    if payload[0] == key: # 2. 해당 index에 저장된 key와 찾는 key가 같다면,
      return payload[1] # 저장된 value를 return한다.
    else :  # 3. 해당 index에 찾는 key와 다른 key가 존재한다면,
      num_collisions = 1
      while payload[0] != key:
        # 3-1 while문 버전
          #먼저 hash값, array_index를 다시 계산하여 새로운 payload를 찾는다.
        new_hash_code = self.hash(key, num_collisions)
        new_array_index = self.compressor(new_hash_code)
        payload = self.array[new_array_index]
        if payload is None:
          return None
        if payload[0] == key:
          return payload[1]
        num_collisions += 1
      return


##테스팅
hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))