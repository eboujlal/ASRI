import string
import re            
# Text cleaning
puncs = ['»',"«",'°','_','...','…','º','ˢ','§']
puncs.extend(string.punctuation)
puncs.remove("'")
puncs.remove("-")
def clean_text(text):
    text = text.replace("$",' dollar ')
    text = text.replace("€",' euro ')
    text = text.replace("°",' degré ')
    text = text.replace("#",' hashtag ')
    text = text.replace("c-a-d"," c'est à dire ")
    text = text.replace(" cad "," c'est à dire ")
    text = text.replace("½"," demi ")
    text = text.replace("œ","oe")
    text = text.replace("&"," et ")
    text = text.replace("’","'")
    text = text.replace("₂","")
    text = text.replace('–','-')
    text = text.replace('-',' ')
    text = re.sub('\s+', ' ', text).strip()
    words = text.split()
    stripped = []
    for word in words:
        word_s = []
        for c in word:
            if c not in puncs:
                word_s.append(c)
            else:
                word_s.append(" ")
        stripped.append("".join(word_s))
    return " ".join(stripped)


#print(clean_text("aujourd'hui,c'est c-a-d fista"))