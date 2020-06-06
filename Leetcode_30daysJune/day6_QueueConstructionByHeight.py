
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people is sorted based on the height if heights are equal based on the no of people infront of that person
        ans = [[] for _ in range(len(people))]
        people.sort(key = lambda x:(x[0],x[1]))
        print(people)
        for i in people:
            count=0 # this is to count the no: of people equal to greater that can be of present person
            for j in range(len(people)):
                if ans[j]==[]:
                    count+=1
                else:
                    if ans[j][0]>=i[0]:
                        #checking the height of the person in that position is greater than or equal to the present one 
                        count+=1
                if count>i[1]:
                    ans[j] = i[::]
                    break
        return ans