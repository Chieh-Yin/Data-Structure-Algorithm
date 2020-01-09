### HW1

<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/QuickSort%E6%B5%81%E7%A8%8B%E5%9C%96.png" width="800" height="800"/>

> pic credit to 我自己的小腦袋:)

### What is Quick Sort ?

這次的作業是Quick Sort，</br>
Quick Sort 是先從要比較的list中選出一個數當作要比較的基準點(我作業取最後一個當基準點)，</br>
並把剩下的數和這個基準點比較大小，</br>
比他小的放左邊、比他大的放右邊，</br>
之後再在左邊的list和右邊的list中分別重複上述動作(recursive)直到每個數列中只剩一個數就完成。</br>


我發現這段程式會需要三個List去裝比基準點大的數、比基準點小的數、以及基準點，</br>
而要可以做排序比較的條件是長度一定要大於1，因為這樣他才有元素可以去做比較跟排序</br>
我的想法很簡單，就是最基本的分來分去，然後左右左右放。</br>
> 大於比較的數的話，放右邊；</br>
> 小於比較的數的話，放左邊；</br>
> 等於比較的數的話，放中間。</br>

### [完整程式碼](https://github.com/Chieh-Yin/Chiehyin/blob/master/HW1/HW1-QuickSort_new.ipynb)</br>
<img src="https://github.com/Chieh-Yin/Chiehyin/blob/master/Pictures/quick%20sort%20code.jpg" width="700" height="400"/>

### Reference
[網路資料 1](http://jialin128.pixnet.net/blog/post/142927691-%5b-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%5d-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95%EF%BC%88quick-sort%EF%BC%89in-python)</br>
