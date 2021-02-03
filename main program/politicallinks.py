# python 3.7
# encoding utf-8
# DUAN UST time：

import os
import pandas as pd
import numpy as np
import json
from datetime import datetime
import re
os.chdir(r'd:\Users\duan\Desktop') # 自行修改

#导入词典
doc=open(os.path.join(".//dictionary.txt"),'r',encoding="utf-8").readlines()
doc=[i.strip( ) for i in doc ]
doc=list(filter(None, doc)) #去除空行
doc=list(set(doc))#去重
doc

####读取简历文件
path=r'\简历.xlsx'
df=pd.read_excel(path )
df.head(5)

######################################设置匹配 pattern
absolutewords = doc
pattern_l = r'.{0,8}(部|署|厅|[^公]司|局|处|[^(本|专)]科[^()]|委|室|办|所|军|(中心) \
              |(办事员)|(科长)|(主任)|(部长)|(干部)|(党组成员)).{0,8}'

patternhigh = r'.{0,8}%s.{0,8}'

pattern_polista = r'.{0,5}(人民代表大会(.(?![，；。]))*代表|人大(.(?![，；。]))*代表|党代表| \
政协(.(?![，；。]))*委员).{0,5}'


# 函数

def re_matchf(matchingdic, text, pattern_lowpro):
    lp = re.compile(pattern_lowpro)
    # relative match

    judg = lp.search(text)
    if judg:
        code = 1
        matching = [contents.group() for contents in lp.finditer(text)]
        for i in range(len(matching)):
            matchingdic[str(i)] = matching[i]
    else:
        code = 0

    return code, matchingdic


def ab_matchf(keyword, matchingdic, text, pattern_highpro):
    hp = re.compile(pattern_highpro)

    judg = hp.search(text)
    if judg:
        code = 1
        matching = [contents.group() for contents in hp.finditer(text)]
        matchingdic[keyword] = matching
    else:
        code = 0

    return code


# political  status match


def polistatus(text, pattern_s):
    ps = re.compile(pattern_s)
    judg = ps.search(text)

    if judg:
        code = 1
        matching = [contents.group() for contents in ps.finditer(text)]
    else:
        code = 0
        matching = None

    return code, matching

# 开始匹配
for index in df['Resume'].index.values:
    text_ = df.loc[index, 'Resume']
    # 针对某一个人的简历进行操作

    ############# relative matching
    dic = {}
    code1, matchcontents = re_matchf(dic, text_, pattern_l)

    # coding
    df.loc[index, 'relative'] = code1
    # input 关键词matching的内容
    if dic is not None:
        df.loc[index, 'relative匹配的关键词和内容'] = json.dumps(matchcontents, ensure_ascii=False)

    ##############absolute matching
    dic1 = {}
    code2 = 0
    for word in absolutewords:
        pattern_h = patternhigh % word

        result1 = ab_matchf(word, dic1, text_, pattern_h)
        code2 = code2 + result1

    # coding
    if code2 == 0:

        df.loc[index, 'absolute'] = 0
    else:

        df.loc[index, 'absolute'] = 1
        # input 关键词matching的内容

        df.loc[index, 'absolute匹配的关键词和内容'] = json.dumps(dic1, ensure_ascii=False)

    ##########political status matching
    code3, matchingpoli = polistatus(text_, pattern_polista)
    df.loc[index, 'politicalstatus'] = code3
    df.loc[index, '政治身份匹配内容'] = matchingpoli

#####导出结果
with pd.ExcelWriter(path, engine = 'openpyxl',mode='a') as f:
    df.to_excel(f,sheet_name='测试结果',index=False)