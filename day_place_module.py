from janome.tokenizer import Tokenizer
from copy import deepcopy

def seikei(s):
    t = Tokenizer()

    #print(type(t.tokenize(s)))
    # <class 'list'>

    #print(type(t.tokenize(s)[0]))
    # <class 'janome.tokenizer.Token'>
    flg=False
    now_target=[]
    target=[]
    p_pd=[]
    purge_part=['空白','サ変接続','括弧開','括弧閉']
    purge_surface=['地区','ブロック','東','西','南']
    place_half=['a','b','ab']
    #print(t.tokenize(s))
    for token in t.tokenize(s):
        if(flg):
            if(token.part_of_speech.split(',')[1] not in purge_part):
                now_target.append(token.surface)
        if(token.part_of_speech.split(',')[1]=='副詞可能'):
            if(flg):
                now_target=[]
            flg= True
            now_target.append(token.surface)
        if((token.surface in place_half)):
            flg= False
            target=deepcopy(now_target)
            now_target=[]

    #print(target)
    for row in target:
        if(row not in purge_surface):
            p_pd.append(str(row))
    return(p_pd)
