def back_track_auxiliary(ans, s, op, cl, n):
    if (len(s) == 2*n):
        ans.append(s)
        return

    if op < n:
        back_track_auxiliary(ans, s+'(', op+1, cl, n)
    if cl < op:
        back_track_auxiliary(ans, s+')', op, cl, n)


def generate_all_parentheses(n):
    answer = []
    back_track_auxiliary(answer, "", 0, 0, n)
    return answer

def comb(s1, s2):
    sf = set()
    for item1 in s1:
        for item2 in s2:
            sf.add(item1+item2)
    return sf

def generateParenthesis2(n: int) -> List[str]:
    dp = [set() for i in range(n+1)]
    dp[1].add("()")
    for c in range(2, n+1):
        for e in dp[c-1]:
            dp[c].add("("+e+")")
        for i in range(1, c):
            f = comb(dp[i], dp[c-i])
            dp[c] = dp[c].union(f)
    return list(dp[n])

if __name__ == "__main__":
    print(generate_all_parentheses(5))