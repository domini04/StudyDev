#Call Stack의 개념을 이해하기 위한 예제

def sum_to_one(n): # n부터 1까지의 합을 구하는 함수
  result = 1
  call_stack = []

  print("------------------Call Stack 쌓는중...------------------")

  while n > 1: # call stack에 function call이 쌓이는 과정
    execution_context = {"n_value" : n} #execution context : 현재 실행중인 함수의 input값 정보
    call_stack.append(execution_context) #현재 실행중인 함수의 정보를 call_stack에 저장
    n -= 1
    print(call_stack)
  
  print("------------------Call Stack 쌓기 완료...------------------")
  print("Call Stack의 길이 : ", len(call_stack))
  print("Call Stack의 내용 : ", call_stack)
  print("------------------Call Stack을 호출합니다------------------")

  while len(call_stack) > 0: #call stack에 쌓인 function call을 하나씩 꺼내면서 실행
    execution_context = call_stack.pop() #call stack에서 가장 최근에 저장된 function call을 꺼냄
    n = execution_context["n_value"] #현재 실행중인 함수의 input값을 꺼냄
    result += n
    print(call_stack)
    
  print("BASE CASE REACHED")

  return result, call_stack


sum_to_one(4) #테스팅용