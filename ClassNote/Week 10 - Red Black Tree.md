### Red Black Tree

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/red%20black%20tree%20ex.jpg" width="800" height="400"/>


> [pic credit](https://docs.google.com/presentation/d/e/2PACX-1vRxyJRARq0BNuGJq_o2cUHIXBWrRSZrAOyXOSt9qCTSjQtyp8XqFq3VuNn3gCt3sXenOZmWLqIjcyFs/pub?start=false&loop=false&delayms=3000&slide=id.g70c10e5ce6_0_32)</br>


### My Note

Red Black Tree中文稱作紅黑樹， </br>
它是一個以樹的資料結構為基礎延伸的， </br>
為了解決一般二元樹的不平衡問題，所以紅黑樹會自動旋轉， </br>
讓樹達到平衡狀態，才進入下一層。 </br>
如圖所示 : </br>
<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/red%20black%20tree%20rotate.jpg" width="800" height="400"/>

> [pic credit](https://docs.google.com/presentation/d/e/2PACX-1vRxyJRARq0BNuGJq_o2cUHIXBWrRSZrAOyXOSt9qCTSjQtyp8XqFq3VuNn3gCt3sXenOZmWLqIjcyFs/pub?start=false&loop=false&delayms=3000&slide=id.g70c10e5ce6_0_32)</br>

紅黑樹的特徵包含 : </br>
每個節點都有顏色(紅或黑)， </br>
而樹根一定是黑色的 </br>
紅色節點下面的子節點一定接黑色的； </br>
但黑色的節點下面的子節點可以是黑或紅色的。 </br>
所有空的節點一定是黑色的。 </br>
從樹根到其他節點或空子節點的每條路徑，一定要有一樣數目的黑色節點。 </br>
如圖所示 :</br>
<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/red%20black%20tree.jpg" width="600" height="500"/>

> [pic credit](https://docs.google.com/presentation/d/e/2PACX-1vRxyJRARq0BNuGJq_o2cUHIXBWrRSZrAOyXOSt9qCTSjQtyp8XqFq3VuNn3gCt3sXenOZmWLqIjcyFs/pub?start=false&loop=false&delayms=3000&slide=id.g70c10e5ce6_0_32)</br>

**想了解更詳細的紅黑數請參閱 :[這個影片](https://www.youtube.com/watch?v=5IBxA-bZZH8) 以及 [這個影片](https://www.youtube.com/watch?v=qvZGUFHWChY
)** </br>

### Complexity
* **Time Complexity :**</br>
**Search 搜尋 :**</br>
Average: O(log n)    </br>
Worst: O(log n)</br>
**Insert 插入 :**</br>
Average: O(log n)    </br>
Worst: O(log n)</br>
**Delete 刪除 :**</br>
Average: O(log n) </br>   
Worst: O(log n)</br>

* **Space Complexity :** </br>
Average: O(n)  </br>
Worst: O(n) </br>




### Reference
[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vRxyJRARq0BNuGJq_o2cUHIXBWrRSZrAOyXOSt9qCTSjQtyp8XqFq3VuNn3gCt3sXenOZmWLqIjcyFs/pub?start=false&loop=false&delayms=3000&slide=id.g70c10e5ce6_0_32)</br>
[網路資料 1](https://zh.wikipedia.org/wiki/%E7%BA%A2%E9%BB%91%E6%A0%91)</br>
[網路資料 2](https://www.youtube.com/watch?v=5IBxA-bZZH8)</br>
[網路資料 3](https://www.youtube.com/watch?v=qvZGUFHWChY)</br>




