# Nodes

### Nodes

- fundamental building blocks of many computer science data structures
- An individual node **contains data** and **links to other nodes.**
    - node 안의 **데이터 +** 다른 node와의 **링크**로 구성
    - The data contained within a node can be a **variety of types**

![Untitled](Nodes%20b90c3507ca634deba36459cc2770679a/Untitled.png)

- **Pointers**
    - 노드 안의 **링크**를 가리킴
        - This is because they “point” to **another node**
    - 포인터가 **null** 값을 갖는 경우는 해당 data structure **경로의 끝**을 가리킴
    - 이러한 관계성을 갖는 node들의 집합이 **data structures**
    - nodes can be **orphaned** if there are **no existing links to them**.
    
    ![Untitled](Nodes%20b90c3507ca634deba36459cc2770679a/Untitled%201.png)
    

### Linking Nodes

- **node를 삭제 할 때 주의점**
    - node가 하나와의 node만 연결되어 있는 경우
        - parent node / child node를 함부로 삭제 할 경우 **다른 노드까지 잃어버릴 수 있음**
    
    ![node_a를 node_b와 바로 연결시켜 버릴 경우, node_b가 작동안함(**orphaned**)](Nodes%20b90c3507ca634deba36459cc2770679a/Untitled%202.png)
    
    node_a를 node_b와 바로 연결시켜 버릴 경우, node_b가 작동안함(**orphaned**)
