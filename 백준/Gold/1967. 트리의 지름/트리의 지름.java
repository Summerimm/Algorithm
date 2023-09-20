import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static class Node {
		int idx, len;

		public Node(int idx, int len) {
			this.idx = idx;
			this.len = len;
		}
	}
	static int N; // 노드 수
	static List<Node> list[]; // (인접 인덱스, 가중치)를 담는 양방향 인접리스트
	static boolean visit[]; // 방문 배열
	static int ans; // 갱신될 max 값

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());

		// list 초기화
		list = new ArrayList[N + 1]; // 1번부터 사용
		for (int i = 1; i < N + 1; i++) {
			list[i] = new ArrayList<>();
		}

		// 양방향 인접 리스트 초기화
		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine(), " ");

			int parent = Integer.parseInt(st.nextToken());
			int child = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());

			list[parent].add(new Node(child, cost));
			list[child].add(new Node(parent, cost));
		}
        
        // dfs
		ans = 0;
		for (int i = 1; i <= N; i++) {
			visit = new boolean[N + 1]; // 매번 방문배열 초기화
			visit[i] = true; // 시작 지점
			dfs(i, 0);
		}
		System.out.println(ans);
	}

	private static void dfs(int idx, int len) {
		for (Node node : list[idx]) {
			if (!visit[node.idx]) {
				visit[node.idx] = true;
				dfs(node.idx, len + node.len);
			}
		}
		ans = (ans < len) ? len : ans;
	}
}