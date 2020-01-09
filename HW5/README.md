### HW5 - Breadth-First Search & Depth-First Search


<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/BFS%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="900" height="1000"/></br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/DFS%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="900" height="900"/></br>

> pic credit to 我的小腦袋 :)</br>



### What is BFS?
BFS(Breadth-First Search)稱作"廣度優先搜尋法"，</br>
他是一種圖形搜索演算法，是屬於盲目搜索。</br>
通常利用Queue來處理，並以迴圈的方式進行。</br>

而執行BFS的步驟可以分成幾個部分講解:</br>
1. 從出發點開始，走訪所有跟出發點有連結到的節點</br>
2. 之後再依序走訪與先前走訪過的節點有相連結但尚未被拜訪過的節點</br>
3. 直到所有節點都已被拜訪過後才算完成BFS</br>



### What is DFS?
DFS(Depth-First Search)稱作"深度優先搜尋法"， </br>
他是一種用來搜尋一個樹或圖的演算法，跟BFS一樣亦屬於盲目搜索。 </br>
通常利用Stack來處理，並以遞迴的方式進行。 </br>

而我認為DFS的步驟可以分成幾個部分講解: </br>
1. 從出發點開始，走訪所有跟出發點有連結到的節點 </br>
2. 之後再走訪與之前走訪的節點有相連結的節點，並依序放入Stack中 </br>
3. 將最上面的拿出來當作下一個要走訪的節點 </br>
4. 重複2、3步驟直到所有節點都被拜訪過後才算完成DFS </br>



### [完整程式碼](https://github.com/Chieh-Yin/Chiehyin/blob/master/HW5/BFS_06170206.py)</br>






### Reference
[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p)</br>
[網路資料 1](https://en.wikipedia.org/wiki/Breadth-first_search)</br>
[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7aa022d8bc_2_0)</br>
[網路資料 1](https://zh.wikipedia.org/zh-tw/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)</br>

