import math
def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 3:
        return values[node_index]
    if maximizing_player:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(depth+1, node_index*2+i, False, values, alpha, beta)

            best = max(best,value)
            alpha = max(alpha, value)

            if alpha >= beta:
                break
        return best
    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(depth+1, node_index*2+i, True, values, alpha, beta)

            best = min(best, value)
            beta = min(beta, value)

            if alpha >= beta:
                break
        return best

values = [3,5,6,9,1,2,0,-1]

result = alpha_beta(0,0,True,values,-math.inf, math.inf)

print("Optimal value:" , result)
