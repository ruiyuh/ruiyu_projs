
import time
import numpy as np
from numpy import linalg as LA
from gensim.models import KeyedVectors
import tokenize

t1 = time.time()
#download link: https://github.com/mmihaltz/word2vec-GoogleNews-vectors
path = 'C:/Users/RayHu/Downloads/google_w2v/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(path, binary=True)
print('-------------------------------------------')
print("Loading word2vec model cost %.3f seconds...\n" % (time.time() - t1))

# -------------------------------------------
#Loading word2vec model cost 108.422 seconds...

def vectorize(words):
    '''
    transform the doc and query into vectors
    '''
    word_vec = []
    for word in words:
        try:
            vec = model[word]
            word_vec.append(vec)
        except KeyError:
            # ignore the word if it is not in the w2v vocablary
            pass
    vector = np.mean(word_vec,axis = 0)
    return vector

def cos_sim(vector1, vector2):
    '''
    the fomula to calculte cosine cimilarity 
    '''
    sim = np.dot(vector1, vector2) / (LA.norm(vector1) * LA.norm(vector2))
    
    if np.isnan(np.sum(sim)):
        return 0
    
    return sim

def calc_sim(query, threshold = 0):
    '''
    calculate similarity scores between documents and the query
    '''
    query = clean_token(query)
    file_list = get_file_names()
    documents = {}
    
    for i in range(len(file_list)):
        documents[file_list[i]] = tokenize(convert(file_list[i]))
        
    query_vec = vectorize(query)
    results = {}
    
    for name, doc in documents.items():
        doc_vec = vectorize(doc)
        sim_score = cos_sim(query_vec, doc_vec)
        if sim_score > threshold:
            results[name] = sim_score
            sort_result = sorted(results.items(),key=operator.itemgetter(1),reverse=True)
    return sort_result
