### Shortest Path (Dijkstra)


<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/Dijkstra%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="900" height="900"/></br>

> pic credit to 我的小腦袋 :)</br>



### My Note
Dijkstra又稱作戴克斯特拉算法，</br>
使用了廣度優先搜尋，</br>
是尋找從起點到其他節點的最短路徑演算法，</br>
用來解決所謂的最短路徑問題(Shortest Path Problem)。</br>
我認為Dijkstra可以細分成三個部分:</br>
1. 找一個節點當作起點，之後找到與起點相連但尚未被選到過的節點中距離最短的那個節點當下一個</br>
2. 並且再從這個選到的節點找到跟他相連的其他節點，並且依樣在取與它距離最短的當作下一個</br>
3. 當所有點都被當所有點都被家道過後，Dijkstra就完成了</br>

**其他更詳細的筆記與流程請參閱 : [我的HW6](https://github.com/Chieh-Yin/Chiehyin/tree/master/HW6)** </br>

### Complexity
* **Time Complexity :**</br>
O(|E||V|log|V|)</br>


### Reference
[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_9)</br>
[網路資料 1](https://zh.wikipedia.org/zh-tw/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95)</br>
