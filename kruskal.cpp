#include<bits/stdc++.h>
using namespace std;

const int N = 1e5+10;
int parent[N], sizeArr[N];

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
        if(sizeArr[a] < sizeArr[b])
            swap(a, b);
        parent[b] = a;
        sizeArr[a] += sizeArr[b];
    }
}

int main(){
    int n, m;
    cin >> n >> m;

    vector<pair<int, pair<int, int>>> edges;

    for(int i = 0; i < m; i++){
        int u, v, wt;
        cin >> u >> v >> wt;
        edges.push_back({wt, {u, v}});
    }

    sort(edges.begin(), edges.end());

    for(int i = 1; i <= n; i++) make_set(i);

    int total_cost = 0;

    cout << "Edges in MST:\n";
    for(auto edge : edges){
        int wt = edge.first;
        int u = edge.second.first;
        int v = edge.second.second;

        if(find_set(u) != find_set(v)){
            union_set(u, v);
            total_cost += wt;
            cout << u << " - " << v << " (wt: " << wt << ")\n";
        }
    }

    cout << "Total Cost of MST = " << total_cost << "\n";
    return 0;
}
