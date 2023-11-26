class Solution:
    def countTracker(self, my_str):
        tracker = {}
        for ii in my_str:
            if ii in tracker:
                tracker[ii] += 1
            else:
                tracker[ii] = 1
        return tracker


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteTracker = self.countTracker(ransomNote)
        magazineTracker = self.countTracker(magazine)
        for k in ransomNoteTracker:
            if (not k in magazineTracker) or (ransomNoteTracker[k] > magazineTracker[k]):
                return False
        return True
