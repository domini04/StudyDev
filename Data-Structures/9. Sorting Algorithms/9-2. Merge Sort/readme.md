# Merge Sort

### 개요

- Sorting algorithm that **breaks the list-to-be-sorted into smaller parts**, then sorts them during the merging process
    - 배열을 element단위로 나누고 다시 합치면서 sort
- ***Divide and Conquer*** 라고도 불림

![Untitled](Merge%20Sort%2014c376f2c4b641139111897e63ac7c90/Untitled.png)

### Divide

- splitting the data into “runs” or smaller components
- **방법**
    - Divide the input to our sort **in half**. Then **recursively** call the sort on each of those halves
        - 각 부분이 single element만 포함할 때까지 divide

![Untitled](Merge%20Sort%2014c376f2c4b641139111897e63ac7c90/Untitled%201.png)

### Conquer(Merge)

- 최소 단위(element)로 나눠진 배열을 다시 합침
    - merge하면서 sort
- **Sorting Algorithm**
    - `left_index` and `right_index` 를 복합 index로 사용
    - 각 `left_index` 와 `right_index` 를 비교
        - 그 중 더 작은 값을 왼쪽에 갖다놓고, 다음 비교할 index를 꺼내서 비교 → 반복

![Untitled](Merge%20Sort%2014c376f2c4b641139111897e63ac7c90/Untitled%202.png)

### Performance

- **Time Complexity**
    - 항상 **$O(N*log(N))$**의 시간 복잡도를 갖음
        - Best Case & Worst Case 모두 동일한 횟수를 비교하기 때문
- **Space Complexity**
    - $O(N)$의 공간 복잡도를 갖음
        - 각 Divide마다 새로운 배열을 메모리에 저장하기 때문