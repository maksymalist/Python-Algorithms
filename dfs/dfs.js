const graph = {
  A: ["B", "C"],
  B: ["D", "E"],
  C: ["F"],
  D: [],
  E: ["F"],
  F: [],
};

const visited = new Set();

const dfs = (visited, graph, node, target) => {
  if (node === target) {
    return true;
  }
  visited.add(node);
  let neighbours = graph[node];
  for (let i = 0; i < neighbours.length; i++) {
    if (
      !visited.has(neighbours[i]) &&
      dfs(visited, graph, neighbours[i], target)
    ) {
      return true;
    }
  }
  return false;
};

const isTarget = dfs(visited, graph, "A", "F");

console.log(isTarget ? "yes" : "no");
