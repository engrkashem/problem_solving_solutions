import math


class Solution:
    def candy(self, ratings):
        indx_ratings_dict = {}
        sorted_indx_ratings_dict = {}
        l, u = 0, len(ratings)
        for k, v in enumerate(ratings):
            if indx_ratings_dict.get(v):
                indx_ratings_dict[v].append(k)
            else:
                indx_ratings_dict[v] = [k]
        for i in sorted(indx_ratings_dict.keys()):
            sorted_indx_ratings_dict[i] = indx_ratings_dict[i]
        candies = [0]*u
        lowest_rating_candy_assign = False
        for l_rating, indx_lr in sorted_indx_ratings_dict.items():
            # print(l_rating, indx_lr)
            for indx in indx_lr:
                # print(indx)
                if not lowest_rating_candy_assign:
                    lowest_rating_candy_assign = True
                    candies[indx] = 1
                    continue
                c1, c2 = 1, 1
                if indx == 0:
                    if ratings[indx] > ratings[indx+1]:
                        # print(ratings[indx], ratings[indx+1], ' +1 29')
                        c1 = candies[indx+1]+1
                elif indx == u-1:
                    if ratings[indx] > ratings[indx-1]:
                        # print(ratings[indx], ratings[indx-1], ' -1 33')
                        c2 = candies[indx-1]+1
                else:
                    if ratings[indx] > ratings[indx+1]:
                        # print(ratings[indx], ratings[indx+1], ' +1 37')
                        c1 = candies[indx+1]+1

                    if ratings[indx] > ratings[indx-1]:
                        # print(ratings[indx], ratings[indx-1], ' -1')
                        c2 = candies[indx-1]+1

                mxc = max(c1, c2)
                candies[indx] = max(mxc, 1)
        ans = 0
        for i in candies:
            ans += i
        return ans


obj = Solution()
# ratings = [1, 0, 2]
# ratings = [1, 2, 2]
ratings = [1, 3, 2, 1, 0]
print(obj.candy(ratings))
