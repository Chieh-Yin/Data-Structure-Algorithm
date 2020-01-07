### Stack & Queue

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/stack%20and%20queue.jpg" width="800" height="400"/>

> [pic credit](https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.g6377a33a16_0_77)



### My Note 

這個禮拜老師教的內容是 Stack 以及 Queue</br>

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/stack.jpg" width="800" height="300"/>

> [pic credit](http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)</br>

* **STACK的部分**</br>
Stack 的功能就像是我們平常在編輯器中用的回到上一步的概念，</br>
好比堆盤子，一層一層往上疊，但要拿時卻是最後一個先取出(LIFO)。</br>
   
   
<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/queue.jpg" width="800" height="300"/>

> [pic credit](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))</br>


* **QUEUE的部分**</br>
Queue 則是當我們的作業系統被多個程式共享資源時，</br>
但一次只能進行一個，這時就會需要他來替我們規劃排程順序。</br>
就好比排隊出場，一個一個按照先後順序，先進先出(FIFO)。</br>


### 語法
* **STACK的部分**</br>

  * **Push(Data)** :  將資料加進去Stack </br>
  * **Pop** : 把最上面的數取出來 </br>
  * **IsEmpty** : 確認Stack裡面是否有資料 </br>
  * **Top** : 回傳最上面的資料 </br>
  * **getSize**: 回傳資料筆數 </br>

* **QUEUE的部分**</br>

  * **Push(Data)** :  將資料加進去Queue後面，並更新成新的Back </br>
  * **Pop** :  把Front所指向的資料從Queue中移除，並更新Front，(也可寫dequeue) </br>
  * **getFront** : 回傳Front所指向的資料 </br>
  * **getBack** : 回傳Back所指向的資料 </br>
  * **IsEmpty** : 確認Queue裡面是否有資料 </br>
  * **getSize**: 回傳資料筆數 </br>
  
  
  ### Reference
  [老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.g6377a33a16_0_77)</br>
  [網路資料 1](http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)</br>
  [網路資料 2](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))</br>
  
  
  
