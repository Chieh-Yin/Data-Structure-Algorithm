## ♧ Merge Sort 與 Heap Sort 比較 ♧

### ♣ 何謂Merge Sort、Heap Sort ♣

Merge Sort是所謂的合併排序法，</br>
他是運用先把一串數列一直對半拆，拆到後來都剩一個一個元素後，</br>
才進行比大小並且排序。</br>

Heap Sort則是所謂的堆積排序法，</br>
他是運用將一串數列寫成樹的形式，然後在一棵一棵小樹中比較，</br>
進而去推導出所謂的樹根，在進行一連串的sift down動作，進行排續等等。</br>
而其中讓樹根變成最大的數，稱為max heap；</br>
讓樹根變為最小的樹，則稱為min heap。</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/heap%20structure.jpg" width="450" height="350"/>
(圖片來自老師的投影片: https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.g6504c48e6e_0_17)

### ♣ 時間、空間複雜度，以及穩定性 ♣

