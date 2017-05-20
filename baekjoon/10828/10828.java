import java.util.Scanner;

public class Main {

	private int count =0;
	private Node top;
	private class Node{
		private int data;
		private Node nextNode;
		Node (int data){
			this.data = data;
		}
	}
	


	void push(int data){
		Node new_node = new Node(data);
		if (count ==0){
			top = new_node;
		}else{
			new_node.nextNode = top;
			top = new_node;
		}
		count++;
	}
	int top(){
		if (top == null){
			
			return -1;
		}else {
			
			int x=top.data;
			
			return x;
		}
		
	}
	Object pop(){
		if (top == null){
			
			return -1;
		}
		else {
			
			Node tmp = top;
			top = tmp.nextNode;
			Object t=tmp.data;	
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
	void printStack(){
		Node node = top;
		System.out.print('(');
		for (int i=0;i<count;i++){
			if(i==(count-1)){
				System.out.print(node.data);
			}
			else{
				System.out.print(node.data+", ");
			}
			node = node.nextNode;
		}
		System.out.print(')');
		System.out.println();
	}
	public static void main(String[] args){
		Main a = new Main();
		Scanner in = new Scanner(System.in);

	
		
		String str;
		String temp;
		String[] tlist;
		str = in.nextLine();
		int number = Integer.parseInt(str);
		
		while (number>0){
			temp =in.nextLine();
			
			if (temp.charAt(1)=='u'){
				tlist=temp.split(" ");
				int ik =Integer.parseInt(tlist[1]);
				a.push(ik);
			}
			else{
				if(temp.equals("pop")){
					System.out.println(a.pop());
				}
				else if(temp.equals("empty")){
					System.out.println(a.empty());
				}
				else if(temp.equals("size")){
					System.out.println(a.size());
				}
				else if(temp.equals("top")){
					System.out.println(a.top());
				}
			}
			number-=1;
		}


		
		
		
		}
	
}

