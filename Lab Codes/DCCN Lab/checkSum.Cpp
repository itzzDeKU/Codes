#include<iostream>
#include<vector>
#include<math.h>
 
using namespace std;
int main()
{
    int a,b;
    cin>>a>>b;
    int m[a][b];
    for (int i = 0; i < a; ++i)
    {
        for (int j = 0; j < b; ++j)
        {
           cin>>m[i][j];
        }

    }
    int d=0,i,j,l=0;
    for (i = 0; i < (a-1); ++i)
    {   d=0;
        for (j = 0; j < (b-1); ++j)
        {
           if(m[i][j]==1)
            d++;
        }
        if((d%2==0 && m[i][b-1]==0 )||(d%2!=0 && m[i][b-1]==1))
            break;
    }
    int w,q;
    for (w = 0; w < (b-1); ++w)
    {   l=0;
        for (q = 0; q < (a-1); ++q)
        {
           if(m[q][w]==1)
            l++;
        }
        if((l%2==0 && m[a-1][w]==0)||(l%2!=0 && m[a-1][w]==1))
            break;
    }
  
        m[i][w]=m[i][w]^1;
        

    cout<<"         --------Error detected-------- "<<"\n\n"<< "Row no. = "<<++i<<" , "<<"Column no. = "<<++w<<"\n\n";

    for (int ii = 0; ii < a; ++ii)
    {
        for (int jj = 0; jj < b; ++jj)
        {
           cout<<m[ii][jj]<<" ";
        }
        cout<<endl;

    }
    
}