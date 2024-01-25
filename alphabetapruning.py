def minimax(depth, node, maximizing_player, values, alpha, beta):
  if depth == 0:
    return values[node]

  if maximizing_player:
    best_value = -float('inf')
    for child in range(2):
      value = minimax(depth - 1, node * 2 + child, False, values, alpha, beta)
      best_value = max(best_value, value)
      alpha = max(alpha, best_value)
      if beta <= alpha:
        break
    return best_value

  else:
    best_value = float('inf')
    for child in range(2):
      value = minimax(depth - 1, node * 2 + child, True, values, alpha, beta)
      best_value = min(best_value, value)
      beta = min(beta, best_value)
      if beta <= alpha:
        break
    return best_value

scores = []


total_nodes = int(input("Enter total number of leaf nodes: "))

for _ in range(total_nodes):
  scores.append(int(input("Enter node value: ")))

depth = int(input("Enter depth value: "))
start_node = int(input("Enter node value: "))

optimal_value = minimax(depth, start_node, True, scores, -float('inf'), float('inf'))

print(f"The optimal value is: {optimal_value}")
