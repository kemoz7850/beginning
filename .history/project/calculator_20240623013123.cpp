#include <iostream>
#include <vector>
#include "functions.cpp"
#include <iomanip>
using namespace std;
string allinone(string eq)
{
    int count  = 0;
    string g,problem;
    vector<vector<int>> checked = sorter(check(eq));
    if(checked[0][0] == -1)
    {
        return "invaild equation";
    }
    bool hasbrackets = false;
    for(int i = 0 ; i < eq.length(); i++)
    {
        if(eq[i] == '(' || eq[i] == ')')
        {
            hasbrackets = true;
            break;
        }
    }
    here:
    int size = (checked[2].size() > 0) ? maxi(checked[2])+1 : 0;
    if(!hasbrackets)
    {
        count++;
        goto pablo;
    }
    for(int i = 0 ; i < size; i++)
    {
        int start = checked[0][i];
        int end = checked[1][i];
        string operation;
        for(int j = start+1 ; j<end ; j++)
        {
            operation += eq[j];
        }
        operation = clear(operation,0,0,true);
        if(!hassign(operation)){continue;}
        else
        {
        problem = eq;
        eq = replace(eq,calc(operation),start,end);
        i=0;
        checked = sorter(check(eq));           
        count++;
        goto here;
        }

    }
    pablo:
    return calc(eq);
}
int main()
{
    string eq;
    cin>>eq;
    bool hasbrackets = false;
    for(int i = 0 ; i < eq.length(); i++)
    {
        if(eq[i] == '(' || eq[i] == ')')
        {
            hasbrackets = true;
            break;
        }
    }
    if(calc(eq)[0]=='I')
    {
        cout<<calc(eq);
    }
    else if(hasbrackets)
    {
    vector<vector<int>> checked = sorter(check(eq));
        cout<<setprecision(2)<<allinone(eq);
    }
    else{
        cout<<setprecision(2)<<stof(calc(eq));
    }
}