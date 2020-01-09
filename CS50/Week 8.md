### Week 8

我觀看的影片是CS50第八周的影片，[CS50-Week8](https://www.youtube.com/watch?v=9qvt6MwBKZQ)</br>

### My Note

第八周的課程先複習了上一周所講的linked list，</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/CS50%20linked%20list.jpg" width="800" height="500"/></br>

> [pic credit](https://www.youtube.com/watch?v=9qvt6MwBKZQ)</br>

影片提到Array跟Linked List的差別，</br>
說道Linked List是用一個節點Node來存取資料，</br>
並且用一個箭頭Pointer指向下一個Node，</br>
他存放資料可以在不連續的記憶體中，所以比較不會浪費空間；</br>
然而Array要儲存資料的話，會需要有足夠的空間才能放。</br>


接著是關於Hash Table，</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/CS50-2.jpg" width="800" height="500"/></br>
<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/CS50-3.jpg" width="800" height="500"/></br>

> [pic credit](https://www.youtube.com/watch?v=9qvt6MwBKZQ)</br>

Hash Table 是所謂的雜湊表，他也是資料結構的一種。</br>
相較其他資料結構，因為用了雜湊函式Hash Function，可以更有效率的存取資料。</br>
所謂的雜湊函式Hash Function是把我們輸入的key轉換成一個固定長度的不規則的雜湊值，</br>
而雜湊值通常用一堆隨機字母或數字組成的字串來代表。</br>

再來是運用Hahs Table帶到Queue，</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/CS50-4.jpg" width="800" height="500"/></br>

> [pic credit](https://www.youtube.com/watch?v=9qvt6MwBKZQ)</br>

Queue是當我們的作業系統被多個程式共享資源時，</br>
一次只能進行一個，這時就會需要他來替我們規劃排程順序。</br>
就好比排隊出場，一個一個按照先後順序，先進先出(FIFO)。</br>

Queue語法:</br>
Push(Data) : 將資料加進去Queue後面，並更新成新的Back</br>
Pop : 把Front所指向的資料從Queue中移除，並更新Front，(也可寫dequeue)</br>
getFront : 回傳Front所指向的資料</br>
getBack : 回傳Back所指向的資料</br>
IsEmpty : 確認Queue裡面是否有資料</br>
getSize: 回傳資料筆數</br>

最後教到Tree的結構以及Binary Tree跟Binary Search Tree，</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/CS50-5.jpg" width="800" height="500"/></br>
<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/CS50-6.jpg" width="800" height="500"/></br>

> [pic credit](https://www.youtube.com/watch?v=9qvt6MwBKZQ)</br>

廣義的樹可以有很多子節點，</br>
但二元樹就最多只能有兩個子節點(左子樹根右子樹)，</br>
而Binary Search Tree中文稱作二元搜索樹，</br>
一棵正確的binary search tree需要符合一些條件 :</br>
樹根的左節點只會存在比他小或相等的值；</br>
樹根的右節點只會存在比他大的值，</br>
也就是說Binary Search Tree 一定不會出現左節點大於右子樹的情況。</br>
且每個節點底下一定只會有小於或等於兩個子節點。</br>


### Reference
[CS50](https://www.youtube.com/watch?v=9qvt6MwBKZQ)</br>
[CS50 Note](http://cdn.cs50.net/2013/fall/lectures/8/m/notes8m/notes8m.html)</br>










