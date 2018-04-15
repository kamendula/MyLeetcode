class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_map = {}
        for m in magazine:
            if m not in m_map:
                m_map[m] = 0
            m_map[m] += 1
        for r in ransomNote:
            if r not in m_map:
                return False;
            if m_map[r] == 0:
                return False;
            m_map[r] -= 1
        return True