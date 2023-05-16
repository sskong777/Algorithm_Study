import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 덱_양석진 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        Deque<Integer> q = new LinkedList<>();

        StringTokenizer comment;

        while(N-- > 0){
            comment = new StringTokenizer(br.readLine(), " ");

            switch(comment.nextToken()){
                case "push_front":
                    q.addFirst(Integer.parseInt(comment.nextToken()));
                    break;
                case "push_back":
                    q.addLast(Integer.parseInt(comment.nextToken()));
                    break;
                case "pop_front":
                    if(q.isEmpty()){
                        sb.append(-1).append('\n');
                    }else{
                        sb.append(q.pollFirst()).append('\n');
                    }
                    break;
                case "pop_back":
                    if(q.isEmpty()){
                        sb.append(-1).append('\n');
                    }else{
                        sb.append(q.pollLast()).append('\n');
                    }
                    break;
                case "size":
                    sb.append(q.size()).append('\n');
                    break;
                case "empty":
                    if(q.isEmpty()){
                        sb.append(1).append('\n');
                    }else{
                        sb.append(0).append('\n');
                    }
                    break;
                case "front":
                    if(q.isEmpty()){
                        sb.append(-1).append('\n');
                    }else{
                        sb.append(q.peekFirst()).append('\n');
                    }
                    break;
                case "back":
                    if(q.isEmpty()){
                        sb.append(-1).append('\n');
                    }else{
                        sb.append(q.peekLast()).append('\n');
                    }
                    break;
            }
        }
        System.out.println(sb);
    }
}