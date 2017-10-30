# Created by: Alireza Teimoori
# Created on: 24 Oct 2017
# Created for: ICS3UR-1
# Lesson: Unit 3-09
# This program if for learning loops inside loops

for outercounter in range(65,90+1):
    for innercounter in range(97,122+1):
        print( unichr(outercounter) + " --> " + unichr(innercounter) )
