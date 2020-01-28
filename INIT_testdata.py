### This script initializes the test data for testing by saving all the test strings into a dict, then saving it physically as a pickle


dictBoundaryStr = {
### Sentence with Quotes "" and ''
"str_doublequote" : '"Sentence with Double Quotes"',
"str_singlequote" : "'Sentence with single quotes'",
"str_slash" : r"""Sentence with forward/slash and backslash\n.""",

### >>> string.punctuation
###   !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
"str_punctuation" : r""""!#$%&()*+,-./:;<=>?@[\]^_`{|}~'""",

### >>> string.whitespace
###   ' \t\n\r\x0b\x0c'
"str_whitespace" : r"Sentence with \t,\n,\r,\x0b, and\x0c.",

### https://emw3.com/unicode-accents.html
###   ábcdeÁ êfghiÊ ïjklmÏ õPQRSÕ ùvwxyzÙ çatsÇ ©opyright ®eserved OnTalk™
"str_accented" : "\u00E1bcde\u00C1 \u00EAfghi\u00CA \u00EFjklm\u00CF \u00F5PQRS\u00D5 \u00F9vwxyz\u00D9 \u00E7ats\u00C7 \u00A9opyright \u00AEeserved OnTalk\u2122",

"str_300" : r"""## Mark Twain ## </xml> Steambo@t slang for 12 % feet % of water..!? Twain became ^_one_^ of the best-known $toryteller$ in the We$t. He honed a **distinctive** narrative style :: friendly, funny, irreverent ( ĭ-rĕv′ər-ənt ), often satirical && always eager to deflate the pretentious; &nbsp;&nbsp;.."""
}


import pickle 
f = open("DATABoundaryStrings.pkl","wb")
pickle.dump(dictBoundaryStr, f)
f.close()



### Sample code on usage 
#    f = open("DATABoundaryStrings.pkl", "r")
#    dict = pickle.load(f)