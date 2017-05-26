/*  
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;
    
*/ 

void decode(String s ,Node root) {
    char[] chars = s.toCharArray();
    
    Node tmp = root;
    for (char c : chars) {
        Node next;
        if (c == '1') {
            next = tmp.right;
        } else {
            next = tmp.left;
        }
        
        if (next != null) {
            tmp = next;
        } else {
            System.out.print(tmp.data);
            tmp = c == '1' ? root.right : root.left;
        }
    }
    System.out.println(tmp.data);
}
