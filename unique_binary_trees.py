def print_tree(tree):
    for line in tree:
        print("".join(line))


def print_binary_trees(n):
    dp = [[] for i in range(n+1)]
    if n < 1:
        print("No trees!")
        return
    dp[0] = [[]]
    dp[1] = [[['o']]]
    for total_nodes in range(2, n+1):
        for right_len in range(1, n):
            left_len = total_nodes-1 - right_len
            for right_tree in dp[right_len]:
                for left_tree in dp[left_len]:
                    right_dim = [len(right_tree), 0]
                    if len(right_tree)>0:
                        right_dim[1] = len(right_tree[0])
                    left_dim = [len(left_tree),0]
                    if len(left_tree)>0:
                        left_dim[1] = len(left_tree[0])
                    final_tree_dim = (right_dim[0] + left_dim[0]+1, 3 + max(right_dim[1], left_dim[1]))
                    tree = [[' ' for j in range(final_tree_dim[1])] for i in range(final_tree_dim[0])]
                    # col1
                    tree[0][0] = 'o'
                    tree[0][1] = '-'
                    # col2
                    if right_dim[0]>0:
                        tree[0][2] = '+'
                    else:
                        tree[0][2] = '|'

                    if left_dim[0] > 0:
                        for i in range(1, right_dim[0]):
                            tree[i][2] = '|'
                        tree[right_dim[0]][2] = '|'
                        tree[right_dim[0]+1][2] = '+'
                    # debug
                    # for i in range(right_dim[0]+2, final_tree_dim[0]):
                    #     tree[i][2] = '*'
                    # ToDo replace left and right
                    for r_i in range(len(right_tree)):
                        for r_j, r_ch in enumerate(right_tree[r_i]):
                            tree[r_i][3+r_j] = r_ch
                    for l_i in range(len(left_tree)):
                        for l_j, l_ch in enumerate(left_tree[l_i]):
                            tree[right_dim[0]+1+l_i][3+l_j] = l_ch
                    dp[total_nodes].append(tree)

    for i, tree in enumerate(dp[n]):
        print("Tree {}:".format(i+1))
        print_tree(tree)
        print()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_binary_trees(10)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
