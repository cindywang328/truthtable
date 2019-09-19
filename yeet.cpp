#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
// assume X is >= 2 and <= 26
void f(int x){
  string row1 = "";
  char a = 'a';
  for (int i = 0; i<(x); i++){
    row1 += a;
    row1 += " | ";
    a = a + 1;
  }
  cout << (row1.substr(0, row1.length()-3)) << " ||" << endl;
  int q = (int)(pow(2, (x)));

  vector<vector<string> > ans(q, vector<string>( x, "" ) );

  string tf = "F";
  int n = pow(2, (x));
  int y = n/2;

  for(int j = 0; j < x; j++){
    for(int i = 0; i<n; i++){
      ans[i][j] = tf;
      if((i+1)%y == 0){
        if (tf == "T") tf = "F";
        else tf = "T";
      }
    }
    y /= 2;
  }
  for (int i = 0; i< ans.size(); i++){
    for(int j = 0; j < ans[0].size()-1; j++){
      cout << ans[i][j] << " | ";
    }
    cout << ans[i][ans[0].size()-1] << " ||"<< endl;
  }
}
int main() {
  f(4);
}

//f(["A", "B"])

    
