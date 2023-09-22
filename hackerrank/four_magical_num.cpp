#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int a[n];
        bool isAllNeg = true;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            if (a[i] > 0)
                isAllNeg = false;
        }

        sort(a, a + n);
        for (int i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }
        cout << "\n";
    }
}
// test = int(input())
// for _ in range(test):
//     n = int(input())
//     str = input().split(' ')
//     num = []
//     for i in str:
//         if i:
//             if i[0] == '-':
//                 num.append(-int(i[0]))
//             else:
//                 num.append(int(i[0]))
//     print(num)
// # num.sort()
// # isAllNeg = True
// # for i in num:
// #     if i > 0:
// #         isAllNeg = False
// # if isAllNeg:
// #     maxN = num[0]
// #     minN = num[-1]
// #     print(maxN*maxN, minN*minN, maxN+maxN, minN+minN)
// # else:
// #     maxN = num[-1]
// #     minN = num[0]
// #     print(maxN*maxN, minN*minN, maxN+maxN, minN+minN)
