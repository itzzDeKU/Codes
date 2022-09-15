#include<iostream>
#include<string.h>

using namespace std;
int main(){
    char txt[50];
    cout<<"Enter Plain Text: ";
    cin.getline(txt,50);
    int choice,len,ch,i,j,key;
    cout<<"Enter Key: ";
    cin>>key;
    len=strlen(txt);
    cout<<"Enter Choice : \n1. Encryption\t2. Decryption \n";
    cin>>choice;
    if(choice==1){
        for(i=0;txt[i]!='0';++i){
            ch=txt[i];
            //For lower-case encryption
            if(ch>='a' && ch<='z'){
                ch+=key;
                if(ch>'z'){
                    ch=ch-'z'+'a'-1;
                }
                txt[i]=ch;
            }
            //For Upper-case encryption
            if(ch>='A' && ch<='Z'){
                ch+=key;
                if(ch>'Z'){
                    ch=ch-'Z'+'A'-1;
                }
                txt[i]=ch;
            } 
        }
        cout<<"Ciphered Text is: "<<txt;
    }
    else if(choice == 2){
        for(i=0;txt[i]!='0';++i){
            ch=txt[i];
            //For lower-case decryption
            if(ch>='a' && ch<='z'){
                ch-=key;
                if(ch<'a'){
                    ch=ch+'z'-'a'+1;
                }
                txt[i]=ch;
            }
            //For Upper-case decryption
            if(ch>='A' && ch<='Z'){
                ch-=key;
                if(ch<'A'){
                    ch=ch+'Z'-'A'+1;
                }
                txt[i]=ch;
            } 
        }
        cout<<"Deciphered Message is: "<<txt;
    }

}