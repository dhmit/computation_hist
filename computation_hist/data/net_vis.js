window.onload = function(){
    forceDirected();
};

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
            .domain(d3.extent(edges, function(d) {return d.weight;}))
            .range([.1, 1]);
        var force = d3.layout.force().charge(-1000)
            .size([500, 500])
            .nodes(nodes)
            .links(edges)
            .on("tick", force_tick);

        d3.select("svg").selectAll("line.link")
            .data(edges, function (d) {return d.source.id + "-" + d.target.id;})
            .enter()
            .append("line")
            .attr("class", "link")
            .style("stroke", "black")
            .style("opacity", 0.5)
            .style("stroke-width", function (d) {return d.weight});

        var node_enter = d3.select("svg").selectAll("g.node")
            .data(nodes, function (d) {return d.id})
            .enter()
            .append("g")
            .attr("class", "node");

        node_enter.append("circle")
            .attr("r", 5)
            .style("fill", "lightgray")
            .style("stroke", "black")
            .style("stroke-width", "1px");

        node_enter.append("text")
            .style("text-anchor", "middle")
            .attr("y", 15)
            .text(function (d) {return d.id;});

        force.start();

        function force_tick() {
            d3.selectAll("line.link")
                .attr("x1", function (d) {return d.source.x;})
                .attr("x2", function (d) {return d.target.x;})
                .attr("y1", function (d) {return d.source.y;})
                .attr("y2", function (d) {return d.target.y;});
            d3.selectAll("g.node")
                .attr("transform", function (d) {
                    return "translate("+d.x+","+d.y+")";
                })
        };
    }
}