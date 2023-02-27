# Quick Sort

### 개요

- **Pivot**과 **Divide and Conquer** strategy를 사용한 정렬 기법
- 각 ****Divide마다 **Pivot이 있어야 할 위치를 찾음**  → Divide하여 Pivot의 위치를 찾는 것을 Recursively 반복 → 정렬된 Pivot들의 위치를 조합
- **Pivot Selection**
    - Always pick the **first element** as a pivot
    - Always pick the **last element** as a pivot
    - Pick a **random element** as a pivot
    - Pick **median** as the pivot
        - first, middle element의 중간값을 pivot으로 사용

### **Divide**

- ***pivot***을 기준으로 다른 모든 element들을 비교하여 **세 그룹**으로 나눔
- **그룹**
    - A sub-array of elements **smaller than** the pivot.
    - The **pivot** itself.
    - A sub-array of elements **greater than** the pivot.

![Untitled](Quick%20Sort%2008b6eac46d734402ab0c9d9e91e0a07d/Untitled.png)

- Pivot의 왼쪽 배열, 오른쪽 배열을 나누어 반복
- **주의점**
    - Elements in the “smaller than” group ***are never compared*** with elements in the “greater than” group
    
    ```python
    [6,5,2,1,9,3,8,7]
    6 # The pivot
    [5, 2, 1, 3] # lesser than 6
    [9, 8, 7] # greater than 6
     
     
    [5,2,1,3]  # these values
    # will never be compared with 
    [9,8,7] # these values
    ```
    

### Implementation

[https://www.youtube.com/watch?v=Vtckgz38QHs](https://www.youtube.com/watch?v=Vtckgz38QHs)

- **Psuedocode**
    - 마지막 element를 pivot으로 선택한 경우

```
partition (arr[], low, high)
{
   pick pivot at rightmost element

    i = (low – 1)  // Index of smaller element and indicates the 
    // right position of pivot found so far

		iterate j loop over low~high
        // If current element is smaller than the pivot
        if (arr[j] < pivot){
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
		//when loop is finished, place pivot at tail pointer
    swap arr[i + 1] and arr[high])
		//divide into left and right of pivot, then repeat the process
}
```

### Performance

- **Time Complexity**
    - **Best Case & Average Case**
        - $O(NlogN)$의 time complexity를 갖는다
    - **Worst Case**
        - 이미 정렬된 list에서 최소/최대값을 pivot으로 선택한 경우 divide횟수가 늘어나므로 $O(N^2)$의 Time Complexity를 갖는다

![Untitled](Quick%20Sort%2008b6eac46d734402ab0c9d9e91e0a07d/Untitled%201.png)

- **Space Complexity**
    - Divide할 때 마다 새로운 배열을 메모리에 올리므로 $O(logN)$