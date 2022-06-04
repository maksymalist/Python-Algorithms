const graph = {
  A: ["B", "C"],
  B: ["D", "E"],
  C: ["F"],
  D: [],
  E: ["F"],
  F: ["G"],
  G: ["B"],
};

const visited = new Set();
const queue = [];

const bfs = (visited, graph, node, target) => {
  visited.add(node);
  queue.push(node);

  while (queue.length > 0) {
    const node = queue.shift();

    if (node === target) {
      return true;
    }

    const neighbours = graph[node];
    for (let i = 0; i < neighbours.length; i++) {
      if (!visited.has(neighbours[i])) {
        visited.add(neighbours[i]);
        queue.push(neighbours[i]);

        if (neighbours[i] === target) {
          return true;
        }
      }
    }
  }
};

const found = bfs(visited, graph, "A", "G");

console.log(found ? "yes" : "no");
