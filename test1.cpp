#include <iostream>
#include <stdlib.h>
#include <time.h> 
#include <string>
using namespace std;
const int MaxP = 45;

class Game{
	private:
		string* list_pname;
	    int* list_pnum;
	    int howmany;
	    int gift;
	    void print_gamer();	
    	void print_status(); 
    	void shuffle_int_list(int pint[]);
    	bool isprime(int n); 
	    
	public:
	    Game(string* list_pname, int* list_pnum);
    	void game_1();
    	void game_2();
    	void game_3();
};

Game::Game(string* list_pname, int* list_pnum)
:list_pname(list_pname), list_pnum(list_pnum)
{
  	howmany = MaxP;
  	gift = 0;
	shuffle_int_list(list_pnum);
	cout << "================================= Game Start ==================================\n" << endl;
	print_gamer();
	print_status(); 
}

void Game::shuffle_int_list(int pint[]){
	srand(time(0));
	
	for (int i = 0; i < MaxP; i++) {
        int temp = (rand() % MaxP + 1); // Random 난수 발생
        int temp2 = pint[i];    // 방저장
        pint[i] = pint[temp];
        pint[temp] = temp2; // 방 바꾸기
    }
}

void Game::print_gamer(){
	for(int i = 0; i < MaxP; i+=5){
    	cout 
		<< ((list_pnum[i+0] < 10)?" ":"") << list_pnum[i+0] << "번:  " << list_pname[i+0] << " | " 
		<< ((list_pnum[i+1] < 10)?" ":"") << list_pnum[i+1] << "번:  " << list_pname[i+1] << " | " 
		<< ((list_pnum[i+2] < 10)?" ":"") << list_pnum[i+2] << "번:  " << list_pname[i+2] << " | " 
		<< ((list_pnum[i+3] < 10)?" ":"") << list_pnum[i+3] << "번:  " << list_pname[i+3] << " | " 
		<< ((list_pnum[i+4] < 10)?" ":"") << list_pnum[i+4] << "번:  " << list_pname[i+4] << " | " 
		<< endl;
	}
}

void Game::print_status(){
	cout << "=============================== 참가인원 : " << ((howmany < 10)?" ":"") << howmany << "명 ===============================" << endl;
	cout << "=============================== 총 상금  : " << ((gift < 10)?" ":"") << gift << "억 ===============================\n" << endl;
}

bool Game::isprime(int n){
	for(int i = 2; i < n; i++){
		if(n%i == 0)
			return false;
	}
	return true;
}

void Game::game_1(){
	int dice = rand() % 6 + 2;
	for(int i = 0; i < MaxP; i++){
		if(list_pnum[i] % dice == 0){
			list_pname[i] = "탈  락";
			howmany--;
			gift++;
		}
	}
	cout << "1. 주사위(2 ~ 7) 게임 : " << dice << endl << endl;
	print_gamer();
	print_status(); 
}

void Game::game_2(){
	cout << "2. 프라임 게임 : 소수 or 합성수" << endl << endl;
	int choice = 0;
	do{
		cout << "다음 중 선택하세요" << endl << "1) 소수 2) 합성  : "; 
		cin >> choice;
		if (choice != 1 && choice != 2) {
            cout << "메뉴에서 고르세요." << endl << endl;
        }
	}while(choice != 1 && choice != 2);
	
	for(int i=0; i < MaxP; i++){
		if(list_pname[i] != "탈  락"){
			if((choice==1?isprime(list_pnum[i]):!isprime(list_pnum[i]))){
				list_pname[i] = "탈  락";
				howmany--;
				gift++;
			}
		}
	}
	cout << endl;
	print_gamer();
	print_status(); 
}

void Game::game_3(){
	cout << "3. 제비뽑기 게임 : 단 한명" << endl << endl;
	int choice = rand() % howmany + 1;
	int cnt = 0, temp = 0;
	for(int i = 0; i< MaxP; i++){
		if(list_pname[i] != "탈  락"){
			cnt++;
			if(cnt != choice){
				list_pname[i] = "탈  락";
				howmany--;
				gift++;
			}
			else temp = i;
		}
	}
	gift++;	//생존자는 자기 몫을 가져감 
	print_gamer();
	cout << endl << "최종우승자 : " << list_pnum[temp] << "번 " << list_pname[temp] << endl << endl; 
	print_status(); 
}

int main(){
    int pnum[MaxP];
    for(int i=0; i< MaxP; i++) pnum[i] = i+1;
    
	string pname[] = {
             //
    };

    Game g1(pname, pnum);
    g1.game_1();
    g1.game_2();
    g1.game_3();
    
	return 0;
}

