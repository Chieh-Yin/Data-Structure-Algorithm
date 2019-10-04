## Week 2 Class

### Design Linked List

這個禮拜老師教的內容是 Design Linked List</br>
Linked List 是一種資料結構，他是用一個節點Node來存取資料，<br/>
並且用一個箭頭Pointer指向下一個Node，這一個一個的Node、Pointer串在一起就是一個Linked List</br>
它的好處在於，存放資料可以放在不連續的記憶體中，所以比較不會浪費空間

-----
### 語法

*  `get(index)` : 輸入位置並取得那個位置上相對應的值
*  `addAtHead(val)` : 將新輸入的值放在這個Linked-List的頭
*  `addAtTail(val)` : 將新輸入的值放在這個Linked-List的尾巴
*  `addAtIndex(index, val)` : 將新輸入的值放在這個Linked-List的指定index的位置上</br>
    如果 :</br>
    index 等於 Linked List 的長度，就會加在尾巴</br>
    index 大於 Linked List 的長度，就沒有變動</br>
    index 小於 0，就加在頭的位置</br>          
*  `deleteAtIndex(index)` : 刪掉指定index位置上的值

