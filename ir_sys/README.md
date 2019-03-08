CSC575_PROJ
==============================

Section: Ruiyu



Project Organization
------------

    ├── LICENSE
    ├── README.md         
    ├── data
    │   ├── document       <- resume rocuments.
    │   ├── index          <- inverted index and lengh index.
    │   ├── jd             <- indeed job description 
    │   └── raw           
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-ir-initial-ranking-exploration`.
    │
    ├── references          
    │
    ├── src                <- py file.
    │   
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`

## Model Selection: BM25

>Bm25 is an algorithm used to evaluate the correlation between search terms and documents. It is an algorithm based on the probability retrieval model. 

**Instruction:**

we have a query and a batch of documents Ds. Now we need to calculate the correlation score between the query and each document D. Our approach is to first split the query to get the word q, and  the score of the word consists of three parts:

* Correlation between words and D
* Correlation between words and query
* Weight of each word

Finally, we calculate the sum each word scores, and get the score between the query and the document.

**Formula:**

See BM25_fomula.pdf in the references folder


