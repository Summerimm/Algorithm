import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int ans;
	static int[] s;
	static int[] w;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		s = new int[N];
		w = new int[N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			s[i] = Integer.parseInt(st.nextToken());
			w[i] = Integer.parseInt(st.nextToken());
		}

		breakEgg(0, 0); // 0번째 계란, 깨진 계란 개수

		System.out.println(ans);
	}

	static void breakEgg(int idx, int cnt) {
		ans = Math.max(ans, cnt);
		// 종료조건
		if (idx == N) return;

		// 손에 든 계란이 깨져있음
		if (s[idx] <= 0) {
			breakEgg(idx + 1, cnt);
			return;
		}

		for (int i = 0; i < N; i++) {
			// 손에 든 계란과 부딪히려고 하는 계란이 같은 계란
			if (idx == i) continue;
			// 부딪히려고 하는 계란이 깨져 있음
			if (s[i] <= 0) continue;

			s[i] -= w[idx];
			s[idx] -= w[i];

			if (s[i] <= 0) cnt++;
			if (s[idx] <= 0) cnt++;

			breakEgg(idx + 1, cnt);

			if (s[i] <= 0) cnt--;
			if (s[idx] <= 0) cnt--;

			s[i] += w[idx];
			s[idx] += w[i];
		}
	}
}