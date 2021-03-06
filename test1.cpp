#include <iostream>
#include <stdlib.h>
#include <time.h> 
#include <string>
using namespace std;
string const Fall = "탈  락"; 

class Game{
	private:
		string* list_pname;
	    int* list_pnum;
	    int max_p;
	    int howmany;
	    int gift;
	    void print_gamer();	
    	void print_status(); 
    	bool isprime(int n);
	    
	public:
	    Game(string* list_pname, int* list_pnum, int max_p);
    	void game_1();
    	void game_2();
    	void game_3();
};

Game::Game(string* list_pname, int* list_pnum, int max_p)
:list_pname(list_pname), list_pnum(list_pnum), max_p(max_p)
{
  	howmany = max_p;
  	gift = 0;
	cout << "================================= Game Start ==================================\n" << endl;
	print_gamer();
	print_status(); 
}

void Game::print_gamer(){
	for(int i = 0; i < max_p; i+=5)
    	cout 
		<< ((list_pnum[i+0] < 10)?" ":"") << list_pnum[i+0] << "번:  " << list_pname[i+0] << " | " 
		<< ((list_pnum[i+1] < 10)?" ":"") << list_pnum[i+1] << "번:  " << list_pname[i+1] << " | " 
		<< ((list_pnum[i+2] < 10)?" ":"") << list_pnum[i+2] << "번:  " << list_pname[i+2] << " | " 
		<< ((list_pnum[i+3] < 10)?" ":"") << list_pnum[i+3] << "번:  " << list_pname[i+3] << " | " 
		<< ((list_pnum[i+4] < 10)?" ":"") << list_pnum[i+4] << "번:  " << list_pname[i+4] << " | " 
		<< endl;
}

void Game::print_status(){
	cout << "=============================== 참가인원 : " << ((howmany < 10)?" ":"") << howmany << "명 ===============================" << endl;
	cout << "=============================== 총 상금  : " << ((gift < 10)?" ":"") << gift << "억 ===============================\n" << endl;
}

bool Game::isprime(int n){
	for(int i = 2; i < n; i++) if(n%i == 0) return false;
	return true;
}

void Game::game_1(){
	int dice = rand() % 6 + 2;
	for(int i = 0; i < max_p; i++)
		if(list_pnum[i] % dice == 0){
			list_pname[i] = "탈  락";
			howmany--;
			gift++;
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
		if (choice != 1 && choice != 2) cout << "어허!! 다시 고르세요!!" << endl << endl;
	}while(choice != 1 && choice != 2);
	
	for(int i=0; i < max_p; i++)
		if(list_pname[i] != Fall)
			if((choice==1?isprime(list_pnum[i]):!isprime(list_pnum[i]))){
				list_pname[i] = Fall;
				howmany--;
				gift++;
			}
	cout << endl;
	print_gamer();
	print_status(); 
}

void Game::game_3(){
	cout << "3. 제비뽑기 게임 : 단 한명" << endl << endl;
	int choice = rand() % howmany + 1;
	int cnt = 0, temp = 0;
	for(int i = 0; i< max_p; i++)
		if(list_pname[i] != Fall){
			cnt++;
			if(cnt != choice){
				list_pname[i] = Fall;
				howmany--;
				gift++;
			}
			else temp = i;
		}
	gift++;	//생존자는 자기 몫을 가져감 
	print_gamer();
	cout << endl << "최종우승자 : " << list_pnum[temp] << "번 " << list_pname[temp] << endl << endl; 
	print_status(); 
}

void shuffle_list(int plist[], int maxp){
	for (int i = 0; i < maxp; i++) {
        int temp = (rand() % maxp + 1); // Random 난수 발생
        int temp2 = plist[i];    // 방저장
        plist[i] = plist[temp];
        plist[temp] = temp2; // 방 바꾸기
    }
}

void shuffle_list(string plist[], int maxp){
	for (int i = 0; i < maxp; i++) {
        int temp = (rand() % maxp + 1); // Random 난수 발생
        string temp2 = plist[i];    // 방저장
        plist[i] = plist[temp];
        plist[temp] = temp2; // 방 바꾸기
    }
}

int main(){
	//랜덤 테이블 설정 
    srand(time(0));	
    
    //플레이어 리스트, 플레이어 인원수, 플레이어 넘버 초기화 및 셔플 
	string pname[] = {
             "장수현", "고명진", "김도현", "김범수", "김수현",
             "박승민", "박태수", "신종현", "안혜원", "이건명",
             "이승재", "정의손", "정희재", "조동휘", "최서영",
             "최승규", "함동균", "허은화", "김하늘", "김민지",
             "임유빈", "이상연", "이수진", "박경원", "김근미",
             "김다예", "김동한", "김민준", "김승구", "김정태",
             "김정훈", "문철현", "방기승", "어경태", "유진규",
             "이상혁", "이세정", "이승윤", "이주희", "임진성",
             "장재은", "최현욱", "한성욱", "함범진", "김태간"
    };
    int max_p = sizeof pname / sizeof pname[0];	//인원수 
    int pnum[max_p];
    for(int i=0; i< max_p; i++) pnum[i] = i+1;
    shuffle_list(pnum, max_p);
    //shuffle_list(pname, max_p);

	//실행 
    Game g1(pname, pnum, max_p);
    g1.game_1();
    g1.game_2();
    g1.game_3();
    
	return 0;
}

