import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int iMax = 0;
        int index = 0;

        int[] arr = new int[9];
        for (int i=0; i<9; i++){
            arr[i] = Integer.parseInt(br.readLine());
            if (arr[i] > iMax) {
                iMax = arr[i];
                index = i;
            }
        }
        System.out.println(iMax);
        System.out.println(index + 1);
        
    }
}
