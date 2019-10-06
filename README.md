## HW1 --- Planning by Dynamic Programming

### Introduction
This homework is relatively simple, yet there are some points that really confunses me. But, let's focus on the key points first.

* Policy Iteration 
    1. policy evaluation(average adjacent states)
    2. policy improvement(greedy method)
    3. finish iteration if ( |V(s)'-V(s)| < epsilon ), else: repeat 1. and 2.
* Value Iteration
    1. update every state by choosing maximum R + V(s)
    2. finish iteration if ( |V(s)'-V(s)| < epsilon ), else: repeat 1.
    3. update policy ***once***

By following the algorithm above, we can easily solve the gridmap testcases.



---


### Problems and Solutions
Two problems occurred while I was doing this homework:
1. the accuracy of floating points
2. the initial state-value really confused me

**For the first probelm**, when I tried to print out the state-value matrix, it seems that the adjacent state-value are the same, e.g., 18.0(17.9996) vs 18.0(17.9993). But, when I sorted them to choose the action greedily, the results were totally wrong, and that's how the bug happened.(In this case, we will get 17.99996 as the direction to go,  but we want them to choose 17.9996 and 17.9994 by 50/50 chance.)    

Thus, I use round() function to round the number to 6 decimal places, and it works well.

**To the second problem**, in the beginning, I tried to write a program that can escape those worst state. However, it contradicted to the algorithm mentioned in the RL lecture. Finally, I figured it out.

The initial value doesn't matter at all since it will converge to a stable value. In other words, it's just a transition, and it won't affect final policy.

---

### Results
Case1:
* Steps of policy iteration: 5
* Steps of value iteration: 3

| Policy Iteration | Value Iteration |
| -------- | -------- |
| ![](https://i.imgur.com/dczLZDl.png)| ![](https://i.imgur.com/hHcz2zk.png)|


Case2:
* Steps of policy iteration: 8
* Steps of value iteration: 6

| Policy Iteration | Value Iteration |
| -------- | -------- |
| ![](https://i.imgur.com/rAiJwRO.png)| ![](https://i.imgur.com/qrVuH9R.png)|


Case3:
* Steps of policy iteration: 8
* Steps of value iteration: 6

| Policy Iteration | Value Iteration |
| -------- | -------- |
| ![](https://i.imgur.com/puH2baC.png)| ![](https://i.imgur.com/pcdKY8c.png)|

Case4:
* Steps of policy iteration: 6
* Steps of value iteration: 4

| Policy Iteration | Value Iteration |
| -------- | -------- |
| ![](https://i.imgur.com/AqMlD6p.png)| ![](https://i.imgur.com/GoLqADl.png)|


---

### Feedback


---


