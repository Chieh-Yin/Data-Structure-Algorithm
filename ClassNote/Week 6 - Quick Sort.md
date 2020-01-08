### Quick Sort

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/QuickSort%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="800" height="800"/>

> pic credit to 我自己的小腦袋:)

### My Note

這粒拜老師教的是Quick Sort，
Quick Sort 是先從要比較的list中選出一個數當作要比較的基準點(我習慣取最後一個)，</br>
並把剩下的數和這個基準點比較大小，</br>
比他小的放左邊、比他大的放右邊，</br>
之後再在左邊的list和右邊的list中分別重複上述動作(recursive)直到每個數列中只剩一個數就完成。</br>

Quick Sort 的特點在於他可以有效率的處理比較大量的資料。</br>

我發現這段程式會需要三個List去裝比基準點大的數、比基準點小的數、以及基準點，</br>
而要可以做排序比較的條件是長度一定要大於1，因為這樣他才有元素可以去做比較跟排序</br>
我的想法很簡單，就是最基本的分來分去，然後左右左右放。</br>
> 大於比較的數的話，放右邊；</br>
> 小於比較的數的話，放左邊；</br>
> 等於比較的數的話，放中間。</br>

### Complexity

* **Time Complexity :**</br>
  Best Time          O(nlogn) </br>
  Average Time       O(nlogn) </br>
  Worst Time         O(n^2) </br>
* **Space Complexity :** O(nlogn)</br>
* **Stable/Unstable :** Unstable</br>
  
  
### Reference:
[網路資料 1](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html)</br>
