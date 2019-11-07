## ♧ Merge Sort 與 Heap Sort 比較 ♧

### ♣ 何謂Merge Sort、Heap Sort ♣

* Merge Sort是所謂的合併排序法，</br>
他是運用先把一串數列一直對半拆，拆到後來都剩一個一個元素後，</br>
才進行比大小並且排序。</br>

* Heap Sort則是所謂的堆積排序法，</br>
他是運用將一串數列寫成樹的形式，然後在一棵一棵小樹中比較，</br>
進而去推導出所謂的樹根，之後將樹根跟最後一個數對調，</br>
再進行一連串的sift down動作，進行排續等等。</br>
而其中Heap Sort 又有分成: max heap以及 min heap。</br>
如圖所示。

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/heap%20structure.jpg" width="470" height="350"/>
(圖片來自老師的投影片: https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.g6504c48e6e_0_17)

### ♣ 時間複雜度 ♣

* Merge Sort 跟 Heap Sort 的時間複雜度均為: </br>
Average Time : O(n log n) </br>
Best Time : O(n log n) </br>
Worst Time : O(n log n) </br>


### ♣ 空間複雜度 ♣

* Merge Sort 的空間複雜度為: O(n) </br>
他會依著輸入的List裡面有多少個元素而改變， </br>
因為再做Merge Sort 的時候，需要先把每個元素都分割好，做暫時存放的動作，變成一個一個的才能做比較。

* Heap Sort 的空間複雜度為: O(1) </br>
他不像Merge Sort一樣需要切個List裡面的元素讓他們都變一個個得才能做比較，</br>
他是直接再同一個空間中做比較與排序的動作。


### ♣ 穩定性 ♣

* Merge Sort: 穩定 </br>
* Heap Sort: 不穩定 </br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/%E8%A4%87%E9%9B%9C%E5%BA%A6.jpg" width="470" height="350"/>

(參考資料(老師的投影片): https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.g6504c48e6e_0_6)
