/**
 * Performs a Breadth-First Search on a graph represented as an adjacency list.
 * Returns the order in which nodes were visited starting from start_node.
 */
function breadthFirstSearch(adjacency_list, start_node) {
    const visited_nodes = new Set();
    const traversal_queue = [];
    const visit_order = [];

    visited_nodes.add(start_node);
    traversal_queue.push(start_node);

    while (traversal_queue.length > 0) {
        const current_node = traversal_queue.shift();
        visit_order.push(current_node);

        const neighbor_nodes = adjacency_list[current_node] || [];
        for (const neighbor_node of neighbor_nodes) {
            if (!visited_nodes.has(neighbor_node)) {
                visited_nodes.add(neighbor_node);
                traversal_queue.push(neighbor_node);
            }
        }
    }

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

const result = breadthFirstSearch(example_graph, 0);
console.log("BFS visit order:", result);
