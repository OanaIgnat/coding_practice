# Time & Space Complexity

1. What is the __time complexity__ of the following code :


        int j = 0;
        for(int i = 0; i < n; ++i) {
            while(j < n && arr[i] < arr[j]) {
                j++;
            }
        }
*Hint:* Variable j is not initialized for each value of variable i.

<details>
<summary>*Solution:*</summary>
<br>
Hence, the inner j++ will be executed at most n times.
The i loop also runs n times. So, the whole thing runs for O(n) times.
</details>

