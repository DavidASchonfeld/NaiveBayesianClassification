# Naive Bayes Classification
Code by David Schonfeld

### Description
This program uses Naive Bayes Classification to classify a series of votes as being from a Democrat or a Republican.
<br />There is no Laplacian smoothing in this script. This causes a "ZeroDivisionError" to occur if
- a vote outcome (Y,N,Q)(Q and ? both represent abstention) in classifying_data does not exist
       in the same vote column in training data for the political
       party it should match with.
- a vote outcome (Y,N,Q) in classifying_data that did not
       at all exist in the training data.

### The Algorithm's Formula
For each party:
<br />(Note: A = each value set for each law (Y, N or ?))
		 
```
P(Party | A, B, C, D, E etc.) =

  P(A|Party) * P(B|Party) * P(C|Party) etc. * P(Party)
= --------------------------------------------------------------------
  P(A|Democ)P(B|Democ)...P(Democrat) + P(A|Repub)P(B|Repub)...P(Repub)
  
```

### Inputs
There are 2 inputs in this script:
- the training set
- the data to be classified

<br />For both of these sets,
- each row represents a different politician.
- each column represents a different bill.
- you can add as many columns and/or rows as you would like.

#### The Training Set
Example:
```
republican,y,y,n,?,y,n,n,?,n,y,?,y,y,n,n,?
democrat,?,n,y,?,y,y,?,?,y,n,n,n,n,y,n,n
republican,n,?,n,?,y,?,n,n,y,n,?,y,y,y,n,?
republican,n,?,n,?,y,?,n,n,y,n,?,y,y,y,n,?
democrat,n,y,y,?,n,y,n,?,y,n,?,?,?,n,y,n
democrat,y,?,n,n,n,?,n,y,y,?,y,n,?,y,n,?
democrat,n,?,?,n,n,y,n,n,y,y,?,n,?,n,n,y
democrat,?,y,n,n,?,?,n,n,y,?,y,y,n,?,y,n
republican,n,?,?,?,y,n,y,n,y,n,y,?,n,n,y,n
democrat,?,?,n,n,?,y,y,n,?,?,y,?,n,y,y,y
```

#### Data to be Classified
Example:
```
party,n,?,n,y,n,y,y,y,?,n,n,n,y,n,?,n
party,n,y,y,?,y,n,n,n,y,?,?,y,n,y,n,y
party,y,?,y,y,y,?,?,n,y,y,n,?,n,n,y,y
party,?,n,?,n,?,y,?,n,n,n,y,n,n,?,n,n
```



