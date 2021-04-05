from nltk import RegexpParser
from nltk.tree import Tree
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize


def is_imperative(tagged_sent):
    if tagged_sent[-1][0] != "?":
        if tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD":
            return True

        else:
            chunk = get_chunks(tagged_sent)
            if type(chunk[0]) is nltk.tree.Tree and chunk[0].label() == "VB-Phrase":
                return True

    else:
        pls = len([w for w in tagged_sent if w[0].lower() == "please"]) > 0
        if pls and (tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD"):
            return True

        chunk = get_chunks(tagged_sent)
        if type(chunk[-1]) == nltk.tree.Tree and chunk[-1].label() == "Q-Tag":
            if chunk[0][1] == "VB" or (type(chunk[0]) is Tree and chunk[0].label() == "VB-Phrase"):
                return True
    return False


def get_chunks(tagged_sent):
    chunkgram = r"""VB-Phrase: {<DT><,>*<VB>}
                    VB-Phrase: {<RB><VB>}
                    VB-Phrase: {<UH><,>*<VB>}
                    VB-Phrase: {<UH><,><VBP>}
                    VB-Phrase: {<PRP><VB>}
                    VB-Phrase: {<NN.?>+<,>*<VB>}
                    Q-Tag: {<,><MD><RB>*<PRP><.>*}"""
    chunkparser = RegexpParser(chunkgram)
    return chunkparser.parse(tagged_sent)


def imperative_parser(input_text):
    tokenized_sentences_list = input_text.split(".")
    parsed_sentences = list()
    for sentence in tokenized_sentences_list:
        if sentence == "":
            continue
        if is_imperative(pos_tag(word_tokenize(sentence))):
            parsed_sentences.append(sentence)
            print(sentence)
    print(parsed_sentences)