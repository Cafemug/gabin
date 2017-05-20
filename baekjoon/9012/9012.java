import java.util.Scanner;

public class Main {

	private int count =0;
		private Node top;
	private class Node{
		private String data;
		private Node nextNode;
		Node (String data){
			
			this.data = data;
		}
	}


	void push(String data){
		Node new_node = new Node(data);
		if (count ==0){
			top = new_node;
		}else{
			new_node.nextNode = top;
			top = new_node;
		}
		count++;
	}
	String top(){
		if (top == null){
			
			return "n";
		}else {
			
			String x=top.data;
			
			return x;
		}
		
	}
	String pop(){
		if (top == null){
			
			return "N";
		}
		else {
			
			Node tmp = top;
			top = tmp.nextNode;
			String t=tmp.data;	
			tmp = null;
			count--;
			return t;
		}
	}
	
	
		
	int size(){
		
		return count;
	}
	int empty(){
		if (top==null){
			 return 1;
		}else {
			return 0;
		}
	}
	
	public static void main(String[] args) {
		Main a = new Main();
		
		Scanner in = new Scanner(System.in);
		
		String str;
		String temp;
		String[] tlist;
		String pop;
		str = in.nextLine();
		int number = Integer.parseInt(str);
		int ui=0;
		while (number>0){
			while(a.size()!=0){
				a.pop();
			}
			temp =in.nextLine();
			tlist=temp.split("");
			for(int i=0 ;i<tlist.length;i++){
				
				if (tlist[i].equals("(")){
					a.push(tlist[i]);
				}
				else{
					pop=a.top();
					
					if(pop.equals("(")){
						a.pop();							
					}
					else{
						ui+=1;
						
					}
						
					}
				
				if(i==(tlist.length-1)){
					if(a.size()!=0){
						ui+=1;
					}
				}
			}
			if (ui ==0){
				System.out.println("YES");
			}
			else{
				System.out.println("NO");
				ui=0;
			}
			number-=1;
		}

		
		
		
		}
	}

	


