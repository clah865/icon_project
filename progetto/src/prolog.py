'''
@author: Massaro, Trotti & Marino
'''

import pytholog as pl

def ospedalization(ris):
    kb = pl.KnowledgeBase('ospedalization')

    if(int(ris[0][3]) > 30):
        bmi = 1
    else:
        bmi = 0

    if(int(ris[0][6])== 2):
        diabetes = 1
    else:
        diabetes = 0


    kb([f"highChol(a,{ris[0][1]})",
        f"BMI(b,{bmi})",
        f"stroke(c,{ris[0][1]})",
        f"diabetes(d,{diabetes})",
        f"diffWalk(e,{ris[0][14]})",
        "several(S) :- highChol(a, S), BMI(b, S), stroke(c, S), diabetes(d, S), diffWalk(e, S)"
        ])

    if (kb.query(pl.Expr(f"several(1)"))[0] == 'Yes'):
        print("Il sistema ha rilevato dei sintomi gravi."
              "\nE' consigliata la visita di uno specialista!")