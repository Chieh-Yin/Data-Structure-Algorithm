### Breadth-First Search


<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/BFS%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="900" height="1000"/></br>

> pic credit to 我的小腦袋 :)</br>


### My Note
BFS(Breadth-First Search)稱作"廣度優先搜尋法"，</br>
他是一種圖形搜索演算法，是屬於盲目搜索。</br>
通常利用Queue來處理，並以迴圈的方式進行。</br>

> 如果對Queue想更瞭解可以參考 : [我的Queue筆記](https://github.com/Chieh-Yin/Chiehyin/blob/master/ClassNote/Week%203%20-%20Stack%20%26%20Queue.md)</br>

而執行BFS的步驟可以分成幾個部分講解:</br>
1. 從出發點開始，走訪所有跟出發點有連結到的節點</br>
2. 之後再依序走訪與先前走訪過的節點有相連結但尚未被拜訪過的節點</br>
3. 直到所有節點都已被拜訪過後才算完成BFS</br>


### Complexity
* **Time Complexity :**</br>
O(|V|+|E|) = O(b^d)</br>
* **Space Complexity :**</br>
O(|V|+|E|) = O(b^d)</br>

### Reference
[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p)</br>
[網路資料 1](https://en.wikipedia.org/wiki/Breadth-first_search)</br>
