import java.util.*;

/*
 * Symbols to be put into the stack. We'll use:
 * P, for "normal parenthesis" --> ()
 * Q, for quad parenthesis --> []
 * C, for curly parenthesis --> {}
 */
enum Symbols {
    P, Q, C
}

class Solution{

    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            String line = sc.next().replace(" ", ""); // Remove whitespaces, if present
            Stack<Symbols> stack = new Stack<>();
            boolean shouldBreak = false;
            for (char c : line.toCharArray()) {
                switch (c) {
                    case '(':
                        stack.push(Symbols.P);
                        break;
                    case ')':
                        if (stack.empty() || stack.pop() != Symbols.P) {
                            System.out.println(false);
                            shouldBreak = true;
                        }
                        break;
                    case '[':
                        stack.push(Symbols.Q);
                        break;
                    case ']':
                        if (stack.empty() || stack.pop() != Symbols.Q) {
                            System.out.println(false);
                            shouldBreak = true;
                        }
                        break;
                    case '{':
                        stack.push(Symbols.C);
                        break;
                    case '}':
                        if (stack.empty() || stack.pop() != Symbols.C) {
                            System.out.println(false);
                            shouldBreak = true;
                        }
                        break;
                }
                
                if (shouldBreak)
                    break;
            }
            
            // String is well balanced iff the stack is empty
            if (!shouldBreak)
                System.out.println(stack.empty());
        }
    }
}

