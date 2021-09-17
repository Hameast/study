import java.util.Scanner;

public class ReviewDemo01 {
    public static void main(String[] args) {
        //소수는 1과 자신 외에는 나누어 떨어지지 않는 수
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        boolean isPrime = true;


        int k = 2;
        while(k<number){
            if(number % k == 0){
                isPrime = false;
                break;
            }
            k++;
        }

        System.out.println(isPrime?number + "은(는) 소수!":number + "은(는) 소수가 아닙니다");
    }
}
