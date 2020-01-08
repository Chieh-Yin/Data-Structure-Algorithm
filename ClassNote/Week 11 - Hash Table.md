### Hash Table

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/HashTable_ex.jpg" width="600" height="500"/>


<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/HashTable_%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="800" height="1000"/>

> pic credit to 我自己的小腦袋:)


### My Note
Hash Table 是所謂的雜湊表，他也是資料結構的一種。</br>
相較其他資料結構，因為用了雜湊函式Hash Function，可以更有效率的存取資料。</br>
我覺得整個Hash Table可以再細分為三個部分說明，</br>
1. Key當作我們輸入的字串。</br>
2. 中間將我們輸入的key經過運算的這個過程，則是所謂的Hash Function。</br>
在Hash Function中會進行的動作是mod(也就是程式碼中的"%")，</br>
將我們所輸入的值去取餘數放進相對應的抽屜中。</br>
3. 最後將輸入的key放進對應那層的抽屜叫做capacity。</br>
Capacity可以想成是一個裡面還沒放東西的陣列(只是轉一下變成直的來看)，
而這個陣列裡面有幾格是可以自行設定的。</br>

所謂的雜湊函式Hash Function是把我們輸入的key轉換成一個固定長度的不規則的雜湊值，</br>
而雜湊值通常用一堆隨機字母或數字組成的字串來代表。</br>
而Hash Function有一些特性:</br>
我們難以將雜湊碼推回去原本的字串，</br>
每組字串都有屬於自己的一組雜湊碼，鮮少會發生不一樣的字串但卻有一樣的雜湊碼。</br>
但如果發生這種"不一樣的字串但卻有一樣的雜湊碼"的狀況時，我們則稱為產生Collision 碰撞，</br>
遇到這種狀況的話，就必須換一個新的函式，一些常見的處理方法為:</br>
1. 開放定址法</br>
2. 單獨鍊表法</br>
3. 雙雜湊</br>
4. 再雜湊</br>


### Complexity
* **Time Complexity :**</br>
**Search 搜尋**</br>
Average: O(1)    </br>
Worst: O(n)</br>
**Insert 插入** </br>
Average: O(1)   </br> 
Worst: O(n)</br>
**Delete 刪除** </br>
Average: O(1)   </br> 
Worst: O(n)</br>

* **Space Complexity :**</br>
Average: O(n) </br>
Worst: O(n)</br>

**其他更詳細的筆記與流程請參閱 : [我的HW4](https://github.com/Chieh-Yin/Chiehyin/tree/master/HW4)** </br>


### Reference
[網路資料 1](https://en.wikipedia.org/wiki/Hash_table)</br>
[網路資料 2](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)</br>


