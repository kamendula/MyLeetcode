class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def all_cap(S):
            for s in S:
                if s < "A" or s > "Z":
                    return False
            return True

        def all_notcap(S):
            for s in S:
                if s < "a" or s > "z":
                    return False
            return True

        if len(word) == 1:
            return True
        if word[0] >= "A" and word[0] <= "Z":
            return all_cap(word[1:]) or all_notcap(word[1:])
        else:
            return all_notcap(word)


