# -*- coding: utf-8 -*-
"""EDGAR (no loop).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13RaCYQC9RbjzbHJaxcaFen32-HeAPvav
"""

from textblob import TextBlob
import nltk
nltk.download('punkt')

!pip install edgar

import edgar

"""https://pypi.org/project/edgar/

This url contains the documentation for the edgar package used to retrieve SEC filings.

**The code block below consists of three variable assignments which will retrieve the specified data.**

The first line of code uses the *Company* function which requires two parameters: company name and CIK. The variable *company* is set to the company of interest using these two fields.

The second line of code uses the *getAllFilings* function which returns a *lxml.html* form. There are four possible parameters for this function (filingType, priorTo, ownership, noOfEntries), however given the structure of the code block only the first two parameters are required in this instance. The *filingType* parameter can be specified for the type of document to be retrieved (10-K, S-8, 8-K). The *priorTo* parameter must be specified in a string as *YYYY-MM-DD*.

The third line of code uses the *getDocuments* function of the *Edgar*-class which returns a list of strings in which each string contains the body of a specified document. The first parameter of this function takes a *lxml.html* form which is returned from the *getAllFilings* function from the line prior. The second parameter is *noOfDocuments* which is the number of documents to be returned; for usage in this IDE, this number should always be set to 1 to avoid crashing.
"""

company = edgar.Company("AMAZON COM INC", "0001018724")
tree = company.getAllFilings(filingType = "10-K", priorTo = '2014-12-31')
docs = edgar.getDocuments(tree, noOfDocuments=1)

print(tree)

print(str(docs))

docstr = str(docs)
type(docs)

article = TextBlob(docs)

articlepolarity = article.sentiment.polarity
articlesubjectivity = article.sentiment.subjectivity
print(articlepolarity)
print(articlesubjectivity)