package com.company;

import java.util.*;

public class Solution {

    public static int n;
    public static int[][] graph = new int[101][101];
    public static int[][] cheese = new int[101][101];

    // 상, 하, 좌, 우
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {-1, 1, 0, 0};

    // DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
    public static boolean DFS(int x, int y, int m) {
        // 주어진 범위를 벗어나는 경우에는 즉시 종료
        if (x <= -1 || x >= n || y <= -1 || y >= n) {
            return false;
        }
        // 현재 노드를 아직 방문하지 않았다면
        if (cheese[x][y] > m) {
            // 해당 노드 방문 처리
            cheese[x][y] = m;
            // 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
            for(int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                DFS(nx, ny, m);
            }
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 테스트케이스 입력 받기
        int T = sc.nextInt();

        for(int tc = 1; tc <= T; tc++) {
            n = sc.nextInt();

            int result = 1;
            int MAX = 0;
            int MIN = 100;

            for(int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                    graph[i][j] = sc.nextInt();
                    MAX = graph[i][j] > MAX ? graph[i][j] : MAX;
                    MIN = graph[i][j] < MIN ? graph[i][j] : MIN;
                }
            }

            for(int m = MIN; m <= MAX; m++) {
                for(int c = 0; c < n; c++) {
                    // 깊은 복사
                    System.arraycopy(graph[c], 0, cheese[c], 0, n);
                }
                int count = 0;

                for(int k = 0; k < n; k++) {
                    for(int l = 0; l < n; l++) {
                        if(DFS(k, l, m) == true) {
                            count += 1;
                        }
                    }
                }

                result = Math.max(result, count);
            }

            System.out.println("#" + tc + " " + result); // 정답 출력
        }
    }
}

