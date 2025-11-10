#include <bits/stdc++.h>
using namespace std;

const int N = 1e5+10;
int parent[N], sizeArr[N];

// DSU functions for Kruskal
void make_set(int v){
    parent[v] = v;
    sizeArr[v] = 1;
}

int find_set(int v){
    if(v == parent[v]) return v;
    return parent[v] = find_set(parent[v]); // path compression
}

void union_set(int a, int b){
    a = find_set(a);
    b = find_set(b);
    if(a != b){
        if(sizeArr[a] < sizeArr[b]) swap(a, b);
        parent[b] = a;
        sizeArr[a] += sizeArr[b];
    }
}

// ---------- MAIN ----------
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    // For Kruskal: list of edges as {weight, {u, v}}
    vector<pair<int, pair<int,int>>> edges;

    // For Prim: adjacency list (1-based)
    vector<vector<pair<int,int>>> adj(n+1); // adj[u] = vector of {v, wt}

    for(int i = 0; i < m; ++i){
        int u, v, wt;
        cin >> u >> v >> wt;
        edges.push_back({wt, {u, v}});

        // undirected graph -> add both directions
        adj[u].push_back({v, wt});
        adj[v].push_back({u, wt});
    }

    // ---------------- KRUSKAL ----------------
    sort(edges.begin(), edges.end()); // sort by weight

    for(int i = 1; i <= n; ++i) make_set(i);

    long long kruskal_cost = 0;
    vector<pair<pair<int,int>, int>> kruskal_mst; // {{u,v}, wt}

    for(auto &e : edges){
        int wt = e.first;
        int u = e.second.first;
        int v = e.second.second;

        if(find_set(u) != find_set(v)){
            union_set(u, v);
            kruskal_cost += wt;
            kruskal_mst.push_back({{u, v}, wt});
        }
    }

    cout << "Kruskal MST edges:\n";
    for(auto &it : kruskal_mst){
        cout << it.first.first << " - " << it.first.second << " (wt: " << it.second << ")\n";
    }
    cout << "Kruskal Total Cost = " << kruskal_cost << "\n\n";

    // ---------------- PRIM ----------------
    // Prim's algorithm (using min-heap). Start from node 1.
    const long long INF = (1LL<<60);
    vector<long long> key(n+1, INF);     // best weight to connect node
    vector<int> parentPrim(n+1, -1);     // parentPrim[v] = parent node in MST
    vector<char> inMST(n+1, false);      // whether node included
    // min-heap of pairs {key, vertex}
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;

    // If graph might be disconnected and you want MST of whole graph,
    // you can run Prim from every unvisited node. Here we run from 1 and then check connectivity.
    key[1] = 0;
    pq.push({0, 1});

    while(!pq.empty()){
        auto cur = pq.top(); pq.pop();
        long long curKey = cur.first;
        int u = cur.second;
        if(inMST[u]) continue;
        inMST[u] = true;

        // relax neighbors
        for(auto &edge : adj[u]){
            int v = edge.first;
            int wt = edge.second;
            if(!inMST[v] && wt < key[v]){
                key[v] = wt;
                parentPrim[v] = u;
                pq.push({key[v], v});
            }
        }
    }

    // collect Prim edges and cost, and check if graph is connected
    long long prim_cost = 0;
    vector<pair<pair<int,int>, int>> prim_mst;
    int visitedCount = 0;
    for(int v = 1; v <= n; ++v){
        if(inMST[v]) visitedCount++;
        if(parentPrim[v] != -1){
            prim_mst.push_back({{parentPrim[v], v}, (int)key[v]});
            prim_cost += key[v];
        }
    }

    if(visitedCount != n){
        cout << "Prim's algorithm: Graph is disconnected. MST for whole graph does not exist.\n";
        // But still print the forest produced (one component reachable from node 1)
    }

    cout << "Prim MST edges (from starting node 1):\n";
    for(auto &it : prim_mst){
        cout << it.first.first << " - " << it.first.second << " (wt: " << it.second << ")\n";
    }
    cout << "Prim Total Cost (sum of added edges) = " << prim_cost << "\n";

    return 0;
}
