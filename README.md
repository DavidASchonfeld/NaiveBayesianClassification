# Naive Bayes Classification
Code by David Schonfeld

### Description
This program uses Naive Bayes Classification to classify a series of votes as being from a Democrat or Republican.
<br />There is no Laplacian smoothing in this script.
<br />This causes a "ZeroDivisionError" to occur if
- a vote outcome (Y,N,Q)(Q represents abstention) in classifying_data does not exist
       in the same vote column in training data for the political
       party it should match with.
- a vote outcome (Y,N,Q) in classifying_data that did not
       at all exist in the training data.

 ### The Algorithms Formula
     For each party:
         <br />(Note: A = each value set for each law (Y, N or ?))
		 
         ```P(Party | A, B, C, D, E etc.)

           P(A|Party) * P(B|Party) * P(C|Party) etc. * P(Party)
         = -----------------------------------------
           P(A|Democ)P(B|Democ)...P(Democrat) + P(A|Repub)P(B|Repub)...P(Repub)```