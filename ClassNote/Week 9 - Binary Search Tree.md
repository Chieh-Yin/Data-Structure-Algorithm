### Binary Search Tree

由於Binary Search Tree成四種功能，</br>
所以圖片分成四張來表示。</br>

> Binary Saerch Tree - Insert</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/insert_ex.jpg" width="700" height="400"/></br>

> Binary Saerch Tree - Delete</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/delete_ex.jpg" width="1000" height="500"/></br>

> Binary Saerch Tree - Search</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/search_ex.jpg" width="500" height="600"/></br>

> Binary Saerch Tree - Modify</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/modify_ex.jpg" width="600" height="500"/></br>

> All pic credit to 我的小腦袋 :)</br>


### My Note

Binary Search Tree中文稱作二元搜索樹，</br>
一棵正確的binary search tree需要符合一些條件 :</br>
樹根的左節點只會存在比他小或相等的值；</br>
樹根的右節點只會存在比他大的值，</br>
也就是說Binary Search Tree 一定不會出現左節點大於右子樹的情況。</br>
且每個節點底下一定只會有小於或等於兩個子節點。</br>

至於各項Binary Search Tree的功能(insert,search,delete,modify)，</br>
請直接參閱上方四張圖片。</br>

### Treversal

Binary Search Tree有三種走訪方式，</br>
1. 前序 pre-order: 樹根、左節點、右節點 </br>
2. 中序 in-order: 左節點、樹根、右節點 </br>
3. 後序 post-order: 左節點、右節點、樹根 </br>
以下以圖片說明。</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/order_ex.jpg" width="700" height="800"/></br>

> pic credit to 我的小腦袋 :)</br>

### Complexity
* **Time Complexity :**</br>
**Search 搜尋 :**</br>
Average: O(log n)    </br>
Worst: O(n)</br>
**Insert 插入 :**</br>
Average: O(log n)    </br>
Worst: O(n)</br>
**Delete 刪除 :**</br>
Average: O(log n) </br>   
Worst: O(n)</br>

* **Space Complexity :** </br>
Average: O(n)  </br>
Worst: O(n) </br>

**其他更詳細的筆記與流程請參閱 : [我的HW3](https://github.com/Chieh-Yin/Chiehyin/tree/master/HW3)** </br>

### Reference
[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.g73e451e679_0_0)</br>
[網路資料 1](https://youtu.be/7vw2iIdqHlM)</br>
[網路資料 2](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)</br>
