#include <iostream>
using namespace std;

int main(){
  int cnt;
  bool flag_1 = true;
  
  tag_test:
  
  cnt = 3;
  
  
  do
  {
    cout << cnt << "do while문과 goto문을 연습해 봅시다.\n";
    cnt--;
  }while(cnt);    //세미콜론 (;) 빼먹지 말 것!!

  if(flag_1){
    flag_1 = false;
    goto tag_test;
  }

  
  return 0;
}
