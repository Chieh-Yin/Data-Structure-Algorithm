### HW6 - Shortest Path (Dijkstra) & Minimum Spanning Tree (Kruskal)


<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/Dijkstra%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="900" height="900"/></br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/Kruskal%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="900" height="900"/>

> pic credit to 我的小腦袋 :)</br>





### What is Shortest Path (Dijkstra) ?
Dijkstra又稱作戴克斯特拉算法，</br>
使用了廣度優先搜尋，</br>
是尋找從起點到其他節點的最短路徑演算法，</br>
用來解決所謂的最短路徑問題(Shortest Path Problem)。</br>
我認為Dijkstra可以細分成三個部分:</br>
1. 找一個節點當作起點，之後找到與起點相連但尚未被選到過的節點中距離最短的那個節點當下一個</br>
2. 並且再從這個選到的節點找到跟他相連的其他節點，並且依樣在取與它距離最短的當作下一個</br>
3. 當所有點都被當所有點都被家道過後，Dijkstra就完成了</br>

### WHat is Minimum Spanning Tree (Kruskal) ?
Kruskal又稱作克魯斯克爾算法，</br>
是尋找最小生成樹(Minimum Spanning Tree)的演算法，</br>
而我認為Kruskal可以細分成三個部分:</br>
1. 將各個點連成的邊按照大小排列，從權值最低的邊開始</br>
2. 在這個過程中不能發生迴圈的問題</br>
3. 直到加了所有節點-1後停止</br>

### [完整程式碼](https://github.com/Chieh-Yin/Chiehyin/blob/master/HW6/Dijkstra_06170206.py)</br> 


### Reference
[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_9)</br>
[網路資料 1](https://zh.wikipedia.org/zh-tw/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95)</br>
[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_9)</br>
[網路資料 1](https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95)</br>


