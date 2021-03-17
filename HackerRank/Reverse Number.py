class Solution:
    def reverse(self, x):
        Rev = 0
        if (x<-10) or (x>10):
            if((x>0) and (x%10 != 0)):
                Rev = [int(i) for i in str(x)]
                Rev[0], Rev[2] = Rev[2], Rev[0]
                Rev = [str(integer) for integer in Rev]
                Rev = int("".join(Rev))
                print(Rev)
                return Rev
            elif((x>0) and (x%10 == 0)):
                Rev = [int(i) for i in str(x)]
                Rev[0], Rev[2] = Rev[2], Rev[0]
                Rev = [str(integer) for integer in Rev]
                Rev = int("".join(Rev))
                print(Rev)
                return Rev
            elif(x<0):
                x*=-1
                Rev = [int(i) for i in str(x)]
                Rev[0], Rev[2] = Rev[2], Rev[0]
                Rev = [str(integer) for integer in Rev]
                Rev = (int("".join(Rev)))*-1
                print(Rev)
                return Rev
        print(Rev)
        return Rev

Test = Solution()
Test.reverse(1234)
