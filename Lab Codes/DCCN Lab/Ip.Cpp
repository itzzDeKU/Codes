#include<string>
#include<iostream>
#include<vector>

using namespace std;

string decToBinary(int n)
{
	string st;
    for (int i = 8; i >= 0; i--) {
        int k = n >> i;
        if (k & 1)
            st+="1";
        else
            st+="0";
    }
	return st;
}

void binIp(vector<int> &ipb){
	string bip;
	for(int i=0;i<4;i++){
		bip+=decToBinary(ipb[i]);
		if(i<3) bip+=".";
	}
	cout<<"Binary Ip address: "<<bip<<endl;
}

void checkClass(vector<int> &ipb){
     char cl;
	 string nwadd;
	 if(ipb[0]>=0 && ipb[0]<=127){
		cl ='A';
        nwadd+=to_string(ipb[0]);
		nwadd+='.';
		for(int i=1;i<4;i++){
			nwadd+='0';
			if(i<3) nwadd+=".";
		}
	 }
	 else if(ipb[0]>127 && ipb[0]<=191){
		cl ='B';
        nwadd+=to_string(ipb[0]);
		nwadd+=".";
		nwadd+=to_string(ipb[1]);
		nwadd+='.';
		nwadd+='0';
		nwadd+='.';
		nwadd+='0';		
	 }
	 else if(ipb[0]>191 && ipb[0]<=223){
		cl ='C';
		for(int i=0;i<3;i++){
			nwadd+=to_string(ipb[i]);
			if(i<3) nwadd+=".";
		}
		nwadd+='0';
	 }
	 else if(ipb[0]>224 && ipb[0]<=239){
		cl='D';
		nwadd+="Multicast";
	 }
	 else{
       cl='E';
	   nwadd+="Reserved";
	 }
	 cout<<"Class: "<<cl<<"\n"<<"Network Address: "<<nwadd;
}
int main(){
	vector<int> ipb;
	cout<<"Enter the Blocks: ";
	for(int i=0;i<4;i++){
	   int j; 
	   cin>>j;
	   ipb.push_back(j);
	}
	string ip;
	for(int i=0;i<4;i++){
		ip+=to_string(ipb[i]);
		if(i<3) ip+=".";
	}
	cout<<"Ip address is: "<<ip<<endl;
	binIp(ipb);
	checkClass(ipb);
	return 0;
}