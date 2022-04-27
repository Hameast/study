//완성해서 commit하세요
#include <iostream>
#include <cstring>
using namespace std;

class CGV {
private:
	string m_name;
	string m_age;
	string m_loc;

	char** makemap() {
		char** p_map = new char*[m_map_row];
		for (int r = 0; r < m_map_row; r++)
			p_map[r] = new char[m_map_col];

		for (int r = 0; r < m_map_row; r++)
			for (int c = 0; c < m_map_col; c++)
				p_map[r][c] = '.';

		return p_map;
	}

public:
	char** map;
	int m_map_row;
	int m_map_col;
	string* havetime;
	CGV() = delete;
	CGV(string name, string age, string loc, int row, int col, string str[])
	:m_name(name), m_age(age), m_loc(loc), m_map_row(row), m_map_col(col), havetime(str) { 
		map = makemap();
	}
	string getName() {
		return m_name;
	}
	string getAge() {
		return m_age;
	}
	string getLoc() {
		return m_loc;
	}
	int getMaprow() {
		return m_map_row;
	}
	int getMapcol() {
		return m_map_col;
	}
	char** getMap() {
		return map;
	}
};

void printwellcome() {
	cout << "=============================================" << endl
		<< "1. 영화 예매" << endl
		<< "2. 프로그램 종료" << endl
		<< "=============================================  " << endl
		<< "원하시는 메뉴를 선택해 주세요:";
}

void printCGV(CGV* cgv) {
	for (int i = 0; i < 4; i++) {
		cout << i + 1 << ". "
			<< cgv[i].getName() << " / "
			<< cgv[i].getAge() << " / "
			<< cgv[i].getLoc() << endl;
	}
	cout << "=============================================  " << endl;
}

void printCGVtime(CGV cgv) {
	int max_t = 4;
	for (int i = 0; i < max_t; i++) {
		cout << i + 1 << ". "
			<< cgv.havetime[i] << "    " 
			<< 0 << " / " << 90 << endl;
	}
}

void printMap(CGV cgv) {
	cout << "  ";
	for (int i = 0; i < cgv.getMapcol(); i++)
		cout << i + 1 << " ";
	cout << endl;

	for (int i = 0; i < cgv.getMaprow(); i++) {
		cout << (char)('A' + i) << " ";
		for (int j = 0; j < cgv.getMapcol(); j++) {
			cout << cgv.map[i][j] << " ";
		}
		cout << endl;
	}
}

void printResume(int many, int price, bool half) {
	cout << "총 인원 : " << many << "명" << endl << endl
		<< ((half) ? "50% 할일" : "") << endl
		<< "총 금액 : " << price << "원" << endl;
}

int main() {
	int choice = 1, select_m = 0, select_t = 0, select_map_col = 0, howmany = 0, price = 0;
	char select_map_row = 'a';
	bool price_half_flag = false;
	int* age;
	string m1[] = {"08:00", "12:00", "15:00", "21:00"};
	string m2[] = { "07:20", "11:30", "13:00", "23:00"};
	string m3[] = { "07:20", "23:30" };
	string m4[] = { "09:50", "18:00", "21:15" };

	CGV* cgv = new CGV[]{
		CGV("1917", "15세 관람가", "A관", 6,15, m1),
		CGV("무간도", "12세 관람가", "B관", 6,15, m2),
		CGV("타짜", "18세 관람가", "A관", 6,15, m3),
		CGV("스폰지밥 극장판", "전체 이용가", "B관", 7,20, m4)
	};

	for (;;) {
		price = 0;
		price_half_flag = false;

		printwellcome();
		cin >> choice;
		if (choice == 2) break;
		if (choice != 1) continue;

		printCGV(cgv);
		cout << "관람하실 영화를 선택해 주세요 : ";
		cin >> select_m;

		printCGVtime(cgv[select_m - 1]);
		cout << "관람하실 시간을 선택해 주세요 : ";
		cin >> select_t;
		if (cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "00" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "01" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "02" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "03" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "04" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "05" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "06" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "07" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "08" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "09" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 5) == "10:00" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "22" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "23" ||
			cgv[select_m - 1].havetime[select_t - 1].substr(0, 2) == "24") {

			cout << "할인시간 적용되었습니다." << endl;
			price_half_flag = true;
		}

		cout << "몇 분이 오셨습니까? : ";
		cin >> howmany;

		age = new int[howmany];
		for (int i = 0; i < howmany; i++) {
			cout << " 나이를 입력하세요 : ";
			cin >> age[i];

			if (age[i] >= 18) price += 11000;
			else if (age[i] >= 12) price += 9000;
			else price += 5000;
		}

		printMap(cgv[select_m - 1]);
		for (int i = 0; i < howmany; i++) {
			retry:
			cout << i + 1 << "번째 관객분의 행을 선택해 주세요 (알파벳): ";
			cin >> select_map_row;
			cout << i + 1 << "번째 관객분의 좌석번호를 선택해 주세요(숫자): ";
			cin >> select_map_col;

			if(cgv[select_m - 1].map[(int)select_map_row - 97][select_map_col - 1] != '#')
				cgv[select_m - 1].map[(int)select_map_row - 97][select_map_col-1] = '#';
			else {
				cout << "이미 지정되었습니다." << endl;
				goto retry;
			}
			//printMap(cgv[select_m - 1]);
			cout << "지정되었습니다." << endl;
		}

		printResume(howmany, price, price_half_flag);
	}

	delete[] cgv;
	cgv = nullptr;

	return 0;
}
