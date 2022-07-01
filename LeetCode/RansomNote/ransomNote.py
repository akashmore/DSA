class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = {}
        magazineNoteDict = {}
        for ele in ransomNote:
            if ele not in ransomNoteDict:
                ransomNoteDict[ele] = 1
            else:
                ransomNoteDict[ele] += 1
        for ele2 in magazine:
            if ele2 not in magazineNoteDict:
                magazineNoteDict[ele2] = 1
            else:
                magazineNoteDict[ele2] += 1
        
        for key in ransomNoteDict.keys():
            if key in magazineNoteDict:
                if ransomNoteDict[key] <= magazineNoteDict[key]:
                    pass
                else:
                    return False
            else:
                return False
        return True