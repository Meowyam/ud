import spacy
import spacy_udpipe

nlp = spacy.load("en_core_web_sm")
from spacy import displacy

from spacy_conll import init_parser

con = init_parser(
     "en", "udpipe", include_headers=True
)

text = "The PDPA covers personal data stored in electronic and non-electronic formats."
doc = nlp(text)
doc_con = con(text)
# print("just spacy")
# for token in nlp(text):
#   print(token.text, token.lemma_, token.pos_, token.dep_, token.head.text)
# displacy.serve(doc, style="dep")

def sub_fun(x, y):
  with open(y, "w") as f:
    for line in x.splitlines()[2:]:
      line_list = line.split()
      if (line_list[3] == 'NOUN'):
        make_fun = "FUN=" + line_list[2] + "_N"
      elif (line_list[3] == 'ADJ'):
        make_fun = "FUN=" + line_list[2] + "_A"
      elif (line_list[3] == 'DET'):
        if (line_list[2] == 'the'):
          make_fun = "FUN=DefArt"
        else:
          make_fun = "FUN=" + line_list[2] + "_Det"
      elif (line_list[3] == 'VERB'):
        make_fun = "FUN=" + line_list[2] + line_list[4]
      elif (line_list[3] == 'PRON'):
        make_fun = "FUN=" + line_list[3] + line_list[4]
      elif (line_list[3] == 'CCONJ'):
        make_fun = "FUN=" + line_list[2] + "_Conj"
      elif (line_list[3] == 'AUX' and line_list[2] == 'be'):
        make_fun = "FUN=UseComp"
      else:
        make_fun = "_"
      line_list[-1] = make_fun + "\n"
      list_to_line = " ".join(line_list)
      f.writelines(list_to_line)

conll = doc_con._.conll_str
sub_fun(conll, "spacy.conllu")


test = con("the black cat")
test_conll = test._.conll_str
#print(sub_fun(test_conll))

print("spacy_udpipe")
nlp_pipe = spacy_udpipe.load("en")
with open("spacy_udpipe.txt", "w") as f:
    for token in nlp_pipe(text):
        f.writelines([token.text, " ", token.lemma_, " ", token.pos_, " ", token.dep_, " ", token.head.text, "\n"])