function forceDirected() {
    queue()
        .defer(d3.csv, "nodes.csv",)
        .defer(d3.csv, "edges.csv")
        .await(function(error, file1, file2){
            create_force_layout(file1, file2);
        });
    function create_force_layout(nodes, edges) {
        var node_hash = {};
        for (x in nodes) {
            node_hash[nodes[x].id] = nodes[x];
        };
        for (x in edges) {
            edges[x].weight = parseInt(edges[x].weight);
            edges[x].source = node_hash[edges[x].source];
            edges[x].target = node_hash[edges[x].target];
        };
        var weight_scale = d3.scale.linear()
            .domain(d3.extent(edges, function(d) {return d.weight}))
    }
}