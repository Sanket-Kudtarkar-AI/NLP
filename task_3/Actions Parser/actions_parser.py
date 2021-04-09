from nltk import RegexpParser
from nltk.tree import Tree
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize
import unidecode


def is_imperative(tagged_sent):
    if tagged_sent[-1][0] != "?":

        if tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD" or tagged_sent[0][1] == "VBP":
            return True

        pls = len([w for w in tagged_sent if w[0].lower() == "please"]) > 0

        if pls:
            return True

        else:
            chunk = get_chunks(tagged_sent)
            if type(chunk[0]) is nltk.tree.Tree and (
                    chunk[0].label() == "VB-Phrase1" or chunk[0].label() == "VB-Phrase2" or chunk[
                0].label() == "VB-Phrase3" or chunk[0].label() == "VB-Phrase4" or chunk[0].label() == "VB-Phrase5" or
                    chunk[0].label() == "VB-Phrase6" or chunk[0].label() == "VB-Phrase7"):
                return True

    else:
        pls = len([w for w in tagged_sent if w[0].lower() == "please"]) > 0

        if pls:
            return True

        chunk = get_chunks(tagged_sent)
        if type(chunk[-1]) == nltk.tree.Tree and chunk[-1].label() == "Q-Tag":
            if (chunk[0][1] == "VB" or (type(chunk[0]) is Tree and (
                    chunk[0].label() == "VB-Phrase1" or chunk[0].label() == "VB-Phrase2" or chunk[
                0].label() == "VB-Phrase3" or chunk[0].label() == "VB-Phrase4" or chunk[0].label() == "VB-Phrase5" or
                    chunk[0].label() == "VB-Phrase6" or chunk[0].label() == "VB-Phrase7"))):
                return True

    return False


def get_chunks(tagged_sent):
    chunkgram = r"""
                    VB-Phrase2: {<RB><VB>}
                    VB-Phrase3: {<RB><VBG>}
                    
                    VB-Phrase4: {<UH><,>*<VB>}
                    VB-Phrase5: {<UH><,><VBP>}
                    VB-Phrase7: {<NN.?>+<,><VB>}
                    
                    Q-Tag: {<,><MD><RB>*<PRP><.>*}"""

    chunkparser = RegexpParser(chunkgram)
    return chunkparser.parse(tagged_sent)


def attach_he(sent):
    sent = word_tokenize(sent.lower())
    return [(word, tag[:2]) if tag.startswith('VB') else (word, tag) for word, tag in pos_tag(['He'] + sent)[1:]]


def imperative_parser(input_text):
    input_text = unidecode.unidecode(input_text)
    tokenized_sentences_list = sent_tokenize(input_text)
    for sentence in tokenized_sentences_list:
        if is_imperative(pos_tag(word_tokenize(sentence))):
            print(sentence, " Y\n")
            continue

        else:
            if pos_tag(word_tokenize(sentence))[0][0] == 'I':
                print(sentence, " N\n")
            elif is_imperative(attach_he(sentence)):
                print(sentence, " Y\n")
                continue
            else:
                print(sentence, " N\n")
