// Exhaustively check all labelled 8-vertex simple graphs with all vertex degrees odd,
// searching for n=8 witness with fewer than 13 edges. Uses global sign symmetry.
// Pure C++20, g++ -O3; generates each odd-degree graph exactly once.
#include <cstdint>
#include <cstdio>
#include <bit>
#include <chrono>
using namespace std;

static unsigned char maj[256][256];
static uint64_t count_m[29]={}, connected_m[29]={}, tested_m[29]={}, positive_m[29]={}, graph_witness_m[29]={}; bool first_print=true;
static const int edges2[21][2]={
{0,1},{0,2},{0,3},{0,4},{0,5},{0,6},
{1,2},{1,3},{1,4},{1,5},{1,6},
{2,3},{2,4},{2,5},{2,6},
{3,4},{3,5},{3,6},
{4,5},{4,6},{5,6}};

int main(int argc, char**argv){
 int limit=12; if(argc>1)sscanf(argv[1],"%d",&limit);
 for(int nb=1;nb<256;nb++) {int d=popcount((unsigned)nb);for(int x=0;x<256;x++) maj[nb][x] = (2*popcount((unsigned)(nb&x))>d);}
 auto begin=chrono::steady_clock::now();
 unsigned char nexts[256];
 for(uint32_t bits=0;bits<(1u<<21);bits++){
  unsigned char adj[8]={};
  for(int k=0;k<21;k++)if((bits>>k)&1) {int u=edges2[k][0],v=edges2[k][1]; adj[u]|=1<<v;adj[v]|=1<<u;}
  for(int u=0;u<7;u++)if(!(popcount((unsigned)adj[u])&1)){adj[u]|=128;adj[7]|=(1<<u);}
  int m=0;for(int u=0;u<8;u++)m+=popcount((unsigned)adj[u]);m/=2;
  count_m[m]++;
  if(m>limit)continue;
  unsigned seen=1;for(int i=0;i<7;i++) {unsigned ext=seen;for(int u=0;u<8;u++)if(seen & (1u<<u))ext|=adj[u];if(ext==seen)break;seen=ext;}
  if(seen!=255)continue;
  connected_m[m]++;
  for(int x=0;x<256;x++) {
   unsigned y=0;for(int u=0;u<8;u++)y|=(unsigned)maj[adj[u]][x]<<u;nexts[x]=(unsigned char)y;
  }
  tested_m[m]++;
  bool had_witness=false;
  for(int x=0;x<128;x++){
    unsigned alive=255,a=x,b=nexts[a];
    for(int t=0;t<30;t++){
      unsigned c=nexts[b];
      alive&=(~(a^c))&255;
      if(alive==0){
       positive_m[m]++;
       had_witness=true;
       if(first_print){
        first_print=false;
        printf("FIRST_COUNTEREXAMPLE m=%d bits=%u x=%d t=%d\n",m,bits,x,t);
        for(int u=0;u<8;u++)printf("v%d: adj=%u degree=%d\n",u,adj[u],popcount((unsigned)adj[u]));
       }
       if(m<13)return 2;
       break;
      }
      if(a==c)break;
      a=b;b=c;
      if(t==29){fprintf(stderr,"internal error: no 2cycle by 30\n");return 3;}
    }
  }
  if(had_witness)graph_witness_m[m]++;
  if((bits&262143)==0){double secs=chrono::duration<double>(chrono::steady_clock::now()-begin).count();fprintf(stderr,"PROGRESS bits=%u elapsed=%.2fsec\n",bits,secs);}
 }
 double secs=chrono::duration<double>(chrono::steady_clock::now()-begin).count();
 printf("FINISHED limit=%d seconds=%.3f\n",limit,secs);
 for(int i=0;i<29;i++)if(count_m[i])printf("m=%d graphs=%llu connected=%llu tested=%llu witness_states=%llu witness_graphs=%llu\n",i,(unsigned long long)count_m[i],(unsigned long long)connected_m[i],(unsigned long long)tested_m[i],(unsigned long long)positive_m[i],(unsigned long long)graph_witness_m[i]);
}
