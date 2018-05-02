# Naive Bayesian Classification
Code by David Schonfeld

<br />Using Naive Bayesian Classification to classify a series of votes as being from a democrat or republican
<br />There is no laplacian smoothCing in this script
<br />This causes a "ZeroDivisionError" to occur if
- a vote outcome (Y,N,Q) in classifying_data does not exist
       in the same vote column in training data for the political
       party it should match with
- a vote outcome (Y,N,Q) in classifying_data that did not
       at all exist in the training data

 ### The Algorithm's Formula
     For each party:
         <br />(Note: A = each value set for each law (Y, N or ?))
		 
         ```
		 P(Party | A, B, C, D, E etc.)

           P(A|Party) * P(B|Party) * P(C|Party) etc. * P(Party)
         = -----------------------------------------
           P(A|Democ)P(B|Democ)...P(Democrat) + P(A|Repub)P(B|Repub)...P(Repub)
		```