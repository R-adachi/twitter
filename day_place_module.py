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

def seikei_comp(s):
    t = Tokenizer()

    #print(type(t.tokenize(s)))
    # <class 'list'>

    #print(type(t.tokenize(s)[0]))
    # <class 'janome.tokenizer.Token'>
    flg=False
    now_target=[]
    target=[]
    pre_dp=[]
    dp=''
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

    for row in target:
        if(row not in purge_surface):
            pre_dp.append(str(row))

    #print(target)
    dow=['土曜日','日曜日','月曜日','火曜日']
    for r in range(len(pre_dp)):
        if(r==0):
            dp+=str(dow.index(pre_dp[r])+1)
            dp+='-'
        else:
            dp+=str(pre_dp[r])
            if(r==1):
                dp+='-'

    return(dp)
