# Bubble Sorting

### 개요

- **알고리즘**
    1. array를 loop하면서 현재 index를 다음 index의 숫자와 비교
    2. 앞의 숫자가 더 크다면 순서를 바꿈
    3. 반복
        
        ![ezgif.com-gif-maker.gif](Bubble%20Sorting%20314994c2897147c4add9824d2a0c2e57/ezgif.com-gif-maker.gif)
        
- **특징**
    - 한 번의 iteration마다 가장 큰 수가 순서대로 뒤에 정렬되는 방식
        - n번의 loop를 돌면서 (n-1)번의 비교가 필요함
        - 따라서 $**O(n^2)**$의 Time Complexity를 갖는다
    - element들의 index를 변경할 때, temp var를 사용해서 옮겨줌
    
    ![Untitled](Bubble%20Sorting%20314994c2897147c4add9824d2a0c2e57/Untitled.png)