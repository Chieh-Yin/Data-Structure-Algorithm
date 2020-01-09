### HW4 - Hash Table

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/HashTable_ex.jpg" width="700" height="500"/>


<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/HashTable_%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="800" height="1000"/>

> pic credit to 我自己的小腦袋:)



### What is Hash Table?
我覺得整個Hash Table可以再細分為三個部分說明，</br>
1. Key當作我們輸入的字串。</br>
2. 中間將我們輸入的key經過運算的這個過程，則是所謂的Hash Function。</br>
在Hash Function中會進行的動作是mod(也就是程式碼中的"%")，</br>
將我們所輸入的值去取餘數放進相對應的抽屜中。</br>
3. 最後將輸入的key放進對應那層的抽屜叫做capacity。</br>
Capacity可以想成是一個裡面還沒放東西的陣列(只是轉一下變成直的來看)，
而這個陣列裡面有幾格是可以自行設定的。</br>

### [完整程式碼](https://github.com/Chieh-Yin/Chiehyin/blob/master/HW4/hash_table_06170206.py)</br>


### Reference
[網路資料 1](https://en.wikipedia.org/wiki/Hash_table)</br>
[網路資料 2](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)</br>
