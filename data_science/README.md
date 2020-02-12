## Classification algorithms: 
### Supervised (labeled data):
- [x] Logistic Regression
- [x] Linear Regression
- [x] SVM 
- [x] K Nearest Neighbours
    - As we decrease the value of K, our **predictions become less stable**
    - The algorithm gets significantly **slower** as the number of examples and/or features/independent variables increase
    - An application of KNN-search: recommender systems, where we have computing resources to speedily handle the data 
- [x] Naive Bayes
    - They are **extremely fast** for both training and prediction
    - They provide straightforward probabilistic prediction
    - They are often very easily **interpretable**
    - They have **very few (if any) tunable parameters**
    - Works well when the **naive assumptions actually match the data** (very rare in practice)
    - Works well for very **well-separated categories**, when model complexity is less important
    - Works well for very **high-dimensional data**, when model complexity is less important
- [x] Decision Trees
    - Use **Entropy** and **Information Gain**
    - Computationally cheap to use 
    - Easy for humans to **understand results**
    - It can deal with irrelevant features
    - Prone to **overfitting**
- [x] Neural Networks
    - Very effective for **high dimensionality** problems 
    - Able to deal with **complex relations between variables**, non-exhaustive category sets  
    - Powerful **tuning options to prevent over- and under-fitting**

### Unsupervised (unlabeled data):
- [x] K-means
- [x] Hierarchical clustering

### Semi-supervised (in between):
- Semi-supervised learning uses both tagged and untagged data to fit a model 
- In some cases, such as Alexa’s, adding the untagged data actually improves the accuracy of the model 
- In other cases, the untagged data can make the model worse

- **Self-training** uses a model’s own predictions on unlabeled data to add to the labeled data set. 
    - You essentially set some threshold for the confidence level of a prediction, often 0.5 or higher, above which you believe the prediction and add it to the labeled data set. 
    - You keep retraining the model until there are no more predictions that are confident.


## Multimodal Methods:
- [x] LXMERT
- [x] Stacked cross attention for image - text matching

## Video:
- [x] I3D, C3D
## Text:
- [x] Transformer, Reformer, BERT, ELMo, .. 
## Tasks:
- [x] Q&A
- [x] Named Entity Recognition
- [x] Text Generation

----------------------------------------------------------------------------------------------------------
---------------------------------------------   Attention    ---------------------------------------------
----------------------------------------------------------------------------------------------------------
![alt text](https://github.com/OanaIgnat/coding_practice/blob/master/img/encoder-decoder-attention.png)
----------------------------------------------------------------------------------------------------------
---------------------------------------------   Transformer    ---------------------------------------------
----------------------------------------------------------------------------------------------------------

![alt text](https://github.com/OanaIgnat/coding_practice/blob/master/img/transformer.png)
----------------------------------------------------------------------------------------------------------
---------------------------------------------   BERT    ---------------------------------------------
----------------------------------------------------------------------------------------------------------
![alt text](https://github.com/OanaIgnat/coding_practice/blob/master/img/bert.png)
----------------------------------------------------------------------------------------------------------
---------------------------------------------   LXMERT    ---------------------------------------------
----------------------------------------------------------------------------------------------------------
![alt text](https://github.com/OanaIgnat/coding_practice/blob/master/img/lxmert.png)
----------------------------------------------------------------------------------------------------------
-----------------------------Stacked Cross Attention for Image-Text matching    -------
----------------------------------------------------------------------------------------------------------
![alt text](https://github.com/OanaIgnat/coding_practice/blob/master/img/SCAi2t.jpg)
----------------------------------------------------------------------------------------------------------
----------------------------- Identifying Visible Actions in Lifestyle Vlogs    --------------
----------------------------------------------------------------------------------------------------------
![alt text](https://github.com/OanaIgnat/coding_practice/blob/master/img/my_proj1.png)



