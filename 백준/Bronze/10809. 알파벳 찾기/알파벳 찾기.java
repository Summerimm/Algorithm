import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = new int[26];

        // 배열 초기화
        for (int i = 0; i < 26; i++) {
            arr[i] = -1;
        }
        
        // 해당 문자가 처음 등장하는 경우에만 값 변경
        String S = br.readLine();
        for (int i = 0; i < S.length(); i++) {
            char ch = S.charAt(i);
            int idx = ch - 'a';
            if (arr[idx] == -1) {
                arr[idx] = i;
            }
        }
        
        // 배열 출력
        for(int val: arr) {
            System.out.print(val + " ");
        }
    }
}