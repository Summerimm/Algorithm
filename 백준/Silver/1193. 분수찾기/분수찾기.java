import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1 2 6 7 15 16 28
        // 3 5 8 14 17 27
        // 4 9 13 18 26
        // 10 12 19 25
        // 11 20 24
        // 21 23
        // 22
        // 14 -> (1+2+3+4) 해놓고 4번째
        // 짝수면 열부터 홀수면 행부터
        int N = Integer.parseInt(br.readLine());
        int idx = 0; // 몇 번째 반복인지
        int num = 0; // N과 비교
        int rem; // 해당 반복에서 몇 번째 요소인지
        int front, back;
        while (num < N) {
            idx++;
            num += idx;
        }
        num -= idx;
        rem = N - num;
        if (idx % 2 == 1) {
            front = idx - rem + 1;
            back = rem;
        } else {
            back = idx - rem + 1;
            front = rem;
        }
        System.out.println(front + "/" + back);
    }
}