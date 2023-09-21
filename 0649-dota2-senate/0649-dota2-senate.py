class Solution(object):
    def predictPartyVictory(self, senate):
        radiant = []  # Radiant 파티 의원을 저장할 큐
        dire = []     # Dire 파티 의원을 저장할 큐

    # 의원을 Radiant 또는 Dire 큐로 나누기
        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
        # Radiant 큐와 Dire 큐의 맨 앞 의원을 추출
            radiant_senator = radiant.pop(0)
            dire_senator = dire.pop(0)

        # 더 늦은 라운드에 투표권을 박탈한 경우, 다음 라운드로 다시 투표권을 부여
            if radiant_senator < dire_senator:
                radiant.append(radiant_senator + len(senate))
            else:
                dire.append(dire_senator + len(senate))

        return "Radiant" if radiant else "Dire"

        
        
            
        