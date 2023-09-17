import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Location {
	int x;
	int y;
	int time;

	Location(int x, int y) {
		this.x = x;
		this.y = y;
		this.time = 0;
	}
}

class Pair {
	int time;
	int type;

	Pair() {}

	Pair(int time, int type) {
		this.time = time;
		this.type = type;
	}
}

public class Main {
	static int N, M, G, R;
	static int[][] garden;
	static int[] greens, reds;
	static ArrayList<Location> possible;
	static boolean[] visited;
	static int max;
	static final int RED = 3;
	static final int GREEN = 4;
	static final int FLOWER = 5;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		// N x M 크기 정원, 초록 수: G, 빨강 수: R
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		G = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		// 초록 index 저장 배열, 빨강 index 저장 배열
		greens = new int[G];
		reds = new int[R];

		// 정원 배열 초기화
		garden = new int[N][M];
		possible = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				garden[i][j] = Integer.parseInt(st.nextToken());
				if (garden[i][j] == 2) {
					possible.add(new Location(i, j));
				}
			}
		}

		visited = new boolean[10];

		greenComb(0, 0);
		System.out.println(max);
	}
	static void greenComb(int start, int cnt) {
		if (cnt == G) {
			redComb(0, 0);
			return;
		}

		for (int i = start; i < possible.size(); i++) {
			if (!visited[i]) {
				visited[i] = true;
				greens[cnt] = i;
				greenComb(i + 1, cnt + 1);
				visited[i] = false;
			}
		}
	}

	static void redComb(int start, int cnt) {
		if (cnt == R) {
			bfs();
			return;
		}

		for (int i = start; i < possible.size(); i++) {
			if (!visited[i]) {
				visited[i] = true;
				reds[cnt] = i;
				redComb(i + 1, cnt + 1);
				visited[i] = false;
			}
		}
	}

	static void bfs() {
		Queue<Location> q = new LinkedList<>();
		Pair[][] state = new Pair[N][M];

		// state 초기화
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				state[i][j] = new Pair();
			}
		}

		// 배양액 놓기
		for (int i = 0; i < G; i++) {
			Location loc = possible.get(greens[i]);
			state[loc.x][loc.y] = new Pair(0, GREEN);
			q.offer(new Location(loc.x, loc.y));
		}
		for (int i = 0; i < R; i++) {
			Location loc = possible.get(reds[i]);
			state[loc.x][loc.y] = new Pair(0, RED);
			q.offer(new Location(loc.x, loc.y));
		}

		int sum = 0;
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};

		while (!q.isEmpty()) {
			Location loc = q.poll();
			int x = loc.x;
			int y = loc.y;
			int curtime = state[x][y].time;
			int curtype = state[x][y].type;

			// 꽃이 핀 자리면 퍼지지 않음
			if (curtype == FLOWER) continue;

			// 4방향 퍼뜨리기
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < M && garden[nx][ny] != 0) {
					if (state[nx][ny].type == 0) {
						state[nx][ny] = new Pair(curtime + 1, curtype);
						q.offer(new Location(nx, ny));
					}
					// 빨강이 있을 때 초록이 퍼짐
					else if (state[nx][ny].type == RED) {
						if (curtype == GREEN && state[nx][ny].time == curtime + 1) {
							sum++;
							state[nx][ny].type = FLOWER;
						}
					}
					// 초록이 있을 때 빨강이 퍼짐
					else if (state[nx][ny].type == GREEN) {
						if (curtype == RED && state[nx][ny].time == curtime + 1) {
							sum++;
							state[nx][ny].type = FLOWER;
						}
					}
				}
			}
		}
		max = max > sum ? max : sum;
	}
}