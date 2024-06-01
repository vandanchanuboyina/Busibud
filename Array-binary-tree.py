def ArrayChallenge(strArr):
    from collections import defaultdict

    parent_map = {}
    child_count = defaultdict(int)

    for relation in strArr:
        child, parent = map(int, relation.strip("()").split(","))
        
        # Check if the child already has a parent
        if child in parent_map:
            return "false"
        
        parent_map[child] = parent
        child_count[parent] += 1
        
        # Check if the parent has more than two children
        if child_count[parent] > 2:
            return "false"

    # Find the root (a node without a parent)
    all_nodes = set(parent_map.keys()).union(set(parent_map.values()))
    root_candidates = all_nodes - set(parent_map.keys())

    # Check if there's exactly one root
    if len(root_candidates) != 1:
        return "false"

    root = root_candidates.pop()
    visited = set()
    
    # DFS to check for cycles and connectedness
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for child in [key for key, value in parent_map.items() if value == node]:
            dfs(child)

    dfs(root)

    # Ensure all nodes are visited (connectedness)
    if len(visited) != len(all_nodes):
        return "false"

    return "true"

# Example usage
print(ArrayChallenge(["(1, 2)", "(2, 4)", "(7, 2)"]))  # Output: "true"
print(ArrayChallenge(["(1, 2)", "(2, 4)", "(4, 7)", "(7, 2)"]))  # Output: "false"
