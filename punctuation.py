
import re
t1= "এইটুকু বলতে চাই, টাকা পয়সা একটু হক-হালাল করে খাওয়া উচিৎ...."

whitespace = re.compile(u"[\s\u0020\u00a0\u1680\u180e\u202f\u205f\u3000\u2000-\u200a]+", re.UNICODE)

bangla_fullstop = u"\u0964"
punctSeq   = u"['\"“”‘’]+|[.?!,…]+|[:;]+"
punc = u"[(), #@_ঃ৳ -$%^&*+={}\[\]:\"|\'\~`<>/,¦!?½£¶¼©⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉¤¿º;-]+"
t1= whitespace.sub(" ",t1).strip()
t1 = re.sub(punctSeq, " ", t1)
t1 = re.sub(bangla_fullstop, " ",t1)
t1 = re.sub(punc, " ", t1)
print(t1)







