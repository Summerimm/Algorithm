import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[30];

        int num;
        for (int i=0; i<28; i++){
            num = Integer.parseInt(br.readLine());
            arr[num-1] += 1;
        }
        for (int i=0; i<30; i++){
            if (arr[i] == 0) System.out.println(i+1);
        }
    }
}
