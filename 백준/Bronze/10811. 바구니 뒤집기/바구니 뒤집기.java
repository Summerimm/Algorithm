import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");;

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        for (int i=0; i<N; i++){
            arr[i] = i+1;
        }

        for (int idx=0; idx<M; idx++){
            st = new StringTokenizer(br.readLine(), " ");;
            int i = Integer.parseInt(st.nextToken()) - 1;
            int j = Integer.parseInt(st.nextToken()) - 1;
            int[] tmp = new int[j-i+1];

            int ridx = 0;
            for (int r=j; r>=i; r--){
                tmp[ridx] = arr[r];
                ridx ++;
            }

            ridx = i;
            for (int t: tmp){
                arr[ridx] = t;
                ridx++;
            }
        }

        for (int k: arr){
            bw.write(k + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
