#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <tuple>
#include "sort.cpp"
#include "tree.cpp"
#include "heap.cpp"
#include "graph.cpp"
#include "patternMatching.cpp"

using namespace std;

int main()
{
    GraphNode *n1 = new GraphNode(1);
    GraphNode *n2 = new GraphNode(2);
    GraphNode *n3 = new GraphNode(3);
    GraphNode *n4 = new GraphNode(4);
    GraphL *testGraph = new GraphL();
    vector<tuple<GraphNode *, GraphNode *, int>> edges = {{n1, n2, 3}, {n1, n4, 1}, {n2, n3, 1}, {n4, n2, 1}};
    for (auto &[from, to, weight] : edges)
    {
        testGraph->addEdge(from, to, weight);
    }
    auto temp = testGraph->dijkstra(n1);
    cout << endl;

    string ts = "ababaca";
    vector<int> out = kmp(ts, "aba");

    return 0;
}
