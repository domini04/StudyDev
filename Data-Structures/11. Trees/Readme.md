# Trees

### 개요

- essential data structure for storing ***hierarchical data*** with a ***directed flow***.
- composed of **nodes** which hold data
    - trees are often displayed with a single node at the top and connected nodes branching downwards
- **nodes**
    - store references to zero or more **other tree nodes**
    
    ![diagram represents nodes as rectangles and data as text](Trees%2094675b60224d4e349496a0c255b687c9/Untitled.png)
    
    diagram represents nodes as rectangles and data as text
    
    - **root node**
        - node at the very top. origin
    - **leaf node**
        - node without any children
- **`level`**: The height or depth of the tree. Root nodes are at level 1, their children are at level 2, and so on.

### 구현

- `TreeNodes`
    - have a value
    - have a reference to zero or more other `TreeNodes`
    - can add a node as a child
    - can remove a child
    - can *traverse* (or travel through) connected nodes

[Tree Traversal](https://www.notion.so/Tree-Traversal-d83f0531369547719f65d66ce54b9d1d)