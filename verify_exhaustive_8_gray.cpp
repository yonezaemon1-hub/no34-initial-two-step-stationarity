// No.34 v0.2 independent census: enumerate odd-degree graphs by Gray-code
// toggling the triangle (u,v),(u,7),(v,7) from the 7-star.
// This differs from verify_exhaustive_8_parity.cpp's parity reconstruction.
// Standard C++20 only: g++ -O3 -std=c++20 verify_exhaustive_8_gray.cpp -o audit2
#include <cstdint>
#include <cstdio>
#include <bit>
#include <cstdlib>
using namespace std;

static const int ij[21][2] = {
{0,1},{0,2},{0,3},{0,4},{0,5},{0,6},
{1,2},{1,3},{1,4},{1,5},{1,6},
{2,3},{2,4},{2,5},{2,6},
{3,4},{3,5},{3,6},
{4,5},{4,6},{5,6}};

int main(){
 unsigned char adj[8] = {128,128,128,128,128,128,128,127};
 uint64_t graph_count[29]={}, bad_graph_count[29]={}, bad_state_count[29]={};
 unsigned char transition[256];
 for(unsigned k=0;k<(1u<<21);k++){
  if(k){int index=countr_zero(k),u=ij[index][0],v=ij[index][1];
    adj[u]^=(1u<<v)|128u; adj[v]^=(1u<<u)|128u; adj[7]^=(1u<<u)|(1u<<v);
  }
  int degree_total=0;
  for(int v=0;v<8;v++){
    int d=popcount((unsigned)adj[v]);
    if(d%2!=1){fprintf(stderr,"ODD DEGREE INVARIANT FAIL\n");return 3;}
    degree_total+=d;
  }
  int edges=degree_total/2; graph_count[edges]++;
  if(edges>13)continue;
  // Independently derive entire transition table, F : {0..255} -> {0..255}.
  for(int state=0;state<256;state++){
    unsigned new_state=0;
    for(int v=0;v<8;v++){
      int yes=popcount((unsigned)(adj[v]&state));
      int no=popcount((unsigned)adj[v])-yes;
      if(yes>no)new_state|=1u<<v;
    }
    transition[state]=(unsigned char)new_state;
  }
  bool graph_has_witness=false;
  for(int start=0;start<128;start++){
    unsigned char visited[256]={};
    unsigned stable_mask=255;
    int now=start;
    // Determine eventually repeated state from scratch. This does not rely
    // on period-two or a stopping bound, unlike the parity verifier.
    while(!visited[now]){
      visited[now]=1;
      int nxt=transition[now];
      int nxt2=transition[nxt];
      stable_mask &= ~(now^nxt2)&255;
      now=nxt;
    }
    if(stable_mask==0){
      if(edges<13){fprintf(stderr,"FAIL: counterexample on <13 edges, state=%d\n",start);return 4;}
      bad_state_count[edges]++;
      graph_has_witness=true;
    }
  }
  if(graph_has_witness)bad_graph_count[edges]++;
 }
 uint64_t sum=0;
 for(int m=0;m<=28;m++){
  if(graph_count[m])printf("m=%02d all_odd_graphs=%llu witness_graphs=%llu half_state_witnesses=%llu\n",m,
    (unsigned long long)graph_count[m],(unsigned long long)bad_graph_count[m],(unsigned long long)bad_state_count[m]);
  sum+=graph_count[m];
 }
 printf("total_graphs=%llu\n",(unsigned long long)sum);
 if(sum!=(1u<<21)||bad_graph_count[13]!=20160||bad_state_count[13]!=40320){
  fprintf(stderr,"EXPECTED COUNTS MISMATCH\n");return 5;
 }
 puts("PASS: all odd-degree 8-vertex graphs; m<13 has no witness; m=13 has 20160 witness graphs and 40320 successful initial states modulo global sign.");
}
