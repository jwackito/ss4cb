/**
 * Performs a Depth-First Search on a graph represented as an adjacency list.
 * Returns the order in which nodes were visited starting from start_node.
 */
function depthFirstSearch(adjacency_list, start_node) {
    const visited_nodes = new Set();
    const visit_order = [];

    function explore_node(current_node) {
        visited_nodes.add(current_node);
        visit_order.push(current_node);

        const neighbor_nodes = adjacency_list[current_node] || [];
        for (const neighbor_node of neighbor_nodes) {
            if (!visited_nodes.has(neighbor_node)) {
                explore_node(neighbor_node);
            }
        }
    }

    explore_node(start_node);
    return visit_order;
}

const example_graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const result = depthFirstSearch(example_graph, 0);
console.log("DFS visit order:", result);
