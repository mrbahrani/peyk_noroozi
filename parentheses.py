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


if __name__ == "__main__":
    print(generate_all_parentheses(5))