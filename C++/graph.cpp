#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

class GraphNode
{
public:
    int id;
    unordered_map<GraphNode *, int> neighbors; // neightbor, weight

    GraphNode(int id)
    {
        this->id = id;
    }

    void addNeighbor(GraphNode *node, int weight = 1)
    {
        neighbors.insert({node, weight});
    }
};

/**
 * Graph represented in adjacency list
 */
class GraphL
{
private:
    unordered_set<GraphNode *> nodes;

public:
    GraphL()
    {
        nodes = {};
    }

    void addNode(GraphNode *node)
    {
        nodes.insert(node);
    }

    void addEdge(GraphNode *from, GraphNode *to, int weight = 1)
    {
        if (nodes.find(from) == nodes.end()) // node not found
        {
            addNode(from);
        }
        if (nodes.find(to) == nodes.end()) // node not found
        {
            addNode(to);
        }
        // edge does not exist or edge weight incorrect
        if (from->neighbors.find(to) == from->neighbors.end() ||
            from->neighbors[to] != weight)
        {
            from->neighbors[to] = weight;
        }
    }

    unordered_map<GraphNode *, int> getNeighbors(GraphNode *node)
    {
        return node->neighbors;
    }

    bool hasCycle()
    {
        stack<GraphNode *> unvisited;
        unordered_set<GraphNode *> visited;
        unvisited.push(*nodes.begin());
        while (!unvisited.empty())
        {
            GraphNode *cur = unvisited.top();
            unvisited.pop();
            if (visited.find(cur) != visited.end()) // cycle detected
            {
                return true;
            }
            visited.insert(cur);
            // push all neighbors into stack
            for (auto it = cur->neighbors.begin(); it != cur->neighbors.end(); it++)
            {
                unvisited.push(it->first);
            }
        }
        return false;
    }

    unordered_map<GraphNode *, int> dijkstra(GraphNode *start)
    {
        // initialize distances
        unordered_map<GraphNode *, int> dists;
        for (auto node : nodes)
        {
            if (node != start)
            {
                dists[node] = __INT_MAX__;
            }
            else
            {
                dists[node] = 0;
            }
        }
        // initialize heap
        unordered_set<GraphNode *> visited;
        priority_queue<
            pair<int, GraphNode *>,
            vector<pair<int, GraphNode *>>,
            greater<pair<int, GraphNode *>>>
            unvisited;
        unvisited.push({0, start});

        while (!unvisited.empty())
        {
            // go to the node with lowest cost
            GraphNode *cur = unvisited.top().second;
            unvisited.pop();
            visited.insert(cur);
            // update distance for all neighbors
            for (auto &[node, weight] : cur->neighbors)
            {
                dists[node] = min(dists[node], dists[cur] + weight);
                // push the node into heap
                if (visited.find(node) == visited.end())
                {
                    unvisited.push({dists[node], node});
                }
            }
        }
        return dists;
    }
};