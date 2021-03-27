import java.util.*;

class Node implements Comparable<Node>{
  private int index;
  private int distance;

  public Node(int index, int distance){
    this.index = index;
    this.distance = distance;
  }
  public int getIndex(){
    return this.index;
  }
  public int getDistance(){
    return this.distance;
  }
  // 거리(비용)가 짧은 것이 높은 우선순위
  @Override
  public int compareTo(Node other){
    if (this.distance < other.distance){
      return -1;
    }
    return 1;
  }
}
class Main {
  public static final int INF = (int)1e9;
  public static int n, m, start;
  public static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
  public static int[] d =new int[100001];

  public static void dijkstra(int start){
    PriorityQueue<Node> pq = new PriorityQueue<>();
    // 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    pq.offer(new Node(start,0));
    d[start] = 0;
    while(!pq.isEmpty()){
      Node node = pq.poll();
      int dist = node.getDistance(); // 현재 노드까지 비용
      int now = node.getIndex(); // 현재노드
      // 현재 노드가 처리되어 있다면 무시
      if (d[now] < dist) continue;
      // 현재 노드와 연결된 다른 인접한 노드 확인
      for( int i=0; i < graph.get(now).size(); i++){
        int cost = d[now] + graph.get(now).get(i).getDistance();
        // 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
        if(cost < d[graph.get(now).get(i).getIndex()]){
          d[graph.get(now).get(i).getIndex()] = cost;
          pq.offer(new Node(graph.get(now).get(i).getIndex(),cost));
        }
      }
    }
    
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    n = sc.nextInt();
    m = sc.nextInt();
    start = sc.nextInt();

    for( int i=0; i<= n;i++){
      graph.add(new ArrayList<Node>());
    }

    // 모든 간선 정보를 입력 받기
    for(int i= 0;i<m;i++){
      int a = sc.nextInt();
      int b = sc.nextInt();
      int c = sc.nextInt();
      graph.get(a).add(new Node(b,c));
    }
    //최단거리 테이블 무한으로 초기화
    Arrays.fill(d,INF);

    dijkstra(start);

    for (int i=1;i<=n;i++){
      if (d[i] == INF){
        System.out.println("INF");
      }
      else{
        System.out.println(d[i]);
      }
    }
  }
}
