# Model Selection

## Boolean Retrieval
**Advantages**
* easy to implement
* easy to interpret

**Disadvantages**
* Effectiveness depends entirely on entered query
* create complex queries are difficult

## BM25- a variant of tf-idf

>Bm25 is an algorithm used to evaluate the correlation between search terms and documents. It is an algorithm based on the probability retrieval model. 

**Instruction:**
we have a query and a batch of documents Ds. Now we need to calculate the correlation score between the query and each document D. Our approach is to first split the query to get the word q, and  the score of the word consists of three parts:

* Correlation between words and D
* Correlation between words and query
* Weight of each word

Finally, we calculate the sum each word scores, and get the score between the query and the document.

**formula**

For query Q and document d, we have BM25 d of Q:
	$ BM25_{score}(Q,d)=\sum_{t\in Q}w(t,d) $

$ w(t,d)=\frac{qtf}{k_3+qtf}\times \frac{k_1\times tf}{tf+k_1(1-b+b\times l_d/avg\_l)}\times log_2\frac{N-df+0.5}{df+0.5} ​$

> qtf：term frequency of Q
> tf：term frequency of d
> ld：length of a document
> avg_l：average length of documents
> N：number of documents
> df：frequency of document
> b,k1,k3：adjustable parameter
>
> * b: 0 $\leqslant$  b $\leqslant$  1; to avoid tiny documents get high weights
> * k1: k1$\geqslant$0;  if k1 = 0, it means we dont consider the term freq; 
> * k3: k3$\geqslant​$0; 
>
> 

Part I: $\frac{qtf}{k_3+qtf}\\$  Relevance between term and query

Part II : $\frac{k_1\times tf}{tf+k_1(1-b+b\times l_d/avg\_l)}\\$ Relevance between term and document

Part III: $log_2\frac{N-df+0.5}{df+0.5}$ term weight

